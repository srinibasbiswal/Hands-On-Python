'''
A thread is a separate flow of execution. This means that your program will have two things happening at once. 
'''
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    # The info of thread is set to x
    x = threading.Thread(target=thread_function, args=(1,))
    #x = threading.Thread(target=thread_function, args=(1,),daemon = True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    #x.join() # The thread will join the main thread
    logging.info("Main    : all done")