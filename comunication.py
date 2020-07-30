import asyncio
import websockets
import  DisplayActions
import ctypes
import os

authenticated = True
dActions = DisplayActions.Actions()
reserved = ["load","fun"]
global websocket_pointer
async def commu(websocket, path):
    async for message in websocket:
        dActions.websocket_pointer = id(websocket)
        try:
            _class,_method = message.split(".")
            if (_class == "change" and authenticated):
                variable,value = _method.split(":",1)
                item = getattr(dActions,variable)
                setattr(item,"websocket_pointer",id(websocket))
                item.value(value,False)
                setattr(item,"name",variable)
                setattr(dActions,variable,item)

            elif (_class == "click" and _method not in reserved and authenticated):
                method = None
                method = getattr(dActions,_method)
                method()

            elif (_class == "load" and authenticated):
                method = getattr(dActions,"load")
                method()
            elif (_class == "auth"):
                if _method == str(os.getpid()): authenticated = True

        except NameError as E:
            print( message +  " not exist")
        except Exception as E:
            print (message)
            if (hasattr(E,"message")):
                print("error" + E.mmessage)
            else:
                print(E)


def start():
    port = int("8" + str(os.getpid())[1:])
    ws = websockets.serve(commu, 'localhost', port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ws)
    loop.run_forever()