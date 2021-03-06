# share.py  17/04/2016  D.J.Whale
#
# A simple cross-process pub-sub mechanism.

import os
import time

#TODO what about locking?


def trace(msg):
    pass#print(str(msg))

EXTN      = ".share"
POLL_RATE = 0.5

class Share():

    def __init__(self, mod):
        self.mod = mod


    def send(self, name, data=None):
        """Signal and send data"""
        trace("send:%s=%s" % (name, data))
        name += EXTN

        # wait for file to not exist
        while os.path.isfile(name):
            time.sleep(POLL_RATE)

        # create file and write optional data to it
        f = open(name, "wb")
        if data != None:
            f.write(data)
        f.close()


    def check(self, name, wait=False):
        """Check if a share has been signalled"""
        trace("check:%s" % name)
        name += EXTN

        if os.path.isfile(name):
            return True

        elif wait:
            while not os.path.isfile(name):
                time.sleep(POLL_RATE)
            return True

        return False


    def get(self, name, wait=False):
        """Get data from a share and reset it"""
        trace("wait:%s" % name)
        name += EXTN
        if wait:
            while not os.path.isfile(name):
                time.sleep(POLL_RATE)

        if os.path.isfile(name):
            f = open(name, 'rb')
            data = f.read()
            f.close()
            os.unlink(name)
            return data
        else:
            return None


    def __repr__(self):
        return "Share"


    def __dir__(self):
        return ["send","check","get"]


    def __getattr__(self, name):
        if name.startswith("is"):
            name = name[2:]
            trace("build a checker for: %s" % name)
            def fn():
                return self.check(name)

        elif name.startswith("get"):
            name = name[3:]
            trace("build a getter for:%s" % name)
            def fn():
                return self.get(name)

        else:
            trace("build a sender for:%s" % name)
            def fn(data=None):
                return self.send(name, data)

        return fn


# Facade this module as a Class, so that we can use __getattr__ to
# dynamically build wrapper functions for any function name provided
# by the caller.

import sys
sys.modules[__name__] = Share(sys.modules[__name__])
