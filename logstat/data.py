# encoding:utf-8


class Data(object):
    def __init__(self, driver, *args, **kwargs):
        super(Data, self).__init__(*args, **kwargs)
        self.driver = driver

    def create_data(self):
        return self.driver.create_data()


class AtopDriver(object):
    def __init__(self, atop_file):
        super(AtopDataDriver, self).__init__()
        self.atop_file = atop_file

    def create_data(self):
        pass



