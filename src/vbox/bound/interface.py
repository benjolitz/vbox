from . import (
    hdd,
    host,
    vm,
    exceptions,
)

class VirtualBox(object):

    exceptions = exceptions

    def __init__(self, cli):
        super(VirtualBox, self).__init__()
        self.cli = cli
        
        self.host = host.Host(self)
        self.vms = vm.Library(self)
        self.hdds = hdd.Library(self)