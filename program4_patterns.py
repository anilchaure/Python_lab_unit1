"""4) Write programs to print: (a) a right-angled triangle of stars, (b) a number pyramid, (c) a
Pascal's triangle up to n rows. Implement at least one using for and one using while.
"""

# Program 4(a): Star Triangle

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# Program 4(b): Number Pyramid

n = int(input("Enter number of rows: "))

i = 1

while i <= n:
    j = 1

    while j <= n - i:
        print(" ", end=" ")
        j = j + 1

    j = 1

    while j <= i:
        print(j, end=" ")
        j = j + 1

    print()
    i = i + 1


# Program 4(c): Pascal's Triangle

n = int(input("Enter number of rows: "))

for i in range(n):
    number = 1

    for j in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)

    print()
