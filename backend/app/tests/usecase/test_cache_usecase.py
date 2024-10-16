from unittest import TestCase
from app.usecase.cache_usecase import CacheUseCase
from app.domain.cache import Cache
from unittest.mock import MagicMock

class TestCacheUseCase(TestCase):
    def setUp(self):
        self.cache_repository = MagicMock()  # CacheRepositoryをモック
        self.use_case = CacheUseCase(self.cache_repository)

    def test_create_cache(self):
        key = 'test_key'
        value = 'test_value'

        self.cache_repository.create.return_value = 'True'  # モックの戻り値を設定

        result = self.use_case.create_cache(key, value)

        # モックのcreateメソッドが呼び出された引数を取得
        self.cache_repository.create.assert_called_once()
        
        # call_argsはタプルのタプルになっているので、1つ目の要素を取り出す
        args = self.cache_repository.create.call_args[0][0]  # 引数を取得
        
        # 属性を比較
        self.assertEqual(args.key, key)
        self.assertEqual(args.value, value)

        self.assertEqual(result, 'True')  # createメソッドの戻り値を確認

    def test_get_caches(self):
        mock_caches = {
            'test_key1': 'value1',
            'test_key2': 'value2'
        }
        self.cache_repository.all_read.return_value = mock_caches

        result = self.use_case.get_caches()

        self.cache_repository.all_read.assert_called_once()
        self.assertEqual(result, mock_caches)

    def test_get_cache(self):
        key = 'test_key'
        expected_value = 'test_value'
        self.cache_repository.read.return_value = expected_value

        result = self.use_case.get_cache(key)

        self.cache_repository.read.assert_called_once_with(key)
        self.assertEqual(result, expected_value)

    def tearDown(self):
        pass  # 特にリソースのクリーンアップは必要ないため、空のtearDown
