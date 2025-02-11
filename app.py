from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  # ✅ Import Flask-Migrate
from models import db
from auth import auth_bp
from admin import admin_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

# ✅ Initialize Flask-Migrate
migrate = Migrate(app, db)  

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

