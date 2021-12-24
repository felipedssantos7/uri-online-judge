start_time, end_time = input().split()
start_time = int(start_time)
end_time = int(end_time)
total_time = 24

if start_time < end_time:
    total_time = end_time - start_time
elif start_time > end_time:
    total_time = 24 - start_time + end_time

print("O JOGO DUROU {} HORA(S)".format(total_time))
