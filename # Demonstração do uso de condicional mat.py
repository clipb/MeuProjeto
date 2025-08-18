# Demonstração do uso de condicional match/case...
print("Digite o número referente ao estado da moeda:")
print("1, Flor de cunho")
print("2, Soberba")
print("3, muito bem conservada")
print("4, bem conservada")
print("5, outros estados")
ESTADO = int(input())

match ESTADO:
    case 1:
        print("perfeita! vou pagar R$ 1.000.000,00!")
    case 2:
        print("Quase perfeita! ofereço  R$ 250.000,00!") 
    case 3:  
        print("Quase ótimo! posso dar uns R$100.000,00!")
    case 4:
        print("que bom , aceitaria R$ 30.000,00?")  
    case 5:
        print("desculpe, não aceito neste estado.")
    case _:
          print("opção não reconhecida!")
     