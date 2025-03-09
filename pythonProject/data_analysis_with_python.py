import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

len(a)

ab = []
for i in range(0, len(a)): #len(b) de olabilir.
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4]) #array = vektör
b = np.array([2, 3, 4, 5])
a * b

#Numpy Array'i oluşturmak

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype = int) #girdiğiniz sayı değerince 0 oluşturur. dtype= verinin türü
np.random.randint(0, 10, size=10) #random integer - #hangi sınırdan hangi sınıra kadar (alt-üst limitler) array oluşturmak istiyorsun ve kaç tane seçim yapmak istiyorsun.
#0 ile 10 arasında rastgele 10 tane integer seç

np.random.normal(10, 4, (3,4)) #ilkine: oluşturmak istediğim normal dağılımlı kitlenin ortalamasını ikincisine: argümanı üçüncüsüne: boyut bilgisini gir
#3 satır 4 sütundan oluşan ortalaması 10 ve standar sapması 4 olan normal dağılımlı sayılar

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5) #başa hiç bir şey girilmezse 0 olarak kabul eder.
a.ndim
a.shape
a.size
a.dtype

np.random.randint(1, 10, size=9)
#bu arrayi iki boyutlu bir array'e (matrise) çevirmek istiyoruz.
np.random.randint(1, 10, size=9).reshape(3, 3)

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

# index seçimi (index selection)
import numpy as np
a = np.random.randint(10, size=10) # array([2, 2, 9, 9, 4, 2, 5, 8, 6, 1]
a[0] # 2
a[0:5] #array([2, 2, 9, 9, 4]
a[0] = 999

m = np.random.randint(10, size=(3, 5)) # 0'dan 10'a kadar 3 sütunlu 5 satırlı bir array oluştur.
# array([[2, 5, 8, 7, 3],
#        [3, 7, 1, 5, 1],
#        [2, 2, 1, 9, 8]]

m[0, 0] #virgülden önce satırları virgülden sonrası sütunları temsil eder. # 2
m[1, 1] # 7
m[2, 3] = 999
m[2, 3] = 2.19 #numpyın kendi özelliğinden dolayı sabit tipli array olduğu için tek bir veri tipi saklar.
m[:, 0] #bütün satırları seç :, 0. sütunu seç
m[1, :]
m[0:2, 0:3] #  array([[2, 5, 8],
            #        [3, 7, 1]])

# Fancy Index

v = np.arange(0, 30, 3) #0'dan 30'a kadar 3'er 3'er artacak şekilde array oluştur. 30 hariç
v[1] #3
v[4] #12

catch = [1, 2, 3]
v[catch] # array([3, 6, 9]) #catch de 1 sayılı rakamı v arrayında 1.indexteki elemanı getirir

v = np.array([1, 2, 3, 4, 5])

#klasik döngü ile
ab = []
for i in v:
    if i < 3:
        ab.append(i)

#numpy ile
v < 3 # array([ True,  True, False, False, False])

v[v<3] #v[] de eleman seçimi yapıcam demek,
# array([1, 2])
v[v>3]
v[v != 3] #array([1, 2, 4, 5])
v[v == 3]
v[v <= 3]
v[v >= 3]

#Matematiksel İşlemler
import numpy as np
v = np.array([1, 2, 3, 4, 5])
v / 5 #array([0.2, 0.4, 0.6, 0.8, 1. ])
v * 5 / 10 #array([0.5, 1. , 1.5, 2. , 2.5])
v ** 2 #array([ 1,  4,  9, 16, 25])
v - 1 #array([0, 1, 2, 3, 4])

v = np.subtract(v, 1) #çıkarma #array([0, 1, 2, 3, 4])
np.add(v, 1) #toplama #array([2, 3, 4, 5, 6])
np.mean(v) #ortalama #np.float64(3.0)
np.sum(v) #toplam alma #15
np.min(v)#1
np.max(v)#5
np.var(v) #varyans 2.0

# Numpy ile iki bilinmeyenli denklem çözümü

#5*x0 + x1 = 12
#x0 + 3*x1 = 10

#1. değişkenin katsayılarını ve 2. değişkenin katsayılarını belirli bir yapıda gönderir
a = np.array([[5, 1], [1, 3]]) #katsayılar array'i
b = np.array([12, 10]) #sonuçlar array'i

np.linalg.solve(a, b) #array([1.85714286, 2.71428571])
#linalg.solve = Doğrusal denklemleri çözmek ve bilinmeyen değişkeni veya doğrusal skaler denklemler sistemini bulmak için kullanılır.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])
#Bu dizi, iki boyutlu ve iç içe iki liste içeriyor. arr[0] ifadesi, ilk satırı yani [1, 2, 3, 4, 5]'i alır.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
#Negatif indeksleme, diziye sondan başlanarak yapılır. -3, dizinin sondan üçüncü elemanı olan 5’e karşılık gelir, -1 ise sondan birinci elemanı olan 7'ye.
#Dilimleme -3 indeksinden başlar ve -1 indeksine kadar gider, ancak -1'i dahil etmez.

array = np.array([1, 2, 3, 4, 5, 6, 7])
filter_array = array % 2 == 0 #array % 2 == 0 ifadesi, dizideki her bir elemanı 2'ye bölüp kalanının 0 olup olmadığını kontrol eder. Sonuç olarak, array'deki çift sayılar True, tek sayılar False olarak işaretlenir.
#filter_array, bu koşullara göre [False, True, False, True, False, True, False] değerini alır.
new_array = array[filter_array] #new_array = array[filter_array] ifadesi, filter_array'de True olan indekslerdeki elemanları seçer. Yani yalnızca çift sayılar alınır.
print(new_array)

#Pandas Serileri
#tek boyutlu.

import pandas as pd
s = pd.Series([10, 77, 12, 4, 5])
#0    10
#1    77
#2    12
#3     4
#4     5
#dtype: int64
type(s) #<class 'pandas.core.series.Series'>

s.index #RangeIndex(start=0, stop=5, step=1)
s.dtype #dtype('int64')
s.size #5
s.ndim #1
s.values #array([10, 77, 12,  4,  5])
type(s.values) #<class 'numpy.ndarray'>
s.head() #ilk 5 i getirir.
s.head(3)
s.tail(3)

#Pandas
import pandas as pd
import seaborn as sns

df = pd.read_csv("../Advertising.csv")
df.head()

df = sns.load_dataset("titanic") #load_dataset bazı yaygın ifadeleri koyarak kolayca veri setleriyle çalışmamızı sağlar
df.head()
#survived bağımlı değişkendir, hedef değişkendir, ana odağıdır.
df.tail()
df.shape #boyut bilgisi
df.info() #bilgi
df.columns #sütun isimleri
df.index #RangeIndex(start=0, stop=891, step=1)
df.describe().T #sayısal olan değişkenlerin özet istatistiklerine erişmek sonuna T ifadesi transpozunu almak
#count(kaç gözlemden(count) oluştuğu) mean(ortalama), std(standart sapma), min, %25, %50, %75, max değerleri gösterilir.

df.isnull().values.any() #sadece veri setinde bir tane dahi olsa bir eksiklik var mı?
#bu değerlerden herhangi birisinde isnull var mı
#True

df.isnull() #True- false lardan oluşan çıktı
df.isnull().values #true-false değerlerini getirir

type(df.isnull().values) #<class 'numpy.ndarray'>

df.isnull().sum() #True=1'i, False=0'ı temsil eder
df["sex"].head() #kategorik değişkenlerden cinsiyette kaç tane sınıf olduğu ve bu sınıfların kaçar tane olduğu bilgisine erişmek
df["sex"].value_counts() #sex
                         #male      577
                         #female    314
                         #Name: count, dtype: int64

#Veri manipülasyonları (Pandas) (Seçim işlemleri)
import pandas as pd

import seaborn as sns
df = sns.load_dataset("titanic")
df.head() #[5 rows x 15 columns]
df.index #RangeIndex(start=0, stop=891, step=1)

#slice işlemleri
df[0:13] #[13 rows x 15 columns] 0 dan 12 ye kadar. 13 hariç
df.drop(0, axis=0).head() #hangi indexi silmek istersin kaçıncı satırdan. satırdan silme işlemi = axis

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10) #silme işlemi kalıcı değildir.

#silme işlemini kalıcı yapmak istiyorsan: df = df.drop(delete_indexes, axis=0)
#2. yöntem df.drop(delete_indexes, axis=0, inplace=True)

# Değişkeni Indexe Çevirmek

df["age"]  #değişken seçmek
df["age"].head()
df.age.head()

df.index #RangeIndex(start=0, stop=891, step=1)
df.index = df["age"] #index olarak eklemek
df.drop("age", axis=1).head() #axis=1 sütunlardan silmek
df.drop("age", axis=1, inplace=True)

#Indexi değişkene çevirmek

df["age"] = df.index #köşeli parantez yazıldığında eğer girilecek olan string değer bu dataframe içerisinde varsa bu durumda bu değişken seçilirken,
#bu dğeişken dataframe içinde yoksa yeni değişken ekleniği anlaşılır.
df.head()

df.drop("age", axis=1, inplace=True)
df = df.reset_index().head() #indexte yer alan değeri silecektir. ikincisi bunu sütun olarak yeni bir değişken olarak ekleyecektir
df.head()

hfhfh