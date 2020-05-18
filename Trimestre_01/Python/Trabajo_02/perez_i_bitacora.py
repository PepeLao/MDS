# Módulo bitacora.py para manejar un archivo de texto como una bitácora
# Importa módulo os.
import os
#Importa módulo datetime.
import datetime as dt

def abrir_bitacora(nombre_archivo='bitacora.txt'):
    """Obtiene el Path del archivo. Sirve para Windows, Mac, Linux."""
    ruta_archivo=os.path.join(os.getcwd(),nombre_archivo)
    
    """Si el archivo existe:
         Abre el archivo en modo agregar data al final del archivo.
    """    
    if os.access(ruta_archivo, os.F_OK):
        puntero_archivo=open(ruta_archivo,'a')
    else:
        """Si el archivo no existe, lo crea y lo abre para escritura."""
        puntero_archivo=open(ruta_archivo,'w')
        
    """Retorna el puntero al archivo."""
    return puntero_archivo
        
def guardar_bitacora(puntero_archivo, mensaje='Hola mundo'):
    """Formatea la fecha y hora del mensaje"""
    fecha_hora = dt.datetime.now().strftime('[ %Y:%m:%d %H:%M ] ')
    """Formatea el registro a ser ingresado en el archivo."""
    registro=fecha_hora + mensaje + '\n'
    """Escribe el registro en el archivo """
    puntero_archivo.write(registro)


def cerrar_bitacora(puntero_archivo, mensaje='Fin del registro'):
    """Formatea la fecha y hora del mensaje"""
    fecha_hora = dt.datetime.now().strftime('[ %Y:%m:%d %H:%M ] ')
    """Formatea el registro a ser ingresado en el archivo."""
    registro=fecha_hora + mensaje + '\n'
    """Escribe el registro en el archivo """
    puntero_archivo.write(registro)
    """Cierra el archivo """
    puntero_archivo.close()

def mostrar_bitacora(nombre_archivo='bitacora.txt'):
    
    """Obtiene el Path del archivo. Sirve para Windows, Mac, Linux."""
    ruta_archivo=os.path.join(os.getcwd(),nombre_archivo)
    
    with open(ruta_archivo) as ptro:
        datos_leidos = ptro.read()
    
    return datos_leidos