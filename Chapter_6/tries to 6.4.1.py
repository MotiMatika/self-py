# # #התכנית קולטת תו ובודקת אם הוא ברשימה
# New_chr=input (str("enter  "))
# New_chr=list(New_chr)
# print(type(New_chr))

# t=True
# f=False

# def update(old_letters_guessed):
#     if New_chr in old_letters_guessed:
#         return t
#     else:
#         return f
# update(["a"])
# print(update(["a"]))



# # #התכנית קולטת תו ובודקת אם הוא ברשימה
# old="s"
# new="b"
# z=[old+new]
# print(z)
# if new in old:
#     print("yes")
# else:
#     print("no")


# #התכנית קולטת תו ובודקת אם הוא ברשימה
# New_chr=input (str("enter  "))
# New_chr=list(New_chr)
# #print(type(New_chr))

# t=True
# f=False

# def update(old_letters_guessed):
#     if New_chr in old_letters_guessed:
#         return t
#     else:
#         return f
# update(["a"])
# print(update(["a"]))




#התבססות על 6.2.4
# import operator                             #ייבוא ספרייה

# def extend_list_x(gu,old): #הגדרת פונקציה עם 2 רשימות

#     old=operator.add(old,old)
#     new=operator.add(gu,old)         #החזרת התוצר
#     last=new[-1]
#     if last in old:
#         print("yes")
#     else:
#         print("no")
# extend_list_x(["a"],["n"])

# def main():                                 #הגדרת הפונקציה מיין
#     extend_list_x([4,5,6],[1,2,3])          #קריאה והשמת ערכים לפונקציה
#     print(extend_list_x([4,5,6],[1,2,3]))   #אם אני רוצה לראות את התוצר של הפונקציה

# if __name__ == "__main__":                  #סיומת שמורה לשימוש בפונקציה מיין
#    	main()





# import operator                             #ייבוא ספרייה

# # #
# # הגדרת פונקציה עם 2 רשימות
# old=[]
# gu=list(input("enter :"))
# def extend_list_x(gu,old):
#     old=operator.add(gu,old)
#     print(old)
#     # new=operator.add(gu,old)         #החזרת התוצר
#     # last=new[-1]
#     # if last in old:
#     #     print("yes")
#     # else:
#     #     print("no")
# extend_list_x(["a"],["n"])










# #האם התו תקין


# #6.4.1
# def is_valid_input(letter_guessed):       #הגדרת הפונקציה
# 	x = letter_guessed.isalpha()            #בדיקה באם כל התווים הם אותיות
# 	num = len(letter_guessed)               #אורך המחרוזת נכנס לתא נאם
# 	if num == 1 and x == True and letter_guessed.isascii():              #אם גם הולדה אות אחת וגם היא אות ולא משהו אחר
# 		return True                         #החזר אמת
# 	else:                                   #אחרת
# 		return False                        #החזר שקר
# print(is_valid_input("V"))                #פלט-הדפס את תוצאת הפונקציה


#האם ניחשו את התו בעבר
# New_List = []
# for i in range(5):
#     char = input("Ente Your Guess : ")
#     if char in New_List:
#         print("         ** You already typed this letter")
#         New_List.sort()
#         print("The updated list is :",New_List)
#     else:
#         New_List.append(char)
#         New_List.sort()
#         print("The updated list is :",New_List)





#6.4.1
def check_valid_input(letter_guessed,old_letter_guessed):
    char = letter_guessed.isalpha()         
    num = len(letter_guessed)  
    if num == 1 and char == True and letter_guessed.isascii() and letter_guessed not in old_letter_guessed:
        return True
    else:
        return False 
print(check_valid_input("a",["b","w"]))




# def check_valid_input2(letter_guessed,old_letter_guessed):
#     if is_valid_input(letter_guessed) and letter_guessed not in old_letter_guessed:
#         return True
#     else:
#         return False 




