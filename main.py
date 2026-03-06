from models import *

asientos_ocupados = []
print("--- REGISTRO MANUAL DE USUARIOS (10 OBJETOS) ---")

usuarios = [
    Usuario(1, "Leonardo", "Leonardo@mail.com", "276-108-05-65", puntosFidelidad=100),
    Usuario(2, "Cristina", "Cristina@mail.com", "276-108-05-87", puntosFidelidad=50),
    Usuario(3, "Miguel", "Miguel@mail.com", "276-108-05-88", puntosFidelidad=75),
    Usuario(4, "Jorge", "Jorge@mail.com", "276-108-05-89", puntosFidelidad=125),
    Usuario(5, "Alejandro", "Alejandro@mail.com", "276-108-05-90", puntosFidelidad=20),
    Usuario(6, "Jazmin", "Jazmin@mail.com", "276-108-05-91", puntosFidelidad=150),
    Usuario(7, "Violeta", "Violeta@mail.com", "276-108-05-92", puntosFidelidad=10),
    Usuario(8, "Viridiana", "Viridiana@mail.com", "276-108-05-93", puntosFidelidad=75),
    Usuario(9, "Michell", "Michell@mail.com", "276-108-05-94", puntosFidelidad=5),
    Usuario(10, "Monica", "Monica@mail.com", "276-108-05-95", puntosFidelidad=0)
]

print("Usuario 1:", usuarios[0].idPersona, "-", usuarios[0].nombre, "-", usuarios[0].email, "-", usuarios[0].telefono, "-", "Puntos:", usuarios[0].puntosFidelidad, "-", usuarios[0].login())
print("Usuario 2:", usuarios[1].idPersona, "-", usuarios[1].nombre, "-", usuarios[1].email, "-", usuarios[1].telefono, "-", "Puntos:", usuarios[1].puntosFidelidad, "-", usuarios[1].login())
print("Usuario 3:", usuarios[2].idPersona, "-", usuarios[2].nombre, "-", usuarios[2].email, "-", usuarios[2].telefono, "-", "Puntos:", usuarios[2].puntosFidelidad, "-", usuarios[2].login())
print("Usuario 4:", usuarios[3].idPersona, "-", usuarios[3].nombre, "-", usuarios[3].email, "-", usuarios[3].telefono, "-", "Puntos:", usuarios[3].puntosFidelidad, "-", usuarios[3].login())
print("Usuario 5:", usuarios[4].idPersona, "-", usuarios[4].nombre, "-", usuarios[4].email, "-", usuarios[4].telefono, "-", "Puntos:", usuarios[4].puntosFidelidad, "-", usuarios[4].login())
print("Usuario 6:", usuarios[5].idPersona, "-", usuarios[5].nombre, "-", usuarios[5].email, "-", usuarios[5].telefono, "-", "Puntos:", usuarios[5].puntosFidelidad, "-", usuarios[5].login())
print("Usuario 7:", usuarios[6].idPersona, "-", usuarios[6].nombre, "-", usuarios[6].email, "-", usuarios[6].telefono, "-", "Puntos:", usuarios[6].puntosFidelidad, "-", usuarios[6].login())
print("Usuario 8:", usuarios[7].idPersona, "-", usuarios[7].nombre, "-", usuarios[7].email, "-", usuarios[7].telefono, "-", "Puntos:", usuarios[7].puntosFidelidad, "-", usuarios[7].login())
print("Usuario 9:", usuarios[8].idPersona, "-", usuarios[8].nombre, "-", usuarios[8].email, "-", usuarios[8].telefono, "-", "Puntos:", usuarios[8].puntosFidelidad, "-", usuarios[8].login())
print("Usuario 10:", usuarios[9].idPersona, "-", usuarios[9].nombre, "-", usuarios[9].email, "-", usuarios[9].telefono, "-", "Puntos:", usuarios[9].puntosFidelidad, "-", usuarios[9].login())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")


print("--- REGISTRO MANUAL DE EMPLEADOS (10 OBJETOS) ---")

empleados = [
    Empleado(11, "Empleado1", "Empl1@mail.com", "276-100-34-73", "E01", Rol.TAQUILLERO, "9:00-17:00"),
    Empleado(12, "Empleado2", "Empl2@mail.com", "276-100-34-89", "E02", Rol.ADMIN, "9:00-17:00"),
    Empleado(13, "Empleado3", "Empl3@mail.com", "276-100-34-49", "E03", Rol.LIMPIEZA, "9:00-17:00"),
    Empleado(14, "Empleado4", "Empl4@mail.com", "276-100-34-76", "E04", Rol.TAQUILLERO, "9:00-17:00"),
    Empleado(15, "Empleado5", "Empl5@mail.com", "276-100-34-97", "E05", Rol.ADMIN, "9:00-17:00"),
    Empleado(16, "Empleado6", "Empl6@mail.com", "276-100-34-77", "E06", Rol.LIMPIEZA, "9:00-17:00"),
    Empleado(17, "Empleado7", "Empl7@mail.com", "276-100-34-70", "E07", Rol.TAQUILLERO, "9:00-17:00"),
    Empleado(18, "Empleado8", "Empl8@mail.com", "276-100-34-30", "E08", Rol.ADMIN, "9:00-17:00"),
    Empleado(19, "Empleado9", "Empl9@mail.com", "276-100-34-33", "E09", Rol.LIMPIEZA, "9:00-17:00"),
    Empleado(20, "Empleado10", "Empl10@mail.com", "276-100-34-11", "E010", Rol.TAQUILLERO, "9:00-17:00")
]

print("Empleado 1:", empleados[0].idEmpleado, "-", empleados[0].nombre, "-", empleados[0].email, "-", empleados[0].telefono, "-", empleados[0].idEmpleado, "-", empleados[0].rol.name, "-", empleados[0].horario)
print("Empleado 2:", empleados[1].idEmpleado, "-", empleados[1].nombre, "-", empleados[1].email, "-", empleados[1].telefono, "-", empleados[1].idEmpleado, "-", empleados[1].rol.name, "-", empleados[1].horario)
print("Empleado 3:", empleados[2].idEmpleado, "-", empleados[2].nombre, "-", empleados[2].email, "-", empleados[2].telefono, "-", empleados[2].idEmpleado, "-", empleados[2].rol.name, "-", empleados[2].horario)
print("Empleado 4:", empleados[3].idEmpleado, "-", empleados[3].nombre, "-", empleados[3].email, "-", empleados[3].telefono, "-", empleados[3].idEmpleado, "-", empleados[3].rol.name, "-", empleados[3].horario)
print("Empleado 5:", empleados[4].idEmpleado, "-", empleados[4].nombre, "-", empleados[4].email, "-", empleados[4].telefono, "-", empleados[4].idEmpleado, "-", empleados[4].rol.name, "-", empleados[4].horario)
print("Empleado 6:", empleados[5].idEmpleado, "-", empleados[5].nombre, "-", empleados[5].email, "-", empleados[5].telefono, "-", empleados[5].idEmpleado, "-", empleados[5].rol.name, "-", empleados[5].horario)
print("Empleado 7:", empleados[6].idEmpleado, "-", empleados[6].nombre, "-", empleados[6].email, "-", empleados[6].telefono, "-", empleados[6].idEmpleado, "-", empleados[6].rol.name, "-", empleados[6].horario)
print("Empleado 8:", empleados[7].idEmpleado, "-", empleados[7].nombre, "-", empleados[7].email, "-", empleados[7].telefono, "-", empleados[7].idEmpleado, "-", empleados[7].rol.name, "-", empleados[7].horario)
print("Empleado 9:", empleados[8].idEmpleado, "-", empleados[8].nombre, "-", empleados[8].email, "-", empleados[8].telefono, "-", empleados[8].idEmpleado, "-", empleados[8].rol.name, "-", empleados[8].horario)
print("Empleado 10:", empleados[9].idEmpleado, "-", empleados[9].nombre, "-", empleados[9].email, "-", empleados[9].telefono, "-", empleados[9].idEmpleado, "-", empleados[9].rol.name, "-", empleados[9].horario)
print("--- VALIDACION DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE PELICULAS (10 OBJETOS) ---")

peliculas = [
    Pelicula("Los guardianes de la Galaxia", 120, "B", "Acción"),
    Pelicula("Barbie", 110, "A", "Comedia"),
    Pelicula("Spiderman", 130, "B", "Acción"),
    Pelicula("Avengers", 150, "B", "Acción"),
    Pelicula("El conjuro", 100, "C", "Terror"),
    Pelicula("Stray Kids", 90, "A", "Musical"),
    Pelicula("Zootopia", 95, "AA", "Animación"),
    Pelicula("Bob Esponja", 85, "AA", "Animación"),
    Pelicula("La Sirenita", 100, "A", "Fantasia"),
    Pelicula("El zorro de las nueve colas", 140, "B", "Drama")
]

print("Pelicula 1:", peliculas[0].titulo, "-", peliculas[0].duracion, "min", "-", peliculas[0].clasificacion, "-", peliculas[0].genero, "-", peliculas[0].obtenerSinopsis(), "-", "Apta:", peliculas[0].esAptaParaTodoPublico())
print("Pelicula 2:", peliculas[1].titulo, "-", peliculas[1].duracion, "min", "-", peliculas[1].clasificacion, "-", peliculas[1].genero, "-", peliculas[1].obtenerSinopsis(), "-", "Apta:", peliculas[1].esAptaParaTodoPublico())
print("Pelicula 3:", peliculas[2].titulo, "-", peliculas[2].duracion, "min", "-", peliculas[2].clasificacion, "-", peliculas[2].genero, "-", peliculas[2].obtenerSinopsis(), "-", "Apta:", peliculas[2].esAptaParaTodoPublico())
print("Pelicula 4:", peliculas[3].titulo, "-", peliculas[3].duracion, "min", "-", peliculas[3].clasificacion, "-", peliculas[3].genero, "-", peliculas[3].obtenerSinopsis(), "-", "Apta:", peliculas[3].esAptaParaTodoPublico())
print("Pelicula 5:", peliculas[4].titulo, "-", peliculas[4].duracion, "min", "-", peliculas[4].clasificacion, "-", peliculas[4].genero, "-", peliculas[4].obtenerSinopsis(), "-", "Apta:", peliculas[4].esAptaParaTodoPublico())
print("Pelicula 6:", peliculas[5].titulo, "-", peliculas[5].duracion, "min", "-", peliculas[5].clasificacion, "-", peliculas[5].genero, "-", peliculas[5].obtenerSinopsis(), "-", "Apta:", peliculas[5].esAptaParaTodoPublico())
print("Pelicula 7:", peliculas[6].titulo, "-", peliculas[6].duracion, "min", "-", peliculas[6].clasificacion, "-", peliculas[6].genero, "-", peliculas[6].obtenerSinopsis(), "-", "Apta:", peliculas[6].esAptaParaTodoPublico())
print("Pelicula 8:", peliculas[7].titulo, "-", peliculas[7].duracion, "min", "-", peliculas[7].clasificacion, "-", peliculas[7].genero, "-", peliculas[7].obtenerSinopsis(), "-", "Apta:", peliculas[7].esAptaParaTodoPublico())
print("Pelicula 9:", peliculas[8].titulo, "-", peliculas[8].duracion, "min", "-", peliculas[8].clasificacion, "-", peliculas[8].genero, "-", peliculas[8].obtenerSinopsis(), "-", "Apta:", peliculas[8].esAptaParaTodoPublico())
print("Pelicula 10:", peliculas[9].titulo, "-", peliculas[9].duracion, "min", "-", peliculas[9].clasificacion, "-", peliculas[9].genero, "-", peliculas[9].obtenerSinopsis(), "-", "Apta:", peliculas[9].esAptaParaTodoPublico())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE SALAS (10 OBJETOS) ---")

salas = [
    Sala(TipoSala.DOSD, 100, False),
    Sala(TipoSala.TRESD, 120, False),
    Sala(TipoSala.IMAX, 150, True),
    Sala(TipoSala.DOSD, 80, False),
    Sala(TipoSala.TRESD, 200, True),
    Sala(TipoSala.DOSD, 90, False),
    Sala(TipoSala.TRESD, 110, False),
    Sala(TipoSala.IMAX, 130, True),
    Sala(TipoSala.DOSD, 140, False),
    Sala(TipoSala.TRESD, 160, True)
]

print("Sala 1:", salas[0].tipo.name, "-", "Capacidad:", salas[0].capacidadTotal, "-", "VIP:", salas[0].esVip)
print("Sala 2:", salas[1].tipo.name, "-", "Capacidad:", salas[1].capacidadTotal, "-", "VIP:", salas[1].esVip)
print("Sala 3:", salas[2].tipo.name, "-", "Capacidad:", salas[2].capacidadTotal, "-", "VIP:", salas[2].esVip)
print("Sala 4:", salas[3].tipo.name, "-", "Capacidad:", salas[3].capacidadTotal, "-", "VIP:", salas[3].esVip)
print("Sala 5:", salas[4].tipo.name, "-", "Capacidad:", salas[4].capacidadTotal, "-", "VIP:", salas[4].esVip)
print("Sala 6:", salas[5].tipo.name, "-", "Capacidad:", salas[5].capacidadTotal, "-", "VIP:", salas[5].esVip)
print("Sala 7:", salas[6].tipo.name, "-", "Capacidad:", salas[6].capacidadTotal, "-", "VIP:", salas[6].esVip)
print("Sala 8:", salas[7].tipo.name, "-", "Capacidad:", salas[7].capacidadTotal, "-", "VIP:", salas[7].esVip)
print("Sala 9:", salas[8].tipo.name, "-", "Capacidad:", salas[8].capacidadTotal, "-", "VIP:", salas[8].esVip)
print("Sala 10:", salas[9].tipo.name, "-", "Capacidad:", salas[9].capacidadTotal, "-", "VIP:", salas[9].esVip)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE FUNCIONES (10 OBJETOS) ---")

funciones = [
    Funcion(1, Pelicula("Los guardianes de la Galaxia", 120, "B", "Acción"), Sala(TipoSala.DOSD, 100, False), "2026-03-05 20:00", 100),
    Funcion(2, Pelicula("Barbie", 110, "A", "Comedia"), Sala(TipoSala.TRESD, 120, False), "2026-03-05 18:00", 80),
    Funcion(3, Pelicula("Spiderman", 130, "B", "Acción"), Sala(TipoSala.IMAX, 150, True), "2026-03-05 21:00", 90),
    Funcion(4, Pelicula("Avengers", 150, "B", "Acción"), Sala(TipoSala.DOSD, 80, False), "2026-03-06 19:00", 120),
    Funcion(5, Pelicula("El conjuro", 100, "C", "Terror"), Sala(TipoSala.TRESD, 200, True), "2026-03-06 20:00", 110),
    Funcion(6, Pelicula("Stray Kids", 90, "A", "Musical"), Sala(TipoSala.DOSD, 90, False), "2026-03-07 17:00", 70),
    Funcion(7, Pelicula("Zootopia", 95, "AA", "Animación"), Sala(TipoSala.TRESD, 110, False), "2026-03-07 22:00", 95),
    Funcion(8, Pelicula("Bob Esponja", 85, "AA", "Animación"), Sala(TipoSala.IMAX, 130, True), "2026-03-08 20:00", 60),
    Funcion(9, Pelicula("La Sirenita", 100, "A", "Fantasia"), Sala(TipoSala.DOSD, 140, False), "2026-03-08 19:00", 85),
    Funcion(10, Pelicula("El zorro de las nueve colas", 140, "B", "Drama"), Sala(TipoSala.TRESD, 160, True), "2026-03-09 21:00", 100)
]

print("Funcion 1:", funciones[0].idFuncion, "-", funciones[0].pelicula.titulo, "-", funciones[0].sala.tipo.name, "-", funciones[0].horarioInicio, "-", "Precio:", funciones[0].precioBase, "-", "Libres:", funciones[0].calcularAsientosLibres())
print("Funcion 2:", funciones[1].idFuncion, "-", funciones[1].pelicula.titulo, "-", funciones[1].sala.tipo.name, "-", funciones[1].horarioInicio, "-", "Precio:", funciones[1].precioBase, "-", "Libres:", funciones[1].calcularAsientosLibres())
print("Funcion 3:", funciones[2].idFuncion, "-", funciones[2].pelicula.titulo, "-", funciones[2].sala.tipo.name, "-", funciones[2].horarioInicio, "-", "Precio:", funciones[2].precioBase, "-", "Libres:", funciones[2].calcularAsientosLibres())
print("Funcion 4:", funciones[3].idFuncion, "-", funciones[3].pelicula.titulo, "-", funciones[3].sala.tipo.name, "-", funciones[3].horarioInicio, "-", "Precio:", funciones[3].precioBase, "-", "Libres:", funciones[3].calcularAsientosLibres())
print("Funcion 5:", funciones[4].idFuncion, "-", funciones[4].pelicula.titulo, "-", funciones[4].sala.tipo.name, "-", funciones[4].horarioInicio, "-", "Precio:", funciones[4].precioBase, "-", "Libres:", funciones[4].calcularAsientosLibres())
print("Funcion 6:", funciones[5].idFuncion, "-", funciones[5].pelicula.titulo, "-", funciones[5].sala.tipo.name, "-", funciones[5].horarioInicio, "-", "Precio:", funciones[5].precioBase, "-", "Libres:", funciones[5].calcularAsientosLibres())
print("Funcion 7:", funciones[6].idFuncion, "-", funciones[6].pelicula.titulo, "-", funciones[6].sala.tipo.name, "-", funciones[6].horarioInicio, "-", "Precio:", funciones[6].precioBase, "-", "Libres:", funciones[6].calcularAsientosLibres())
print("Funcion 8:", funciones[7].idFuncion, "-", funciones[7].pelicula.titulo, "-", funciones[7].sala.tipo.name, "-", funciones[7].horarioInicio, "-", "Precio:", funciones[7].precioBase, "-", "Libres:", funciones[7].calcularAsientosLibres())
print("Funcion 9:", funciones[8].idFuncion, "-", funciones[8].pelicula.titulo, "-", funciones[8].sala.tipo.name, "-", funciones[8].horarioInicio, "-", "Precio:", funciones[8].precioBase, "-", "Libres:", funciones[8].calcularAsientosLibres())
print("Funcion 10:", funciones[9].idFuncion, "-", funciones[9].pelicula.titulo, "-", funciones[9].sala.tipo.name, "-", funciones[9].horarioInicio, "-", "Precio:", funciones[9].precioBase, "-", "Libres:", funciones[9].calcularAsientosLibres())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE PROMOCIONES (10 OBJETOS) ---")

promociones = [
    Promocion("PROMO1", "Promocion 1", 0.10, "2026-05-01"),
    Promocion("PROMO2", "Promocion 2", 0.15, "2026-05-02"),
    Promocion("PROMO3", "Promocion 3", 0.20, "2026-05-03"),
    Promocion("PROMO4", "Promocion 4", 0.25, "2026-05-04"),
    Promocion("PROMO5", "Promocion 5", 0.30, "2026-05-05"),
    Promocion("PROMO6", "Promocion 6", 0.35, "2026-05-06"),
    Promocion("PROMO7", "Promocion 7", 0.40, "2026-05-07"),
    Promocion("PROMO8", "Promocion 8", 0.45, "2026-05-08"),
    Promocion("PROMO9", "Promocion 9", 0.50, "2026-05-09"),
    Promocion("PROMO10", "Promocion 10", 0.55, "2026-05-10")
]

print("Promocion 1:", promociones[0].codigo, "-", promociones[0].descripcion, "-", "Descuento:", promociones[0].porcentajeDescuento, "-", "Vigencia:", promociones[0].fechaExpiracion)
print("Promocion 2:", promociones[1].codigo, "-", promociones[1].descripcion, "-", "Descuento:", promociones[1].porcentajeDescuento, "-", "Vigencia:", promociones[1].fechaExpiracion)
print("Promocion 3:", promociones[2].codigo, "-", promociones[2].descripcion, "-", "Descuento:", promociones[2].porcentajeDescuento, "-", "Vigencia:", promociones[2].fechaExpiracion)
print("Promocion 4:", promociones[3].codigo, "-", promociones[3].descripcion, "-", "Descuento:", promociones[3].porcentajeDescuento, "-", "Vigencia:", promociones[3].fechaExpiracion)
print("Promocion 5:", promociones[4].codigo, "-", promociones[4].descripcion, "-", "Descuento:", promociones[4].porcentajeDescuento, "-", "Vigencia:", promociones[4].fechaExpiracion)
print("Promocion 6:", promociones[5].codigo, "-", promociones[5].descripcion, "-", "Descuento:", promociones[5].porcentajeDescuento, "-", "Vigencia:", promociones[5].fechaExpiracion)
print("Promocion 7:", promociones[6].codigo, "-", promociones[6].descripcion, "-", "Descuento:", promociones[6].porcentajeDescuento, "-", "Vigencia:", promociones[6].fechaExpiracion)
print("Promocion 8:", promociones[7].codigo, "-", promociones[7].descripcion, "-", "Descuento:", promociones[7].porcentajeDescuento, "-", "Vigencia:", promociones[7].fechaExpiracion)
print("Promocion 9:", promociones[8].codigo, "-", promociones[8].descripcion, "-", "Descuento:", promociones[8].porcentajeDescuento, "-", "Vigencia:", promociones[8].fechaExpiracion)
print("Promocion 10:", promociones[9].codigo, "-", promociones[9].descripcion, "-", "Descuento:", promociones[9].porcentajeDescuento, "-", "Vigencia:", promociones[9].fechaExpiracion)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE ESPACIOS (10 OBJETOS) ---")

espacios = [
    Espacio(1, "Lobby", "Entrada principal"),
    Espacio(2, "Pasillo A", "Planta baja"),
    Espacio(3, "Pasillo B", "Planta alta"),
    Espacio(4, "Baños Hombres", "Planta baja"),
    Espacio(5, "Baños Mujeres", "Planta baja"),
    Espacio(6, "Estacionamiento", "Exterior"),
    Espacio(7, "Terraza", "Segundo piso"),
    Espacio(8, "Sala de espera", "Planta baja"),
    Espacio(9, "Área VIP", "Planta alta"),
    Espacio(10, "Oficina Administrativa", "Planta alta")
]

print("Espacio 1:", espacios[0].idEspacio, "-", espacios[0].nombre, "-", espacios[0].ubicacion)
print("Espacio 2:", espacios[1].idEspacio, "-", espacios[1].nombre, "-", espacios[1].ubicacion)
print("Espacio 3:", espacios[2].idEspacio, "-", espacios[2].nombre, "-", espacios[2].ubicacion)
print("Espacio 4:", espacios[3].idEspacio, "-", espacios[3].nombre, "-", espacios[3].ubicacion)
print("Espacio 5:", espacios[4].idEspacio, "-", espacios[4].nombre, "-", espacios[4].ubicacion)
print("Espacio 6:", espacios[5].idEspacio, "-", espacios[5].nombre, "-", espacios[5].ubicacion)
print("Espacio 7:", espacios[6].idEspacio, "-", espacios[6].nombre, "-", espacios[6].ubicacion)
print("Espacio 8:", espacios[7].idEspacio, "-", espacios[7].nombre, "-", espacios[7].ubicacion)
print("Espacio 9:", espacios[8].idEspacio, "-", espacios[8].nombre, "-", espacios[8].ubicacion)
print("Espacio 10:", espacios[9].idEspacio, "-", espacios[9].nombre, "-", espacios[9].ubicacion)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE ZONAS DE COMIDA (10 OBJETOS) ---")

zonas = [
    ZonaComida(["Palomitas", "Refresco"], {"Palomitas": 50, "Refresco": 100}),
    ZonaComida(["Nachos", "Queso"], {"Nachos": 40, "Queso": 80}),
    ZonaComida(["Hotdog", "Refresco"], {"Hotdog": 30, "Refresco": 90}),
    ZonaComida(["Pizza", "Agua"], {"Pizza": 25, "Agua": 70}),
    ZonaComida(["Hamburguesa", "Papas"], {"Hamburguesa": 20, "Papas": 60}),
    ZonaComida(["Sandwich", "Jugo"], {"Sandwich": 15, "Jugo": 50}),
    ZonaComida(["Tacos", "Salsa"], {"Tacos": 35, "Salsa": 40}),
    ZonaComida(["Ensalada", "Agua"], {"Ensalada": 10, "Agua": 30}),
    ZonaComida(["Helado", "Galletas"], {"Helado": 45, "Galletas": 55}),
    ZonaComida(["Café", "Donas"], {"Café": 60, "Donas": 20})
]

print("Zona 1:", zonas[0].listaProductos, "-", "Stock:", zonas[0].stockActual)
print("Zona 2:", zonas[1].listaProductos, "-", "Stock:", zonas[1].stockActual)
print("Zona 3:", zonas[2].listaProductos, "-", "Stock:", zonas[2].stockActual)
print("Zona 4:", zonas[3].listaProductos, "-", "Stock:", zonas[3].stockActual)
print("Zona 5:", zonas[4].listaProductos, "-", "Stock:", zonas[4].stockActual)
print("Zona 6:", zonas[5].listaProductos, "-", "Stock:", zonas[5].stockActual)
print("Zona 7:", zonas[6].listaProductos, "-", "Stock:", zonas[6].stockActual)
print("Zona 8:", zonas[7].listaProductos, "-", "Stock:", zonas[7].stockActual)
print("Zona 9:", zonas[8].listaProductos, "-", "Stock:", zonas[8].stockActual)
print("Zona 10:", zonas[9].listaProductos, "-", "Stock:", zonas[9].stockActual)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

print("--- REGISTRO MANUAL DE RESERVAS (10 OBJETOS) ---")

reservas = [
    Reserva(1, usuarios[0], funciones[0], ["A1", "A2"], 200),
    Reserva(2, usuarios[1], funciones[1], ["B1", "B2"], 160),
    Reserva(3, usuarios[2], funciones[2], ["C1", "C2"], 180),
    Reserva(4, usuarios[3], funciones[3], ["D1", "D2"], 240),
    Reserva(5, usuarios[4], funciones[4], ["E1", "E2"], 220),
    Reserva(6, usuarios[5], funciones[5], ["F1", "F2"], 140),
    Reserva(7, usuarios[6], funciones[6], ["G1", "G2"], 190),
    Reserva(8, usuarios[7], funciones[7], ["H1", "H2"], 120),
    Reserva(9, usuarios[8], funciones[8], ["I1", "I2"], 170),
    Reserva(10, usuarios[9], funciones[9], ["J1", "J2"], 200)
]

print("Reserva 1:", reservas[0].idReserva, "-", reservas[0].usuario.nombre, "-", reservas[0].funcion.pelicula.titulo, "-", reservas[0].funcion.sala.tipo.name, "-", reservas[0].asientos, "-", "Monto:", reservas[0].montoTotal, "-", "Estado:", reservas[0].estado.name)
print("Reserva 2:", reservas[1].idReserva, "-", reservas[1].usuario.nombre, "-", reservas[1].funcion.pelicula.titulo, "-", reservas[1].funcion.sala.tipo.name, "-", reservas[1].asientos, "-", "Monto:", reservas[1].montoTotal, "-", "Estado:", reservas[1].estado.name)
print("Reserva 3:", reservas[2].idReserva, "-", reservas[2].usuario.nombre, "-", reservas[2].funcion.pelicula.titulo, "-", reservas[2].funcion.sala.tipo.name, "-", reservas[2].asientos, "-", "Monto:", reservas[2].montoTotal, "-", "Estado:", reservas[2].estado.name)
print("Reserva 4:", reservas[3].idReserva, "-", reservas[3].usuario.nombre, "-", reservas[3].funcion.pelicula.titulo, "-", reservas[3].funcion.sala.tipo.name, "-", reservas[3].asientos, "-", "Monto:", reservas[3].montoTotal, "-", "Estado:", reservas[3].estado.name)
print("Reserva 5:", reservas[4].idReserva, "-", reservas[4].usuario.nombre, "-", reservas[4].funcion.pelicula.titulo, "-", reservas[4].funcion.sala.tipo.name, "-", reservas[4].asientos, "-", "Monto:", reservas[4].montoTotal, "-", "Estado:", reservas[4].estado.name)
print("Reserva 6:", reservas[5].idReserva, "-", reservas[5].usuario.nombre, "-", reservas[5].funcion.pelicula.titulo, "-", reservas[5].funcion.sala.tipo.name, "-", reservas[5].asientos, "-", "Monto:", reservas[5].montoTotal, "-", "Estado:", reservas[5].estado.name)
print("Reserva 7:", reservas[6].idReserva, "-", reservas[6].usuario.nombre, "-", reservas[6].funcion.pelicula.titulo, "-", reservas[6].funcion.sala.tipo.name, "-", reservas[6].asientos, "-", "Monto:", reservas[6].montoTotal, "-", "Estado:", reservas[6].estado.name)
print("Reserva 8:", reservas[7].idReserva, "-", reservas[7].usuario.nombre, "-", reservas[7].funcion.pelicula.titulo, "-", reservas[7].funcion.sala.tipo.name, "-", reservas[7].asientos, "-", "Monto:", reservas[7].montoTotal, "-", "Estado:", reservas[7].estado.name)
print("Reserva 9:", reservas[8].idReserva, "-", reservas[8].usuario.nombre, "-", reservas[8].funcion.pelicula.titulo, "-", reservas[8].funcion.sala.tipo.name, "-", reservas[8].asientos, "-", "Monto:", reservas[8].montoTotal, "-", "Estado:", reservas[8].estado.name)
print("Reserva 10:", reservas[9].idReserva, "-", reservas[9].usuario.nombre, "-", reservas[9].funcion.pelicula.titulo, "-", reservas[9].funcion.sala.tipo.name, "-", reservas[9].asientos, "-", "Monto:", reservas[9].montoTotal, "-", "Estado:", reservas[9].estado.name)

print("--- VALIDACIÓN DE DATOS FINALIZADA ---\n")

print(" ---------------RESERVA DE ENTRADAS ---------------")
print("Usuario:", usuarios[0].nombre, "(Puntos de fidelidad :", usuarios[0].puntosFidelidad, ")")
print("Película:", funciones[0].pelicula.titulo, "| Sala:", funciones[0].sala.tipo.name)

cantidad = int(input("¿Cuántos asientos quieres reservar?: "))
asientos_elegidos = []

i = 1
while i <= cantidad:
    asiento = input(f"Ingrese asiento #{i}: ")
    if asiento in funciones[0].asientosOcupados:
        print(f"El asiento {asiento} ya está ocupado. Seleccione otro.")
        
    else:
        funciones[0].asientosOcupados.append(asiento)
        asientos_elegidos.append(asiento)
        print(f"El asiento {asiento} ha sido reservado.")
        i += 1   

monto = funciones[0].precioBase * len(asientos_elegidos)
reserva1 = Reserva(1, usuarios[0], funciones[0], asientos_elegidos, monto)

print("Monto base:", monto)


print("\n-----------------PROMOCIONES-----------------")
codigo = input("Ingrese el código de promocion: ")
promo_valida = None

for promo in promociones:
    if promo.codigo == codigo:
        promo_valida = promo
        break

if promo_valida:
    print("Escaneando código...")
    print(f"(Descuento del {promo_valida.porcentajeDescuento*100}% aplicado).")
    reserva1.montoTotal = reserva1.montoTotal * (1 - promo_valida.porcentajeDescuento)
    print(f"Promoción aplicada: {promo_valida.descripcion}, Precio final: {reserva1.montoTotal}")
    reserva1.confirmarPago()
    reserva1.generarTicket()
else:
    print("Código inválido.")


print("\n--------------- FUNCIONES---------------")
empleados[1].gestionarFunciones(funciones[1])  
empleados[0].gestionarFunciones(funciones[1])  


print("\n---------------ESPACIOS---------------")
espacios[0].verificarDisponibilidad()
espacios[0].limpiarEspacio()


print("\n--------------- VENTA DE PRODUCTOS ---------------")

menu = {}
contador = 1
for m in zonas:
    for producto in m.listaProductos:  
        menu[contador] = producto
        contador += 1

print("Menú:")
for id, nombre in menu.items():
    print(f"{id}. {nombre}")

opcion = input("Ingrese el ID o nombre del producto que desea comprar: ")

if opcion.isdigit():
    opcion = int(opcion)
    if opcion in menu:
        producto = menu[opcion]
        vendido = False
        for m in zonas:
            if producto in m.listaProductos:
                m.venderProducto(producto)
                vendido = True
                break
        if not vendido:
            print(f"El producto {producto} no está disponible.")
    else:
        print("ID inválido.")
else:
    producto = opcion
    vendido = False
    for m in zonas:
        if producto in m.listaProductos:
            m.venderProducto(producto)
            vendido = True
            break
    if not vendido:
        print(f"El producto {producto} no está disponible.")
print("\n----------------DATOS VALIDADOS ----------------")
