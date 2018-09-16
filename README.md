# aiohttp_wsf


Websocket Framework for aiohttp


add into create_app 
```
import aiohttp_wsf
from views import WSGoals
...
ws_handlers = {
    'test': WSTest
}
...
aiohttp_wsf.setup(app, ws_handlers, '/api/ws/')
```

handler can looks like
```
from aiohttp_wsf.ws import WS
...
class WSGoals(WS):

    async def get(self, request, ws):
        message = {'type': 'test', 'message': 'test done'}
        await ws.send_str(json.dumps(message))

```


