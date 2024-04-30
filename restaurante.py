tipoMesa = ["pareja", "familiar ","extra familiar ", "ejecutiva "]
cantidad = [2,4,6,10]
# modulo # 1

#variables


numero_documento=int(input("igrese su nuemro de indentificacion: "))
numero_personas=int(input("numero de personas para la mesa: "))

if numero_personas >= 1 and numero_personas <= 2 :
     print("se te asigno la mesa", tipoMesa[0])
elif numero_personas >= 3 and numero_personas <= 4 :
      print ("se te asigno la mesa", tipoMesa[1])
elif numero_personas >= 5 and numero_personas <= 6 :
      print (" se te asigno la mesa",tipoMesa[2])
elif numero_personas >= 7 and numero_personas <= 10 :
      print("se le asigno la mesa ", tipoMesa[3])
else:
      print ("no hay mesas disponibles para ese numero de personas ")
#modulo # 2







numero_entradas=int()
tipo_entrada = int()
valor_entradas = float(0)


entrada = ["0- dedos de queso ", "1- patacon con hogao ", "2- ceviche ", "3- sopa de tomate "]
preciosEntrada = [ 2.5,6, 12, 5]

 
for e in range(4): 
    print(entrada[e],preciosEntrada[e],"usd ")

numero_entradas = int(input("cuantas entradas desea? "))

#Entradas
for e in range(numero_entradas):
      tipo_entrada = int(input("escriba la entrada que desea "))
      print("Seleccionó ", entrada[tipo_entrada])
      valor_entradas = valor_entradas + preciosEntrada[tipo_entrada]

print("El valor de las entradas es ", valor_entradas)


#fin entradas

# platos fuertes

numero_pf = int()
tipo_pf = int ()
valor_pf = float(0)

plato_fuerte= [ "0- pasta carbonara con pollo y champiñones ",  "1- salmon con pure de papa ", "2- pollo a la naranja con arroz ", "3- cositalla BBQ con papas rusticas ", "4- pollo a la plancha con ensalada", "5- cerdo en salsa de piña con yuca frita"]
preciosPlatosFuertes = [20,40,35,37,23,32]

for f in range (5):
    print (plato_fuerte[f], preciosPlatosFuertes[f], "usd")

numero_pf = int(input("seleccione la cantidad platos fuertes "))

for f in range (numero_pf):
      tipo_pf = int(input("digite el numero, para seleccionar el plato fuerte "))
      print ("ha seleccionado ", plato_fuerte [tipo_pf] )
      valor_pf = valor_pf +  preciosPlatosFuertes[tipo_pf]
print ("el valor de los platos fuertes es de: ", valor_pf)

#fin platos fuertes



# bebidas

numero_bebidas = int()
tipo_bebida = int ()
valor_bebida = float(0)


bebidas = ["0- Limonada natural ","1- Limonada cerezada ", "2- Limonada de coco ", "3- cerveza corona ","4- agua natural "]
preciosBebidas = [2,2.5,4,6, 1.5]           

for b in range (5):
           print(bebidas[b], preciosBebidas[b], "usd")

numero_bebidas = int(input("cantidad de bedidas "))

for b in range (numero_bebidas):
      tipo_bebida = int (input("seleccione la bebida "))
      print ("selecciono ", bebidas[tipo_bebida])
      valor_bebida = valor_bebida + preciosBebidas [tipo_bebida]
print ("el valor de las bebidas es de : ", valor_bebida )


#fin bebidas




#postres

cantidad_postres = int ()
tipo_postres =()
valor_postres= float(0)


postres = ["0- helado de macadami ", "1- helado de browni ","2- creps con helado ","3- torta redbelbed "]
preciosPostres = [1.5,2,3.5,7]

for p in range (4):
    print ( postres[p], preciosPostres[p], "usd") 

cantidad_postres = int(input("seleccione la cantidad de postres "))

for p in range (cantidad_postres):

      tipo_postres = int(input("seleccione el postre "))
      print ("selecciono ", postres[tipo_postres])
      valor_postres = valor_postres + preciosPostres [tipo_postres]
print("el precio de los postres es de ", valor_postres)














