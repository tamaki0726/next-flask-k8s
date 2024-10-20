# app/rest/user_controller.py
from flask import Blueprint, request, jsonify, make_response
from bson.json_util import dumps
from app.gateway.mongo_content_gateway import MongoContentGateway
from app.gateway.openai_content_gateway import OpenAiContentGateway
from app.usecase.content_usecase import ContentUseCase
from app.usecase.upload_usecase import UploadUseCase
from app.config import Config

content_bp = Blueprint('content', __name__)

# ゲートウェイとユースケースの初期化
content_gateway = MongoContentGateway(Config.MONGO_URI)
content_openai_gateway = OpenAiContentGateway(Config.OPENAI_API_KEY)
content_usecase = ContentUseCase(content_gateway)
content_openai_usecase = UploadUseCase(content_openai_gateway)

@content_bp.route('/v1/contents', methods=['GET'])
def get_users():
    users = content_usecase.get_contents()
    return dumps(users), 200

@content_bp.route('/v1/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'ファイルがリクエストに含まれていません'}), 400
    file = request.files['file']
    response_data = content_openai_usecase.upload_file(file)

     # レスポンスを作成し、Content-Typeを指定
    return make_response(response_data)