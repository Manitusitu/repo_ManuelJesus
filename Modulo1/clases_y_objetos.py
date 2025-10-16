"""
Crea una clase llamada Libro que represente un libro en una biblioteca. La clase debe tener los siguientes atributos:
detalle aleatorio
titulo: el título del libro
autor: el autor del libro
paginas: el número total de páginas
disponible: un booleano que indica si el libro está disponible para préstamo (inicialmente True)
La clase debe tener los siguientes métodos:

Un constructor (__init__) que inicialice los atributos mencionados
Un método prestar() que cambie el estado de disponibilidad a False y devuelva un mensaje indicando que el libro ha sido prestado. Si el libro ya está prestado, debe devolver un mensaje indicando que no está disponible.
Un método devolver() que cambie el estado de disponibilidad a True y devuelva un mensaje indicando que el libro ha sido devuelto. Si el libro ya está disponible, debe devolver un mensaje indicando que el libro ya estaba en la biblioteca.
Un método informacion() que devuelva una cadena con toda la información del libro, incluyendo su estado de disponibilidad.
Prueba tu clase creando al menos dos objetos libro diferentes y llamando a todos sus métodos.
"""


class Libro:
    
        def __init__(self, titulo, autor, paginas, disponible=True):
            self.titulo = titulo
            self.autor = autor
            self.paginas = paginas
            self.disponible = disponible
            
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        
        def prestar(self):
            if self.disponible == False:
                return f"El libro {self.titulo} no esta disponible"
            else:
                self.disponible = False
                return f"El libro {self.titulo} ha sido prestado"
            
            
            
        def devolver(self):
            if self.disponible == True:
                return f"El libro {self.titulo} ya estaba en la biblioteca"
            else:
                self.disponible = True
                return f"El libro {self.titulo} ha sido devuelto"
            
    
        def informacion(self):
            return f"El libro que buscas es {self.titulo} escrito por {self.autor} el cual tiene {self.paginas} paginas y su estado de disponibilidad es {self.disponible}"


# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863, True)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471, False)
    
    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())
    print("\n")
    
    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print("\n")
    
    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print("\n")
    
    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print("\n")
    
    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print("\n")
    
    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print("\n")
    
    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print("\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()
