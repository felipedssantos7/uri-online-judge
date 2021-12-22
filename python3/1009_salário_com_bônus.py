nome_vend = input()
sal_fixo = float(input())
montante = float(input())

comissao = (15 * montante) / 100
total_receber = sal_fixo + comissao

print("TOTAL = R$ {:.2f}".format(total_receber))
