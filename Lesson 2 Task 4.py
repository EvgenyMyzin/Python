##Homework 2 Task 4
#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
txt = input( "Enter text " )
list = txt.split()
#i=int(1)
#for el in list:
#        el_reverse = el[0:9:]
#        print(i,el_reverse)
#        i=i+1
for ind, el in enumerate(list):
#        el_reverse = el[0:9:]
        print(ind, el[0:10:])
