a = 4
result = 1

for i in range(a):  # Iterates from 0 to a-1
    if i > 0:       # Only considers positive i
        result *= i  # Multiplies result by i if i is greater than 0

print(result + 2)  # Outputs the final result