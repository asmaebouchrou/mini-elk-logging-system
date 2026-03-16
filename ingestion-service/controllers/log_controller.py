from flask import Blueprint, request, jsonify
from services.log_service import LogService

log_blueprint = Blueprint("logs", __name__)

@log_blueprint.route("/logs", methods=["POST"])
def create_log():
    data = request.get_json(silent=True) or {}
    service = data.get("service")
    level = data.get("level")
    message = data.get("message")

    if not service or not level or not message:
        return jsonify({
            "error": "Missing required fields: service, level, message"
        }), 400

    result = LogService.create_log(service, level, message)

    return jsonify(result), 201
