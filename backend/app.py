from flask import Flask, jsonify

from config import Config
from database.init_db import initialize_database
from routes.prediction import prediction_bp
from routes.history import history_bp
from routes.auth import auth_bp
from routes.analytics import analytics_bp
from routes.export import export_bp
from routes.route import route_bp
from routes.dashboard import dashboard_bp
from routes.profile import profile_bp
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

initialize_database()

app.register_blueprint(prediction_bp)
app.register_blueprint(history_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(export_bp)
app.register_blueprint(route_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)



# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Smart Energy Bus API is running"
    })


# -----------------------------
# Health Check
# -----------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend is healthy"
    }), 200


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )