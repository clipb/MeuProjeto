# Demonstração de operadores lógicos em condicionais 2...
print("o que vc vai fazer amanhã?")
print("dormir / estudar / planejar")
MANHA = input()
print("o que vc vai fazer amanhã de tarde?")
print("jogar / treinar /trabalhar")
TARDE = input()

if not MANHA or not TARDE:
        print("vc precisa dizer o que vai fazer!")
else:
    if MANHA == "dormir" or TARDE == "jogar":
        print("vc está desperdiçando o seu dia!")
    elif MANHA == "estudar" or TARDE == "treinar":
         print("que bom! vc irá se aperfeiçor!")
    elif MANHA == "planejar" and TARDE == "trabalhar":
         print("para trabalhar melhor , devo planejar!")
    else:
         print ("não combinamos estas ações...")
         print("tenha um bom dia!")

                                      