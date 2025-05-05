
contraseña = input("Escribe tu contraseña: ")
confirme_contraseña = input("Repite la contraseña: ")
if contraseña ==  "" or confirme_contraseña == "":
    print("contraseña vacia")
elif contraseña == confirme_contraseña:
    print("Ingresando...")
else: 
    print("contraseña equivocada")


#Aqui si quiero que en el primer dato vacio me salte el error
contraseña = input("Escribe tu contraseña: ")
if contraseña == "":
    print("Contraseña vacía")
else:
    confirme_contraseña = input("Repite la contraseña: ")
    if confirme_contraseña == "":
        print("Contraseña vacía")
    elif contraseña == confirme_contraseña:
        print("Ingresando...")
    else:
        print("Contraseña equivocada")
