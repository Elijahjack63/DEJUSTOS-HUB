from app import app
from database import db

# Import all models so they are registered with SQLAlchemy
import models

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
