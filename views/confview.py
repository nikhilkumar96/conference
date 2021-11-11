from sanic.response import json
import json as json1
from sanic.views import HTTPMethodView
from controllers.conference_data import ConferenceData


class ConfView(HTTPMethodView):

    async def get(self, request):
        response = ConferenceData(None).get_data()
        return json(json1.loads(response))

    async def post(self, request):
        response = ConferenceData(request.json['data']).add_data()
        return json(response)

    async def patch(self, request):
        response = ConferenceData(request.json).edit_data(int(request.args['id'][0]))
        return json(response)
