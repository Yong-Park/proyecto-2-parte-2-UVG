from csv import reader
from neo import HelloWorldExample
import sys

# Proyecto 2
# Estructuras de Datos
# Yong Bum Park 20117
# Pedro Pablo Arriola Jimenez 20188
# Oscar Fernando Lopez Barrios 20679

# Variables que guardaran los datos de la comida 
# y los datos elegidos por el usuario
food =[]
foodCounter=[]
price =[]
time =[]
nutricion =[]
relation =[]
platillos=[]
# Los distintos tipos de elecciones
timeGeneral=["rapido","medio","lento"]
nutricionGeneral=["alta","media","baja"]
priceGeneral=["alto","medio","bajo"]

# Se guarda la eleccion del usuario
myfood = "-"
myprice = "-"
mytime= "-"
mynutricion= "-"

# Listas donde se guarda la recomendacion
foodInterest=[]
timeInterest=[]
priceInterest=[]
nutricionInterest=[]

#usuarios
user=[]
password=[]
maindish=[]

# Se leen los datos y se separan por medio de su categoria
with open('export.csv', 'r') as csvDataFile:    
    csvReader = reader(csvDataFile)
    # Se crea un ciclo para agregar los parametros
    i=0
    for row in csvReader:
        # Se agregan los parametros de busqueda
        food.append(row[0])
        foodCounter.append(0)
        price.append(row[1])
        time.append(row[2])
        nutricion.append(row[3])
        relation.append(row[4])

        #Se guardan los tipos de platillos que existen
        if(i!=0):
            foodtype = row[4].split()
            for add in foodtype:
                # Si se contiene el tipo de platillo se guarda
                if(list.__contains__(platillos,add)):
                    True
                else:
                    platillos.append(add)
        else:
            i=i+1



print("Inicializando la Base de Datos...")
greeter = HelloWorldExample.Constructor(HelloWorldExample, "bolt://34.205.171.52:7687", "light-mirrors-plants")

#funcion dle menu
def menu_function(indice_user_recieved):
    menu = True
    while menu:
        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴\n")
        print("Bienvenido al Sistema de Recomendacion de Alimentos")
        print("___________________________________")
        print("Tiene las siguientes opciones:")
        print("1. Recibir Recomendacion de comida")
        print("2. Agregar Nuevo Platillo")
        print("3. Remover Platillo")
        print("4. Salir del programa\n")
        
        opcionprincipal =  input("Ingrese la opcion: ")
            
        if(int(opcionprincipal) == 1):
            print("1. Seleccionar ingredientes principales")
            print("2. Seleccionar tiempo de entrega")
            print("3. Seleccionar contenido nutricional")
            print("4. Seleccionar precio")
            print("5. Buscar listado de recomendaciones")
            print("6. Regresar al inicio\n")
            
            opcion = input("Ingrese una opcion: ")
            print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

            # Se escogen los tipos de ingredientes para los platos del usuario
            if(opcion=="1"):
                
                # Se muestran los platillos disponibles para el usuario
                comida = True
                while(comida):
                    for tipoPlatillo in platillos:
                        print("\n------- INGREDIENTES -------\n")
                        print(tipoPlatillo)
                        print("1. Agregar ingrediente a la lista")
                        print("2. Siguiente ingrediente")
                        print("3. Regresar al menu principal\n")
                        
                        op = input("Ingrese una opcion: ")
                        if(op=="1"):
                            myfood = tipoPlatillo
                            comida = False
                            break
                        elif(op=="2"):
                            True
                        elif(op=="3"):
                            comida=False
                            break
                        else:
                            print("Error, ingresa solo del 1-3")
                        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

                print("\n\n___________________________________")
                print("Ingredientes escogidos:")
                print(myfood)
                print("Tiempos de preparacion escogidos:")
                print(mytime)
                print("Contenidos Nutrcionales escogidos:")
                print(mynutricion)
                print("Precios escogidos:")
                print(myprice)
                    
            #escoger tiempo
            elif(opcion=="2"):
                tiempo = True
                while tiempo:
                    for tipoTiempo in timeGeneral:
                            print("\n------- TIEMPO DE PREPARACION -------\n")
                            print(tipoTiempo)
                            print("1. Seleccionar tiempo de preparacion")
                            print("2. Siguiente opcion")
                            print("3. Regresar al menu principal\n")
                            op = input("Ingrese una opcion: ")
                            if(op=="1"):
                                mytime = tipoTiempo
                                tiempo = False
                                break
                            elif(op=="2"):
                                True
                            elif(op=="3"):
                                tiempo=False
                                break
                            else:
                                print("Error, ingresa solo del 1-3")
                            print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

                print("\n\n___________________________________")
                print("Ingredientes escogidos:")
                print(myfood)
                print("Tiempos de preparacion escogidos:")
                print(mytime)
                print("Contenidos Nutrcionales escogidos:")
                print(mynutricion)
                print("Precios escogidos:")
                print(myprice)
                
            #escoger contenido nutricional
            elif(opcion=="3"):
                nutri = True
                while nutri:
                    for tipoNutricion in nutricionGeneral:
                            print("\n------- CONTENIDO NUTRICIONAL -------\n")
                            print(tipoNutricion)
                            print("1. Agregar el contenido nutricional deseado a la lista")
                            print("2. Siguiente opcion de contenido nutricional")
                            print("3. Regresar al menu principal\n")
                            op = input("Ingrese una opcion: ")
                            if(op=="1"):
                                mynutricion = tipoNutricion
                                nutri = False
                                break
                            elif(op=="2"):
                                True
                            elif(op=="3"):
                                nutri=False
                                break
                            else:
                                print("Error ingresa solo del 1-3")
                            print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

                print("\n\n___________________________________")
                print("Ingredientes escogidos:")
                print(myfood)
                print("Tiempos de preparacion escogidos:")
                print(mytime)
                print("Contenidos Nutrcionales escogidos:")
                print(mynutricion)
                print("Precios escogidos:")
                print(myprice)
            
            #escoger precio
            elif(opcion=="4"):
                precio = True
                while precio:
                    for tipoPrecio in priceGeneral:
                            print("\n------- PRECIO -------\n")
                            print(tipoPrecio)
                            print("1. Agregar el tipo de precio deseado a la lista")
                            print("2. Siguiente opcion de tipo de precio")
                            print("3. Regresar al menu principal\n")
                            op = input("Ingrese una opcion: ")
                            if(op=="1"):
                                myprice = tipoPrecio
                                precio = False
                                break
                            elif(op=="2"):
                                True
                            elif(op=="3"):
                                precio=False
                                break
                            else:
                                print("Error ingresa solo del 1-3")
                            print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

                print("\n\n___________________________________")
                print("Ingredientes escogidos:")
                print(myfood)
                print("Tiempos de preparacion escogidos:")
                print(mytime)
                print("Contenidos Nutrcionales escogidos:")
                print(mynutricion)
                print("Precios escogidos:")
                print(myprice)

            #buscar platillos que satisfacen con lo que se desea
            elif(opcion=="5"):
                HelloWorldExample.find_node(greeter,"alto", "rapido", "alta", "mariscos")
                """
                nutricioncopy=[]
                #limpiar el original
                foodInterest.clear()
                timeInterest.clear()
                priceInterest.clear()
                nutricionInterest.clear()

                #para el tipo de platillo
                if(len(myfood)!=0):
                    i=0
                    for types in relation:
                        for cliente in myfood:
                            if(types.__contains__(cliente)):
                                if(foodInterest.__contains__(food[i])):
                                    True
                                else:
                                    #original
                                    foodInterest.append(food[i])
                                    timeInterest.append(time[i])   
                                    priceInterest.append(price[i])   
                                    nutricionInterest.append(str(nutricion[i]))                 
                        #aumentar
                        i=i+1 
                
                #para el tiempo
                if(len(mytime)!=0):
                    i=0
                    for types in timeInterest:
                        yes=0
                        for cliente in mytime:
                            if(types.__contains__(cliente)):
                                yes = yes + 1
                        #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                        if(yes==0):
                            indice = foodInterest.index(foodInterest[i])
                            foodInterest[indice]= "0"
                            timeInterest[indice]= "0"
                            priceInterest[indice]= "0"
                            nutricionInterest[indice]= "0"
                        #aumentar
                        i=i+1

                #para nutricion 
                if(len(mynutricion)!=0):
                    i=0
                    for types in nutricionInterest:
                        yes=0
                        for cliente in mynutricion:
                            if(types.__contains__(cliente)):
                                yes = yes + 1
                        #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                        if(yes==0):
                            indice = foodInterest.index(foodInterest[i])
                            foodInterest[indice]= "0"
                            timeInterest[indice]= "0"
                            priceInterest[indice]= "0"
                            nutricionInterest[indice]= "0"
                        #aumentar
                        i=i+1

                #para precio
                if(len(myprice)!=0):
                    i=0
                    for types in priceInterest:
                        yes=0
                        for cliente in myprice:
                            if(types.__contains__(cliente)):
                                yes = yes + 1
                        #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                        if(yes==0):
                            indice = foodInterest.index(foodInterest[i])
                            foodInterest[indice]= "0"
                            timeInterest[indice]= "0"
                            priceInterest[indice]= "0"
                            nutricionInterest[indice]= "0"
                        #aumentar
                        i=i+1

                #mostar resultado final
                print("\n\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴 RECOMENDACIONES EN BASE A SU BUSQUEDA 🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴\n")
                for plato in foodInterest:
                    if(plato!="0"):
                        print(plato)
                        food_index=food.index(plato)
                        data = foodCounter[food_index]
                        data = data + 1
                        foodCounter.insert(food_index, data)

                maindish.insert(int(indice_user_recieved),foodInterest)"""
                
            #terminar el ciclo
            elif(opcion=="6"):
                print("\n🍴 Vuelve pronto al sistema de recomendaciones alimenticias 🍴\n")
                menu=False
            #mostrar error
            else:
                print("Error, Ingrese solo del 1-6") 
        
        #Opcion para poder agregar un nuevo platillo a la base de datos.
        elif(int(opcionprincipal) == 2):
            
            nombre = ""
            precio = ""
            tiempo = ""
            nutricion = ""
            relacion = ""
            opcion = ""
            
            print("Ingresa el nombre del platillo que desea agregar:\n")
            nombre = input("")
            nombre.lower()
            
            print("Ingresa el precio del platillo que desea agregar:")
            print("1. Bajo")
            print("2. Medio")
            print("3. Alto\n")
            
            verificador = False

            while(verificador == False):
                
                opcion = input("")
                
                if(opcion == "1"):
                    precio = "bajo"
                    verificador = True
                elif(opcion == "2"):
                    precio = "medio"
                    verificador = True
                elif(opcion == "3"):
                    precio = "alto"
                    verificador = True
                else:
                    print("\nOpcion no valida, ingrese uno existente\n")

                
            print("Ingresa el tiempo de preparacion del platillo que desea agregar:")
            print("1. Lento")
            print("2. Medio")
            print("3. Rapido\n")

            verificador = False

            while(verificador == False):
                opcion = input("")
                
                if(opcion == "1"):
                    tiempo = "lento"
                    verificador = True
                elif(opcion == "2"):
                    tiempo = "medio"
                    verificador = True
                elif(opcion == "3"):
                    tiempo = "rapido"
                    verificador = True
                else:
                    print("\nOpcion no valida, ingrese uno existente\n")

            
            
            print("Ingresa el contenido nutricional del platillo que desea agregar:")
            print("1. Baja")
            print("2. Media") #Puede que en esta parte haya error.
            print("3. Alta\n")

            verificador = False

            while(verificador == False):
                opcion = input("")

                if(opcion == "1"):
                    nutricion = "baja"
                    verificador = True
                elif(opcion == "2"):
                    nutricion = "media"
                    verificador = True
                elif(opcion == "3"):
                    nutricion = "alta"
                    verificador = True
                else:
                    print("\nOpcion no valida, ingrese uno existente\n")
            
            
            print("Ingresa la relacion de su platillo que desea agregar:")
            print("1. Carne")
            print("2. Pasta")
            print("3. Ensalada")
            print("4. Tacos")
            print("5. Pan")
            print("6. Pollo")
            print("7. Glutenfree")
            print("8. Verduras")
            print("9. Frutas")
            print("10. Lacteo")
            print("11. Mousse")
            print("12. Chocolate")
            print("13. Mariscos\n")
            

            verificador = False

            while(verificador == False):
                opcion = input("")

                if(opcion == "1"):
                    relacion = "carne"
                    verificador = True
                elif(opcion == "2"):
                    relacion = "pasta"
                    verificador = True
                elif(opcion == "3"):
                    relacion = "ensalada"
                    verificador = True
                elif(opcion == "4"):
                    relacion = "tacos"
                    verificador = True
                elif(opcion == "5"):
                    relacion = "pan"
                    verificador = True
                elif(opcion == "6"):
                    relacion = "pollo"
                    verificador = True
                elif(opcion == "7"):
                    relacion = "glutenfree"
                    verificador = True
                elif(opcion == "8"):
                    relacion = "verduras"
                    verificador = True
                elif(opcion == "9"):
                    relacion = "frutas"
                    verificador = True
                elif(opcion == "10"):
                    relacion = "lacteo"
                    verificador = True
                elif(opcion == "11"):
                    relacion = "mousse"
                    verificador = True
                elif(opcion == "12"):
                    relacion = "chocolate"
                    verificador = True
                elif(opcion == "13"):
                    relacion = "mariscos"
                    verificador = True
                else:
                    print("\nOpcion no valida, ingrese uno existente\n")
            content = []
            content.append(nombre)
            content.append(precio)
            content.append(tiempo)
            content.append(nutricion)
            content.append(relacion)
            HelloWorldExample.add_row('export.csv',content)
            HelloWorldExample.add_newPlatillo(greeter, nombre, precio, tiempo, nutricion, relacion)
            


        #Opcion para poder eliminar un registro de la base de datos.
        elif(int(opcionprincipal) == 3):
            print("Ingresa el nombre del platillo que desea eliminar:")
            nombre = input("")
            HelloWorldExample.delete_relationship(greeter, nombre)
            HelloWorldExample.delete_platillo(nombre)

        elif(int(opcionprincipal) == 4):
            print("🍴 Gracias por utilizar el sistema de recomendaciones 🍴")
            sys.exit()
    

# Se crea el ciclo para el menu
i=0
ciclo = True
while ciclo:
    print(user)
    print(password)
    #print(maindish)
    #print(food)
    #print(foodCounter)
    if(len(user)==0):
        print("Generando nuevo usuario")
        name = input("Ingrese el nombre de la cuenta: ")
        coss = input("Ingrese la contraseña: ")
        user.append(name)
        password.append(coss)
        maindish.append("")
    elif(len(user)>0):
        print("1. Crear nuevo usuario")
        print("2. Iniciar sesion")
        print("3. Salir del programa")
        opcion = input("Ingrese su opcion: ")
        if((opcion) =="1"):
            print("Generando nuevo usuario")
            name = input("Ingrese el nombre de la cuenta: ")
            coss = input("Ingrese la contraseña: ")
            user.append(name)
            password.append(coss)
            maindish.append("")
        elif((opcion) =="2"):
            print("Iniciar sesion")
            input_user=input("Ingrese su nombre de usuario: ")
            input_pass=input("Ingrese la contraseña: ")
            if(user.__contains__(input_user)):
                indice_user = user.index(input_user)    
                if(user[indice_user]==input_user):
                    if(password[indice_user] == input_pass):
                        menu_function(indice_user)
                    else:
                        print("Contraseña incorrecta")
        elif((opcion) =="3"):
            print("🍴 Espero que vuelva pronto 🍴")
            ciclo = False
        else:
            print("Ingrse solo de las opciones que se le muestran")