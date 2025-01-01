import os
import configparser
import requests
from getgauge.python import step

# --------------------------
# Gauge step implementations
# --------------------------
@step("pingを打つと<response_text>が返ってくる")
def ping(expect):
    app_url = get_property("APP_URL")  # プロパティファイルからURLを取得
    url = app_url + "/v1/systems/ping"
    try:
        # HTTP GETリクエストを送信
        response = requests.get(url)
        
        # ステータスコードが200であることを確認
        if response.status_code != 200:
            raise AssertionError(f"Expected status code 200, but got {response.status_code}")
        
        # レスポンスボディが 'pong' であることを確認
        if response.text.strip() != expect:
            raise AssertionError(f"Expected response body {expect}, but got '{response.text.strip()}'")
        
        print("Ping request successful and response is 'pong'.")
    except Exception as e:
        raise RuntimeError(f"Failed to send {expect} request or verify response: {e}")
# ---------------
# Execution Hooks
# ---------------
def get_property(property_name):
    """
    default.properties ファイルから指定したプロパティを取得する。
    """
    config = configparser.ConfigParser()
    properties_file = os.path.join(os.getcwd(), "env/default", "default.properties")
    print(properties_file)
    config.read(properties_file)
    return config["DEFAULT"].get(property_name)