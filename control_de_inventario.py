class Producto:
    def __init__(self, id, nombre, cantidad):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}) - Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, nombre, cantidad):
        for producto in self.productos:
            if producto.id == id:
                producto.cantidad += cantidad
                return
        nuevo_producto = Producto(id, nombre, cantidad)
        self.productos.append(nuevo_producto)

    def quitar_producto(self, id, cantidad):
        for producto in self.productos:
            if producto.id == id:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    if producto.cantidad == 0:
                        self.productos.remove(producto)
                else:
                    print("Cantidad no disponible")
                return
        print("Producto no encontrado")

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                print(producto)
                return
        print("Producto no encontrado")


# Interfaz
def main():
    inventario = Inventario()

    while True:
        print("\nControl de Inventario")
        print("1. Agregar producto")
        print("2. Quitar producto")
        print("3. Mostrar inventario")
        print("4. Buscar producto por ID")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad del producto: "))
            inventario.agregar_producto(id, nombre, cantidad)

        elif opcion == "2":
            id = input("Introduce el ID del producto a quitar: ")
            cantidad = int(input("Introduce la cantidad a quitar: "))
            inventario.quitar_producto(id, cantidad)

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            id = input("Introduce el ID del producto a buscar: ")
            inventario.buscar_producto(id)

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

