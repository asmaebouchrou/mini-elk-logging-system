from flask import Flask
from controllers.log_controller import log_blueprint

app=Flask(__name__)
app.register_blueprint(log_blueprint)

@app.route("/")
def health():
    return {"status":"ingestion service is running"}

if __name__ == "__main__":
    app.run(debug=True)
