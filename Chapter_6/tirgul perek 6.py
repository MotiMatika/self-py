                            #פרק 6 - רשימות
#@@@@@@@@@@@@@@@@@@@@@@@@@
# x=["moti","yair","1964"]                               #רשימת מילים
# print("family:",x[1],"   name:",x[0],"   year:",x[2])  #פלט לפי מיקום

#@@@@@@@@@@@@@@@@@@@@@@@@@@
# letters="moti"                                        #מחרוזת לתוך לטרז
# x=list(letters)                                       #מילה שמורה ליסט על המחרוזת מפרידה את האותיות של המחרוזת
# print(x)                                              #פלט-אותיות מופרדות

#@@@@@@@@@@@@@@@@@@@@@@@@@@
# x=["moti","yair","1964"]                                #רשימת מילים
# name,family,year=x                                      #הכנסת כל הרשימה  לשלשה משתנים בהתאמה
# print(name)                                             #פלט לערך הראשון
# print(family)
# print(year)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                         #6.1.2


# def shift_left (my_list):                                         #הגדרת פונקציה עם ערך בודד
#     new_list = [ my_list[1], my_list[2], my_list[0] ]             #שינוי סדר ההופעה לפי מיקום
#     return new_list                                               #תוצר הפונקציה

# def main():                                                       #הגדרת הפונקציה מיין
#       shift_left(["1","2","3"])
#       print(shift_left(["1", "2", "3"]))                          #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                                        #סיומת שמורה לשימוש בפונקציה מיין
#  	main()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# list1 = [1, 2, 3, 4]
# list2 = [5,6,7]
# list3 = list1 + list2
# list4 = [list1 + list2]
# print (list1)
# print (list2)
# print (list3)
# print (list4)
# print(list4[0][3])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def x(a):
#     b=a+1
#     return b              #ללא ריטרן - לא יחזיר את תוצאת הפונקציה
# print(x(9))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#6.2.3

# def format_list(my_list):

#     zugi = my_list[0::2]                              #שליפת כל ערך במקום זוגי ברשימה
#     Comma_Space =  ", ".join(zugi)                     #שילוב של פסיק ורווח בין כל איבר ברשימה
#     Comma_and = ", and "                              #הוספת מחרוזת
#     last = my_list[-1]                                #מציאת הערך האחרון ברשימה
#     return(Comma_Space+Comma_and+last)                 #החזרת שילוב כל 3 המשתנים

# def main():                                           #הגדרת הפונקציה מיין
#       format_list(["1","2","3","4","5","6"])          #השמת ערכים לפונקציה
#       print(format_list(["1","2","3","4","5","6"]))   #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                            #סיומת שמורה לשימוש בפונקציה מיין
#  	main()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

              #6.2.4
# import operator                             #ייבוא ספרייה

# def extend_list_x(list_x,list_y):           #הגדרת פונקציה עם 2 רשימות
#     return operator.add(list_y,list_x)      #החזרת התוצר

# def main():                                 #הגדרת הפונקציה מיין
#     extend_list_x([4,5,6],[1,2,3])          #קריאה והשמת ערכים לפונקציה
#     print(extend_list_x([4,5,6],[1,2,3]))   #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                  #סיומת שמורה לשימוש בפונקציה מיין
#    	main()



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


                             #6.3.1
def are_lists_equal(list1,list2):  #הגדרת פונקציה שתקבל 2 רשימות
    list1.sort()                   #מיון הרשימה מהקטן לגדול
    list2.sort()                   #מיון הרשימה מהקטן לגדול
    t = list1 == list2             #השוואה בין 2 הרשימות
    return t                       #החזרת ערך בוליאני


def main():                                           #הגדרת הפונקציה מיין

    are_lists_equal([4,1],[1,4])              #השמת 2 רשימות וקריאה לפונקציה
    print(are_lists_equal([4,1],[1,4]))       #אם אני רוצה לראות את התוצר של הפונקציה

if __name__ == "__main__":                    #סיומת שמורה לשימוש בפונקציה מיין
  	main()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 6.3.2
# def longest(my_list):                           #הגדרת פונקציה שתקבל רשימת מחרוזות

#     x = sorted(my_list,key=len)                 #מיון הרשימה לפי מפתח של אורך
#     return (x[-1])                              #החזרת הערך האחרון ברשימה

# def main():                                     #הגדרת הפונקציה מיין

#     longest(["a","bb","ccc","e"])               #השמת 2 רשימות וקריאה לפונקציה
#     #print(longest(["a","bb","ccc","e"]))       #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                      #סיומת שמורה לשימוש בפונקציה מיין
#     main


#6.4.1 - check1
#def check_valid_input(letter_guessed, old_letters_guessed):
#הפונקציה בודקת אם הוכנסה יותר מאות אחת או הוכנס תו שהוא לא אות
# def is_valid_input(letter_guessed):         #הגדרת הפונקציה
# 	x = letter_guessed.isalpha()            #בדיקה באם כל התווים הם אותיות
# 	num = len(letter_guessed)               #אורך המחרוזת נכנס לתא נאם
# 	if num == 1 and x == True:              #אם גם הוקלד תו אחד וגם הוא אות ולא משהו אחר
# 		return True                         #החזר אמת
# 	else:                                   #אחרת
# 		return False                        #החזר שקר
# print(is_valid_input("8"))























# #הפונקציה מעדכנת את הרשימה של האותיות שכבר הוקלדו
# def uptae(old_letters_guessed):
#     old_letters_guessed.extend(old_letters_guessed)

# #הפונקציה בודקת אם האות שהוקלדה כבר נמצאת ברשימה ששומרת את ההקלדות הקודמות
# def are_lists_equal(letter_guessed,old_letters_guessed):  #הגדרת פונקציה שתקבל 2 רשימות
#     letter_guessed.sort()                   #מיון הרשימה מהקטן לגדול
#     old_letters_guessed.sort()                   #מיון הרשימה מהקטן לגדול
#     t = letter_guessed == old_letters_guessed             #השוואה בין 2 הרשימות
#     return t                       #החזרת ערך בוליאני

# def main():                                           #הגדרת הפונקציה מיין

#     are_lists_equal([4,1],[1,4])              #השמת 2 רשימות וקריאה לפונקציה
#     print(are_lists_equal([4,1],[1,4]))       #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                    #סיומת שמורה לשימוש בפונקציה מיין
#    	    main()

# print(is_valid_input("g"))                  #פלט-הדפס את תוצאת הפונקציה













#6.4.2
#הפונקציה בודקת אם המחרוזת תקינה לפי התנאים : אורך של תו יחיד,אם המחרוזת מורכבת רק מאותיות,ואם התו נוחש בעבר.
# #אם קיבלתי שלילה על כל הבדיקות,אזי הפונקציה תחזיר אמת,אחרת שקר
# def check_valid_input(letter_guessed, old_letters_guessed):#  הפונקציה מקבלת 2 משתנים:מחרוזת לקלט של המשתמש ורשימה לאותיות שנוחשו
#     lower_char= letter_guessed.casefold()
#     if len(lower_char)!=1:                        #בודקת אם האורך הוא תו אחד
#         return False

#     if not lower_char.isalpha():                  #בודק אם המחרוזת מורכבת מאותיות בלבד
#         return False

#     if lower_char in old_letters_guessed:             #בודקת אם המחרוזת כבר נוחשה
#         return False

#     return True                             #אם שלשת התנאים אינם מתקיימים החזר אמת

#שידרוג של כל תוכן הפונקציה שלעיל - כל התנאים בשורה אחת
 #   lower_char= char.casefold()
   # if (len(lower_char)!=1) or (not lower_char.isalpha()) or (lower_char in letters_guessed):
    #     return False
    #return True                             #אם שלשת התנאים אינם מתקיימים החזר אמת

# def print_guessed_letters(old_letters):
#     old_letters.sort()
#     stam=""
#     for x in old_letters:
#         stam=stam+x+" -> "
#     length=len(stam)
#     y=stam[:length-4]
#     print(y)

# def try_update_letter_guessed(letter_guessed, old_letters_guessed):
#     lower_char= letter_guessed.casefold()
#     if check_valid_input(lower_char,old_letters_guessed):
#         old_letters_guessed.append(lower_char)
#         return True
#     else:
#         print("X")
#         print_guessed_letters(old_letters_guessed)
#         return False

# def main():
#     old_letters = ['a', 'p', 'c', 'f']
#     try_update_letter_guessed('$', old_letters)

# if __name__ == "__main__":                    #סיומת שמורה לשימוש בפונקציה מיין
#    	    main()
















