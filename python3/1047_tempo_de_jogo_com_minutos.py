start_hour, start_minute, end_hour, end_minute = input().split()
start_hour = int(start_hour)
start_minute = int(start_minute)
end_hour = int(end_hour)
end_minute = int(end_minute)

total_start_minutes = (start_hour * 60) + start_minute
total_end_minutes = (end_hour * 60) + end_minute

total_minutes = 1440

if total_start_minutes < total_end_minutes:
    total_minutes = total_end_minutes - total_start_minutes
elif total_start_minutes > total_end_minutes:
    total_minutes = 1440 - total_start_minutes + total_end_minutes

hours = int(total_minutes / 60)
minutes = total_minutes % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))
