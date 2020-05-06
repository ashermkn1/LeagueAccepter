from pprint import pprint

from lcu_driver import Connector
from lcu_driver.connection import Connection
from lcu_driver.events.responses import WebsocketEventResponse
from schema import LolMatchmakingMatchmakingReadyCheckResource, LolMatchmakingMatchmakingReadyCheckState
connector = Connector()


@connector.ws.register('/', event_types=('CREATE', 'UPDATE', 'DELETE'))
async def debug_print(_connection: Connection, event: WebsocketEventResponse) -> None:
    pprint({'data': event.data, 'type': event.type, 'uri': event.uri})


@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def auto_decline(connection: Connection, event: WebsocketEventResponse) -> None:
    resource = LolMatchmakingMatchmakingReadyCheckResource(**event.data)
    if resource.state == LolMatchmakingMatchmakingReadyCheckState.IN_PROGRESS.value:
        await connection.request('post', '/lol-matchmaking/v1/ready-check/decline')


@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')


@connector.close
async def disconnect(connection: Connection) -> None:
    print('The client was closed')
    await connector.stop()


if __name__ == '__main__':
    connector.start()
