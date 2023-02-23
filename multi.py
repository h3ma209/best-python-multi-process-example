import time
import threading


class test(threading.Thread):
    def __init__(self, name,sleep_time=1):
        threading.Thread.__init__(self)
        self._stop = threading.Event()
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        print("Starting " + self.name)
        time.sleep(self.sleep_time)
        print("Ending " + self.name)


if __name__ == '__main__':
    t1 = test("Thread-1", 2)
    t1.start()
    t1._stop.set()
    
    t2 = test("Thread-2", 3)
    t2.start()
    t2._stop.set()

    t3 = test("Thread-3", 2)
    t3.start()
    t3._stop.set()

