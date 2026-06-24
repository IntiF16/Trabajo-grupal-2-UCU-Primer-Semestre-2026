usuarios ={} #{numero_socio: nombre}
prestamos ={}
catalogo  ={}
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

class ErrorValorNumSo(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.value)
    
def registrar_usuario(usuarios,numero_socio,nombre):
    try:
        if numero_socio not in usuarios:
            usuarios[numero_socio] = {"numero de socio":numero_socio, "nombre":nombre, "prestamos activos":[]}
            return usuarios[numero_socio]
    except ErrorValorNumSo:
        print("Usuario ya reguistrado")
                
def dar_baja_usuario (usuarios, prestamos, numero_socio):
    if numero_socio in usuarios and not usuarios[numero_socio]['prestamos activos']:
        del usuarios[numero_socio]

def guardar_datos(catalogo,usuarios,prestamos):
    with open ("archivo.txt", "a") as archivo:
        for catalogo in lista:
            print(catalogo, file=archivo)
        for usuarios in lista:
            print(usuarios, file=archivo)
        for prestamos in lista:
            print (prestamos, file=archivo)

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
                        n_socio= input("ingrese numero de socio")
                        nom_usuario= input("ingrese nombre de usuario")
                        registrar_usuario(usuarios,n_socio,nom_usuario)
                
                    case 2:
                        e_socio=input("ingrese numero de socio a eliminar")
                        dar_baja_usuario (usuarios, usuarios[e_socio]['prestamos activos'], e_socio)
                        
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
guardar_datos(catalogo,usuarios,prestamos)




