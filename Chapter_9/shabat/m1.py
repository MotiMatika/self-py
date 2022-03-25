# #קריאה לקובץ
# print("\n")
# file_1 = open("f1.txt","r")
# x = file_1.read()
# # print(x)

# #קריאה לקובץ
# print("\n")
# file_2 = open("f2.txt","r")
# y = file_2.read()
# # print(y)

# #קריאה לקובץ
# print("\n")
# file_3 = open("f3.txt","r")
# z = file_3.read()
# # print(z)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#השוואה בין תכני 2 קבצים
# if z==x:
#     print("\ny")
# else:
#     print("\nn")

#בדיקת שם הקובץ
# print(file_3.name)

#בדיקת המוד של הקובץ
# print(file_3.mode)

#בדיקת מצב הקובץ:פתוח/סגור
# print(file_3.closed)

#סגירת קובץ-לאחר סגירתו ניתן למחוק אותו
# file_3.close()

#מצביע על מיקום הסמן בקובץ
# print(file_2.tell())

#מחזיר את הסמן להתחלה
# file_2.seek(0

#חושף את תוכן הטקסט לפי אותיות
# #הדפסה סינית של כל האותיות בטקסט   
# file_1 = open("f1.txt","r")
# for i in file_1.read():
#     print(i)

# #-חושף רק את השורה הראשונה בטקסט 
#הדפסה סינית של אותיות השורה הראשונה
# file_1 = open("f1.txt","r")
# for i in file_1.readline():
#     print(i)


# #חושף את תוכן הטקסט לפי שורות 
#file_1 = open("f1.txt","r")
# for i in file_1.readlines():
#     print(i)



# #הפיכת כל  הטקסט למחרוזת
# file_1 = open("f1.txt","r").read()
# #הפעלת פקודות שונות על הטקסט/מחרוזת
# lengh = len(file_1)
# print(lengh)


# #הפיכת כל  הטקסט למחרוזת
# file_1 = open("f1.txt","r").read()
# #הפיכת הטקסט לרשימה של מחרוזות-מילים מופרדות בתוך רשימה
# x=file_1.split()#פיצול הטקסט למילים
# print(x)
# print(len(x))#כמות המילים


#הפיכת השורה הראשונה למחרוזת
# file_1 = open("f1.txt","r").readline()
# lengh = len(file_1)
# print(lengh)


# file_1 = open("f1.txt","r").readline()
# x=file_1.split()#פיצול השורה הראשונה למילים
# print(x)
# print(len(x))#כמות המילים


#הפיכת כל הטקסט לפי שורות
# file_1 = open("f1.txt","r").readlines()
# lengh = len(file_1)
# print(lengh)


# file_2 = open("f2.txt","r").readlines()
# print(len(file_2))#כמות השורות

#יצירת קובץ טקסט חדש לחלוטין שלא היה קיים-מתוך הפייתון
# print("\n")
# file_4 = open("f4.txt","w")     #נתינת שם לקובץ עם אפשרות לכתיבה
# file_4.write("hello")           #כתיבה לתוך הקובץ החדש
# file_4.close()                  #סגירת הקובץ
# f= open("f4.txt","r")           #פתיחת הקובץ לקריאה
# print(f.read())                 #הדפסת הקובץ
# file_4.close()                  #סגירת הקובץ


#סגירה אוטומטית של הקובץ
# with open("f6.txt","w") as file_6:# יצירת קובץ חדש שלא היה קיים ונתינת שם בשורה אחת
#     file_6.write("wow,u r doing fine\n")
#     file_6.write("all good")
# print(file_6.closed)#בדיקה שהקובץ אכן נסגר


# with open ("f7.txt","w") as file_7:         #פתיחת קובץ לכתיבה שייסגר אוטומטית
#     file_7.write("\ngood morning,sir\n")    #כתיבה לתןך הקובץ
#     file_7.write("how do u do ?\n")         #כתיבה לתןך הקובץ
#     file_7.write("have a good day")         #כתיבה לתןך הקובץ
# x=open("f7.txt","r")                        #פתיחת הקובץ לקריאה
# print(x.read())                             #הדפסת התוכן


# import random as rd
# rd.randint(1,100)
# numbers =  []
# for i in range(8):
#     numbers.append(rd.randint(1,100))
# print(numbers)

# y = []
# x = ["moti","yair"]
# for word in x:
#     y.append(word)
# print(y)


#הגדרת פונקציות כרצוננו למבדה

#כאן הגדרתי פונ' שמחזירה מספר בחזקת 2
# x = lambda n: n**2
# print(x(3))

#הגדרתי פונ' שמקבלת 2 מספרים ומחזירה רק את הראשון
# x = lambda a,b: a
# print(x(4,6))

# x = lambda a,b: a if a>b else b
# print(x(12,3))

#הגדרתי פונ' שמקבלת מספר ומחזירה את השורש שלו
# import math as m
# x = lambda a: m.sqrt(a)
# print(x(25))


