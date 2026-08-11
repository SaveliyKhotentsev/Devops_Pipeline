FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y make
COPY . .
RUN make up
EXPOSE 5000
CMD [ "python", "app.py"]