import threading
import time



def hilo(i):
    """
 :param i: numero de hilo a efectos ilustrativos
 :return:  Nada
 """
    print ("[+] hilo %d\n" % i)
    time.sleep(3)
    print ("[-] hilo %d finalizado\n" % i)

# Se crea y Ejecuta el hilo 1 paralelo a hilo 2

simplethread=threading.Thread(target=hilo, args=[1])
simplethread.start()

# Ejecutado como proceso principal

hilo(2)
# Esperamos a que acabe el hilo paralelo 1