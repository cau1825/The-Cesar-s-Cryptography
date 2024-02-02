
def cifradoCesar13(MensajeInput):
    #Se declara la variable mensaje para guardar el texto recibido
    mensaje = MensajeInput
    #La variable diccionario cuenta con las letras del alfabeto
    diccionario="abcdefghijklmnopqrstuvwxtz"
    #La variable auxiliar nos permite guardar la iteraccion para crear el mensaje encriptado
    auxiliar=""
    for i in mensaje:
        #se lee cada elemento  de la variable  para buscarlo en la variable diccionario se suman 13 ya que esa es la clave del cifrado y usa el modulo para estar iterando en el diccionario
        auxiliar = auxiliar +  diccionario[(diccionario.find(i) + 13) % len(diccionario)]
    print(f"El mensaje cifrado es: {auxiliar}")
    
def descifradoCesar13(MensajeInputCifrado):
    #Se declara la variable mensaje para guardar el texto recibido
    mensaje = MensajeInputCifrado
    #La variable diccionario cuenta con las letras del alfabeto
    diccionario="abcdefghijklmnopqrstuvwxtz"
    
    #La variable auxiliar nos permite guardar la iteraccion para crear el mensaje encriptado
    auxiliar=""
    for i in mensaje:
        #se lee cada elemento  de la variable  para buscarlo en la variable diccionario se restan 13 ya que esa es la clave del cifrado y usa el modulo para estar iterando en el diccionario
        auxiliar = auxiliar +  diccionario[(diccionario.find(i) - 13) % len(diccionario)]
    print(auxiliar)

if __name__ == "__main__":
   #cifradoCesar13(input("Escriba su mensaje sin espacios ni la letra ñ: "))
   #descifradoCesar13("ubtn")