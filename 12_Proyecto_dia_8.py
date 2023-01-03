import numeros
from os import system

def preguntar():

    print("Bienvenido a 'Farmacia Pipi'")

    while True:
        system("cls")
        print("Elige una opcion deseada:\n"
              "[P] - Perfumeria\n"
              "[F] - Farmacia\n"
              "[C] - Cosmetica")

        try:
            mi_rubro = input("Elija un rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quiere sacar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion correcta")
        else:
            if otro_turno == "N":
                print("Gracias, vuelva pronto")
                break

inicio()