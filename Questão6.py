peso_comida = float(input("Informe o peso da comida em quilogramas: "))
peso_prato = 0.7

print(f"O valor a pagar é: R$ {peso_comida * 12 - peso_prato:.2f}")