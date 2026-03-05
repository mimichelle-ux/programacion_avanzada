from enum import Enum
import datetime

class Persona:
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        return f"{self.nombre} inició sesión"
    
    def logout(self):
        return f"{self.nombre} cerró sesión"

    def actualizarDatos(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        print(f"{self.nombre}, tus datos fueron actualizados")

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono, puntosFidelidad=0):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = []

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)
        print(f"Reserva {reserva.idReserva} creada para {self.nombre}")

    def consultarPromociones(self, promociones):
        for promo in promociones:
            print(f"Promo: {promo.descripcion} - {promo.porcentajeDescuento}%")

    def cancelarReserva(self, reserva):
        reserva.estado = EstadoReserva.CANCELADA
        print(f"La reserva {reserva.idReserva} ha sido cancelada.")

class Rol(Enum):
    TAQUILLERO = 1
    ADMIN = 2
    LIMPIEZA = 3

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol: Rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        print(f"El {self.nombre} ({self.rol.name}) marcó entrada")

    def gestionarFunciones(self, funcion):
        if self.rol == Rol.ADMIN:
            print(f"El {self.nombre} gestionó la función {funcion.pelicula.titulo}")
        else:
            print("No puedes gestionar estas funciones, no eres administrador!")

class EstadoReserva(Enum):
    PENDIENTE = 1
    PAGADA = 2
    CANCELADA = 3

class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos, montoTotal, estado=EstadoReserva.PENDIENTE):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = montoTotal
        self.estado = estado
    def confirmarPago(self):
        self.estado = EstadoReserva.PAGADA
        print(f"Reserva {self.idReserva} confirmada y pagada")
    def generarTicket(self):
        ticket = f"""
        --- Ticket ---
        Reserva: {self.idReserva}
        Usuario: {self.usuario.nombre}
        Película: {self.funcion.pelicula.titulo}
        Sala: {self.funcion.sala.tipo.name}
        Asientos: {self.asientos}
        Monto: {self.montoTotal}
        Estado: {self.estado.name}
        ---------------
        """
        print(ticket)
        return ticket

    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
            precio_final = promo.aplicarDescuento(self.montoTotal)
            print(f"Promoción aplicada: {promo.descripcion}, Precio final: {precio_final}")
            return precio_final
        else:
            print("Promoción no válida")
            return self.montoTotal

class Promocion:
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion 

    def esValida(self, usuario: Usuario):
        hoy = datetime.date.today()
        fecha_exp = datetime.datetime.strptime(self.fechaExpiracion, "%Y-%m-%d").date()
        return usuario.puntosFidelidad >= 10 and hoy <= fecha_exp

    def aplicarDescuento(self, monto):
        descuento = monto * (self.porcentajeDescuento / 100)
        return monto - descuento

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        return f"{self.titulo} es una película de género {self.genero} con duración de {self.duracion} minutos"

    def esAptaParaTodoPublico(self):
        return self.clasificacion in ["A", "AA"]

class TipoSala(Enum):
    DOSD = "2D"
    TRESD = "3D"
    IMAX = "IMAX"
class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificarDisponibilidad(self):
        print(f"El {self.nombre} está disponible")

    def limpiarEspacio(self):
        print(f"El {self.nombre} ha sido limpiado")
class Sala(Espacio):
    def __init__(self, tipo: TipoSala, capacidadTotal, esVip):
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip

    def ajustarAforo(self, nuevoAforo):
        self.capacidadTotal = nuevoAforo
        print(f"Aforo ajustado a {nuevoAforo}")

    def obtenerTipoSala(self):
        return self.tipo.name

class Funcion:
    def __init__(self, idFuncion, pelicula: Pelicula, sala: Sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.asientosOcupados = []

    def calcularAsientosLibres(self):
        return self.sala.capacidadTotal - len(self.asientosOcupados)

    def obtenerDetallesFuncion(self):
       return (
    f"Función {self.idFuncion}: {self.pelicula.titulo} "
    f"en sala {self.sala.tipo.name}, "
    f"inicio {self.horarioInicio}, "
    f"precio {self.precioBase}"
)

class ZonaComida(Espacio):
    def __init__(self, listaProductos, stockActual):
        self.listaProductos = listaProductos
        self.stockActual = stockActual 

    def venderProducto(self, producto):
        if producto in self.stockActual and self.stockActual[producto] > 0:
            self.stockActual[producto] -= 1
            print(f"El producto {producto} vendido. Stock restante: {self.stockActual[producto]}")
        else:
            print(f"El producto {producto} no está disponible")

    def actualizarInventario(self, producto, cantidad):
        self.stockActual[producto] = cantidad
        print(f"Inventario actualizado: {producto} = {cantidad}")