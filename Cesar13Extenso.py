#Se declara la variable mensaje para guardar el texto recibido

#La variable diccionario cuenta con las letras del alfabeto
diccionario="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/"
    #La variable auxiliar nos permite guardar la iteraccion para crear el mensaje encriptado

auxiliar=""
#Recorremos cada elemento del mensaje que nos ingresa el usuario
print("Cifrado Cesar 13 Extenso")
print("1.Encriptar Mensaje")
print("2.Desencriptar Mensaje")
opcion= input("Selecciona una opcion:  ")
opcion= int(opcion)
if opcion== 1:
    mensaje = input("Escibre el mensaja a Encriptar: ")
    for elemento in mensaje:
    #Si el elemento se encuenta en el mensaje lo buscamos en el diccionario y lo guardarmos en la variable diccionarioIndice
        if elemento in mensaje:
            #almacenamos la busqueda del elemento del mensaje en la variable diccionarioIndice
            diccionarioIndice = diccionario.find(elemento)
            auxiliarIndice = diccionarioIndice + 13
            if auxiliarIndice >= len(diccionario):
                auxiliarIndice = auxiliarIndice - len(diccionario)
            elif auxiliarIndice <=0:
                auxiliarIndice = auxiliarIndice + len(diccionario)    
            auxiliar = auxiliar +  diccionario[auxiliarIndice]
    
        else: 
            auxiliar = auxiliar + elemento
    print(f"El mensaje desencriptado es:  {auxiliar}" )

elif opcion== 2:
    mensaje = input("Escibre el mensaja a Descriptar: ")
    for elemento in mensaje:
        #Si el elemento se encuenta en el mensaje lo buscamos en el diccionario y lo guardarmos en la variable diccionarioIndice
            if elemento in mensaje:
                #almacenamos la busqueda del elemento del mensaje en la variable diccionarioIndice
                diccionarioIndice = diccionario.find(elemento)
                auxiliarIndice = diccionarioIndice - 13
                auxiliar = auxiliar +  diccionario[auxiliarIndice]
            else: 
                auxiliar= auxiliar + elemento           
    print(f"El mensaje desencriptado es:  {auxiliar}" )