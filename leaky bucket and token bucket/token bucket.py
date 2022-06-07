# NAME : RAHUL AGRAWAL
# TOKEN BUCKET


from time import time
from threading import Lock
import sys
from time import sleep
import random


class TokenBucket:
    def __init__(self):
        self.tokens = 0
        self.rate = 0
        self.last = time()
        self.lock = Lock()

    def set_rate(self, rate):
        with self.lock:
            self.rate = rate
            self.tokens = self.rate

    def consume(self, tokens):
        with self.lock:
            if not self.rate:
                return 0
            now = time()
            lapse = now - self.last
            self.last = now
            self.tokens += lapse * self.rate
            if self.tokens > self.rate:
                self.tokens = self.rate
            self.tokens -= tokens
            if self.tokens >= 0:
                return 0
            else:
                return -self.tokens / self.rate

n = int(input('Enter no of packets: '))
bucket = TokenBucket()
rate = int(input('Enter rate:'))
bucket.set_rate(rate)
for i in range(n):
    nap = bucket.consume(rate)
    print('Nap time:',nap)
    sleep(nap)
    print('Passed packet -',i+1,' with size',rate)



