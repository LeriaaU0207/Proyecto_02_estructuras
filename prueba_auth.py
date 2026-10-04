from auth_manager import AuthManager

auth = AuthManager()

print("=== PRUEBA DEL SISTEMA DE AUTENTICACION ===")


# PRUEBA 1: Registrar usuarios
print("\n1. Registrando usuarios:")

print("Anthony:", auth.registrar_usuario("Anthony", "1234"))
print("Maria:", auth.registrar_usuario("Maria", "abcd"))
print("Carlos:", auth.registrar_usuario("Carlos", "5678"))


# PRUEBA 2: Usuario repetido
print("\n2. Intentando registrar un usuario repetido:")

print("Anthony:", auth.registrar_usuario("Anthony", "otra"))


# PRUEBA 3: Inicio de sesion
print("\n3. Probando inicio de sesion:")

print(
    "Anthony con contrasena correcta:",
    auth.iniciar_sesion("Anthony", "1234")
)

print(
    "Anthony con contrasena incorrecta:",
    auth.iniciar_sesion("Anthony", "9999")
)

print(
    "Usuario que no existe:",
    auth.iniciar_sesion("Pedro", "1234")
)


# PRUEBA 4: Mostrar tabla
print("\n4. Contenido de la tabla Hash:")

auth.mostrar_tabla()


# PRUEBA 5: Eliminar usuario
print("\n5. Eliminando usuario Maria:")

print(
    "Resultado:",
    auth.eliminar_usuario("Maria")
)


# PRUEBA 6: Mostrar tabla despues de eliminar
print("\n6. Tabla despues de eliminar a Maria:")

auth.mostrar_tabla()


# PRUEBA 7: Buscar dos nombres que produzcan una colision
print("\n7. Buscando una colision automaticamente:")

nombre1 = None
nombre2 = None
indice_colision = None

nombres = []

for numero in range(100):
    nombre = "Usuario" + str(numero)
    nombres.append(nombre)


for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):

        indice1 = auth.tabla_usuarios.funcion_hash(nombres[i])
        indice2 = auth.tabla_usuarios.funcion_hash(nombres[j])

        if indice1 == indice2:
            nombre1 = nombres[i]
            nombre2 = nombres[j]
            indice_colision = indice1
            break

    if nombre1 is not None:
        break


print("Primer usuario:", nombre1)
print("Segundo usuario:", nombre2)
print("Ambos pertenecen al indice:", indice_colision)


# PRUEBA 8: Insertar los usuarios que colisionan
print("\n8. Insertando usuarios con colision:")

print(
    nombre1,
    auth.registrar_usuario(nombre1, "1111")
)

print(
    nombre2,
    auth.registrar_usuario(nombre2, "2222")
)


# PRUEBA 9: Mostrar la tabla con la colision
print("\n9. Tabla Hash con la colision:")

auth.mostrar_tabla()


# PRUEBA 10: Comprobar que ambos usuarios funcionan
print("\n10. Comprobando usuarios de la colision:")

print(
    nombre1,
    auth.iniciar_sesion(nombre1, "1111")
)

print(
    nombre2,
    auth.iniciar_sesion(nombre2, "2222")
)