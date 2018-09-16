# from .cfg import cfg
from aiohttp import web
from .const import APP_KEY
from .base import WebSocket
# from . import handlers
# from .decorators import (login_required, admin_required, user_to_request,  # noqa
#                          restricted_api)
# from .utils import url_for  # noqa
# from . import flash  # noqa


async def startup(app: web.Application):
    app['websockets'] = []


async def cleanup(app: web.Application):
    for ws in app['websockets']:
        await ws.close(code=1001, message='Server shutdown')


def setup(app, routes, base_url='/ws', app_key=APP_KEY):
    # config = (config or {}).copy()
    # config['APP'] = app
    # # config['STORAGE'] = storage
    # cfg.configure(config)
    app.router.add_get(base_url, WebSocket)

    wsf = web.Application(loop=app.loop)
    app[app_key] = wsf

    app['ws_routes'] = routes

    wsf.on_startup.append(startup)
    wsf.on_cleanup.append(cleanup)

    return wsf
