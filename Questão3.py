paes = float(input("Informe a quantidade de pães que foram vendidos: "))
broas = float(input("Informe a quantidade de broas que foram vendidas: "))

valor_vendas = (paes*0.12) + (broas*1.50)
print(f"""Foi arrecadado: R$ {valor_vendas:.2f}.
Deve guardar numa conta de poupança: R$ {valor_vendas*0.10}""")