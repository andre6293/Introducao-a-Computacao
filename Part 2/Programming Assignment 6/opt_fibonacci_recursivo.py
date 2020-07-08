def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

user = int(input("Digite o número: "))
print(fibonacci(user))
