from constants import *
from sanic import Blueprint
from views.confview import ConfView
from views.talkview import TalkView

API_VERSION = 'v1'


def setup_api(app):
    api_prefix = f'/{SERVICENAME.lower()}/{API_VERSION}'
    api_v1 = Blueprint(API_VERSION, url_prefix=api_prefix)

    api_v1.add_route(ConfView.as_view(), '/conference', strict_slashes=False)
    api_v1.add_route(TalkView.as_view(), '/talk', strict_slashes=False)
    app.blueprint(api_v1)
