import threading
import time


class LoopThread(threading.Thread):
    n = 0

    def run(self):
        while self.n < 5:
            print(self.n)
            now_thread = threading.current_thread()
            print('[loop]now thread name : {0}'.format(now_thread.name))
            time.sleep(1)
            self.n += 1


if __name__ == '__main__':
    t = LoopThread(name='loop_thread_oop')
    t.start()
    t.join()
