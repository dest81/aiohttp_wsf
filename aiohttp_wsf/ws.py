import json
from .exceptions import HandlerNotFoundException, RouteNotFoundException


class WS:
    def __init__(self, request, ws, data):
        self.ws = ws
        self.data = data

class WSHandler:

    def __init__(self, request, ws, data):
        self.request = request
        self.ws = ws
        self.data = json.loads(data)
        handler = self.get_route()

        await handler(request, ws, self.data).run(request, ws)

    def get_route(self):
        route = self.data.get('type', None)
        if not route:
            raise RouteNotFoundException
        ws_routes = self.request.app['ws_routes']
        handler = ws_routes.get(route, None)
        if not handler:
            raise HandlerNotFoundException
        return handler

