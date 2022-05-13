from typing import Callable

import mongoengine
from app import mdbConfig
from types import FunctionType


def loadmdb(function: FunctionType) -> Callable[[], None]:
    def load():
        mongoengine.connect(**mdbConfig['MONGODB_SETTINGS'])
        function()

    return load
