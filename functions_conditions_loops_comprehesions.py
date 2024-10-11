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
    

