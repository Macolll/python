
import re
class Registrar_examen:

    
    
    DNI_p=""

    primer_nombre_p=""
    
    segundo_nombre_p="" 
   
    primer_apellido_p=""
    
    segundo_apellido_p=""
    
    edad_p=""
    
    DNI_m=""
    
    primer_nombre_m=""
    
    segundo_nombre_m =""
    
    primer_apellido_m =""
    
    segundo_apellido_m=""
    tipoanalisis=""
    tipoexamen=""
    cod_registro=""
    fecha=""
    
   
    
    
    def registrar_datos(self):
    
        print("\nIngrese los datos del paciente")
        
        patron = ('[0-9]{8}')

        ip = re.compile(patron)
        __class__.DNI_p=(input("DNI: "))
        while (ip.search(__class__.DNI_p)==None or len(__class__.DNI_p)>8):
          __class__.DNI_p=input("ingresa corectamente el DNI: ")
        __class__.DNI_p=int(__class__.DNI_p)
        __class__.primer_nombre_p=input("primer nombre: ")
        while (__class__.primer_nombre_p.isalpha()==False):
           __class__.primer_nombre_p=input("ingresa correctamente el primer nombre: ")
        __class__.segundo_nombre_p =input("segundo nombtre: ")
        while (__class__.primer_nombre_p.isalpha()==False):
           __class__.segundo_nombre_p=input("ingresa correctamente el segundo nombre: ")
        
        __class__.primer_apellido_p =input("primer apellido: ")
        while (__class__.primer_apellido_p.isalpha()==False):
           __class__.primer_apellido_p=input("ingresa correctamente el primer  apellido: ")
        
        __class__.segundo_apellido_p =input("segundo apellido: ")
        while (__class__.segundo_apellido_p.isalpha()==False):
           __class__.segundo_apellido_p=input("ingresa correctamente el segundo  apellido: ")
        
        __class__.edad_p=input("edad: ")
        while (__class__.edad_p.isdigit()==False or __class__.edad_p.startswith("0")==True):
          __class__.edad_p=input("ingresa correctamente la edad")
        __class__.edad_p=int(__class__.edad_p)
  
        print("\nIngrese los datos del medico")
        


        while (ip.search(__class__.DNI_m)==None or len(__class__.DNI_m)>8):
          __class__.DNI_m=input("ingresa corectamente el DNI: ")
        __class__.DNI_m=int(__class__.DNI_m)
        __class__.primer_nombre_m=input("primer nombre: ")
        while (__class__.primer_nombre_m.isalpha()==False):
           __class__.primer_nombre_m=input("ingresa correctamente el primer nombre: ")
        __class__.segundo_nombre_m =input("segundo nombtre: ")
        while (__class__.primer_nombre_m.isalpha()==False):
           __class__.segundo_nombre_m=input("ingresa correctamente el segundo nombre: ")
        
        __class__.primer_apellido_m =input("primer apellido: ")
        while (__class__.primer_apellido_m.isalpha()==False):
           __class__.primer_apellido_m=input("ingresa correctamente el primer  apellido: ")
        
        __class__.segundo_apellido_m =input("segundo apellido: ")
        while (__class__.segundo_apellido_m.isalpha()==False):
           __class__.segundo_apellido_m=input("ingresa correctamente el segundo  apellido: ")
        
        
    
       
        __class__.tipoanalisis=input("""Ingrese el tipo de analisis a realizarce:
       
        a)BIOQUIMICA
        b)HEMATOLOGIA
        c)HORMONAS
=>""")
        if (__class__.tipoanalisis.isalpha()==False or len(__class__.tipoanalisis)>1):
            __class__.tipoanalisis=input("""Ingrese correctamente el tipo de analisis a realizarce:
       
        a)BIOQUIMICA
        b)HEMATOLOGIA
        c)HORMONAS
=>""")
        
        c=1
        if __class__.tipoanalisis=="a":
            __class__.tipoanalisis="BIOQUIMICA"
            __class__.tipoexamen=input("""\nIngrese el tipo de examen BIOQUIMICO  a realizarce:
            
            1) Ácido úrico en la sangre
            2) Alanina aminotransferasa (ALT)
            3) Albúmina
            4) Aspartato aminotransferasa (AST) 
            5) Bilirrubina (total y directa)
            6) Calcio (Ca) en la sangre 
            7) Cloruro (Cl) 
            8) Depuración de la creatinina  
=>""")      
            
            while __class__.tipoexamen not in ["1","2","3","4","5","6","7","8"]:
                __class__.tipoexamen=input("""\nIngrese correctamente el tipo de examen BIOQUIMICO  a realizarce:
            
            1) Ácido úrico en la sangre
            2) Alanina aminotransferasa (ALT)
            3) Albúmina
            4) Aspartato aminotransferasa (AST) 
            5) Bilirrubina (total y directa)
            6) Calcio (Ca) en la sangre 
            7) Cloruro (Cl) 
            8) Depuración de la creatinina  
=>""")
            
            li=["Ácido úrico en la sangre","Alanina aminotransferasa (ALT)","Albúmina","Aspartato aminotransferasa (AST)","Bilirrubina (total y directa)","Calcio (Ca) en la sangre","Cloruro (Cl)","Depuración de la creatinina"]
            
            for i in li:
                
                if __class__.tipoexamen==str(c):
                

                    __class__.tipoexamen=f"{i}"
                c+=1
                
        elif __class__.tipoanalisis=="b":
            __class__.tipoanalisis="HEMATOLOGIA"
            __class__.tipoexamen=input("""\nIngrese el tipo de examen HEMATOLOGICO  a realizarce:
            
            1) Recuento de globulos blancos 
            2) Recuento de globulos rojos 
            3) Volumen de globulos rojos en el hematocrito
            4) Recuento de plaquetas
            5) Concentración de hemoglobina (HB)
            6) Recuento diferencial de glóbulos blancos
            7) Índice de globulos rojos (mediciones)
=>""")
            while __class__.tipoexamen not in ["1","2","3","4","5","6","7"]:
                __class__.tipoexamen=input("""\nIngrese correctamente el tipo de examen HEMATOLOGICO  a realizarce:
            
            1) Recuento de globulos blancos 
            2) Recuento de globulos rojos 
            3) Volumen de globulos rojos en el hematocrito
            4) Recuento de plaquetas
            5) Concentración de hemoglobina (HB)
            6) Recuento diferencial de glóbulos blancos
            7) Índice de globulos rojos (mediciones)
=>""")
            lis=["Recuento de globulos blancos","Recuento de globulos rojos","Volumen de globulos rojos en el hematocrito","Recuento de plaquetas","Concentración de hemoglobina (HB)","Recuento diferencial de glóbulos blancos","Índice de globulos rojos (mediciones)"]
            for i in lis:
                
                if __class__.tipoexamen==str(c):
                
                    
                    __class__.tipoexamen=f"{i}"
                c+=1
                
        else  :
            __class__.tipoanalisis="HORMONAS"
            __class__.tipoexamen=input("""\nEscoja el tipo de examen HORMONAL a realizarce:

            1) Hormona Adrenocorticotropa en Plasma (ACTH)
            2) Hormona Antidiurética
            3) Androstendiona
            4) Testosterona libre
            5) Dehidroepiandrosterona
            6) FSH (hormona foliculoestimulante)
            7) LH (hormona luteinizante)
=>""")      
            while __class__.tipoexamen not in ["1","2","3","4","5","6","7"]:
                __class__.tipoexamen=input("""\nIngrese correctamente el tipo de examen HORMONAL a realizarce:

            1) Hormona Adrenocorticotropa en Plasma (ACTH)
            2) Hormona Antidiurética
            3) Androstendiona
            4) Testosterona libre
            5) Dehidroepiandrosterona
            6) FSH (hormona foliculoestimulante)
            7) LH (hormona luteinizante)
=>""")
            liis=["Hormona Adrenocorticotropa en Plasma (ACTH)","Hormona Antidiurética","Androstendiona","Testosterona libre","Dehidroepiandrosterona","FSH (hormona foliculoestimulante)","LH (hormona luteinizante)"]
            for i in liis:
                
                if __class__.tipoexamen==str(c):

                    __class__.tipoexamen=f"{i}"
                c+=1
                
        __class__.fecha=input("""Ingrese la fecha del examen a realizarce,tenga en cuenta el formato(dd/mm/aaaa):
        =>""")
        patron1=re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')

        while patron1.search(__class__.fecha)==None:
            __class__.fecha=input("""Ingrese correctamente la fecha del examen a realizarce,tenga en cuenta el formato(dd/mm/aaaa):
        =>""")



