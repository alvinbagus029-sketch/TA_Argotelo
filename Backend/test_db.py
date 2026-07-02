from Backend.app import app
from Backend.model import db

with app.app_context():
    try:
        result = db.session.execute(db.text("SELECT DATABASE()"))
        print("✅ Connected")
        print(result.fetchone())
    except Exception as e:
        print("❌ Connection Failed")
        print(e)