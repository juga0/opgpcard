""""""
import pytest


@pytest.fixture()
def datadir(request):
    class D:
        def __init__(self, basepath):
            self.basepath = basepath

        def open(self, name):
            return self.basepath.join(name).open()

        def join(self, name):
            return self.basepath.join(name).strpath

    return D(request.fspath.dirpath("data"))
