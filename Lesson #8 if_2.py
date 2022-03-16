#ממיינת בין 2 מספרים מי גדול יותר רק אם הם שונים
# x = int(input ("a = "))
# y = int(input ("b = "))
# if x>y:
#     print(x,">",y)
# else:
#     print(y,">",x)


#ממיינת בין 2 מספרים מי גדול יותר גם אם הם שווים

# a = int(input ("a = "))
# b = int(input ("b = "))
# if a>b:
#     print(a,">",b)
# elif a==b:
#     print(a,"=",b)
# else:
#     print(b,">",a)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# משווה יחסית למספר קבוע
# num = int(input(" ?בחר מספר.מהי הבחירה שלך"))      #קלט של מספר מהמשתמש
# x=10                                        # השמת ערך בתא איקס
# if num > x:                                 #אם המספר שהקליד המשתמש גדול מ 10 ... אז
# 	print(num,">",x)                        # פלט-המספר שבחרת גדול מ 10
# elif num < x:                               #אחרת- אם המספר שהקליד המשתמש קטן מ 10 ... אז
# 	print(num,"<",x)                        #פלט-המספר שבחרת קטן מ 10
# else:                                       # אחרת
# 	print(num,"=",x)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # משווה יחסית למספר קבוע
# print("Choose a Number ",)                        # פלט - הודעה
# choice1 = int(input("What is Your Choice?  "))    #קלט של מספר מהמשתמש
# x=10                                              # השמת ערך בתא איקס
# if choice1 > x:                                   #אם המספר שהקליד המשתמש גדול מ 10 ... אז
# 	print("your number is bigger than ",x)         # פלט-המספר שבחרת גדול מ 10
# elif choice1 < x:                                 #אחרת- אם המספר שהקליד המשתמש קטן מ 10 ... אז
# 	print("your number is smaller than ",x)        #פלט-המספר שבחרת קטן מ 10
# else:                                             # אחרת
# 	print("your number is equal to ",x) 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#התכנית תמיין שלשה מספרים רק אם הם שונים
# a = input ("a = ")
# b = input ("b = ")
# c = input ("c = ")
# if a>b:
#     if a>c :
#         if b>c:
#             print(" "*5,"a > b > c\n"," "*4,a,">",b,">",c)
#         else:
#             print(" "*5,"a > c > b\n"," "*4,a,">",c,">",b)
#     else:
#         print(" "*5,"c > a > b\n"," "*4,c,">",a,">",b)
# else:
#     if b>c:
#         if a>c:
#            print(" "*5,"b > a > c\n"," "*4,b,">",a,">",c) 
#         else:
#             print(" "*5,"b > c > a\n"," "*4,b,">",c,">",a)
#     else:
#         print(" "*5,"c > b > a\n"," "*4,c,">",b,">",a)        


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#שידרוג ?
# התכנית תמיין שלשה מספרים רק אם הם שונים
a = input ("a = ")
b = input ("b = ")
c = input ("c = ")
if a>b and a>c and b>c:
    print(" "*5,"a > b > c\n"," "*4,a,">",b,">",c)
if a>b and a>c and b<c:
    print(" "*5,"a > c > b\n"," "*4,a,">",c,">",b)
if a>b and a<c :
    print(" "*5,"c > a > b\n"," "*4,c,">",a,">",b)
if b>a and b>c and a>c:
    print(" "*5,"b > a > c\n"," "*4,b,">",a,">",c)
if b>c and a<c :
        print(" "*5,"b > c > a\n"," "*4,b,">",c,">",a)
if b>a and b<c:
      print(" "*5,"c > b > a\n"," "*4,c,">",b,">",a)  
 