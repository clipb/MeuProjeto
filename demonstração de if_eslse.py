# Demonstração do uso de if / else...
print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    print("você não é maior de idade!")
    print("não poderá realizar operações bancárias!")

else:
    print("voce é maior de idade.")
    print("Portanto, poderá realizar a operação.")
    
    print("obrigado por escolher os nossos serviços!")