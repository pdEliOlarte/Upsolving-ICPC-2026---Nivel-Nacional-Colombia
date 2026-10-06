# Problema  G Math United FC version Nacional Icpc 2026 Colombia
import sys 
import heapq
def solve():
    # Leo toda la informacion
    input_data = sys.stdin.read().split()
    #Con esta varible se va a guaradar el indice que se va a manejar manual,con la info
    index = 0
    # Se va a guardar la respuesta que va a salir, dado que son varios casos
    resultados =[]
    while index < len(input_data):
        # Se toman los dos valores principales, se usa index < pq se va a acceder a la posicion =1, 
        A = int(input_data[index])
        B = int(input_data[index +1])
        index += 2
        #Condicion Final
        if A == 0 and B == 0:
            break
        #Se va a manejar el MinHeap
        heap =[]
        # Se reoccre la B cantidad de numeros
        for _ in range(B):
            # Se toma un dato en especifico
            value = int(input_data[index])
            index += 1
            # Se verifica, si no es un prospecto se toma siempre
            if value > 0:
                A += value
            else:
            # Se toma el prospecto, dado que value es negativo, sumar resta
                A += value
                heapq.heappush(heap, -value)
                if A < 0:
                    # Si A se convierte negativo, sacamos el que tiene mayor costo, para maximizar A.
                    peor_costo = heapq.heappop(heap)
                    A+= peor_costo
        # Se guarda el resultado de la cantidad de prospectos que se tomaron
        resultados.append(str(len(heap)))
    print("\n".join(resultados))

solve()




