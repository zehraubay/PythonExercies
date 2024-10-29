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

salaries = [1000, 2000, 3000, 4000, 5000]

# break ifadesi aranan koşul yakalandığında döngünün durmasını sağlar.

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

#continue

for salary in salaries:
    if salary  == 3000:
        continue #görmezden gel, pas geç, diğer iterasyona geç, devam et
    print(salary)

#while -dı sürece

number = 1
while number < 5: #sayı 5'den küçük olduğu sürece
    print(number) #şunu yap
    number += 1 #sayı 1 geldi ve print edildi sonra üstüne 1 eklenip 5 'den küçük mü diye güncellendi.. en son 4 geldi ve 4 5'den küçük mü dedi print etti üstüne 1 ekledi ama 5 5'den küçük olmadığı için işlem durdu

# Enumerate: otomatik counter/ındexer ile for loop
# örneğin bir liste içerisinde gezerken bu elemanlara belirli bir işlem uygularken aynı zamanda işlem uygulanan elemanların index bilgisini de tutup gerekirse bu index bilgisine göre de bir işlem yapmak istediğimizde kullanılır

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students): #parantez içinde: neyi kullanarak hem index hemde ilgili nesnenin elemanlarını temsil edeceksin diyor
    print(index, student)                     # enumerate(students, 1): ile 1 gibi istediğin sayıdan da başlatabilirsin

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
# öğrenciler listesinde gezerken enumerate bana hem öğrencileri temsil etme hem de öğrencilerin liste içerisindeki indexlerini temsil etme imkanı veriyor
# eğer yakalamış olduğum indexlerden ikiye bölümünden kalan 0 ise bu durumda ilgili öğrenciyi A listesine at, değilse B listesine at.

#Uygulama
#divide_students fonksiyonu yazınız.
#Çift indexte yer alan öğrencileri bir listeye alınız
#Tek indexte yer alan öğrencileri bir listeye alınız.
#Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
        print(groups)
        return groups
    
st = divide_students(students)
st[0]
st[1]

#alternating fonksiyonunun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")

# Zip
#birbirinden farklı olan listeleri bir arada değerlendirme imkanı sağlar.

students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

# lambda, map, filter, reduce

def summer(a, b):
    return a + b

summer(1, 3) * 9

#lambda bir fonksiyon tanımlama şeklidir. def ten farkı bunlar kullan at fonksiyonlardır.
new_sum = lambda a, b: a + b
new_sum(4, 5)

#map
#döngü yazmaktan kurtarır
 
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(1000)

for salary in salaries:
    print(new_salary(salary))

list(map(lambda x: x * 20 / 100 + x, salaries))

list(map(lambda x: x ** 2, salaries))

# Filter

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# Reduce
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)
 # 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10

sayi = 10

for num in range(0,sayi):
    if num % 2 == 0:
        print(num)

if sayi % 2 == 0:
    print("Sayı çifttir")

# ALIŞTIRMALAR

#GÖREV 1
x = 8 
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z) # complex

a = "Hello world"
type(a)

b = True
type(b) #bool

c = 23 < 22
type(c) #bool

l = [1, 2, 3, 4, "String", 3, 2, False]
type(l)

d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d) #dict

t = ("Machine Learning", "Data Science")
type(t) #tuple

s = {"Python", "Machine Learning", "Data Science"}
type(s)

# GÖREV 2
text = "The goal is to turn data into information, and iformation into insight."

text.upper().replace(","," ").replace("."," ").split()

#GÖREV 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

len(lst)
lst[0]
lst[10]
list = lst[0:4]
lst.pop(8)
lst.append("Z")
lst[8] = "N" 

#GÖREV 4

dict = {'Christian': ["Amerika", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

dict.keys()
dict.values()
dict['Daisy'] = ["England", 13]
dict.update({'Ahmet': ["Türkiye, 24"]})
dict.pop('Antonio')

#Görev 5

l = [2,13,18,93,22]

def func(lst):
    even_list = [] #çift
    odd_list = [] #tek
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)
    return even_list, odd_list

even_list, odd_list = func(l)

#Görev 6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler):
    if i < 3:
        i += 1
        print("Mühendislik Fakültesi",i,".öğrenci:", ogrenci)
    else:
        i -= 2
        print("Tıp Fakültesi",i,".öğrenci:",ogrenci)

#Görev 7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, krd, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {krd} olan {kod} kodlu dersin kontenjanı {kont} kişidir")

#Görev 8

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume1.issuperset(kume2)
kume2.difference(kume1)

kume2 - kume1

# COMPREHENSIONS

# List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []
for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
# if' i yalnız kullanacaksanız sol tarafta kalır ancak if-else kullanacaksanız sağ tarafta olmalı

[new_salary(salary * 2) if salary < 3000 else salary * new_salary(salary * 0.2) for salary in salaries]

students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]

#Dict Comprehension

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items() # key ve value değerlerine tuple şeklinde görmek

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v ** 2 for (k, v) in dictionary.items()}

#Uygulama
# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
#Key'ler orijinal değerler value'lar ise değiştilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}
 
# Bir veri setindeki değişken isimlerini değiştirmek

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

#after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn
df = seaborn.load_dataset("car_crashes") # seaborn üzerinden araba kazaları data setini getir
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())
df.columns = A

df = seaborn.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

#İçerisinde "INS" olan değişkenlerin başına FLAF diğerlerine NO_FLAG eklemek istiyoruz.

["FLAG_" + col for col in df.columns if "INS" in col]

"A" + "B"  # 'AB'

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak
#sadece sayısal değişkenler için yapmak istiyoruz.

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding: ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns #sütunlar

num_cols = [col for col in df.columns if df[col].dtype != "O"]
# dataframe içerisinden ilgili değişkeni yakaladığımızda (df[col]) ve dtype (tipi) eşit değildir (!=) object yani "O"
# örneğin df[alcohol] yazdığımızda bu değişkeni seçer ve dtype ile bunun tipine bakar 0 işareti kategorik(object) (string) değişkenleri temsil eder.
# numeric(sayısal) değişkenleri getirmesini istiyoruz

soz = {}
agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols: #numeric kolonlarda geziyoruz
    soz[col] = agg_list #soz isimli sözlüğe num_cols'daki kolonları ekledim (keyleri ekledim) ve bunların value bölümüne sabit bir liste girdik

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)