
                                            # WHILE loop
# i=0                #מונה=0
# while i<10:        #כל עוד המונה קטן מ 10-תבצע
#     i=i+1          #הוסף 1
#     print(i)       #פלט

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# i=0                #מונה=0
# while i<10:        #כל עוד המונה קטן מ10 -תבצע
#      i=i+1         #הוסף 1
#      print(i)      #פלט
#      break         #הלולאה הספיקה להדפיס רק סבב יחיד


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# i=0                  #מונה=0
# while i<10:          #כל עוד המונה קטן מ 10 -תבצע
#     i=i+1            #הוסף 1
#     if i%2==0:       #אם השארית שווה לאפס,כלומר המספר זוגי,
#         continue     #אל תדפיס ותמשיך לשלב הבא בלולאה - לדלג
#     print(i)         #פלט

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                              #7.1.4
#התכנית מקבלת 2 ערכים ומחזיר את כל ריבועי המספרים בין הגבולות שניתנו

# import math                        #ייבוא ספרייה
# def squared_numbers(start,stop):   #הגדרת פונקציה עם 2 ערכים שלמים
#     list1=[]                       #הגדרת רשימה

#     while start<=stop:             #כל עוד ההתחלה קטנה או שווה לסוף
#         x=int(pow(start,2))        #תא איקס יקבל את המספר בריבוע
#         start+=1                   #הגדלת ההתחלה ב1
#         list1.append(x)            #עידכון הרשימה-הכנסת הערך האחרון בריבוע לרשימה
#     return list1                   #החזר את הרשימה המעודכנת

# def main():                        #הגדרת הפונקציה מיין
#     squared_numbers(-3,3)          #קריאה לפונקציה והשמת ערכים
#     print(squared_numbers(-3,3))   #אם אני רוצה לראות את הפלט

# if __name__ == "__main__":         #סיומת שמורה לשימוש בפונקציה מיין
#     main()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                             #FOR loop
#

# list=["y4","ya4","ya7","yb8"]              #הגדרת רשימה
# New_list=[]                                #הגדרת רשימה
# for kita in list:                          #עבור כיתה בתוך הרשימה
#     New_list.append(kita)                  #דחוף את האובייקט ברשימה לסופה
# print(New_list)                            #לשים לב להבדל במיקום הפקודה פרינט
#                                            #התכנית תדפיס פעם אחת את הרשימה

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# list=["y4","ya4","ya7","yb8"]          #הגדרת רשימה
# New_list=[]                            #הגדרת רשימה
# for kita in list:                      #עבור כיתה בתוך הרשימה
#     New_list.append(kita)              #דחוף את האובייקט ברשימה לסופה
#     print(New_list)                    #לשים לב להבדל במיקום הפקודה פרינט
                                       #התכנית תדפיס בכל מחזור רשימה מעודכנת יותר עד שתסתיים הלולאה

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#7.2.1 - Shahar
# def is_greater(my_list,n):
#     New_list=[]
#     for num in my_list:
#         if num>n:
#             New_list.append(num)
#         else:
#             continue
#     return New_list

# def main():                            #הגדרת הפונקציה מיין
#     is_greater([7,0,1,3,5],2)          #קריאה לפונקציה והשמת ערכים
#     print(is_greater([7,0,1,3,5],2))   #אם אני רוצה לראות את הפלט

# if __name__ == "__main__":             #סיומת שמורה לשימוש בפונקציה מיין
#     main()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                           #7.2.2
"""
def numbers_letters_count(my_str):     #הגדרת פונקציה שמקבלת מחרוזת

    num_of_chr=0                       #איפוס מונה לתווים שאינם מספרים
    num_of_digits=0                    #איפוס לתווים שהם מספרים

    for chr in my_str:                 #עבור משתנה בתוך המחרוזת שנקלטת - תבצע:את
        if chr.isnumeric():            #אם המשתנה הוא מספר
            num_of_digits+=1           #הוסף 1 למונה המספרים
        else:                          #אחרת
            num_of_chr+=1              #הוסף 1 למונה התווים שאינם מספרים
    list1=(num_of_digits,num_of_chr)   #התא ליסט1 מקבל את 2 הערכים
    list2=list(list1)                  #שינוי הטיפוס לרשימה
    return(list2)                      #החזר את הרשימה

def main():                                       #הגדרת הפונקציה מיין
    numbers_letters_count("1,2,  ")          #קריאה לפונקציה והשמת ערכים
    print(numbers_letters_count("1,2,  "))   #אם אני רוצה לראות את הפלט

if __name__ == "__main__":                        #סיומת שמורה לשימוש בפונקציה מיין
      main()
      """

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




def numbers_letters_count(my_str):     #הגדרת פונקציה שמקבלת מחרוזת
    list1=[0,0]                        #התא ליסט1 מקבל את 2 הערכים
    for chr in my_str:                 #עבור משתנה בתוך המחרוזת שנקלטת - תבצע:את
        if chr.isnumeric():            #אם המשתנה הוא מספר
            list1[0]+=1                #הוסף 1 למונה המספרים
        else:                          #אחרת
            list1[1]+=1                #הוסף 1 למונה התווים שאינם מספרים
    return(list1)                      #החזר את הרשימה

def main():                                       #הגדרת הפונקציה מיין
    numbers_letters_count("1,2,  ")          #קריאה לפונקציה והשמת ערכים
    print(numbers_letters_count("1,2,  "))   #אם אני רוצה לראות את הפלט

if __name__ == "__main__":                   #סיומת שמורה לשימוש בפונקציה מיין
      main()







