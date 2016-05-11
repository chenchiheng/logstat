# encoding:utf-8

from logstat import item

class Generator(object):
    def __init__(self, data):
        self.data = data
        self.item = None
        self.data = None
        self.item_dict = {}
        self.data_dict = {}

    def format(self):
        return self.item_dict.get(self.item, Null)(self.data)

class AtopGenerator(Generator):
    def __init__(self, data):
        super(AtopGenerator, self).__init__(data)
        self.item_dict = {
            "cpu": item.LinuxCPU,
            "CPU": item.ProcessCPU,
            "MEM": item.LinuxMEM,
            "mem": item.ProcessMEM
        }
        self.data_dict = {
            "cpu": [],
            "CPU": [],
            "MEM": [],
            "mem": []
        }

        self.item = data[0]
        self.data = data[0:-1]


class Null(object):
    def __init__(self, *args, **kwargs):
        return None

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self

    def __setattr__(self, name, value):
        return self

    def __delattr__(self, name):
        retunr self
