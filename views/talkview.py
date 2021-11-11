from sanic.response import json
import json as json1
from sanic.views import HTTPMethodView
from controllers.talk_data import TalkData


class TalkView(HTTPMethodView):

    async def get(self, request):
        response = TalkData(None).get_data()
        return json(json1.loads(response))

    async def post(self, request):
        response = TalkData(request.json['data']).add_data()
        return json(response)

    async def patch(self, request):
        response = TalkData(request.json).edit_data(int(request.args['id'][0]))
        return json(response)
