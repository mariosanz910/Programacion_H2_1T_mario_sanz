import random

# Estructuras de datos para almacenar clientes, productos y pedidos
clientes = {}
productos = {"Café con leche": 10.0, "Napolitana de chocolate": 15.0, "Postre VIP": 20.0, "Pack de pipas": 5.0}
pedidos = {}

# Variable para finalizar la compra
fin = "fin"

# Inicio el espacio que tiene que haber entre cada operación para que se vea mejor
def espacio():
    print("                                                                          ")

# Función para mostrar el menú principal
def menu_principal():
    while True:
        espacio()
        print("--- Menú de Gestión de Pedidos ---")
        print("Eliga su opción introduciendo el número de la opción porfavor")
        espacio()
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
            espacio()
            print("--- 5 Salir del programa ---")
            print("Muchas gracias por usar la tienda online de la cafetería a domicilio: Starshark.")
            break
        else:
            print("Opción no válida. Intente de nuevo porfavor.")

# Función para registrar un cliente
def registrar_cliente():
    espacio()
    print("--- 1 Registro de Cliente ---")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección: ")
    email = input("Ingrese el correo electrónico: ")
    
    id_cliente = random.randint(1000, 9999)  # Genera un ID único entre 1000 y 9999
    
    clientes[id_cliente] = {"nombre": nombre, "direccion": direccion, "email": email} # Almacena el cliente en el diccionario clientes relacionando id_clientes con el diccionario clientes
    
    print("Cliente registrado con éxito. ID:", id_cliente, "Nombre:", nombre, "Dirección:", direccion, "Email:", email)

# Función para ver todos los clientes 
def ver_clientes():
    espacio()
    print("--- 2 Ver Clientes ---")
    print("Estos son los datos de los clietnes")
    for id_cliente, dato in clientes.items():
        print("ID:", id_cliente, "Nombre:", dato['nombre'], "Dirección:", dato['direccion'], "Email:", dato['email']) # Muestra los datos de cada cliente "despiezando" solo los items del diccionario 

# Función para realizar una compra
def realizar_compra():
    espacio()
    print("--- 3 Realizar Compra ---")
    id_cliente = int(input("Ingrese el ID del cliente que realiza la compra: "))
    
    if id_cliente not in clientes: # Comprueba que el id de clientes se encuentre en el diccionario clientes donde se almacenan todos los ID
        print("Cliente no registrado. Regístrelo primero.")
        return
    
    print("Productos disponibles:") # Muestra la cantidad de productos disponibles
    for producto, precio in productos.items():
        print("Producto:", producto, "Precio:", precio)

    productos_comprados = [] # Inicia la lista de la compra
    total_compra = 0 # Inicia el total de la compra, lo iniciamos a cero para evitar problemas 

    while True: # Bucle para comprar los productos e indicar la cantidad que quieres de ellos, lo cual multiplica el precio
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto == fin: # Condicional que termina el bucle de compra
            break
        if producto in productos: # Función que pide la cantidad de producto y actualiza el precio correspondiente al producto y la cantidad, primero comprueba que el producto exista
            cantidad = int(input("Ingrese la cantidad: "))
            productos_comprados.append((producto, cantidad))
            total_compra += productos[producto] * cantidad
        else:
            print("Ese producto no existe")
    
    numero_pedido = random.randint(1000, 9999)  # Genera un número de pedido 1000 y 9999
        
    pedidos[numero_pedido] = {"id_cliente": id_cliente, "productos": productos_comprados, "total": total_compra} # Almacena el Id del pedido en el diccionario pedidos relacionando el número de pedido con el id del cliente
    
    print("Compra realizada con éxito. Número de pedido:", numero_pedido, "Total de la compra:", total_compra)

# Función para realizar el seguimiento de un pedido
def seguimiento_pedido():
    print("--- 4 Seguimiento de Pedido ---")
    numero_pedido = int(input("Ingrese el número de pedido: "))

    if numero_pedido in pedidos:
        pedido = pedidos[numero_pedido]
        cliente = clientes[pedido["id_cliente"]]
        
        # Mostrar solo ID del pedido y nombre del cliente
        print("ID del pedido:", numero_pedido)
        print("Nombre del cliente:", cliente['nombre'])
    else:
        print("Pedido no encontrado.")

# Ejecutar el menú del programa
menu_principal()