# encoding:utf-8


class BasicItem(object):
    def __init__(self, timestamp, *args, **kwargs):
        super(BasicItem, self).__init__(*args, **kwargs)
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class LinuxCPU(BasicItem):
    def __init__(self, timestamp, *args, **kwargs):
        super(LinuxCPU, self).__init__(timestamp, *args, **kwargs)
        self.sys_cpu = kwargs.get("sys_cpu", 0)
        self.usr_cpu = kwargs.get("usr_cpu", 0)
        self.idle_cpu = kwargs.get("idle_cpu", 0)


class ProcessCPU(BasicItem):
    def __init__(self, timestamp, *args, **kwargs):
        super(ProcessCPU, self).__init__(timestamp, *args, **kwargs)
        self.cpu = kwargs.get("cpu", 0)


class LinuxMEM(BasicItem):
    def __init__(self, timestamp, *args, **kwargs):
        super(LinuxMEM, self).__init__(timestamp, *args, **kwargs)
        self.total = float(kwargs.get("total", 0))
        self.free = float(kwargs.get("free", 0))
        self.buff = float(kwargs.get("buff", 0))
        self.cache = float(kwargs.get("cache", 0))

    @property
    def used(self):
        return self.total - self.free - self.buff - self.cache


class ProcessMEM(BasicItem):
    def __init__(self, timestamp, *args, **kwargs):
        super(ProcessMEM, self).__init__(timestamp, *args, **kwargs)
        self.rsize = float(kwargs.get("rsize", 0))


def main():
    pass

if __name__ == "__main__":
    main()
