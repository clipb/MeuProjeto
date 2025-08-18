# Demonstração do uso de if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())

if  IDADE < 18:
    print("você não é maior de idade!")
    print("não poderá realizar operações bancárias!")
elif IDADE >= 65:
    print("public")
    print("podemos ofercer suporte técnico...")
else:
    print("você é maior de idade.")
    print("portanto, poderá realizar a operação.")

print("obrigado por escoher os nossos serviços!")