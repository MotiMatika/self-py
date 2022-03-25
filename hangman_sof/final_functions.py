# # 7.3.2 check if user won
# def check_win(secret_word,old_letters_guessed):
#     for letter in secret_word:
#         if letter not in old_letters_guessed:
#             return False
#     return True

# # 7.3.1
# def show_hidden_word(secret_word,old_letters_guessed):
#     res = []
#     is_guessed = False
#     for letter in secret_word:
#         for old_letter in old_letters_guessed:
#             if old_letter == letter:
#                 res.append(old_letter)
#                 is_guessed = True
#                 break
#         if not is_guessed:
#             res.append("_")
#         is_guessed = False
#     return ' '.join(res)

# # 6.4.1
# def check_valid_input(letter_guessed,old_letter_guessed):
#     char = letter_guessed.isalpha()         
#     num = len(letter_guessed)  
#     if num == 1 and char == True and letter_guessed.isascii() and letter_guessed not in old_letter_guessed:
#         return True
#     else:
#         return False 
# print(check_valid_input("a",["b","w"]))

# # 6.4.2
# def try_update_letter_guessed(letter_guessed, old_letters_guessed):
#     lower_char= letter_guessed.casefold()
#     if check_valid_input(lower_char,old_letters_guessed):
#         old_letters_guessed.append(lower_char)
#         return True
#     else:
#         print("X")
#         print_guessed_letters(old_letters_guessed)
#         return False

# # Relevant to 6.4.2
# def print_guessed_letters(old_letters):
#     old_letters.sort()
#     stam=""
#     for x in old_letters:
#         stam=stam+x+" -> "
#     length=len(stam)
#     y=stam[:length-4]
#     print(y)

# old_letters = ['a', 'p', 'c', 'f']
# try_update_letter_guessed('$', old_letters)

# 9.4.1
def choose_word(file_path, index):                  #הגדרת הפונקציה- 2 ערכים : נתיב ומיקום המילה בתוך הרשימה
    read_txt = open(file_path)                      #פתיחת הקובץ לקריאה עם מילים לניחוש
    content = read_txt.read()                       #הכנסת הרשימה למשתנה
    all_words = content.split(" ")                  #הפרדת הקובץ למילים בתוך מערך/רשימה
    unique_words = list(dict.fromkeys(all_words))   #ביטול הכפילויות ע"י הפיכת המערך למילון,ואח"כ הפיכת המילון לרשימה
    print(unique_words)                             #הדפס את המערך/רשימה
    length_unique = len(unique_words)               #כמות המילים ברשימה
    print(length_unique)                            #הדפסת האורך של הרשימה -ללא כפילויות
    #print(all_words[index-1])                       #הדפסת המילה במיקום המסויים
    times_circle = index%(len(all_words))
    the_word = all_words[times_circle-1]
    print("the word is : ",the_word)
    print("x :",times_circle)
    return(length_unique,the_word)

choose_word("./words_to_guess.txt",-1)               #הפונקציה מקבלת את הנתיב ואת מיקום המילה שתנוחש ע"י המשתמש
