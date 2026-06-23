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
            

running = True
print("Bienvenido al gestor de bibliotecas de la UCU")
while running == True:
    print("¿Que quieres gestionar?")
    choice = input("Estudiantes, Libros, Prestamos o Salir")
    choice = normalizar(choice)
    match menu[choice]:
        case "estudiantes":
            print 
        case "libros":
            print ("Libros")
            print("1: Agregar libro")
            print("2: Remover libro")
            print("3: Buscar libros")
        case "prestamos":
            print ("Prestamos")
        case "salir":
            running == False
        case _:
            Print("Ingrese un valor valido")