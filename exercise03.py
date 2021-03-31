# Exercise Three
# Write a simple program that finds the number of digits of a given integer value
def numDigits(n):
  n = str(n)
  n = n.replace("-", "")
  n = n.replace(".", "")
  return len(n)

ans = numDigits(-100.12)
print(ans)
