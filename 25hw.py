a = float(input("Введите число А "))
x = a
if x <= 2:
    fx = x**2 + 4*x + 5
    print("x <= 2; f(a) = ", fx)
else:
    fx = 1 / (x**2 + 4*x + 5)
    print("x > 2; f(a) = ", fx)
