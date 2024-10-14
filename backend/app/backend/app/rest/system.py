from flask import Blueprint

system_bp = Blueprint('system', __name__)

@system_bp.route('/v1/systems/ping', methods=['GET'])
def ping():
    return "pong", 200