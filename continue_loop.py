#This is a continue statement
#In a continue statement, the compiler will skip to another statement when it encounters a false one.

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)