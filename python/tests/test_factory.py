from dtuservice import create_app

def test_config():
    """Test create_app with no config"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    """Test the home route works"""
    response = client.get('/')
    assert response.data == b'hello there'

