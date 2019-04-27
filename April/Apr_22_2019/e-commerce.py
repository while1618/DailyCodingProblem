# This problem was asked by Twitter.
#
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Logger:
    def __init__(self, n):
        self.n = n

    def record(self, order_id):
        with open('ids.log', 'r+') as f:
            lines = [line for line in f][:self.n - 1]
            f.seek(0, 0)
            f.write(order_id + '\n' + ''.join(lines))
            f.close()

    def get_last(self, i):
        if i > self.n:
            return 'Index out of range'
        f = open('ids.log', 'r')
        for index, line in enumerate(f):
            if index == i - 1:
                return line


logger = Logger(3)
logger.record('72183')
logger.record('05928')
logger.record('55001')
logger.record('83728')
logger.record('43204')
logger.record('34955')
logger.record('12225')
print(logger.get_last(2))
print(logger.get_last(5))
