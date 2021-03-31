# Exercise Two
# Write a simple program that finds the value at the nth position in the Fibonacci sequence
def fibFinder(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #xn = xn-1 + xn-2
        return fibFinder(n-1) + fibFinder(n-2)
