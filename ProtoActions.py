import ctypes
import asyncio
import concurrent.futures


class ActionsMaster():
    websocket_pointer = None

    def fun(self,command):
        websocket = ctypes.cast(self.websocket_pointer, ctypes.py_object).value
        pool = concurrent.futures.ThreadPoolExecutor()
        pool.submit(asyncio.get_event_loop().run_until_complete,websocket.send(command))



class Input(ActionsMaster):

    __Value = None
    name = None
    def value(self,new_value = None,update = True):
        if new_value == None:
            return self.__Value
        else:
            self.__Value = new_value
            if update:
                self.update()

    def update(self):
        self.fun("document.getElementById('{}').value = '{}'".format(self.name, self.__Value))

