qtt_pos = 0
sum_pos = 0

for i in range(6):
    num = float(input())
    if num > 0:
        qtt_pos = qtt_pos + 1
        sum_pos = sum_pos + num

med_pos = sum_pos / qtt_pos

print("{} valores positivos".format(qtt_pos))
print("{:.1f}".format(med_pos))
