# Veri yapıları (data structures)

#Sayılar (numbers): int, float, complex

a = 5
b = 10.5
a

a * 3
a / 7
a * b / 10
a ** 2

# Tipleri değiştirme

int(b)
float(a)
int(a * b /50) # a * b /50 bu değer normalde 1.05

c = a * b /50
int(c)

# Karakter dizileri (strings)

print("Zehra")
print('Zehra')

"Zehra"
#Bu iki kullanım şeklinin farkı yoktur ancak ekrana bilgi paylaşımında print() tercih edilir.

name = "Zehra"
name = 'Zehra'

#Çok satırlı karakter dizileri

""" veri yapıları
numbers
strings
list
dictionary
tuple
set """

long_str = """ veri yapıları numbers strings list dictionary tuple set """

#Karakter dizilerinin elemanlarına erişmek

name[0]
name[3]

#Karakter dizilerinde slice(dilimleme) işlemi

name[0:3] #0 dan 3'e kadar git. 3 hariç.
long_str[0:30]

#String içerisinde karakter sorgulamak

long_str
"veri" in long_str #True
"Veri" in long_str #False

#String Methods

dir(str)
dir(int)

#len() fonksiyonu karakter dizisinin uzunluğunu verir.

name = "ubay"
type(name)
type(len) # <class 'builtin_function_or_method'>
#Kullanmış olduğumuz bir yapının fonksiyon mu method mu olduğunu nasıl anlarız?
#Fonksiyonlar class içinde tanımlandıysa methood denir. Eğer bir class yapısı içinde değilse fonksiyondur ama ikisi de aynı şeydir.


len(name)
len("zehra")

#upper() lower() küçük-büyük

"zehra".upper()
"Zehra".lower()

#replace: karakter değiştirir.

hi = "Hello AI Era"
hi.replace("l", "p") #ilki değiştirmek istediğin harf, ikincisi ne ile değiştirmek istediğin harf

#split: böler

hi.split() #içine bir şey yazmazsan ön tanımlı argümana göre böler ['Hello', 'AI', 'Era']

#strip: kırpar
" ofofof ".strip()
"ofofof".strip("o")
"ofofofo".strip("o")

#capitalize: ilk harfi büyültür

"zehra".capitalize()

#Liste (list)
# değiştirilebilir. sıralıdır. index işlemleri yapılabilir. kapsayıcıdır.

notes = [1,2,3,4]
type(notes)

names = ["a", "b", "c"]

mix = [1,2,3,"a","b",True, [1,2,3]] #kapsayıcı özelliği (içerisinde birden fazla yapıyı aynı anda tutabilir.)

mix[0]
mix[5]
mix[6]
mix[6][0] #sıralı olma özelliği yani index işlemleri yapılabilir.

type(mix[6]) #list
type(mix[6][0]) #int 

mix[1] = 99 #değiştirebilir özelliği

mix[0:4]

#liste metodları (list methods)

dir(notes) #dir() fonksiyonu bir objenin içinde ne tür metodlar olduğunu gösterir.

len(mix)

#append: eleman ekler

mix.append(100)

#pop: indexe göre eleman siler

mix.pop(0)

#insert: indexe ekler

mix.insert(0, "star") #0. elemana 1000 sayısını ekler

# Sözlük (dictionary)
#değiştirebilir, sıralı ve kapsayıcıdır.
#key-value

dictionary = {"Name": "Zehra"}

dictionary = {"Name": "Zehra",
              "Surname":"Ubay",
              "Age": 21,
              "City": "Istanbul",
              "Country": "Turkey",
              }

dictionary["Name"] #'Zehra'

dictionary = {"Name n Age": ["Zehra", 21],
              "Name n Surname": ["Zehra", "Ubay"]}

dictionary["Name n Surname"]

dictionary = {"Name": 21,
              "School No": 123456789,
}

dictionary["School No"]

# dictionary["Name n Surname"][0]

#Key sorgulama

"Name" in dictionary
"Name n Surname" in dictionary

#Key'e göre value'ya erişmek

dictionary["Name n Age"]
dictionary.get("Name n Age")

#Value değiştirmek

dictionary["Name n Age"] = ["Mehmet", 24]

#Tüm keylere erişmek

dictionary.keys()

# tüm value'lara erişmek

dictionary.values()

# tüm çiftleri tuple halinde listeye çevirme

dictionary.items() # dict_items([('Name n Age', ['Mehmet', 24]), ('Name n Surname', ['Zehra', 'Ubay'])])

#Key-Value değerlerini güncelleme

dictionary.update({"Name n Age": ["Hidayet", 50]})

#Key-Value eklemek

dictionary.update({"City": "Istanbul"})

#Demet (Tuple)
#değiştirelemez, sıralı ve kapsayıcıdır.

x = ("zehra", "ubay", 21)
type(x)

x[0]
x[0:3]
x[0] = 99 # TypeError: 'tuple' object does not support item assignment

# x = list(x)
# x[0] = 99
# x = tuple(x) yaparsan yeni bir şey eklemiş olursun.

#Set
#değiştirebilir, sırasızdır + eşşizdir, kapsayıcıdır.

set1 = set([1,2,3])
set2 = set([1,2,5])

type(set1)

# difference(): iki kümenin farkı

#set1 de olup set2 de olmayan
set1.difference(set2) # {3}
set1 - set2

#set2 de olup set1 de olmayan
set2.difference(set1) #{5}
set2 - set1

#symmetric_difference(): iki kümenin de birbirlerine göre olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#intersection(): iki kümenin kesişimi

set1.intersection(set2)
set2.intersection(set1)

set1 & set2 # &: kesişim ifadesi

#union(): iki kümenin birleşimi

set1.union(set2)
set2.union(set1)

#isdisjoint(): iki kümenin birleşimi boş mu, değil mi?

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

# issubset(): bir küme diğer kümenin alt kümesi mi?

set1.issubset(set2)
set2.issubset(set1)

#issuperset(): bir küme diğer kümeyi kapsıyor mu?

set2.issuperset(set1)
set1.issuperset(set2)

# liste = []
# dictionary = {} ":"
# tuple = ()
# set = {}


#Not: Liste, tuple, set ve dictionary yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.