#Custom Exception
class ApplicationException(Exception):
    def __init__(self, args):
        self.msg = args
