"""Test default decoy behaviour."""


def test_decoy(decoy_app):
    """Check default behaviour of decoy app."""
    response = decoy_app.get('/')
    assert response.status_code == 302
