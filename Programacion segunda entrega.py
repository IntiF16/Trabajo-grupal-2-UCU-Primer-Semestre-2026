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
menu = {"estudiantes":1, "libros": 2, "prestamos":3}

print("Bienvenido al gestor de bibliotecas de la UCU")
while running == True:
    print("¿Que quieres gestionar?")
    choice = input("Estudiantes, Libros, Prestamos o Salir")
    choice = normalizar(choice)
    match menu[choice]:
        case 1:
            Print("1: Agregar libro")
            Print("2: Remover libro")
            Print("3: Buscar libros")
        case 2:
            print ("Libros")
        case 3:
            print ("Prestamos")
        case 4:
            running == False
        case _:
            Print("Ingrese un valor valido")