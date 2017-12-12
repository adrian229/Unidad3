#!/usr/bin/python

import threading
import time

NTHREADS=20
WIDTH=1

sem=Semaphore(WIDTH)

def hilo(i):
    """
 :param i: numero de hilo a efectos ilustrativos
 :return: nada
 """
    print ("[+] En hilo %d\n" % i)
    time.sleep(3)
    sem.acquire()
    print ("[+] En tunel hilo %d\n" % i)
    time.sleep(1)
    sem.release()
    print ("[-] hilo %d, estoy fuera\n" % i)

simplethread=[]
for i in range(NTHREADS):
    # arranque y comienzo de hilo num i+1
 simplethread.append(threading.Thread(target=hilo, args=[i+1]))
 simplethread[-1].start()

for i in range(NTHREADS):
    # esperamos que acabe el hilo num i
 simplethread[i].join()

print ("[*] all threads finished")