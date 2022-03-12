                                            #4.2.2

# txt = input("please Enter a String : ")         #קלט של מחרוזת
# txt1 = txt.replace(" ","")                      #ביטול כל הרווחים - אם קיימים
# txt2=txt1.lower()                               #ביטול כל האותיות הגדולות
# print("You typed :",txt,"...but, I deleted the spaces and changed the CAPITAL letters\n","Your String is : ",txt2)
# if txt2[::1] ==  txt2[::-1]:                    #בדיקת האותיות מההתחלה לסוף מול כל האותיות מהסוף להתחלה
#     print("You typed a Palindrom")              #אם הן זהות ידפיס שזהו פלינדרום
# else:                                           #אחרת
#     print("Your String is not a Palindrom")     #ידפיס שזהו אינו פלינדרום



#4.2.3
temp = input("Your Temp : ")
temp1 = float(temp)
scale = input("if You Want to Conver from Fahrenheit to Celsius type F or f\n if You Want to Conver from Celsius to Fahrenheit type C or c : ")
scale1 = scale.lower()
if "f" == scale1:
    #print("You Want to Convert Fahrenheit to Celsius ")
    c = (5*temp1-160)/9
    #print(temp, " in Fahrenheit is :", c, " in Celsius")
    print(c)
else:
    #print("You Want to Convert Celsius to  Fahrenheit ")
    c = (9*temp1+160)/5
    #print(temp, " in Celsius is :", c, " in Fahrenheit")
    print(c)


# txt = input("please Enter a String : ")         #קלט של מחרוזת
# txt1 = txt.replace(" ","")                      #ביטול כל הרווחים - אם קיימים
# txt2=txt1.lower()                               #ביטול כל האותיות הגדולות
# print("You typed :",txt,"...but, I deleted the spaces and changed the CAPITAL letters\n","Your String is : ",txt2)
# if txt2[::1] ==  txt2[::-1]:                    #בדיקת האותיות מההתחלה לסוף מול כל האותיות מהסוף להתחלה
#     print("You typed a Palindrom")              #אם הן זהות ידפיס שזהו פלינדרום
# else:                                           #אחרת
#     print("Your String is not a Palindrom")     #ידפיס שזהו אינו פלינדרום



#4.2.3
# temp = input("Your Temp and scale : ")
# x = float(temp[:-1])
# scale = temp.lower()
# if "f" in scale:
#     print("You Want to Convert Fahrenheit to Celsius ")
#     c = (5*x-160)/9
#     print(x, " degrees in Fahrenheit is :", c, " degrees in Celsius")
# else:
#     print("You Want to Convert Celsius to  Fahrenheit ")
#     fr = (9*x+160)/5
#     print(x, " degrees in Celsius is :", fr, " degrees in Fahrenheit")



#4.2.4
# date = input("enter the date and find which day it is ")
# d   =  int(date[0:2])         #הפיכת קטע ממחרוזת למספר שלם
# m  =   int(date[3:5])         #הפיכת קטע ממחרוזת למספר שלם
# y =    int(date[6::])         #הפיכת קטע ממחרוזת למספר שלם
# import datetime               #ייבוא ספרייה
# x = datetime.datetime(y,m,d)  #אובייקט שמקבל 3 ערכים של שנה,חודש ויום כמספרים שלמים
# print(x.strftime("%A"))       # מוצא את היום המדובר