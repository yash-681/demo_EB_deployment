from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def root():
    return "Hello World"


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # Local dev convenience; production uses gunicorn (see Dockerfile).
    app.run(host="0.0.0.0", port=8000)




