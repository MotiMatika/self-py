# def sum_and_avg(a, b):
#     sum_num = a + b
#     avg_num = (a + b) / 2
#     return sum_num, avg_num
# x,y=sum_and_avg(3,6)
# print(x)
# print(y)




# i=3
# a=32
# x=(i,a)
# print(x)

# a="moti"
# for i in a:
#     print(i)










################################מילונים########################
# new_dict = {"A": "a", "B": "b", "C": "c"}   #יצירת המילון
# print(new_dict)

# new_dict["D"] = "d"                         #הוספת מפתח
# print(new_dict)

# new_dict.pop("D")                           #מחיקת מפתח
# print(new_dict)

# x=new_dict.keys()                           #הדפסת המפתחות
# print(x)

# x=new_dict.values()                         #הדפסת הערכים
# print(x)

# x=len(new_dict)                             #אורך המילון
# print(x)

# x=new_dict["B"]                             #קריאה למפתח
# print(x)

#8.3.2
# my_first_dict = {"first_name": "Mariah","last_name": "Carey","birth_date": "27.03.1970","hobbies": ["Sing", "Compose", "Act"]}
# pressed=input("enter a number between 1 to 7 :  ")
# if pressed == "1":                                  #שם משפחה
#     x=my_first_dict["last_name"]
#     print(x)
# elif pressed == "2":                                #החודש בו נולדה
#     x=str(my_first_dict["birth_date"])
#     print(x[3]+x[4])
# elif pressed == "3":                                #מספר התחביבים
#      x=list(my_first_dict["hobbies"])
#      length=len(x)
#      print(length)
# elif pressed == "4":                                #התחביב האחרון ברשימת התחביבים
#     x=list(my_first_dict["hobbies"])
#     print(x[2])
# elif pressed == "5":                                #לעדכן את רשימת התחביבים
#     my_first_dict["hobbies"] = ["Sing","Compose","Act","Cooking"]
#     print(my_first_dict)
# elif pressed == "6":                                #הפיכת מחרוזת התאריך לטיפוס טאפל
#     x=str(my_first_dict["birth_date"])
#     (day,month,year) = (x[0]+x[1],x[3]+x[4],x[6]+x[7]+x[8]+x[9])
#     y=(day,month,year)
#     print(y)
# elif pressed == "7":                                #הוספת מפתח חדש
#     my_first_dict.update({"Age": "52"})
#     print(my_first_dict)


