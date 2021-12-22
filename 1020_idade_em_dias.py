days = int(input())
years = int(days / 365)
rest = days % 365
mounths = int(rest / 30)
days = rest % 30

print("{} ano(s)".format(years))
print("{} mes(es)".format(mounths))
print("{} dia(s)".format(days))
