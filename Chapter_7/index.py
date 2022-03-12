# x="axsddess"
# count = x.count("s")
# x=x.index("s")
# print(x)
# # for i in range(count):
# #     y=x.index("s")
# #     print(y)
# #     x = x.replace("s","@",1)
# #     print(x)

# # #print(x.replace("s","@"))

# def all_indexses(letter,secret_word):
#     indexses=[]
#     i=0
#     length = len(secret_word)
#     #while i<=length:
#     if letter in secret_word:
#         times = secret_word.count(letter)
#         print(times)
#         print(secret_word.replace(letter,"@"))
#         indexses.append(secret_word.index(letter))
#         print("\n",indexses,"\n")
#         #if i == times:
#             #print(secret_word.replace(letter,"@"))
#             #break
#         else:
#     else:
#         print(" \n there isn't any  \n")
#         i=i+1
        
# all_indexses("i","motiyair")





#8-3-22

####קווים תחתונים כמספר האותיות במילה הסודית
# def len_lines(secret_word):
#     length = len(secret_word)
#     return "_ "*length

# print(len_lines("motiyair"))


####מונה את מספר ההופעות של אות במילה
# def number_of_times(letter,secret_word):
#     times = secret_word.count(letter)
#     return times

# print(number_of_times("i","motiyair"))


####מזהה את מיקומה של אות במילה הסודית
# def position(letter,secret_word):
#     if letter in secret_word:
#         print(secret_word.index(letter))    
#     else:
#         print("wrong")

# position("o","motiyair")


####מחליף ל@ אם האות נמצאת 
def replace_letter(letter,secret_word):
    if letter in secret_word:
        rep = secret_word.replace(letter,"@")
        print(rep)
replace_letter("i","_ _ _ _ _ _ _ _")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# def replace_letter(letter,secret_word):
#     length = len(secret_word)
#     lines = "_ "*length
#     i=0
#     for i<=length:
#     if letter in secret_word:
#             lines.replace("_ ",letter)
# # #         #כאן ייכנס האינדקס-למצוא את מיקום האות במילה הסודית 
#         # print(secret_word.index("i"))
#             print(lines.replace("_ ",letter))
# replace_letter("i","motiyair")



# def position(letter,secret_word):
#     if letter in secret_word:
#         #posi = secret_word.index(letter)
#         x=secret_word.replace(letter,"_")
#         print(x)
#     else:
#         print("wrong")

# print(position("i","motiyair"))



# def shahar(letter,secret_word):
#     indexes = []
#     for index, chr in enumerate(secret_word):
#         if letter==chr:
#             indexes.append(index)
#             print(indexes)
# shahar("z","motiyair")
            




#המשתמש יכניס מילה ואות.
# התכנית תדפיס קווים תחתונים כמספר האותיות הזהות במילה #
# ועבור כל אות הזהה לאות שהמשתמש הכניס במילה ,התכנית תחליף בסימן @ ותדפיס את המילה החדשה

# def main():
#     w = input("enter word : ")
#     l = input("enter a letter : ")
    
#     print(len_lines(l,w))
#     print(replace_letter(l,w))
# main()


# def t(char):
#     New_List = []
#     for i in range(4):
#         char = input("Ente Your Guess : ")
#         if char in New_List:
#             print(" "*18,"** You already typed this letter")
#             New_List.sort()
#         else:
#             New_List.append(char)
#             New_List.sort()
            
# print(t("a"))




#קולטת 5 תווים,מחליטה אם הם הוקלדו בעבר,פולטת רשימה ללא כפילויות

# New_List = []
# for i in range(5):
#     char = input("Ente Your Guess : ")
#     if char in New_List:
#         print("           You already typed this letter")
#         New_List.sort()
#         print("The updated list is :",New_List)
#     else:
#         New_List.append(char)
#         New_List.sort()
#         print("The updated list is :",New_List)

#הפונקציה מקבלת מילה ולפי אורכה היא מאפשרת ניחושים.
#הפלט:רשימה ובה כל הניחושים
# def len_lines(secret_word):
#     length = len(secret_word)
#     my_list = [] 
#     i=0
#     while i<length : 
#         letter = input("enter ")                  
#         my_list.append(letter) 
#         i=i+1       
#     return my_list                    

# print(len_lines("motiyair"))

# def len_lines(secret_word):
#     length = len(secret_word)
#     return "_ "*length

# print(len_lines("motiyair"))


#תירגול לבניית פונקציה 
#הפונקציה מקבלת רשימה ומחרוזת-ומחזירה 4 משתנים
# אורך הרשימה,ספירת כמות ההופעות של אות ברשימה
#אורך המחרוזת והמחרוזת עם אות גדולה
# def li(old_gussed_letters,secret_word):
#     x = len(old_gussed_letters)
#     z = old_gussed_letters.count("b")
#     y = len(secret_word)
#     t = secret_word.capitalize()
#     return x,y,z,t
    
# print(li(["c","b","p","c"],"moti yair"))


def show_hidden_word(secret_word,old_letters_guessed):
    res = []
    is_guessed = False
    for letter in secret_word:
        for old_letter in old_letters_guessed:
            if old_letter == letter:
                res.append(old_letter)
                is_guessed = True
                break
        if not is_guessed:
            res.append("_")
        is_guessed = False
    return ' '.join(res)

# print(show_hidden_word("mammals",["s","p","j","i","m","k"]))     



#גירסה מקוצרת לתרגיל 7.3.1
def show_hidden_word_2(secret_word,old_letters_guessed):
    res = []
    is_guessed = False
    for letter in secret_word:
        if letter in old_letters_guessed:
            res.append(letter)
            is_guessed = True
        
        if not is_guessed:
            res.append("_")
        is_guessed = False
    return ' '.join(res)

# print(show_hidden_word_2("mammals",["s","p","j","i","m","k","a","l"]))    
    



#7.3.2 check if user won
def check_win(secret_word,old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

isWon = check_win("mammals",["s","p","j","i","m","k","a","l"])

print(isWon)