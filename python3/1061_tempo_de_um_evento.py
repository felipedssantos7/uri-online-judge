start_day, start_number_day = input().split()
start_number_day = int(start_number_day)

start_hour, start_minute, start_second = input().split(" : ")
start_hour = int(start_hour)
start_minute = int(start_minute)
start_second = int(start_second)

end_day, end_number_day = input().split()
end_number_day = int(end_number_day)

end_hour, end_minute, end_second = input().split(" : ")
end_hour = int(end_hour)
end_minute = int(end_minute)
end_second = int(end_second)

start_time_in_seconds = (start_number_day * 86400) + (start_hour * 3600) + (start_minute * 60) + (start_second)
end_time_in_seconds = (end_number_day * 86400) + (end_hour * 3600) + (end_minute * 60) + (end_second)

total_time_in_seconds = end_time_in_seconds - start_time_in_seconds
total_days = int(total_time_in_seconds / 86400)
rest = total_time_in_seconds % 86400
total_hours = int(rest / 3600)
rest = rest % 3600
total_minutes = int(rest / 60)
total_seconds = rest % 60

print("{} dia(s)".format(total_days))
print("{} hora(s)".format(total_hours))
print("{} minuto(s)".format(total_minutes))
print("{} segundo(s)".format(total_seconds))
