
#La instrucción match es una forma más moderna y ordenada de usar muchos if/elif/else

fruta = input("Escribe el nombre de una fruta que te guste: ").lower()
match fruta:
    case "banana":
        print("Las bananas tienen mucho potasio")
    case "manzana":
        print("las manzanas son rojas o verdes")
    case "frutilla":
        print("las frutillas son ricas y dulces")
    case _:
        print("no conozco esa fruta")
    