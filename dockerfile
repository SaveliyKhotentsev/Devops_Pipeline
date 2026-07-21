FROM python:3.12-slim
WORKDIR /app
RUN make
COPY . .
EXPOSE 5000
CMD [ "python", "app.py"]