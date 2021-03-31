# Exercise Three
# Write a simple program that finds the number of digits of a given integer value
def numDigits(n):
  return len(str(abs(n)))

ans = numDigits(-1007849)
print(ans)
