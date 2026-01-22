from jeux import snake, morpion, quizz, pendu, nombremystère

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
<<<<<<< HEAD
    elif choix == "5":
        nombremystère.start()
=======
    
>>>>>>> a210dc7de3a5ff24273f36ad4610bd81f57fd16e
    else:
        print("Choix invalide")

# si tu veux tester directement le menu
if __name__ == "__main__":
    show_menu()
from jeux import snake

def show_menu():
    while True:
        print("\n--- MINI ARCADE ---")
        print("1 - Snake")
        print("2 - Quitter")

        choix = input("Choix : ")

        if choix == "1":
            snake.start()  # 🎮 lance le mini-jeu pygame
        elif choix == "2":
            break
