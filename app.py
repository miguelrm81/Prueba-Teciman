from src.routes.parte_obra_routes import parte_bp
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(parte_bp)

if __name__ == "__main__":
    app.run(debug=True)
