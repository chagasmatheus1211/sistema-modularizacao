
def calcular_troco(valor_compra, valor_pago):
    if valor_compra < 0 or valor_pago < 0:
        print("Erro: os valores não podem ser negativos.")

    elif valor_pago < valor_compra:
        print("Pagamento insuficiente!")
        print("Faltam R$", round(valor_compra - valor_pago, 2))

    else:
        troco = round(valor_pago - valor_compra, 2)

        print("\n========== RESUMO DA COMPRA ==========")
        print(f"Valor da compra: R$ {valor_compra:.2f}")
        print(f"Valor pago: R$ {valor_pago:.2f}")
        print(f"Troco: R$ {troco:.2f}")

        # Converte o troco em centavos para evitar erros com decimais
        troco_centavos = round(troco * 100)

        # Cédulas disponíveis em centavos
        cedulas = [10000, 5000, 1000, 500, 100]

        print("\nCédulas para devolver:")

        for cedula in cedulas:
            quantidade = troco_centavos // cedula
            troco_centavos = troco_centavos % cedula

            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R$ {cedula / 100:.2f}")

        if troco_centavos > 0:
            print("Atenção: restaram moedas que não são contempladas pelas cédulas disponíveis.")

        print("=======================================")


print("=======================================")
print("    SISTEMA DE AUTOMAÇÃO DE TROCO")
print("=======================================")

try:
    valor_compra = float(input("Digite o valor da compra: R$ ").replace(",", "."))
    valor_pago = float(input("Digite o valor pago pelo cliente: R$ ").replace(",", "."))

    calcular_troco(valor_compra, valor_pago)

except ValueError:
    print("Erro: digite valores numéricos válidos.")
