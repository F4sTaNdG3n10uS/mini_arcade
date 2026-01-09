from games import snake, morpion, quizz, pendu, nombre_mystere

def show_menu():
    print("Bienvenue dans Mini-Arcade !")
    print("1 - Snake")
    print("2 - Morpion")
    print("3 - Quizz")
    print("4 - Pendu")
    print("5 - Nombre Mystère")

    choix = input("Choisis un jeu (1-5) : ")

    if choix == "1":
        snake.start()
    elif choix == "2":
        morpion.start()
    elif choix == "3":
        quizz.start()
    elif choix == "4":
        pendu.start()
    elif choix == "5":
        nombre_mystere.start()
    else:
        print("Choix invalide")

# si tu veux tester directement le menu
if __name__ == "__main__":
    show_menu()
