"""5) Write a program that iterates through numbers 1-50: skip multiples of 3 using continue, stop
the loop entirely if a number greater than 40 that is also prime is found (break), use pass as a
placeholder for a future feature, and use a for-else block to print "Loop completed without
interruption" when the loop finishes naturally.
--- --- --"""

# Loop Control Statements

for num in range(1, 51):

    if num % 3 == 0:
        continue
    else:
        pass

    if num > 40:
        prime = 1

        for i in range(2, num):
            if num % i == 0:
                prime = 0
                break
            else:
                pass

        if prime == 1:
            print("Prime number found:", num)
            break
        else:
            print(num)
    else:
        if num == 10:
            pass
        else:
            print(num)

else:
    print("Loop completed without interruption")
