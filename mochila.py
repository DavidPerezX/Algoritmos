'''Se tiene una mochila de determinado tamaño y se desea ingresar una cantidad n de elementos que cada uno 
posee un peso y un valor, diseñar un algoritmo que introduzca los elementos que posean la mejor optimización
priorizando el valor que se llevará en total '''

#DPX

def mochila (tamano_mochila, peso, valor,n):
#Caso base: si ya no quedan elementos o si la mochila se llenó
    if n == 0 or tamano_mochila == 0: 
        return 0
#Segundo Caso base si el elemento pesa más que el tamaño del morral disponible       
    if peso [n-1] > tamano_mochila:
        return mochila(tamano_mochila, peso, valor,n-1)
#Comparando los elementos de la mochila y priorizando los de valor máximo    
    return max(valor[n-1]+mochila(tamano_mochila - peso[n-1],peso,valor,n-1),mochila(tamano_mochila,peso,valor,n-1))


if __name__ == '__main__':
    valor =[10,80,150,200,400]
    peso =[50,20,100,40,30]
    tamano_mochila =120
    n=len(valor)

    resultado = mochila(tamano_mochila, peso, valor,n)
    print(f"El mayor valor que se puede conseguir con una mochila de tamaño {tamano_mochila} es :",resultado)