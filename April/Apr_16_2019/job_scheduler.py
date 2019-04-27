# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


import time


def job_scheduler(function, sleep):
    time.sleep(sleep / 1000)
    function()


def test_function():
    print('Hello')


job_scheduler(test_function, 5000)
