#Demonstação de operadores lógicos em condicionais.

print("o que vc vai fazer amanhã de manhã?")
print("domir / estudar / planejar")
MANHA = input()
print("o que vc vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if MANHA == "domir":
    print("vc está desperdiçando o seu dia!")
if TARDE == "jogar":
    print("vc está disperdiçando o seu dia!")

if MANHA == "estudar":
    print("que bom! vc irá se aperfeiçoar!")
if TARDE == "treinar":
    print("que bom! vc irá se aperfeiçoar!")

if MANHA == "planejar":
        if TARDE == "trabalhar":
            print("para trabalhar melhor , devo planejar!")
                        
print("tenha um bom dia!")