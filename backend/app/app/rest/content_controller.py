# app/rest/user_controller.py
from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from app.gateway.mongo_content_gateway import MongoContentGateway
from app.usecase.content_usecase import ContentUseCase
from app.config import Config

content_bp = Blueprint('content', __name__)

# MongoDBゲートウェイとユースケースの初期化
content_gateway = MongoContentGateway(Config.MONGO_URI)
content_usecase = ContentUseCase(content_gateway)

@content_bp.route('/v1/contents', methods=['GET'])
def get_users():
    users = content_usecase.get_contents()
    return dumps(users), 200

# @content_bp.route('/v1/upload', methods=['POST'])
# def create_user():
#     data = request.json
#     user_id = content_usecase.upload_file(data['name'], data['email'])
#     return jsonify({"id": user_id}), 201
