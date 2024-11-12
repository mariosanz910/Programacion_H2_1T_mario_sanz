import random

# Inicio los diccionarios necesarios
clientes = {}
productos = {"Café con leche": 10.0, "Napolitana de chocolate": 15.0, "Postre VIP": 20.0, "Pack de pipas": 5.0}
pedidos = {}

# Función para mostrar el menú principal
def menu_principal():
    while True:
        print("--- Menú de Gestión de Pedidos ---")
        print("Eliga su opción introduciendo el número de la opción porfavor")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Realizar compra")
        print("4. Seguimiento de compra")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            seguimiento_pedido()
        elif opcion == "5":
            print("--- 5 Salir del programa ---")
            print("Muchas gracias por usar la tienda online de la cafetería a domicilio: Starshark.")
            break
        else:
            print("Opción no válida. Intente de nuevo porfavor.")

# Función para registrar un cliente
def registrar_cliente():
    print("--- 1 Registro de Cliente ---")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección: ")
    email = input("Ingrese el correo electrónico: ")
    
    id_cliente = random.randint(1000, 9999)  # Genera un ID único entre 1000 y 9999
    while id_cliente in clientes:
        id_cliente = random.randint(1000, 9999)
    
    clientes[id_cliente] = {"nombre": nombre, "direccion": direccion, "email": email}
    
    print("Cliente registrado con éxito. ID:", id_cliente, "Nombre:", nombre, "Dirección:", direccion, "Email:", email)

# Función para ver todos los clientes o buscar un cliente específico
def ver_clientes():
    print("--- 2 Ver Clientes ---")
    opcion = input("Desea ver todos los clientes (1) o buscar por ID (2): ")
    
    if opcion == "1":
        for id_cliente, datos in clientes.items():
            print("ID:", id_cliente, "Nombre:", datos['nombre'], "Dirección:", datos['direccion'], "Email:", datos['email'])
    elif opcion == "2":
        id_cliente = int(input("Ingrese el ID del cliente a buscar: "))
        if id_cliente in clientes:
            datos = clientes[id_cliente]
            print("ID:", id_cliente, "Nombre:", datos['nombre'], "Dirección:", datos['direccion'], "Email:", datos['email'])
        else:
            print("Cliente no encontrado.")
    else:
        print("Opción no válida.")

# Función para realizar una compra
def realizar_compra():
    print("--- 3 Realizar Compra ---")
    id_cliente = int(input("Ingrese el ID del cliente que realiza la compra: "))
    
    if id_cliente not in clientes:
        print("Cliente no registrado. Regístrelo primero.")
        return
    
    print("\nProductos disponibles:")
    for producto, precio in productos.items():
        print("Producto:", producto, "Precio:", f"${precio:.2f}")

    productos_comprados = []
    total_compra = 0

    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == "fin":
            break
        if producto in productos:
            cantidad = int(input("Ingrese la cantidad: "))
            productos_comprados.append((producto, cantidad))
            total_compra += productos[producto] * cantidad
        else:
            print("Producto no disponible. Intente de nuevo.")
    
    numero_pedido = random.randint(1000, 9999)  # Genera un número de pedido único entre 1000 y 9999
    while numero_pedido in pedidos:
        numero_pedido = random.randint(1000, 9999)
        
    pedidos[numero_pedido] = {"id_cliente": id_cliente, "productos": productos_comprados, "total": total_compra}
    
    print("Compra realizada con éxito, por el cliente con número de pedido:", numero_pedido, "Total de la compra:", f"${total_compra:.2f}")

# Función para realizar el seguimiento de un pedido
def seguimiento_pedido():
    print("--- 4 Seguimiento de Pedido ---")
    numero_pedido = int(input("Ingrese el número de pedido: "))
    
    if numero_pedido in pedidos:
        pedido = pedidos[numero_pedido]
        cliente = clientes[pedido["id_cliente"]]
        
        print("Detalles del Pedido", numero_pedido)
        print("Cliente:", cliente['nombre'], "Dirección:", cliente['direccion'], "Email:", cliente['email'])
        print("Productos:")
        for producto, cantidad in pedido["productos"]:
            print("Producto:", producto, "Cantidad:", cantidad)
        print("Total:", f"${pedido['total']:.2f}")
    else:
        print("Pedido no encontrado.")

# Ejecutar el menú principal
menu_principal()
