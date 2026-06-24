import datetime
from datetime import timedelta

Now = datetime.datetime.now()
usuarios ={
     "001": { "numero_socio": "001", "nombre": "Ana", 
"prestamos_activos": ["978-1"]
    }	} 
prestamos = [{ "numero_socio": "001", "isbn": "978-1",  
"fecha_prestamo": "02/06/2026",  
"fecha_limite": "09/06/2026", "devuelto": False}]
catalogo  ={
    "978-1": {  "isbn": "978-1", 
'titulo': 'Cien años de soledad',  
'autor': 'García Márquez', 'genero': 'Novela', 
'ejemplares_totales': 2, 
'ejemplares_disponibles': 1 }, 
'978-2': {  'isbn': '978-2', 
'titulo': 'El túnel',  
'autor': 'Sábato', 'genero': 'Novela', 
'ejemplares_totales': 1, 
'ejemplares_disponibles': 1 }
    }
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
            usuarios[numero_socio] = {"numero de socio":numero_socio, "nombre":nombre, "prestamos_activos":[]}
            return usuarios[numero_socio]
    except ErrorValorNumSo:
        print("Usuario ya reguistrado")
                
def dar_baja_usuario (usuarios, prestamos, numero_socio):
    if numero_socio in usuarios and not usuarios[numero_socio]['prestamos_activos']:
        del usuarios[numero_socio]

def historial_usuario(prestamos, numero_socio):
    historial = []
    for i in range(len(prestamos)):
        if prestamos[i]["numero_socio"] == numero_socio:
            historial.append(prestamos[i])
    return historial

def registrar_prestamo(catalogo, usuarios, prestamos, 
numero_socio, isbn, fecha_prestamo):
    try:
        if catalogo[isbn]["ejemplares_disponibles"] != 0 and numero_socio in usuarios:     
            prestamos.append({'numero_socio': numero_socio, 'isbn': isbn,  
    'fecha_prestamo': fecha_prestamo.strftime("%d/%m/%Y") ,  
    'fecha_limite': (fecha_prestamo + timedelta(weeks = 1)).strftime("%d/%m/%Y") , 'devuelto': False})
            usuarios[numero_socio]["prestamos_activos"].append(isbn)
            catalogo[isbn]["ejemplares_disponibles"] -= 1
    except:
        print("ingrese los datos correctos")

def registrar_devolucion(usuarios,catalogo, prestamos, numero_socio, isbn):
    try:
       for b in range(len(prestamos)):
            if prestamos[b]["numero_socio"] == numero_socio and prestamos[b]["isbn"] == isbn and prestamos[b]["devuelto"] == False:
                prestamos[b]["devuelto"] = True
                catalogo[isbn] ["ejemplares_disponibles"] += 1
                usuarios[numero_socio]["prestamos_activos"].remove(isbn)
                break
    except KeyError:
        print("Error: El número de socio o el ISBN ingresado no existen en el sistema.")
    except ValueError:
        print("Error: El libro no se encuentra en la lista de préstamos activos del usuario.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")            
        
def listar_vencidos(prestamos, fecha_actual):
    vencidos = []
    
    for d in prestamos:
        fecha_objeto = datetime.datetime.strptime(d["fecha_limite"], "%d/%m/%Y")
        if fecha_objeto < fecha_actual and d["devuelto"] == False:
            vencidos.append(d)
    return vencidos
    
def guardar_datos(catalogo,usuarios,prestamos):
    with open ("archivo.txt", "a") as archivo:
        for item in catalogo:
            print(catalogo, file=archivo)
        for item in usuarios:
            print(usuarios, file=archivo)
        for item in prestamos:
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
            Userchoice=0
            while UserChoice != 4:
                print("--- Menú gestión de usuario ---")
                print("1: Agregar Usuarios")
                print("2: Remover Usuarios")
                print("3: Historial Usuario")
                print("4: Salir")
                UserChoice = int(input("Ingrese un numero para elegir su acción "))
                match UserChoice:
                    case 1:
                        n_socio= input("ingrese numero de socio")
                        nom_usuario= input("ingrese nombre de usuario")
                        registrar_usuario(usuarios,n_socio,nom_usuario)
                    case 2:
                        e_socio=input("ingrese numero de socio a eliminar")
                        dar_baja_usuario(usuarios, prestamos, e_socio)
                    case 3:
                        h_socio = input("Ingrese numero de socio: ")
                        historial = historial_usuario(prestamos, h_socio)
                        if historial:
                            for p in historial:
                                print(p)
                        else:
                            print("El usuario no tiene préstamos registrados.")
                    case 4:
                        continue
                    case _:
                        print ("ingresa un numero valido ")
        case "libros":
            BooksChoice = 0
            while BooksChoice != 4:
                print ("--- Menú gestión de Libros ---")
                print("1: Agregar libro")
                print("2: Remover libro")
                print("3: Buscar libros")
                print("4: Salir")
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
            LoanChoice= 0
            while LoanChoice != 4:
                print ("--- Menú gestión de Prestamos ---")
                print("1: Registrar prestamo")
                print("2: Registrar devolución")
                print("3: Mostrar prestamos vencidos")
                print("4: Salir")
                LoanChoice = int(input("Ingrese un numero para elegir su acción "))
                match LoanChoice:
                    case 1:
                        print ("--- Ingresar Prestamo ---")
                        Ns = input("ingresa el numero del socio")
                        Nbok = input("ingresa el isbn del libro")
                        registrar_prestamo(catalogo, usuarios, prestamos, Ns, Nbok, Now)
                        print (prestamos)
                        print("ingreso registrado con exito")
                    case 2:
                        print("--- Registrar Devolución ---")
                        LoanRUser = input("Ingresa el número del socio: ")
                        LoanRIsbn = input("Ingresa el ISBN del libro a devolver: ")
                        registrar_devolucion(usuarios, catalogo, prestamos, LoanRUser, LoanRIsbn)
                        print (prestamos)
                        print("¡Devolución registrada con éxito!")
                    case 3:
                        print("--- Listar Prestamos vencidos ---")
                        print(listar_vencidos(prestamos, Now))
                    case 4:
                        continue
                    case _:
                        print ("ingresa un numero valido ")
        case "salir":
            running = False
        case _:
            print("Ingrese un valor valido")
