import MySQLdb as db
import threading
import bluetooth
from random import randint

blacklist=[]

def queryDataBase():
    global result
    threading.Timer(120.0, queryDataBase).start()
    HOST = "45.55.21.26"
    PORT = 3306
    USER = "root"
    PASSWORD = "1234567278"
    DB = "pruebabase"
    try:
        connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute("SELECT * from datos")
        result = dbhandler.fetchall()
        #print "Base de datos actualizada"
    except Exception as e:
        print e
    
    finally:
        connection.close()
        return result

def bluetoothScann():
    threading.Timer(30.0, bluetoothScann).start()
    #print "Realizando escaneo bluetooth"
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    #print "Escaneo terminado"
    available_devices = []
    for item in nearby_devices:
        for element in result:
            if item[0] == element[5]:
                available_devices.append((item[0],element[0]))
    sayHi(available_devices)

def sayHi(available_devices):
    number_devices = len(available_devices) - 1
    index = randint(0,number_devices)
    #print "Saludar a usuario con MAC %s" % (available_devices[index][0])
    if available_devices[index][0] not in blacklist: 
        #print "Saludando ..."
        blacklist.append(available_devices[index][0])
        print "Hola %s!" % available_devices[index][1]
        #print "Usuario agregado a blacklist para no repetir saludo"
        return 0
    #print "Usuario en blacklist, buscar otro usuario..."
    if (len(blacklist) == len(available_devices)):
        print "Ya no hay usuarios para saludar"
        return 0
    else:
        sayHi(available_devices)
    return 0


queryDataBase()
bluetoothScann()