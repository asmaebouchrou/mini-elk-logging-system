from flask import Flask
from controllers.log_controller import log_blueprint

app = Flask(__name__)

app.register_blueprint(log_blueprint)


@app.route("/")
def health():
    return {"status": "search service running"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)