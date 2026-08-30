import json 
import os 
import psycopg 
import redis 
from flask import Flask, jsonify, request
from importlib.metadata import version


VERSION = version("flask-app")


app = Flask(__name__)


# PostgreSQL configuration
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "flaskdb")
POSTGRES_USER = os.getenv("POSTGRES_USER", "flaskuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "flaskpassword")


# Redis configuration 
REDIS_HOST = os.getenv("REDIS_HOST", "localhost") 
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))


def get_postgres_connection(): 
   return psycopg.connect( 
      host=POSTGRES_HOST, 
      port=POSTGRES_PORT, 
      dbname=POSTGRES_DB, 
      user=POSTGRES_USER, 
      password=POSTGRES_PASSWORD, 
   )


redis_client = redis.Redis( 
   host=REDIS_HOST, 
   port=REDIS_PORT, 
   decode_responses=True, 
)


@app.route('/')
def hello_world():
   return 'Hello, world'


@app.route('/version')
def version():
   return VERSION


@app.route('/health')
def health():
   return {'status': 'OK'}


@app.route('/users/<int:user_id>', methods=['GET'] )
def get_user(user_id):
   cache_key = f"user:{user_id}"
   cached_user = redis_client.get(cache_key)

   if cached_user:
      print(f"Redis HIT: {cache_key}")
      return jsonify(json.loads(cached_user))

   print(f"Redis MISS: {cache_key}")

   with get_postgres_connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute(
            """
            SELECT id, name, email
            FROM users
            WHERE id = %s
            """,
            (user_id,),
         )

         row = cursor.fetchone()

         if row is None: 
            return jsonify({"error": "User not found"}), 404

         user = {
            "id": row[0],
            "name": row[1],
            "email": row[2],
         }

         redis_client.setex( 
            cache_key, 
            300, 
            json.dumps(user), 
         )

         return jsonify(user)


@app.route("/users", methods=["POST"])
def post_user(id, name, email):
   data = request.get_json()

   if not data:
      return jsonify({"error": "JSON body is required"}), 400

   name = data.get("name")
   email = data.get("email")

   if not name or not email:
      return jsonify(
         {"error": "name and email are required"}
      ), 400
   
   with get_postgres_connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id
            """,
            (name, email),
         )

         user_id = cursor.fetchone()[0] 

      conn.commit()

   user = {
      "id": user_id,
      "name": name,
      "email": email,
   }

   redis_client.setex(
      f"user:{user_id}",
      300,
      json.dumps(user),
   )

   return jsonify(user), 201


if __name__ == '__main__':
  app.run(
     host='0.0.0.0', 
     port=5000, 
     debug=True
   )

