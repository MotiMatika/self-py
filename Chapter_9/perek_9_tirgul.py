#פרק 9 - קבצים

# a=open("./myInputFiles/1.txt", "r")   #פתיחת קובץ עם הנתיב שלו לקריאה
# print(a.read())                       #הדפסת תוכן הקובץ
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# a=open("./myInputFiles/1.txt", "w")             #פתיחת קובץ עם הנתיב שלו לכתיבה
# a.write("hi,\nmy name is Moti\nI'm a teacher\n\n") #עידכון המלל בקובץ
# a=open("./myInputFiles/1.txt", "r")             #פתיחת קובץ עם הנתיב שלו לקריאה
# print(a.read())                                 #הדפסת הקובץ המעודכן
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#הקובץ המדובר כתוב בשלש שורות
# a = open("./myInputFiles\secret_words.txt","r")
# x=a.readline()# קורא רק את השורה הראשונה
# length = len(x)#אורך הקובץ
# print(x)#ומדפיס כמו שמופיעה בקובץ
# print(x[1])#מדפיס את התו במקום השני
# print(length)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# a = open("./myInputFiles\secret_words.txt","r")
# y=a.readlines()# קורא את כל תוכן הקובץ 
# length = len(y)# כמות השורות
# print(y)#מדפיס את התוכן כרשימת מחרוזות
# print(y[1])#מדפיס את השורה השניה
# print(y[1][3])#מדפיס את התו הרביעי בשורה השניה
# print(length)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# a = open("./myInputFiles\secret_words.txt","r")
# x=a.readline()# קורא רק את השורה הראשונה
# for i in x:#מדפיס תו אחר תו.תו בכל שורה
#     print(i)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# a = open("./myInputFiles\secret_words.txt","r")
# x=a.readlines()# קורא את כל הקובץ
# for i in x:
#     print(i) #מדפיס שורה אחר שורה 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#9.1.2
file1 = open("./myInputFiles\secret_words.txt","r")
x=file1.readlines()# קורא את כל הקובץ
pressed = input("your wish: sort,rev or last : ")

if pressed=="sort":
    print(x[:])
    print(len(x))
    a=x[0]
    a.rsplit()
    print(a[2])
    # b=list(a)
    # b.sort()
    # print(b)
    # a=t[4]
    # print(a)

elif pressed=="rev":
    a=str(x) 
    b=list(a)
    b.reverse()
    print(b)
# elif pressed=="last":
#     print(x.lasl)


#9.1.1
# def are_files_equal(file1, file2):
#     if file1==file2:
#         print("True")
#     else:
#         print("False")
# are_files_equal("./myInputFiles/1.txt","./myInputFiles/11.txt")

#9.4.1

# def choose_word(file_path,index):
    
# a = open("./myInputFiles\secret_words.txt","r")
# x=a.readline()
# x=a.readline()
# length = len(x)
# print(x)


# print(x)
# print(choose_word("./myInputFiles\secret_words.txt",2) )  














