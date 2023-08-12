def fibonacci_seq(n):

    if n == 1 or n == 0:
        return n
    else:
        return fibonacci_seq(n-2) + fibonacci_seq(n - 1)
    

number = int(input("Enter a positive interger: "))
if number < 0:
    print("Number is invalid")

i = 0

print("Fibonacci sequence is... ")

for i in range(0, number):
    print(fibonacci_seq(i))