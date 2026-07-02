from flask import Flask
from flask_cors import CORS

from Backend.config import Config
from Backend.model import db
from Backend.routes.auth import auth_bp

app = Flask(__name__)

# Load Config
app.config.from_object(Config)

# Session
app.secret_key = Config.SECRET_KEY

app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# CORS
CORS(
    app,
    supports_credentials=True
)

# Database
db.init_app(app)

# Blueprint
app.register_blueprint(auth_bp)


@app.route("/")
def home():

    return "AMSP Backend Running"


if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(
        debug=True
    )