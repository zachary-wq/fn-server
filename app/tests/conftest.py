import pytest
from dotenv import load_dotenv
import os
import sys
from app.main import app
from fastapi.testclient import TestClient

@pytest.fixture(autouse=True, scope="session")
def setup_test_env():
    """设置测试环境"""
    # 设置测试标志（在导入配置之前）
    os.environ["TESTING"] = "True"
    os.environ["POSTGRES_DB"] = "app_test"
    print("This is setup_test_env execute")


def get_client():
    client = TestClient(app)
    return client