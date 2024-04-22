import json

# Leer el archivo JSON
with open('running-config.json', 'r') as archivo:
    configuracion_router = json.load(archivo)

# Mostrar el nombre del router
print("Hostname del router:", configuracion_router["router"]["hostname"])

# Mostrar las interfaces y sus configuraciones
print("\nInterfaces:")
for interfaz in configuracion_router["router"]["interfaces"]:
    print("Nombre:", interfaz["name"])
    print("Descripción:", interfaz["description"])
    print("Dirección IP:", interfaz["ip_address"])
    print("Máscara de subred:", interfaz["subnet_mask"])
    print("Estado:", interfaz["status"])
    print("-----------------------")

# Mostrar los protocolos de enrutamiento y sus configuraciones
print("\nProtocolos de enrutamiento:")
for protocolo in configuracion_router["router"]["routing"]["protocols"]:
    print("Nombre:", protocolo["name"])
    print("Estado:", protocolo["status"])
    print("Parámetros:", protocolo["parameters"])
    print("-----------------------")

# Mostrar las configuraciones de seguridad
print("\nConfiguraciones de seguridad:")
for password in configuracion_router["router"]["security"]["passwords"]:
    print("Nombre de usuario:", password["username"])
    print("Contraseña:", password["password"])
    print("-----------------------")
