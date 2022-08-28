import random
from cola import Cola

if __name__ == "__main__":
    cliente = Cola()
    clienteA = 0
    TiempoA = 0
    Reloj = 0
    cajero = False
    TMS = int(input('Ingrese la cantidad tiempo que quiera realizar la simulacion:'))
    while (Reloj <= TMS):
        if (random.uniform(0,1)>=0.5):
            cliente.insertar(TiempoA)
            if not cajero:
                if not cliente.vacio():
                    cliente.suprimir()
                    TiempoA += 5
                    clienteA += 1
                    cajero = True
            if TiempoA == 0:
                cajero = False
        if TiempoA > 0:
            TiempoA -= 1
        Reloj += 1
    
    print('\nLa cantidad de tiempo maxima de espera es: {} Minutos'.format(cliente.max()))