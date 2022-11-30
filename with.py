# コンテキストマネージャーのお勉強 (contextlib を使わない方法と使う方法)
# (『Pythonトリック』2.3 の課題)

import time

class Timer:
    def __init__(self):
        pass
    def __enter__(self):
        self.time_strt = time.time()
    def __exit__(self, dmy1, dmy2, dmy3):
        self.time_end = time.time()
        print(self.time_end - self.time_strt)

with Timer():
    time.sleep(5)


from contextlib import contextmanager

@contextmanager
def timer():
    try:
        time_strt = time.time()
        yield 'dmy'
    finally:
        time_end = time.time()
        print(time_end - time_strt)

with timer():
    time.sleep(3)
