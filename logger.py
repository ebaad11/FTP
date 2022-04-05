# class for logging requests/response from the client and server
from datetime import datetime
from os import path, mkdir


class logger:
    def __init__(self):
        today = datetime.today()

        self.file = 'log-' + today.strftime('%m%d%Y') + '.txt'

        # error handeling not added because of time constraints
        self.outStremam = open(self.file, 'a+')


def info(self, msg):
    self.today = logger.GetDate()
    self.outStremam.write(f'{self.today} - {msg}\n')


if __name__ == "__main__":
    loggerFile = logger()

    loggerFile.info("hello")
