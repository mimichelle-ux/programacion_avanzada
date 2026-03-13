from Cafeteria import *

print("----- CLIENTES -----")

cliente1 = Cliente(1,"Ana","ana@email.com")
cliente2 = Cliente(2,"Luis","luis@email.com")
cliente3 = Cliente(3,"Sofia","sofia@email.com")
cliente4 = Cliente(4,"Pedro","pedro@email.com")
cliente5 = Cliente(5,"Maria","maria@email.com")
cliente6 = Cliente(6,"Jose","jose@email.com")
cliente7 = Cliente(7,"Elena","elena@email.com")
cliente8 = Cliente(8,"Carlos","carlos@email.com")
cliente9 = Cliente(9,"Laura","laura@email.com")
cliente10 = Cliente(10,"Diego","diego@email.com")

print(cliente1.idPersona, cliente1.nombre, cliente1.email)
print(cliente2.idPersona, cliente2.nombre, cliente2.email)
print(cliente3.idPersona, cliente3.nombre, cliente3.email)
print(cliente4.idPersona, cliente4.nombre, cliente4.email)
print(cliente5.idPersona, cliente5.nombre, cliente5.email)
print(cliente6.idPersona, cliente6.nombre, cliente6.email)
print(cliente7.idPersona, cliente7.nombre, cliente7.email)
print(cliente8.idPersona, cliente8.nombre, cliente8.email)
print(cliente9.idPersona, cliente9.nombre, cliente9.email)
print(cliente10.idPersona, cliente10.nombre, cliente10.email)

print("----- BEBIDAS -----")

bebida1 = Bebida(1,"Cafe",30,"Grande",Temperatura.CALIENTE)
bebida2 = Bebida(2,"Latte",35,"Mediano",Temperatura.CALIENTE)
bebida3 = Bebida(3,"Capuccino",40,"Grande",Temperatura.CALIENTE)
bebida4 = Bebida(4,"Chocolate",45,"Grande",Temperatura.CALIENTE)
bebida5 = Bebida(5,"Te",20,"Chico",Temperatura.CALIENTE)
bebida6 = Bebida(6,"Frappe",50,"Grande",Temperatura.FRIA)
bebida7 = Bebida(7,"Iced Coffee",35,"Mediano",Temperatura.FRIA)
bebida8 = Bebida(8,"Malteada",55,"Grande",Temperatura.FRIA)
bebida9 = Bebida(9,"Smoothie",60,"Grande",Temperatura.FRIA)
bebida10 = Bebida(10,"Limonada",25,"Mediano",Temperatura.FRIA)

print("Bebida:", bebida1.idProducto, bebida1.nombre, bebida1.precioBase, bebida1.tamaño, bebida1.temperatura.value)
print("Bebida:", bebida2.idProducto, bebida2.nombre, bebida2.precioBase, bebida2.tamaño, bebida2.temperatura.value)
print("Bebida:", bebida3.idProducto, bebida3.nombre, bebida3.precioBase, bebida3.tamaño, bebida3.temperatura.value)
print("Bebida:", bebida4.idProducto, bebida4.nombre, bebida4.precioBase, bebida4.tamaño, bebida4.temperatura.value)
print("Bebida:", bebida5.idProducto, bebida5.nombre, bebida5.precioBase, bebida5.tamaño, bebida5.temperatura.value)
print("Bebida:", bebida6.idProducto, bebida6.nombre, bebida6.precioBase, bebida6.tamaño, bebida6.temperatura.value)
print("Bebida:", bebida7.idProducto, bebida7.nombre, bebida7.precioBase,bebida7.tamaño,bebida7.temperatura.value)
print("Bebida:", bebida8.idProducto, bebida8.nombre, bebida8.precioBase, bebida8.tamaño, bebida8.temperatura.value)
print("Bebida:", bebida9.idProducto, bebida9.nombre, bebida9.precioBase, bebida9.tamaño, bebida9.temperatura.value)
print("Bebida:", bebida10.idProducto, bebida10.nombre, bebida10.precioBase, bebida10.tamaño, bebida10.temperatura.value) 

print("----- POSTRES -----")

postre1 = Postresito(1,"Pastel",50,"si,","no")
postre2 = Postresito(2,"Brownie",35,"no,","no")
postre3 = Postresito(3,"Galleta",20,"no,","no")
postre4 = Postresito(4,"Cheesecake",60,"no,","no")
postre5 = Postresito(5,"Pay de limon",55,"no,","no")
postre6 = Postresito(6,"Donut",25,"no,","no")
postre7 = Postresito(7,"Cupcake",30,"no,","no")
postre8 = Postresito(8,"Pastel vegano",65,"si,","si")
postre9 = Postresito(9,"Flan",40,"no,","no")
postre10 = Postresito(10,"Gelatina",15,"si,","si ")

print("Postre:", postre1.idProducto, postre1.nombre, postre1.precioBase, postre1.vegano, postre1.gluten)
print("Postre:", postre2.idProducto, postre2.nombre, postre2 .precioBase, postre2.vegano, postre2.gluten)
print("Postre:", postre3.idProducto, postre3.nombre, postre3.precioBase, postre3.vegano, postre3.gluten)
print("Postre:", postre4.idProducto, postre4.nombre, postre4.precioBase, postre4.vegano, postre4.gluten)
print("Postre:", postre5.idProducto, postre5.nombre, postre5.precioBase, postre5.vegano, postre5.gluten)
print("Postre:", postre6.idProducto, postre6.nombre, postre6.precioBase, postre6.vegano, postre6.gluten)
print("Postre:", postre7.idProducto, postre7.nombre, postre7.precioBase, postre7.vegano, postre7.gluten)
print("Postre:", postre8.idProducto, postre8.nombre, postre8.precioBase, postre8.vegano, postre8.gluten)
print("Postre:", postre9.idProducto, postre9.nombre, postre9.precioBase, postre9.vegano, postre9.gluten)
print("Postre:", postre10.idProducto, postre10.nombre, postre10.precioBase, postre10.vegano, postre10.gluten)

from Cafeteria import *

clientes = [
    cliente1, cliente2, cliente3, cliente4, cliente5,
    cliente6, cliente7, cliente8, cliente9, cliente10
]


bebidas = [
    bebida1, bebida2, bebida3, bebida4, bebida5,
    bebida6, bebida7, bebida8, bebida9, bebida10
]

postres = [
    Postresito(1, "Brownie", 25, "No", "Sí"),
    Postresito(2, "Galleta", 15, "Sí", "No"),
    Postresito(3, "Cheesecake", 30, "No", "Sí")
]

# CREAR PEDIDOS
idPedido = 1

for c in clientes:
    pedido = Pedido(idPedido)
    idPedido += 1

    # Agregar bebidas
    pedido.agregarProducto(bebidas[(c.idPersona-1)%10])
    pedido.agregarProducto(bebidas[(c.idPersona)%10])

    # Agregar un postre
    pedido.agregarProducto(postres[(c.idPersona-1)%3])

    # Agregar extras 
    pedido.productos[0].cosas_extras = ["Leche", "Azúcar"]

    # Calcular total del pedido
    total = 0
    for leon in pedido.productos:
        if leon == "Bebida":
            total += leon.calcularPrecio()
        else:  
            total += leon.precioBase
    pedido.total = total

    # Registrar pedido
    c.realizarPedido(pedido)

    # Mostrar pedido
    print(f"\nCliente: {c.nombre}")
    print(f"ID Pedido: {pedido.idPedido}, Total: {pedido.total}")
    print("Productos:")
    for p in pedido.productos:
        if p.__class__.__name__ == "Bebida":
            print(f"- Bebida: {p.nombre}, Extras: {p.cosas_extras}, Precio: {p.calcularPrecio()}")
        else: 
            print(f"- Postre: {p.nombre}, Precio: {p.precioBase}")

clientes[0].verHistorial()
