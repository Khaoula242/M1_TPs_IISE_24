class Animal:
    def faire_du_bruit(self):
        print("noise")

# Sous-classe "Chien"
class Chien(Animal):
    def faire_du_bruit(self):
        return "Woof!"

# Sous-classe "Chat"
class Chat(Animal):
    def faire_du_bruit(self):
        return "Miaou!"


# Exemple d'utilisation
chien = Chien()
chat = Chat()

print("Le chien fait :", chien.faire_du_bruit())
print("Le chat fait :", chat.faire_du_bruit())
