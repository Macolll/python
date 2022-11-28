import sqlite3 as sql
import os


ruta = os.getcwd()#ruta actual 
#concatenar de manera inteligente \
file_path = os.path.join(ruta,'repo','proyectoclinicaa','CLINICA.db')

mi_co=sql.connect(file_path)
cursor=mi_co.cursor()
cursor.execute(
       """create table if not exists paciente(
        DNI integer primary key,
        primer_nombre text,
        segundo_nombre text,
        primer_apellido text,
        segundo_apellido text,
        edad integer
        )""")
cursor.execute(
       """create table if not exists medico(
        DNI integer primary key ,
        primer_nombre text,
        segundo_nombre text,
        primer_apellido text,
        segundo_apellido text
        )""")

    
cursor.execute(
       """create table if not exists registro_examen(
        id_registro integer primary key autoincrement,
        DNI_paciente integer,
        DNI_medico integer,
        tipode_analisis text,
        tipode_examen  text,
        fecha text,
        foreign key(DNI_paciente)  references paciente(DNI),
        foreign key(DNI_medico) references medico(DNI)
        
        )""")

    
