import pytest
def pytest_collection_modifyitems(session,config,items:list):
    print(items)
    print(type(items))

    for i in items:
        if "add" in i.nodeid:
            i.add_marker(pytest.mark.add)
        if "sub" in i.nodeid:
            i.add_marker(pytest.mark.sub)
        if "div" in i.nodeid:
            i.add_marker(pytest.mark.div)
        if "mul" in i.nodeid:
            i.add_marker(pytest.mark.mul)