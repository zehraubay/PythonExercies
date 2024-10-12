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





# Koşullar (Conditions)

# True - False
1 == 1
1 == 2
1 != 2

#if 

if 1 == 1:
    print("Doğru")

if 1 == 2:
    print("Yanlış") # if sadece sonucu True olan işlemi yapar

number = 11
if number == 10:
    print("number is 10") # if ifadenisinin sonucu False olduğu için bu bloğu çalıştırmıyor

number = 10
if number == 10:
    print("number is 10")

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(10)
number_check(20)

#else 

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(8)


#Elif

def number_ten(x):
    if x > 10:
        print("Bu sayı 10'dan büyüktür.")
    elif x < 10: #10'dan büyük değilse(el) ama küçükse(if) "el-if"
        print("Bu sayı 10'dan küçüktür.")
    else:
        print("Bu sayı 10'a eşittir.")

number_ten(50)

# Döngüler (Loops)
# for loop

students = ["Zehra", "Zeynep", "Melek", "Ahmet"]

# her bir elemana erişmek
students[0]
students[1]
students[2]
students[3]

for student in students: # ilk önce her bir elemanı gezerken (dönerken) bu elemanları bir şey ile temsil etmeni ister sonra döngüyü nerede gerçekleştireceksin.
    print(student)

#yakaladığımız her bir öğrencinin ismini büyültmek istersek

for student in students:
    print(student.upper()) # her bir öğrencinin ismini büyütür.

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

# her bir elemana %20 zam uygulansın

for salary in salaries:
    print(int(salary * 20 / 100 + salary))

for salary in salaries:
    print(int(salary * 30 / 100 + salary))

# habire zam değerini girmektense fonksiyon yaz

def new_salary(maas, zam):
    return int(maas * zam / 100 + maas)

new_salary(1500, 10)

for salary in salaries:
    print(new_salary(salary, 10))

salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

# Uygulama

#Amaç: aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
#before: "hi my name is john and i am learning python"
#after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
#çift indekstekiler büyük tek indeksler küçük


# 1. çift ve tek indexlerinde gezmek
# 2. gezme işlemlerinden sonra indexin tek mi çift mi olduğunu sorgulamak
# 3. çift olanı büyültmek, tek olanı küçültmek
# 4. yaptığın değişikleri de bir yere kaydetmek

def alternating(string):
    new_string = "" # yapılan değişiklikleri bir yere kaydetmek
    #girilen string'in indexlerinde gez. # girilen herhangi bir stringi boyutunu (len) düşünerek bütün elemanlarını gezmek
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir
        if string_index % 2 == 0: 
            new_string += string[string_index].upper() # += ifadesi buraya(new_string) ilgili ifadeyi ekle ve bu ifadenin yeni değeri olarak mevcut hali koru
        # index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower() #"zehra"[1].lower()
    print(new_string)

alternating("zehra")


# range(len("zehra")) çıktı --> range(0, 5)
# range(0, 10) #iki değer arasında sayı üretmeyi sağlar
for i in range(0, 5):
    print(i)

for i in range(len("zehra")):
    print(i)

4 % 2 == 0

m = "zehra"
m[0]

#break & continue & while

