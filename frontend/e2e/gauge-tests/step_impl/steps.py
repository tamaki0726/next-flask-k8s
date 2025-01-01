import os
import configparser
from getgauge.python import step, before_suite, after_suite
from playwright.sync_api import sync_playwright

playwright = None
browser = None
page = None

# --------------------------
# Gauge step implementations
# --------------------------
@step("ユーザーはホームページに遷移することができる")
def navigate_to_homepage():
    global page
    app_url = get_property("APP_URL")  # プロパティファイルからURLを取得
    if not app_url:
        raise RuntimeError("APP_URL is not defined in default.properties")
    browser_context = browser.new_context()
    page = browser_context.new_page()
    page.goto(app_url)

@step("ユーザーはページタイトルが<expected_title>であることを確認できる")
def check_title(expected_title):
    global page
    title = page.text_content("h1")
    if title != expected_title:
        raise AssertionError(f"Expected title to be '{expected_title}' but got '{title}'")
# ---------------
# Execution Hooks
# ---------------
@before_suite
def before_suite(context):
    print("before_suite")
    global playwright, browser
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()

@after_suite
def after_suite(context):
    print("after_suite")
    global playwright, browser
    if browser:
        browser.close()
    if playwright:
        playwright.stop()

def get_property(property_name):
    """
    default.properties ファイルから指定したプロパティを取得する。
    """
    config = configparser.ConfigParser()
    properties_file = os.path.join(os.getcwd(), "env/default", "default.properties")
    print(properties_file)
    config.read(properties_file)
    return config["DEFAULT"].get(property_name)