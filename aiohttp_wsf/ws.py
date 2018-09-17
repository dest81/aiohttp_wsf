import json
from asyncinit import asyncinit
from .exceptions import HandlerNotFoundException, RouteNotFoundException


@asyncinit
class WS:

    serializer = None

    anonymous = 'Anonymous'

    async def __init__(self, request, ws, data):
        self.ws = ws
        self.data = data
        self.request = request
        self.action = data.get('action', 'get')

        if self.action == 'get':
            return await self.get(request, ws, data)
        elif self.action == 'post':
            return await self.post(request, ws, data)
        elif self.action == 'delete':
            return await self.delete(request, ws, data)
        elif self.action == 'list':
            return await self.list(request, ws, data)

    async def get_user(self):
        # session = await get_session(self.request)
        # user = User(self.request.db, {'id': session.get('user')})
        return self.anonymous

    async def get(self, request, ws, data):
        pass

    async def post(self, request, ws, data):
        pass

    async def delete(self, request, ws, data):
        pass

    async def list(self, request, ws, data):
        pass


@asyncinit
class WSHandler:

    async def __init__(self, request, ws, data):
        self.request = request
        self.ws = ws
        self.data = data
        handler = await self.get_handler()
        await handler(request, ws, data) # .get(request, ws)

    async def get_handler(self):
        route = self.data.get('type', None)
        if not route:
            raise RouteNotFoundException
        ws_routes = self.request.app['ws_routes']
        handler = ws_routes.get(route, None)
        if not handler:
            raise HandlerNotFoundException
        return handler

