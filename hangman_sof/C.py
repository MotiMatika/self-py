#6.4.1
def check_valid_input(letter_guessed,old_letter_guessed):
    char = letter_guessed.isalpha()         
    num = len(letter_guessed)  
    if num == 1 and char == True and letter_guessed.isascii() and letter_guessed not in old_letter_guessed:
        return True
    else:
        return False 
print(check_valid_input("a",["b","w"]))




#6.4.1 - check1
#def check_valid_input(letter_guessed, old_letters_guessed):
#הפונקציה בודקת אם הוכנסה יותר מאות אחת או הוכנס תו שהוא לא אות
# def is_valid_input(letter_guessed):         #הגדרת הפונקציה
# 	x = letter_guessed.isalpha()            #בדיקה באם כל התווים הם אותיות
# 	num = len(letter_guessed)               #אורך המחרוזת נכנס לתא נאם
# 	if num == 1 and x == True:              #אם גם הוקלד תו אחד וגם הוא אות ולא משהו אחר
# 		return True                         #החזר אמת
# 	else:                                   #אחרת
# 		return False                        #החזר שקר
# print(is_valid_input("8"))