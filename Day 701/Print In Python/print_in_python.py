a = input()
b = input()
separator = input()[0]

# Print with space
print(a,b)
# Print without newline at the end
print(a,b,end="")
# Print with separator
print(a+separator+b)
# Print without space
print(a+b)