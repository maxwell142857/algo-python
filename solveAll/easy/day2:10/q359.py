class Logger:

    def __init__(self):
        self.content2T = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.content2T :
            self.content2T[message] = timestamp
            return True
        else:
            if self.content2T[message]+10 > timestamp:
                return False
            else:
                self.content2T[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)