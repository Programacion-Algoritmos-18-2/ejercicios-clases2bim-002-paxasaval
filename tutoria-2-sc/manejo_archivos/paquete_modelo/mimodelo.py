"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, nota1, nota2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1=int(nota1)
        self.nota2=int(nota2)

    def set_nota1(self,nota1):
        self.nota1=nota1

    def get_nota1(self):
        return self.nota1

    def set_nota2(self,nota2):
        self.nota2=nota2

    def get_nota2(self):
        return self.nota2


    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.get_nota1(), self.get_nota2())


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
    def obtener_promedio_n1(self):
        """ """
        suma=0
        for n in self.listado_personas:
            suma=suma+n.get_nota1()
        promedio=suma/len(self.listado_personas)
        return promedio
    def obtener_promedio_n2(self):
        """ """
        suma=0
        for n in self.listado_personas:
            suma=suma+n.get_nota2()
        promedio=suma/len(self.listado_personas)
        return promedio

    def obtener_notas1_menores_n(self,x):
        """ """
        lista=[]
        for n in self.listado_personas:
            if n.get_nota1()<x:
                #print("%sNombre: %s %-30sNota 1: %d\n"%(cadena,n.obtener_nombre(),n.obtener_apellido(),n.get_nota1()))
                lista.append(n)
        return lista

    def obtener_notas2_menores_n(self,x):
        """ """
        lista=[]

        for persona in self.listado_personas:
            if persona.get_nota2()<x:
                lista.append(persona)
        return lista

    def listar_por_caracter(self,x):
        lista=[]
        for persona in self.listado_personas:
            if persona.obtener_nombre()[0]==x:
                lista.append(persona)
        return lista


    def __str__(self):
        """ """
        cadena=""
        for n in self.listado_personas:
            cadena="%s%s %s\tNota1: %d\tNota2:%d\n"%(cadena,n.obtener_nombre(),n.obtener_apellido(),n.get_nota1(),n.get_nota2())
        return cadena
