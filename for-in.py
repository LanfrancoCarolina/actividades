
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes","Sabado","Domingo"]
for dia in dias_semana:
    print(f"Hoy es {dia}")

while True:
    numero = int(input("Elige un número del 1 al 10 a ver si adivinás cuál estoy pensando: "))
    if numero == 3:
        print("¡Adivinaste!")
        break  
    else:
        print("Sigue participando")


    

