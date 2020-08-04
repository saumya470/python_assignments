# Current thread is MainThread which the Python interpretor creates at runtime. Below is the code to check.

import threading

print('Current thread:',  threading.currentThread().getName())  # This will give you the current thread

# To compare it wilth main Thread without getting the name - used to check when using multiple threading


if threading.currentThread() == threading.main_thread():
    print('Main thread')
else:
    print('Some other thread')

