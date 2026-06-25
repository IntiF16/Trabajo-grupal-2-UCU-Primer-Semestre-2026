def normalizar(text):
    text = text.lower()
    Ftext = ""
    subtext = list(text)
    for space in range(len(subtext)):
        match subtext[space]:
            case "á":
                subtext[space] = "a"
            case "é":
                subtext[space] = "e"
            case "í":
                subtext[space] = "i"
            case "ó":
                subtext[space] = "o"
            case "ú":
                subtext[space] = "u"
        Ftext = Ftext + subtext[space]
    return Ftext

def agregar_libro(catalogo,isbn,titulo,autor,genero,ejemplares):
    if isbn not in catalogo:
        catalogo[isbn]={"isbn": isbn, "titulo": titulo, "autor": autor, "ejemplares_disponibles": ejemplares, "ejemplares_totales": ejemplares}
    else:
        print("este libro ya esta en el catalogo")
    
def buscar_libro(catologo,termino):
    libros=[]
    termino= normalizar(text)
    for isbn in catalogo:
        if termino in normalizar(catalogo[isbn]["titulo"]) or termino in normalizar(catalogo[isbn]["autor"]) or termino in normalizar(catalogo[isbn]["genero"]):
            libros.append(catalogo[isbn])
    return libros

def eliminar_libro(catalogo,prestamos,isbn):
    if:
        todos_devueltos = True
        for i in prestamos:
            if isbn in catalogo:
                todos_devueltos = False
                break
        if todos_devueltos == True and isbn in catalogo:
            del isbn[catalogo]
    else:
        raise Exception ("este libro ya no se escuentra")

def cargar_datos(ruta):
    catalogo = {}
    usuarios = {}
    prestamos = {}
    
    try:
        with open(ruta,"r") as archivo:
            seccion_actual = None
            for linea in archivo:
                linea = linea.strip()
                
                if linea =="[CATALOGO]":
                    seccion_actual = "catalogo"
                elif linea =="[USUARIOS]":
                    seccion_actual = "usuarios"
                elif linea =="[PRESTAMOS]":
                    seccion_actual = "prestamos"
                elif linea == "":
                    continue
                
                elif seccion_actual == "catalogo":
                    partes = linea.split("|")
                    isbn = partes [0]
                    titulo = partes [1]
                    autor = partes [2]
                    genero = partes [3]
                    ejemplaresTotales = int(partes [4])
                    ejemplaresDisponibles = int(partes [5])
                    catalogo[isbn] = {
                        "isbn" = isbn
                        "titulo" = titulo
                        "autor" = autor
                        "genero" = genero
                        "ejemplaresTotales" = ejemplaresTotales
                        "ejemplaresDisponibles" = ejemplaresDisponibles
                    }
                elif seccion_actual == "usuarios":
                    partes = linea.split("|")
                    
                        
    
            
BooksChoice = 0            
UserChoice = 0
LoanChoice = 0
running = True
print("Bienvenido al gestor de bibliotecas de la UCU")
while running == True:
    print("¿Que quieres gestionar?")
    choice = input("Usuarios, Libros, Prestamos o Salir ")
    choice = normalizar(choice)
    match choice:
        case "usuarios":
            print("Menú gestión de usuario")
            print("1: Agregar Usuarios")
            print("2: Remover Usuarios")
            print("3: Historial Usuario")
            print("4: Salir")
            while UserChoice != 4:
                UserChoice = int(input("Ingrese un numero para elegir su acción "))
                match UserChoice:
                    case 1:
                        print('a')
                    case 2:
                        print('b')
                    case 3:
                        print('c')
                    case 4:
                        continue
                    case _:
                        print ("ingresa un numero valido ")
        case "libros":
            print ("Menú gestión de Libros")
            print("1: Agregar libro")
            print("2: Remover libro")
            print("3: Buscar libros")
            print("4: Salir")
            while BooksChoice != 4:
                BooksChoice = int(input("Ingrese un numero para elegir su acción "))
                match BooksChoice:
                    case 1: 
                        print('a')
                    case 2:
                        print('b')
                    case 3:
                        print('c')
                    case 4:
                        continue
                    case _:
                        print ("ingresa un numero valido ")
        case "prestamos":
            print ("Menú gestión de Prestamos")
            print("1: Registrar prestamo")
            print("2: Registrar devolución")
            print("3: Mostrar prestamos vencidos")
            print("4: Salir")
            while LoanChoice != 4:
                LoanChoice = int(input("Ingrese un numero para elegir su acción "))
                match LoanChoice:
                    case 1:
                        print('a')
                    case 2:
                        print('b')
                    case 3:
                        print('c')
                    case 4:
                        continue
                    case _:
                        print ("ingresa un numero valido ")
        case "salir":
            running = False
        case _:
            print("Ingrese un valor valido")
            
        
            