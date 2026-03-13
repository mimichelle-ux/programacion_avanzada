from enum import Enum

class Rol(Enum):
    BARISTA = "Barista"
    MESERO = "Mesero"
    GERENTE = "Gerente"


class Temperatura(Enum):
    FRIA = "Fria"
    CALIENTE = "Caliente"


class EstadoPedido(Enum):
    PENDIENTE = "Pendiente :/"
    PREPARANDO = "Preparando :)"
    ENTREGADO = "Entregado :D"

class Persona:

    def __init__(self, idPersona, name, email):
        self.idPersona = idPersona
        self.nombre = name
        self.email = email

    def login(self):
        print(f"{self.nombre}, bienvenido/a, ha iniciado sesion :)! ")

class Cliente(Persona):

    def __init__(self, idPersona, name, email):
        self.idPersona = idPersona
        self.nombre = name
        self.email = email
        self.puntosFidelidad = 0
        self.historialPedidos = []

    def realizarPedido(self, pedido):

        self.historialPedidos.append(pedido)
        print("Pedido realizado con exito :D")

    def verHistorial(self):

        if self.historialPedidos == []:
            print("No hay pedidos :(")
        else:
            for m in self.historialPedidos:
                print("Pedido", m.idPedido, "Total:", m.total)

class Empleado(Persona):
    def __init__(self, idPersona, name, email, idEmpleado, rol):

        self.idPersona = idPersona
        self.nombre = name
        self.email = email
        self.idEmpleado = idEmpleado
        self.rol = rol

class ProductoBase:

    def __init__(self, idProducto, name, precioBase):
        self.idProducto = idProducto
        self.nombre = name
        self.precioBase = precioBase

class Bebida(ProductoBase):

    def __init__(self, idProducto, name, precioBase, size, temperature):
        self.idProducto = idProducto
        self.nombre = name
        self.precioBase = precioBase
        self.tamaño = size
        self.temperatura = temperature
        self.cosas_extras = []

    def agregarExtra(self):
        extra = input("Algo Extra: ")
        self.cosas_extras.append(extra)

    def calcularPrecio(self):
        contador = 0
        for l in self.cosas_extras:
            contador += 1
        precio = self.precioBase + (contador * 5)
        return precio


class Postresito(ProductoBase):
    def __init__(self, idProducto, name, precioBase, vegano, gluten):
        self.idProducto = idProducto
        self.nombre = name
        self.precioBase = precioBase
        self.vegano = vegano
        self.gluten = gluten
        
class Pedido:
    def __init__(self, idPedido):
        self.idPedido = idPedido
        self.productos = []
        self.estado = EstadoPedido.PENDIENTE
        self.total = 0

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularTotal(self):
        total = 0
        for leon in self.productos:
            if leon.__class__.__name__ == "Bebida":
                total = total + leon.calcularPrecio()
            else:
                total = total + leon.precioBase
        self.total = total

def menu():

    cliente = Cliente(1, "Cliente", "correo@email.com")

    pedidoActual = 0
    idPedido = 1

    while True:

        print("\n--- CAFETERIA FLOWRS MICHELLE ---")
        print("1 Crear pedido")
        print("2 Agregar bebida")
        print("3 Agregar postre")
        print("4 Calcular total")
        print("5 Ver historial")
        print("6 Salir de nuestra cafeteria")

        op = input("Opcion: ")

        if op == "1":

            pedidoActual = Pedido(idPedido)
            idPedido = idPedido + 1
            cliente.realizarPedido(pedidoActual)

        elif op == "2":

            if pedidoActual == 0:
                print("Por favor, crea un pedido")
            else:
                nombre = input("Nombre bebida: ")
                precio = float(input("Precio: "))
                tamaño = input("Tamaño: ")
                temp = input("Temperatura (fria/caliente): ")
                if temp == "fria":
                    temperatura = Temperatura.FRIA
                else:
                    temperatura = Temperatura.CALIENTE
                bebida = Bebida(1, nombre, precio, tamaño, temperatura)
                extra = input("Agregar extra? (si/no): ")
                if extra == "si":
                    bebida.agregarExtra()
                pedidoActual.agregarProducto(bebida)

        elif op == "3":
            
            if pedidoActual == 0:
                print("Por favor,crea un pedido")
            else:
                nombre = input("Nombre postre: ")
                precio = float(input("Precio: "))
                vegano = input("Vegano? (si/no): ")
                gluten = input("Sin gluten? (si/no): ")
                postre = Postresito(2, nombre, precio, vegano, gluten)
                pedidoActual.agregarProducto(postre)

        elif op == "4":
            
            if pedidoActual == 0:
                print("Por favor, crea un pedido")
            else:
                pedidoActual.calcularTotal()
                print("Total:", pedidoActual.total)

        elif op == "5":

            cliente.verHistorial()

        elif op == "6":

            print("Gracias por visitarnos, difruta tu orden :)")
            break
        else:
            print("Elige una opcion del (1-6)")


menu()
