# app/rest/user_controller.py
from flask import Blueprint, request, jsonify
from app.gateway.redis_cache_gateway import RedisCacheGateway
from app.usecase.cache_usecase import CacheUseCase
from app.config import Config

cache_bp = Blueprint('cache', __name__)

# Redisゲートウェイとユースケースの初期化
cache_gateway = RedisCacheGateway(Config.REDIS_URI)
cache_usecase = CacheUseCase(cache_gateway)

@cache_bp.route('/v1/cache', methods=['POST'])
def create_cache():
    data = request.json
    value = cache_usecase.create_cache(data['key'], data['value'])
    return jsonify({"id": value}), 201

@cache_bp.route('/v1/cache/<key>', methods=['GET'])
def get_cache(key):
    value = cache_usecase.get_cache(key)
    print(value)
    return jsonify({"value": value}), 200

@cache_bp.route('/v1/caches', methods=['GET'])
def get_caches():
    keys = cache_usecase.get_caches()
    return jsonify({"keys": keys}), 200