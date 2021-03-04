list = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
month = int(input("Month: "))
if month > 12:
    print("Wrong value")
for el in list:
       if (month-1==list.index(el)):
        print(el)
dict = {1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
print(dict.get(month))
