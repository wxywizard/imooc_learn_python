import threading
import time


def loop():
    n = 0
    while n < 5:
        print(n)
        now_thread = threading.current_thread()
        print('[loop]now thread name : {0}'.format(now_thread.name))
        time.sleep(1)
        n += 1


def use_thread():
    now_thread = threading.current_thread()
    print('now thread name : {0}'.format(now_thread.name))
    t = threading.Thread(target=loop, name='loop_thread')
    # 启动线程
    t.start()
    # 挂起线程
    t.join()


if __name__ == '__main__':
    use_thread()