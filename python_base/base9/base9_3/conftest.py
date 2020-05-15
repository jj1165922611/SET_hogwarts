import pytest
@pytest.fixture()
def connect():
    print("连接数据库")