import asyncio
import logging


from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink

async def amain(loop):
    cont = Controller(Sink(), hostname='0.0.0.0', port=25)
    cont.start()


logging.basicConfig(level=logging.DEBUG)

loop = asyncio.get_event_loop()
loop.create_task(amain(loop=loop))

try:
    print("Server running...")
    loop.run_forever()
except KeyboardInterrupt:
    pass