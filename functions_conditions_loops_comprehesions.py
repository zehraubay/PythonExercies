#Fonksiyon okuryazarlığı

print("a")

# print bir fonksiyondur. Parametre ifadesi fonksiyon tanımlanması esnasında ifade edilen değişkenlerdir.
# Argüman ise bu fonksiyonlar çağırıldığında bu parametre değerlerine karşılık girilen değerlerdir.

print("a", "b")
print("a", "b", sep=",", end="/")
help(print)

#Fonksiyon tanımlama

def calculate(x): #def ile fonksiyon tanımlanır. parantez içine argümanı veya başka bir değişle parametresini koyabilirsiniz.
    print(x*2)    #fonksiyonun gövde(body) kısmı (statement)

calculate(10)

#İki argümanlı/parametreli bir fonksiyon yazdırma

def summer(arg1,arg2):
    print(arg1 + arg2)
 
summer(7,8) # = summer(arg1=7, arg2=8)
summer(8,7)

summer(arg1=7, arg2=8)

# Docstring: bilgi notu ekleme (dip not)

def summer(arg1, arg2):  # 3 x (") + enter ile açılır. 
    """ sum of the numbers #özet, fonksiyonun ne yaptığı
    Args/Parameters:
        arg1 (int, float): _description_ #tanım
        arg2 (int, float): _description_
    Returns:
        int, float
    Examples:

    Notes:
    """
    print(arg1 + arg2)

summer(1, 3)

#Fonksiyonların Statement/Body bölümü

#def function_name(parameters/arguments):
#    statement (function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")
say_hi() # say_hi() missing 1 required positional argument: 'string'
say_hi("zehra")

def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9)

# girilen iki sayıyı çarpsın sonra sonucu bir liste içinde saklayacak fonksiyon

list_store =[]

def add_element(a, b):      #bu satır global etki alanıdır.
    c = a * b               #1.
    list_store.append(c)    #2.
    print(list_store)       #3. satırlar local etki(geçici şekilde kullan-at) alanıdır.

add_element(9, 10)
add_element(18, 8)
add_element(180, 99)

#Ön tanımlı argümanlar/Parametreler (Default Parameters/Arguments)

def divide(a, b):
    print(a / b)

divide(1, 2)

def divide(a, b=1): # "=" ile tanımlanır.
    print(a / b)

divide(10)

def divide(a, b):
    print(a / b)

divide(1) # divide() missing 1 required positional argument: 'b'

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi()

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb")

#Ne zaman fonksiyon yazma ihtiyacımız olur?

#ısı(varm), nem(moisture), pil(charge)

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80

#birbirini tekrar eden görevler söz konusu olduğunda fonksiyon yazma ihtiyacı doğar.

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(98, 12, 78)

# Return: Fonksiyon çıktılarını girdi olarak kullanmak

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(98, 12, 78) * 10 #unsupported operand type(s) for *: 'NoneType' and 'int'
type(10)
type(calculate(98, 12, 78)) #class 'NoneType'

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

calculate(98, 12, 78) * 10 

a = calculate(98, 12, 78)

#girilen argümanların yeni değerlerinin çıkması ve bu 3 argüman üzerinden hesaplanacak yeni değerin çıktı olarak verilmesi

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

calculate(98, 12, 78)
type(calculate(98, 12, 78)) # <class 'tuple'>

#çağırmakla kalmayıp çıktılarını kaydedip daha sonra kullanmak istenilirse

varm, moisture, charge, output = calculate(98, 12, 78)

#Fonksiyon içerisinden fonksiyon çağırmak

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90, 12, 12) * 10

def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(45, 1)

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 19, 12)

# Lokal & Global değişkenler (Local & Global Variables)

list_store = [1, 2] # list_store global etki alanında

def add_element(a, b):
    c = a * b      # c lokal etki alanında 
    list_store.append(c)
    print(list_store)

add_element(1, 9)

# Örnekler

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def combined_operation(x, y, z):
    sum_result = add(x, y)  # Önce toplama işlemi
    product_result = multiply(sum_result, z)  # Sonra çarpma işlemi
    return product_result

print(combined_operation(2, 3, 4))  # 5 * 4 = 20


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    celsius = fahrenheit_to_celsius(f)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

print(fahrenheit_to_kelvin(98.6))  # 310.15
