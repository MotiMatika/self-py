#7.3.1
# def show_hidden_word(secret_word, old_letters_guessed):
#     for i in secret_word:
#         lines.append()
#     for letter in old_letters_guessed:
#         if letter in secret_word:
#            loc = secret_word.find(letter)    

# print(show_hidden_word("mammals",["s","p","j","i","m","k"]))


#קווים תחתונים כמספר האותיות
def len_lines(secret_word, old_letters_guessed):
    x = secret_word.count("a")
    print("_ "*x) 
          
len_lines("motiyair",["d","a"])

# number_of_times("c","motiyair")

#מחליף ל@ אם האות נמצאת 
# def replace_letter(letter,secret_word):
#         rep = secret_word.replace(letter,"@")
#         return rep

# replace_letter("c","motiyair")





# def main():



























# text="moti yair"
# x = str(text)
# x.split()
# for i in x:
#     print("_",end="")
#     #print("\u0332".join())

#     # x=0
#     # old_letters_guessed = []
#     # while x < length:  
#     #     letter = input("your geuss ")
#     #     if letter not in old_letters_guessed:
#     #         old_letters_guessed.append(letter) 
#     #         print(old_letters_guessed)
#     #         x=x+1
#     #     else:
#     #         x=x+1
#     #         print(old_letters_guessed)
# letter = ""   
#         if letter in old_letters_guessed:
#             old_letters_guessed.append(letter) 
#             print(old_letters_guessed)
#             x=x+1
#         else:
#             x=x+1
#             print(old_letters_guessed)