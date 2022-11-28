
from conectando import *
from registrando import *



class Registro_db_clinica:

    
    
    
    Registrar_examen().registrar_datos()
    
    def guardardatosen_tabla_paciente(self):
        cursor.execute(f"insert into paciente(DNI,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,edad) values ({Registrar_examen.DNI_p},'{Registrar_examen.primer_nombre_p}','{Registrar_examen.segundo_nombre_p}','{Registrar_examen.primer_apellido_p}','{Registrar_examen.segundo_apellido_p}',{Registrar_examen.edad_p})")
        mi_co.commit()
    def guardardatosen_tabla_medico(self):
        cursor.execute(f"insert into medico(DNI,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido) values ({Registrar_examen.DNI_m},'{Registrar_examen.primer_nombre_m}','{Registrar_examen.segundo_nombre_m}','{Registrar_examen.primer_apellido_m}','{Registrar_examen.segundo_apellido_m}')")
        mi_co.commit()
    def guardardatosen_tabla_registroexamen(self):
        cursor.execute(f"insert into registro_examen(id_registro,DNI_paciente,DNI_medico,tipode_analisis,tipode_examen,fecha) values (null,{Registrar_examen.DNI_p},{Registrar_examen.DNI_m},'{Registrar_examen.tipoanalisis}','{Registrar_examen.tipoexamen}','{Registrar_examen.fecha}')")
        mi_co.commit()
    def mostrar_registro(self):
        cursor.execute("select * from  registro_examen")
        datos=cursor.fetchall()
        mi_co.commit()
        print("id_registro |DNI_paciente |DNI_medico |tipode_analisis |tipode_examen                                   |fecha")
        for i in datos:
            print(i)
            
    def __del__(self):
        mi_co.close()
    
o=Registro_db_clinica()
o.guardardatosen_tabla_paciente()
o.guardardatosen_tabla_medico()
o.guardardatosen_tabla_registroexamen()
o.mostrar_registro()






