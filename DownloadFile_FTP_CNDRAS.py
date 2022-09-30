# -*- coding: utf-8 -*-
"""

@author: Equipo Analítica XM

Mediante este script se puede realizar la descarga de archivos contenidos en el servidor CNDRAS
en las carpetas públicas y privadas de este servidor FTP

En la parte inferior se especifica los campos que deben cambiarse para descargar los archivos del servidor

IMPORTANTE
La forma como está elaborado este script, es para descargar archivos unicamente de un mismo mes, si se requiere descargar archivos de varios meses se debe cambiar los parametros y ejecutar nuevamente.
"""

import urllib.request
import os

class Download_Files(object):
    
    def __init__(self):

        self.abspath = os.path.abspath(__file__)
        self.dname = os.path.dirname(self.abspath)
        self.usuario = 'XXXXX'   ########## Debe ingresarse el nombre de usuario asignado para descargar archivos del servidro FTP, por ejemplo el número de cédula
        self.contraseña = 'XXXXX'  ####### COntraeña asignada para el ingreso al servidor FTP del CNDRAS
        
        
    def get_file(self, anio, mes, dia, archivo, version, agente):
        try:
            archivo_dia = archivo + mes + dia
            print('ftp://' + self.usuario + ':' + self.contraseña + '@sv01.xm.com.co/Usuariosk/' + agente + '/SIC/COMERCIA/' + anio + '-' + mes + '/' + archivo_dia +'.' + version)
            print('files/' + archivo_dia +'.' + version)
            urllib.request.urlretrieve('ftp://' + self.usuario + ':' + self.contraseña + '@sv01.xm.com.co/Usuariosk/' + agente + '/SIC/COMERCIA/' + anio + '-' + mes + '/' + archivo_dia +'.' + version, 'files/' + archivo_dia +'.' + version)
            print('Archivo descargado: ' + archivo_dia + '.' + version)
        except:
            print("El archivo " + archivo_dia + '.' + version + " No se encuentra publicado o las credenciales de acceso son incorrectas")


    def get_files_range_days(self, anio, mes,dia_inicial, dia_final,  archivo, version, agente, ruta):
        
        os.makedirs(ruta + os.sep + 'files', exist_ok=True)
                
        for dia in range(dia_inicial, dia_final + 1):
            if dia < 10:
                numdia = '0' + str(dia)
            else:
                numdia = str(dia)
            
            if mes < 10:
                nummes = '0' + str(mes)
            else:
                nummes = str(mes)
                
            main.get_file(str(anio), nummes, numdia, archivo, version, agente)
            


        
        
if __name__ == '__main__':

    main = Download_Files()
    
    anio = 2022   #### Año al cual corresponde el archivo que se desea descargar
    mes = 9    ###  Mes al cual corresponde el archivo que se desea descargar
    dia_inicial = 1  ###  Día inicial del mes al cual corresponde el archivo que se desea descargar
    dia_final = 1   ###  Día inicial del mes al cual corresponde el archivo que se desea descargar
    archivo = 'aenc'  ###  Nombre del archivo soporte a la liquidación que se requiere descargar
    version = 'Tx2'  ###  Versión de la liquidación, correspondiente al archivo que se desea descargar
    agente = 'EPMC'  ###  Código SIC del agente al cual se requiere descargar archivos, por ejemplo EPMG, EPMC, CMMC; en caso de que corresponda a archivos publicos, se debe poner "Publico"

    ruta = r'D'  ##  Ruta del directorio donde se tiene descargado el script y donde se quiere que queden descargados los archivos.
    
    main.get_files_range_days(anio, mes,dia_inicial, dia_final,  archivo, version, agente, ruta)

