from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User  # Ensure models.py defines User & db
from auth import auth_bp
from admin import admin_bp

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize database
db.init_app(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = "auth.login"  # Redirect unauthorized users to login
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints (for Authentication & Admin Panel)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

