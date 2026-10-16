
cola = []
pila = []
siguiente_id = 1


def registrar(cliente, asunto):
    global siguiente_id

    if not cliente.strip() or not asunto.strip():
        print("Datos inválidos")
        return

 
