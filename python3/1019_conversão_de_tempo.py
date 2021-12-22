seconds = int(input())
hours = int(seconds / 3600)
rest = seconds % 3600
minutes = int(rest / 60)
seconds = rest % 60

print("{}:{}:{}".format(hours, minutes, seconds))
