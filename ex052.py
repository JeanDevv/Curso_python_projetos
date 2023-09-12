number = int(input("\n\033[mDigite um número: ".strip()))
divisivel = 0
for c in range(1, number + 1):
    if number % c == 0:
        print("\033[32m", end=" ")
        divisivel += 1
    else:
        print("\033[31m", end=" ")
    print("{} ".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(number, divisivel))
if divisivel == 2:
    print("É por isso ele é PRIMO!")
else:
    print("É por isso que ele não e PRIMO!")