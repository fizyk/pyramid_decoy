"""pyramid_decoy's main test."""
from pytest_pyramid import factories

decoy_config = factories.pyramid_config(  # pylint:disable=invalid-name
    {
        "pyramid.includes": ["pyramid_decoy"],
        "decoy.url": "http://www.example.com/",
    }
)

decoy_app = factories.pyramid_app("decoy_config")  # pylint:disable=invalid-name
