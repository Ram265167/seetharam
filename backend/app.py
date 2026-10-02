import os
from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import text
from dotenv import load_dotenv
from config import db

load_dotenv()

app = Flask(__name__)
CORS(app)

database_url = os.getenv("DATABASE_URL")
if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

@app.get("/api/health")
def health():
    if not database_url:
        return jsonify({"status":"error","database":"not configured","message":"DATABASE_URL is missing."}), 500
    try:
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return jsonify({"status":"ok","database":"supabase"})
    except Exception as exc:
        return jsonify({"status":"error","database":"unreachable","message":str(exc)}), 500

@app.get("/")
def index():
    return jsonify({"app":"Seetharam","api":"Flask REST API","database":"Supabase PostgreSQL"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT",5000)), debug=True)
