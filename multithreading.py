# thread = a flow of execution. Like a separate order of instructions.
# threading = a module that provides a way to run multiple threads (function calls) simultaneously


import threading
import time

print(threading.active_count()) # Returns the number of threads currently running.
print(threading.enumerate())    # Returns a list of all threads currently running.
