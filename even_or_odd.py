def even_or_odd(y):
  if(y % 2 == 0):
      print("even")
  else:
      print("odd")
i=1
while i < 5:
    print("{} time calling is ".format(i))
    even_or_odd(i)
    i = i + 1
