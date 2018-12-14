from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]

lista_personas=[]
p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0], lista[1][4], lista[1][5])
for d in lista:
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    lista_personas.append(p)
operaciones=OperacionesPersona(lista_personas)
#print("Promedio nota1: "+str(operaciones.obtener_promedio_n1())+"\n"+"Promedio nota2: "+str(operaciones.obtener_promedio_n2()))
print(OperacionesPersona(operaciones.obtener_notas1_menores_n(15)))#Creamos un objeto OperacionesPersona que recibe de atributo la lista obtenida por el metodo obtener_notas1_menores_a_n que a su vez recibe de entrada el valor 15 y devuelve una lsita de personas cuya nota 1 es menor a 15
print(OperacionesPersona(operaciones.obtener_notas2_menores_n(15)))#Creamos un objeto OperacionesPersona que recibe de atributo la lista obtenida por el metodo obtener_notas2_menores_a_n que a su vez recibe de entrada el valor 15 y devuelve una lista de personas cuya nota 2 es menor a 15
print(OperacionesPersona(operaciones.listar_por_caracter("R")))#Creamos un objeto de OperacionesPersona que recibe de atributo la lista de obtenida por el metodo listar_por_caracter que a su vez recibe de entrada el caracter "R" y devuelve una lista de persona cuyo nombre empieza con "R"
print(OperacionesPersona(operaciones.listar_por_caracter("J")))#Creamos un objeto de OperacionesPersona que recibe de atributo la lista de obtenida por el metodo listar_por_caracter que a su vez recibe de entrada el caracter "J" y devuelve una lista de persona cuyo nombre empieza con "J"
