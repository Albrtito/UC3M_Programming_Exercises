seconds = int(input("""input a number of seconds to
 convert into hours:minutes:seconds: """))


minutes = seconds// 60
seconds %= 60
hours = minutes//60
minutes %= 60

print(hours,":", minutes,":",seconds)


