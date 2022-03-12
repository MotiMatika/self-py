# def pratim():
#     first_name,second_name,year="moti","yair",1964
#     # print("my name is :",first_name,second_name,"and i born in",year)
#     # print(type((first_name,second_name)))
#     return year
# print("your age is :",2022-pratim())


#דוגמא להפיכת טאפל לרשימה כדי לשנות אותה והחזרתה לטאפל
# x = ("apple", "banana", "cherry")           # טאפל
# y = list(x)                                 # שינוי טיפוס לרשימה
# y[1] = "kiwi"                               #השמת ערך אחר
# x = tuple(y)                                #שינוי הרשימה לטאפל
# print(x)                                    # הדפסת הטאפל

#8.2.1
#עובד אצלי אך לא באתר
# data = ("self", "py", 1.543)
# format_string = "Hello"
# print(format_string,"%s.%s learner,you have only, %3.1f, units left befor you master the course!" %(data))

# strings = ['cat', 'mammal', 'goat', 'is']
# print(strings)
# x=strings.sort()# מדוע כשמדפיסים את איקס הוא נותן נאן ?
# # print(x)
# print(strings)
# y=strings.sort(key = len)#מדוע כשמדפיסים את ואיי הוא נותן נאן ?
# #print(y)
# print(strings)



#פעולת המיון בתוך רשימה
# x=["4444","333","1","22"]
# y=x.sort(key=len)
# print(x)



#8.2.2
#דרך מסורבלת למצוא את האובייקט היקר בטאפל
# def sort_prices(list_of_tuples):
# x=[("milk",5.5),("candy",2.5),("bread",9.0)]
# a=0
# b=1

# print(x[a][b])
# print(x[a+1][b])
# print(x[a+2][b])

# if (x[a][b])>(x[a+1][b]) and (x[a][b]>x[a+2][b]):
#     print(x[0])
# elif (x[a+1][b])>(x[a][b]) and (x[a+1][b]>x[a+2][b]):
#     print(x[1])
# else:
#     print(x[2])


#wors 8.2.2
#הפונקציה מקבלת רשימה של טאפלים שבכל אחד פריט ומחירו.
#הפונקציה מחזירה רשימה של טאפלים ממוינים על פי מחיר הפריטים שבהם מהגדול לקטן
# def sort_prices(list_of_tuples):
#     products=[("milk",5.5),("candy",2.5),("bread",9.0)]
#     x=list(products)
#     x.sort(key=(lambda a:a[1]))
#     x.reverse()
#     print(x)
# sort_prices([("milk",5.5),("candy",2.5),("bread",9.0)])


#works
#8.2.2
# x=[("milk",5.5),("candy",2.5),("bread",9.0)]
# x.sort(key=(lambda a:a[1]))
# x.reverse()
# print(x)
#works
# def sort_prices(list_of_tuples):                            #הגדרת הפונקציה
#     products=list(list_of_tuples)                           #הפיכת רשימת הטאפלים לרשימה
#     products.sort(key=(lambda a:a[1]))                      #מיון הרשימה לפי מפתח שממיין את הערך השני בכל אובייקט מהקטן לגדול
#     products.reverse()                                      #הפיכת הסדר ,כדי שיופיע מהגדול לקטן
#     print(products)                                         #הדפסת רשימת הטאפלים הממויינת
# sort_prices([("milk",5.5),("candy",2.5),("bread",9.0)])     #קריאה לפונקציה והשמת רשימת הטאפלים


#הפונקציה מקבלת כפרמטרים שני איברים מהטיפוס טאפל.
#הפונקציה מחזירה טאפל המכיל את כל הזוגות שאפשר ליצור מאיברי הטאפלים שהועברו כארגומנטים.

# def mult_tuple(tuple1):
#     a=list(tuple1)
#     b=list(tuple1)
#     a.sort(key=(lambda c:c[0]))
#     print(a)
#     b.sort(key=(lambda d:d[0]))
#     print(b)

#     # t=a+b
#     # print(t)
# mult_tuple([(1,2),(3,4)])

#8.2.3
#יש פלט אך לא בטוח שלזה התכוונו כי זה לא טאפל
# def sum(tuple1,tuple2):
#     a=list(tuple1)
#     b=list(tuple2)
#     c=0
#     for i in a :
#         print(i,",",b[c])
#         print(b[c],",",i)
#     c=1
#     for i in a:
#         print(i,",",b[c])
#         print(b[c],",",i)
#sum((1,2),(4,5))



# tuple_four = (4,2,3)        #טאפל עם שלשה מספרים
# x=sorted(tuple_four)        # פעולת מיון מהקטן לגדול על טאפל-שמחזירה רשימה חדשה-כי טאפל הוא immutible
# print(tuple_four)           #למרות פעולת המיון הטאפל לא משתנה
# print(x)                    #יצרתנו רשימה חדשה וממויינת
# x.reverse()                 #היפוך הרשימה-מהגדול לקטן
# print(x)                    #הדפסת הרשימה ההופכה


#8.2.3
#יש פלט .בדאבינג עובד , אך לא מדפיס את כל האפשרויות
# def sum(tuple1,tuple2):
#     a=list(tuple1)
#     b=list(tuple2)
#     length_tuple=len(b)
#     rounds=1
#     mikum=0
#     while rounds<=length_tuple and mikum<=2:
#         for i in a :
#             new_tuple=(i,b[mikum])
#             print(new_tuple)
#             new_tuple=list(new_tuple)
#             new_tuple.reverse()
#             new_tuple=tuple(new_tuple)
#             print(new_tuple)
#         rounds+=1
#         mikum+=1
# sum((1,2,3),(4,5,6))

#8.3.2












#8.2.4
# list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

# def sort_anagrams(list_of_strings):


    # for i in range(len(list_of_strings)):                         #איי מייצגת מילה ראשונה ברשימה
    #     length=len(i)
    #     for j in range(len(list_of_strings[i+1])):                # שנייה והלאהג'יי מייצגת מילה
    #         if len(list_of_strings[i])==len(list_of_strings[j]) :
    #             for k in range (len(list_of_strings[j])):         #קיי מייצגת אות בתוך מילה
    #                 if list_of_strings[j][k]:

# sort_anagrams(list_of_words)




# list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
# print(list_of_words[1][0])


# x="abcdef" #כל אות לחוד
# for i in x:
#     print(i)

# x=["abc","def"]#כל מחרוזת לחוד
# for i in x:
#     print(i)

# x=["abc","def"]     #
# for i in x:         #
#     if i=="def":#גורם ללולאה להתבצע פעם אחת
#         break
#     else:
#         for j in i:
#             print(j)
#             if j=="c":#התנאי גורם ללולאה להתבצע 3 פעמים.
#                 break





# #8.2.4#לבד על בסיס דרור
# list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries',
#                  'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

# # def sort_anagrams(list_of_strings):

# for i in range(len(list_of_words)):#איי מייצגת מילה ראשונה ברשימה
#         #length=len(i)
#     for j in range(len(list_of_words[i+1])):# שנייה והלאהג'יי מייצגת מילה
#         if len(list_of_words[i])==len(list_of_words[j]):
#             for k in range (len(list_of_words[j])):#קיי מייצגת אות בתוך מילה
#                 if list_of_words[j][k]:

# # sort_anagrams(list_of_words)







# x=["abc","def"]
#
#
#
# #
# for i in range(len(x)):                       #החלטה כמה סבבים תתבצע הלולאה הבאה-במקרה זה פעמיים
#     for j in x:                               #המילה הראשונה נשארת קבועה
#         if len(x[i])==len(x[j]):              #אם האורך של המילה הנמצאת במקום 0 שווה
#                                               # לאורך של המילה שנמצאת במקום ה0-תבצע
#             for k in range(len (x[j])):
#                 if x[j][k]==x[j+1][k]:
#                     print("yes")
#                 else:
#                     print("no")

#         # for k in j:     #קיי עובר על כל אות בתוך המילה הראשונה
#         #                 #עד שהיא מסתיימת ואז עוברים למילה השניה
#         #     if










#8.2.4
#בודקת אם קיימות מילים נוספות ברשימה באורך של המילה הראשונה ומדפיסה את הרשימה המעודכנת
# i=0
# x=["abc","n","de","tttt","wkw","s","sdq","ahg"]
# length=len(x)
# while i <= length:
#     if i==length-1:
#         break
#     elif len(x[0])==len(x[i+1]):
#         pass
#     else:
#         # print((x[i+1]))
#         x.pop(i+1)
#         length=length-1
#         i-=1
#     i+=1

# print(x)



x=["abc","n","dey","tttt"]
length=len(x)
for i in range(length):

    if i<=length:
        if len(x[0])==len(x[i+1]):
            pass
        else:
        # print((x[i+1]))
            x.pop(i+1)
            length-=1
            if length==1:
                break

print(x)





