from flask import Blueprint, request, jsonify
from services.log_service import LogService

log_blueprint = Blueprint("search_logs", __name__)


@log_blueprint.route("/logs", methods=["GET"])
def get_logs():
    service = request.args.get("service")
    level = request.args.get("level")

    result = LogService.get_logs(service, level)

    return jsonify(result)
