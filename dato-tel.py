
nombre = input("Dime tu nombre: ")
edad = int(input("¿Tu edad es?: "))
telefono = input("Dime tu numero telefonico")
if nombre == "" or edad == 0 or telefono == "": 
    print("Los datos ingresados no son validos")
else:
    print(f"Hola {nombre}, como estas? ")