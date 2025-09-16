from ..conftest import get_client

def test_health():
    client = get_client()
    response = client.get("/api/v1/health/home")
    assert response.status_code == 200
    assert response.text == "success"


def test_check_postgres_env():
    import os
    print(f"POSTGRES_DB 环境变量: {os.getenv('POSTGRES_DB')}")

    # 检查你的配置类是否读取到了新值
    from app.core import settings  # 替换成你的配置导入
    print(f"配置中的数据库名: {settings.POSTGRES_DB}")  # 或者你的配置字段名