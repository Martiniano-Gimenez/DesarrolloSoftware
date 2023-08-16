import random

def generar_lista_de_atletas():
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

def mostrar_atletas(lista_atletas):
    print("------------------------------------------------------ATLETAS----------------------------------------------------------------------\n")
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']} - : {atleta['tiempo_llegada']} segundos")
 
def atleta_ganador(lista_atletas):
    ganador = None
    tiempo_ganador = float('inf')
    for atletas in lista_atletas:
        if atletas['tiempo_llegada'] < tiempo_ganador:
            ganador = atletas['numero']
            tiempo_ganador = atletas['tiempo_llegada']
    return ganador

def datos_atleta(numero_atleta,lista_atletas):
    for atleta in lista_atletas:
        if atleta['numero'] == numero_atleta:
            print(f"Nombre: {atleta['nombre']}\nNumero: {atleta['numero']}\nTiempo de llegada: {atleta['tiempo_llegada']}")

if __name__ == '__main__':
    lista_atletas = generar_lista_de_atletas()
    mostrar_atletas(lista_atletas)
    
    print("\n--------------------------------GANADOR--------------------------------------\n")
    ganador = atleta_ganador(lista_atletas)
    print(f"El ganador es el atleta con numero: {ganador}")
    
    print("\n--------------------------------ATLETA---------------------------------------\n")
    num_atleta = int(input("Ingrese el numero del atleta a buscar: "))
    datos_atleta(num_atleta,lista_atletas)