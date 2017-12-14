"""Experimenting with very non standard implementation of FizzBuzz

   Correct operation with no if statements.
   Instead of treating the problem as 'control flow' it treats it as
   'string manipulation'

   This is really a bit too clever to be practical.  I actually prefer
   the commented out implementation for simplicity sake
"""

for i in range(1,101):
    out = ''.join(["Fizz"][i%3:] + ["Buzz"][i%5:])
    out += ''.join([str(i)][len(out):])
    print(out)

# for i in range(1,101):
#     out = ''
#     if not i%3:
#         out = "Fizz"
#     if not i%5:
#         out += "Buzz"
#     if not out:
#         out = i
#     print(out)
