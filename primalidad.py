#Compilador en línea
# https://www.programiz.com/python-programming/online-compiler/


#esta función reconoce el número primo con el cálculo:
#recorre la secuencia de números desde el #1 al número consultado (for)
#PLANTEA los LIMITES del recorrido e ignora para el contador
#PLANTEA la condición de DIVISIÓN, (módulo %=0)
#AGREGA +1 al contador por cada valor que NO ESTÉ en los valores LIMITE
#CONSIDERA true si no hay valores divisorios entre los límites (contador ==0)
#CONSIDERA false si hay valores divisorios entre los limites (es dividido por algún otro número)
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

    
#esta función hace la diferencia si es o no un numero primo
#depende de otra función (previa) que hace el cálculo
def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


#esta unción inicia el programa
if __name__ == '__main__':
    run()
