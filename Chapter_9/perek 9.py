# def are_files_equal(file1, file2):
# x=True
# open1=open("C:\Users\motim\Desktop\yair.txt", "r")
# print(open1.read())
# open2=open("yair.txt", "r")
# x = open1 == open2
# print(x)

# are_files_equal()

# with open("empty.txt", "w") as input_file:
#     input_file.write("So, call me mabye?")
#     print(input_file.read())

###############################################################
#################        WITH SHAHAR     ######################
###############################################################

# Relative path: ./ means the current directory where this file resides. 
# In this case: "Cahpter_9" is th directory
# openedFile = open("./myInputFiles/file1.txt")
# print(openedFile.read())

# openedFile = open("./myInputFiles/file2.txt")
# print(openedFile.read())
#פתיחת הקובץ כדי לעדכן-כתיבה

# openedWrite = open("./myInputFiles/writeHere.txt", "w")
# openedWrite.write("Hello! is this working?")
# openedWrite.close()#סגירת הקובץ

# openedFile = open("./myInputFiles/writeHere.txt")#פתיחת הקובץ כדי לקרוא ממנו
# print(openedFile.read())#הדפסת הקובץ
# openedFile.close()#סגירת הקובץ


# def choose_word(file_path, index):
#     read_txt = open(file_path)
#     content = read_txt.read()
#     all_words = content.split(" ")
#     unique_words = list(dict.fromkeys(all_words))
#     print(unique_words)
#     length = len(unique_words)
#     print(length)
#     print(unique_words[index-1])
# choose_word("./words_to_guess.txt",15)

# def choose_word(file_path, index):                  #הגדרת הפונקציה- 2 ערכים : נתיב ומיקום המילה בתוך הרשימה
#     read_txt = open(file_path)                      #פתיחת הקובץ לקריאה עם מילים לניחוש
#     content = read_txt.read()                       #הכנסת הרשימה למשתנה
#     all_words = content.split(" ")                  #הפרדת הקובץ למילים בתוך מערך/רשימה
#     unique_words = list(dict.fromkeys(all_words))   #ביטול הכפילויות ע"י הפיכת המערך למילון,ואח"כ הפיכת המילון לרשימה
#     print(unique_words)                             #הדפס את המערך/רשימה
#     length_unique = len(unique_words)               #כמות המילים ברשימה
#     print(length_unique)                            #הדפסת האורך של הרשימה -ללא כפילויות
#     #print(all_words[index-1])                       #הדפסת המילה במיקום המסויים
#     times_circle = index%(len(all_words))
#     the_word = all_words[times_circle-1]
#     print("the word is : ",the_word)
#     print("x :",times_circle)
#     return(length_unique,the_word)

# choose_word("./words_to_guess.txt",-1)               #הפונקציה מקבלת את הנתיב ואת מיקום המילה שתנוחש ע"י המשתמש



def game():
    file_path = input("enter a file path : ")
    loc_word = int(input("enter a number : ")

game()























