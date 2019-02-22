import time


def wait_until(callable, interval=0.1, timeout=1):
    start = time.time()
    while not callable() and time.time() - start < timeout:
        time.sleep(interval)
    if time.time() - start > timeout:
        raise TimeoutError
