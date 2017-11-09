#!/usr/bin/python

import threading
import time


def procesador(i):
    
    
    """
 :param i: numero de procesador a efectos ilustrativos
 :return: nada
 """
    print ("[+] En procesador  %d\n" % i)
    time.sleep(3)
    print ("[-] procesador %d finalizado\n" % i)

# Creacion y Ejecucion de 1 procesador paralelo a procesador 2

simplethread=threading.Thread(target=procesador, args=[1])
simplethread.start()

# Esto se ejecuta como proceso principal

procesador(2)
# Esperamos a que acabe el procesador paralelo 1
simplethread.join()