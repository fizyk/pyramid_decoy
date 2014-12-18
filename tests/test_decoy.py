"""Test default decoy behaviour."""
import pytest


@pytest.mark.parametrize('path', ('/', '/check/', '/check', '/a/b/s'))
def test_decoy(decoy_app, path):
    """Check default behaviour of decoy app."""
    url = decoy_app.app.registry['decoy']['url']
    response = decoy_app.get(path)
    assert response.status_code == 302
    assert response.location == url
