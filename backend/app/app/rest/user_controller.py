# app/rest/user_controller.py
from flask import Blueprint, request, jsonify
from app.gateway.mongo_user_gateway import MongoUserGateway
from app.usecase.user_usecase import UserUseCase
from app.config import Config

user_bp = Blueprint('user', __name__)

# MongoDBゲートウェイとユースケースの初期化
user_gateway = MongoUserGateway(Config.MONGO_URI)
user_usecase = UserUseCase(user_gateway)

@user_bp.route('/v1/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = user_usecase.create_user(data['name'], data['email'])
    return jsonify({"id": user_id}), 201

@user_bp.route('/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_usecase.get_user(user_id)
    return jsonify(user), 200

@user_bp.route('/v1/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user_usecase.update_user(user_id, data['name'], data['email'])
    return jsonify({"message": "User updated"}), 200

@user_bp.route('/v1/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_usecase.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 204
