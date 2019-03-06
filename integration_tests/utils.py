import hashlib
import time
from concurrent.futures import TimeoutError


def wait_until(callable, interval=0.1, timeout=1):
    start = time.time()
    while not callable() and time.time() - start < timeout:
        time.sleep(interval)
    if time.time() - start > timeout:
        raise TimeoutError


def files_match(f1, f2):
    with open(f1, 'rb') as file1, \
            open(f2, 'rb') as file2:
        hash1 = hashlib.md5(file1.read()).hexdigest()
        hash2 = hashlib.md5(file2.read()).hexdigest()
        assert hash1 == hash2
