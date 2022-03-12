A_B_C = {"A": "aba", "B": "bee", "C": "cat"}   #יצירת מילון עם מפתחות וערכיהם

# print(A_B_C["A"])         #הדפסת ערך במילון-לפי המפתח
# if "A" in A_B_C:          #חיפוש הימצאות של מפתח במילון
#      print("yes")
# # A_B_C["D"]="dad"            #הוספת ערך חדש למילון
# # A_B_C["D"]="dood"                              #עידכון ערך במילון - לפי המפתח
# # A_B_C.pop("D")                                 #מחיקת ערך מהמילןן - לפי המפתח
# # print(A_B_C.keys())                              #הדפסת מפתחות המילון
# # print(A_B_C.values())                            #הדפסת ערכי המילון
# # print(A_B_C)

# #print(A_B_C.items())#הדפסת כל הפריטים:מפתחות וערכים בצמדים - טאפל

print(A_B_C.get("A"))# הדפסת הערך של מפתח

# #print(len(A_B_C))#אורך המילון

# # print(A_B_C["A"])

# #8.3.2
# First_Dict = {"first_name": "Mariah","last_name": "Carey","birth_date": "27.03.1970","hobbies": ["Sing","Compose","Act"]}
# x=input("enter ")
# if x=="1":
#     print(First_Dict.get("last_name"))
# if x=="2":
#     print(First_Dict.get("birth_date"))
# if x=="3":
#     print(len(First_Dict.get("hobbies")))
# if x=="4":
#     print(First_Dict.get("hobbies")[2])
# if x=="5":
#     First_Dict["hobbies"].append("Cooking")                        
#     print(First_Dict["hobbies"])
# if x=="6":
#     y=tuple(First_Dict.get("birth_date"))
#     a=((y[0]+y[1]),(y[3]+y[4]),(y[6]+y[7]+y[8]+y[9]))
#     print(a)
# if x=="7":
#     First_Dict["Age"]="52"
#     print(First_Dict.get("Age"))

#8.3.3
# def count_chars(my_str):
#     my_str=list(my_str)
#     length=len(my_str)
#     i=1
#     j=0
#     while i<=length:
#         if my_str[j]== 
#         if i==i+1:
#         print(i)
#     print(length)
# print(count_chars("aboba"))



















#8.4.1
# HANGMAN_PHOTOS={
# "1": "x-------x"
# , "2": """x-------x
# |
# |
# |
# |
# | """
# , "3": """ 
# x-------x
# |       |
# |       0
# |
# |
# |          
# """
# , "4": """
# x-------x
# |       |
# |       0
# |       |
# |
# |             		 
# """
# , "5": """ 
# x-------x
# |       |
# |       0
# |      /|\                                                                                                 
# |      
# |       
# """
# , "6": """ 
# x-------x
# |       |
# |       0
# |      /|\                                                                                                      
# |      /
# |       
# """
# , "7": """ 
# x-------x
# |       |
# |       0
# |      /|\                                                                                                      
# |      / \
# |       
# """
# }

# print(HANGMAN_PHOTOS["7"])
# def print_hangman(num_of_tries):
#     num_of_tries





# print_hangman(6)