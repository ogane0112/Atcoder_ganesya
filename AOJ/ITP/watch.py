s = int(input())
hour = s//3600
temp = s%3600
minute = temp//60
secound = temp%60
print(str(hour)+":"+str(minute)+":"+str(secound))

