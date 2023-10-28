import queue
import time
import random
import threading

# COLA DE PRIORIDADES
cola = queue.PriorityQueue()

# FUNCION PARA CONTROLAR LAS INTERRUPCIONES
def manejador_interrupciones():
    while True:
        tarea, prioridad, a, b, mensaje = cola.get()
        resultado = tarea(a, b)
        print(f"{mensaje}: {tarea.__name__}({a}, {b}) = {resultado}")
        cola.task_done()

# CREACION DE HILO
hilos = [threading.Thread(target=manejador_interrupciones) for _ in range(4)]

# INICIAR EL HILO
for hilo in hilos:
    hilo.start()

# FUNCIONES DE OPERACIONES RESTA, SUMA, DIVISION Y MULTIPLICACION
def resta(a, b):
    return a - b

def suma(a, b):
    return a + b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def multiplicacion(a, b):
    return a * b

# CICLOS
prioridades = [
    (resta, 4, "Ejecución de proceso"),
    (suma, 3, "Interrupción de prioridad 3"),
    (division, 2, "Interrupción de prioridad 2"),
    (multiplicacion, 1, "Interrupción de prioridad 1")
]

ciclo_principal = True

while True:
    ciclo_actual = prioridades if ciclo_principal else list(reversed(prioridades))
    for i, (operacion, prioridad, mensaje) in enumerate(ciclo_actual):
        a, b = random.randint(1, 100), random.randint(1, 100)
        cola.put((operacion, prioridad, a, b, mensaje))
        time.sleep(0.1)  
    
    ciclo_principal = not ciclo_principal
