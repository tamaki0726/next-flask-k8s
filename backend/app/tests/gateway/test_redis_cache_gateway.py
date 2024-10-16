from unittest import TestCase
from app.gateway.redis_cache_gateway import RedisCacheGateway
from app.domain.cache import Cache
from unittest.mock import MagicMock

class TestRedisCacheGateway(TestCase):
    def setUp(self):
        self.gateway = RedisCacheGateway('redis://localhost:6379')
        self.gateway.client = MagicMock()

    def test_create(self):
        cache = Cache(key='test_key', value='test_value')
        self.gateway.client.set.return_value = True  # モックの戻り値を設定

        result = self.gateway.create(cache)

        self.gateway.client.set.assert_called_once_with('test_key', 'test_value')
        self.assertEqual(result, 'True')  # RedisのsetはTrueを返す

    def test_all_read(self):
        # モックデータの設定
        self.gateway.client.keys.return_value = [b'test_key1', b'test_key2']
        self.gateway.client.get.side_effect = [b'value1', b'value2']

        result = self.gateway.all_read()

        self.gateway.client.keys.assert_called_once_with('*')
        self.assertEqual(result, {
            'test_key1': 'value1',
            'test_key2': 'value2'
        })

    def test_read(self):
        self.gateway.client.get.return_value = b'test_value'

        result = self.gateway.read('test_key')

        self.gateway.client.get.assert_called_once_with('test_key')
        self.assertEqual(result, 'test_value')

    def tearDown(self):
        self.gateway.close()
