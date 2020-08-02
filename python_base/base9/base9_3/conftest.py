import pytest
@pytest.fixture(scope="session")
def connect():
    print("连接数据库")