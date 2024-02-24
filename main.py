list_methods = []
for method in dir(list):
    if method.startswith("__"):
        continue
    list_methods.append(method)
set_methods = []
for method in dir(set):
    if method.startswith("__"):
        continue
    set_methods.append(method)
string_methods = []
for method in dir(str):
    if method.startswith("__"):
        continue
    string_methods.append(method)
tuple_methods = []
for method in dir(tuple):
    if method.startswith("__"):
        continue
    tuple_methods.append(method)
dict_methods = []
for method in dir(dict):
    if method.startswith("__"):
        continue
    dict_methods.append(method)
basliklar = ["List Methods", "Set Methods", "String Methods", "Tuple Methods", "Dict Methods"]
classes = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]
max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)
with open("Methods.txt","w") as f:
    for baslik in basliklar:
        print(baslik,end="")
        print(" " * (30 - len(baslik)),end="")
        f.write(baslik)
        f.write(" " * (30 - len(baslik)))
    for i in range(max_len):
        print()
        f.write("\n")
        for class_ in classes:
            if i >= len(class_):
                print("-------",end="")
                print(" " * 23,end="")
                f.write("-------")
                f.write(" " * 23)
            else:
                print(class_[i],end="")
                print(" " * (30 - len(class_[i])),end="")
                f.write(class_[i])
                f.write(" " * (30 - len(class_[i])))
#Beş boş liste (list_methods, set_methods, string_methods, tuple_methods, dict_methods)
# oluşturulur.
#dir() fonksiyonu kullanılarak list, set, str, tuple ve dict sınıflarının yöntemleri alınır.
#Her sınıf için yöntemleri içeren listeler oluşturulur. Yöntem adları "__" ile başlayan
# yöntemler hariç alınır.
#basliklar listesi, çıktıda kullanılacak başlıkları içerir.
#classes listesi, her sınıfın yöntemlerini içeren listeleri içerir.
#max_len değişkeni, en uzun yöntem listesinin uzunluğunu tutar.
#"Methods.txt" adında bir dosya oluşturulur ve içine yöntemleri yazılır.
#basliklar ve classes listeleri kullanılarak dosyaya başlıklar ve yöntemler yazılır.
#İşlem tamamlandıktan sonra dosya kapatılır.