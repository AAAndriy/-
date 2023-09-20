def dodavannya(x, y):
    return x + y

def vidnimannya(x, y):
    return x - y

def mnozhennya(x, y):
    return x * y

def dilyannya(x, y):
    return x / y

print("Виберіть операцію:")

print("1. Додавання")

print("2. Віднімання")

print("3. Множення")

print("4. Ділення")

vybir = input("Ваш вибір (1/2/3/4): ")

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))


if vybir =='1':
    print (num1, "+", num2, dodavannya(num1,num2))
elif vybir =='2':
    print (num1, "-",num2, vidnimannya(num1, num2))
elif vybir =='3':
    print (num1,"*",num2, mnozhennya (num1, num2 ))
elif vybir =='4':
    print (num1,"/",num2, dilyannya(num1,num2))
    print ("калькулятор")