tipoMesa = ["Pareja", "Familiar ","Extra familiar ", "Ejecutiva "]
cantidad = [2,4,6,10]
# modulo # 1

#variables


numero_documento=int(input("Ingrese su numero de indentificacion: "))

print("Sea Bienvenido al restaurante HyP comidas vallunas del pacifico. Porfavor conteste las siguientes preguntas de acuerdo a sus necesidades")
numero_personas=int(input("Cuantas personas para la mesa: "))

if numero_personas >= 1 and numero_personas <= 2 :
     print("Se te asigno la mesa", tipoMesa[0])
elif numero_personas >= 3 and numero_personas <= 4 :
      print ("Se te asigno la mesa", tipoMesa[1])
elif numero_personas >= 5 and numero_personas <= 6 :
      print (" Se te asigno la mesa",tipoMesa[2])
elif numero_personas >= 7 and numero_personas <= 10 :
      print("Se le asigno la mesa ", tipoMesa[3])
else:
      print ("No hay mesas disponibles para ese numero de personas ")
#modulo # 2







numero_entradas=int()
tipo_entrada = int()
valor_entradas = float(0)


entrada = ["0- Dedos de queso ", "1- Patacon con hogao ", "2- Ceviche ", "3- Sopa de tomate "]
preciosEntrada = [ 2.5,6, 12, 5]

 
for e in range(4): 
    print(entrada[e],preciosEntrada[e],"usd ")

numero_entradas = int(input("Cuantas entradas desea? "))

#Entradas
for e in range(numero_entradas):
      tipo_entrada = int(input("Que entrada que desea "))
      print("Seleccionó ", entrada[tipo_entrada])
      valor_entradas = valor_entradas + preciosEntrada[tipo_entrada]

print("El valor de las entradas es ", valor_entradas)


#fin entradas

# platos fuertes

numero_pf = int()
tipo_pf = int ()
valor_pf = float(0)

plato_fuerte= [ "0- Pasta carbonara con pollo y champiñones ",  "1- Salmon con pure de papa ", "2- Pollo a la naranja con arroz ", "3- Cositalla BBQ con papas rusticas ", "4- Pollo a la plancha con ensalada", "5- Cerdo en salsa de piña con yuca frita"]
preciosPlatosFuertes = [20,40,35,37,23,32]

for f in range (5):
    print (plato_fuerte[f], preciosPlatosFuertes[f], "usd")

numero_pf = int(input("Seleccione la cantidad platos fuertes "))

for f in range (numero_pf):
      tipo_pf = int(input("Digite el numero, para seleccionar el plato fuerte "))
      print ("Ha seleccionado ", plato_fuerte [tipo_pf] )
      valor_pf = valor_pf +  preciosPlatosFuertes[tipo_pf]
print ("El valor de los platos fuertes es de: ", valor_pf)

#fin platos fuertes



# bebidas

numero_bebidas = int()
tipo_bebida = int ()
valor_bebida = float(0)


bebidas = ["0- Limonada natural ","1- Limonada cerezada ", "2- Limonada de coco ", "3- Cerveza corona ","4- Agua natural "]
preciosBebidas = [2,2.5,4,6, 1.5]           

for b in range (5):
           print(bebidas[b], preciosBebidas[b], "usd")

numero_bebidas = int(input("Cantidad de bedidas "))

for b in range (numero_bebidas):
      tipo_bebida = int (input("Seleccione la bebida "))
      print ("Selecciono ", bebidas[tipo_bebida])
      valor_bebida = valor_bebida + preciosBebidas [tipo_bebida]
print ("El valor de las bebidas es de : ", valor_bebida )


#fin bebidas




#postres

cantidad_postres = int ()
tipo_postres =()
valor_postres= float(0)


postres = ["0- Helado de macadami ", "1- Helado de browni ","2- Creps con helado ","3- Torta redbelbed "]
preciosPostres = [1.5,2,3.5,7]

for p in range (4):
    print ( postres[p], preciosPostres[p], "usd") 

cantidad_postres = int(input("Seleccione la cantidad de postres "))

for p in range (cantidad_postres):

      tipo_postres = int(input("Seleccione el postre "))
      print ("Selecciono ", postres[tipo_postres])
      valor_postres = valor_postres + preciosPostres [tipo_postres]
print("El precio de los postres es de ", valor_postres)


valorNoIva = valor_entradas + valor_bebida + valor_pf + valor_postres 
iva = valorNoIva * 0.19
valorTotal = valorNoIva + iva

print("El total a pagar es de ", valorTotal)












