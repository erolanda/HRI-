# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import MySQLdb as db
import threading

def queryDataBase():
    global result
    threading.Timer(5.0, queryDataBase).start()
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
        print "Datos actualizados"
    except Exception as e:
        print e
    
    finally:
        connection.close()
        return result


queryDataBase()
for item in result:
    print item