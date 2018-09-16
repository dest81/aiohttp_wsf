import logging
from aiohttp import web, WSMsgType
from .ws import WSHandler

logger = logging.getLogger('aiohttp_wsf')


class WebSocket(web.View):
    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        # session = await get_session(self.request)
        # user = User(self.request.db, {'id': session.get('user')})
        # login = await user.get_login()

        # for _ws in self.request.app['websockets']:
        #     _ws.send_str('%s joined' % 'login')
        # self.request.app['websockets'].append(ws)

        # import pdb; pdb.set_trace()
        # await ws.send_str('(%s) %s' % ('login', 'msg.data'))

        async for msg in ws:
            logger.debug('======== WEBSOCKET =========')
            logger.debug(msg)
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    logger.debug('closing connection')
                    await ws.close()
                else:
                    logger.debug('handling data')
                    await WSHandler(self.request, ws, msg.data)

                    # handler()
                    # await ws.send_str(msg.data + '/answer')
            elif msg.type == WSMsgType.ERROR:
                logger.debug('ws connection closed with exception %s' % ws.exception())

        # self.request.app['websockets'].remove(ws)
        # for _ws in self.request.app['websockets']:
        #     _ws.send_str('%s disconected' % 'login')
        logger.debug('websocket connection closed')

        return ws
