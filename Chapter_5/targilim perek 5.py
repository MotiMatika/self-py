                                                              # 5.3.5
								# התכנית מקבלת שלשה מספרים ומחזירה אמת אם מתקיימים 2 התנאים
								# תנאי ראשון: אחד המספרים השני או השלישי  קרוב מרחק יחידה באופן אבסולוטי מהמספר הראשון
								# תנאי שני: אחד המספרים השני או השלישי רחןק מרחק שתי יחידות מהמספר הראשון

# def distance(num1,num2,num3):                  #הגדרת הפונקציה
# 	a = abs(num2-num1)                          #המרחק בין הראשון לשני
# 	b = abs(num3-num1)                          #המרחק בין הראשון לשלישי
# 	c = abs(num3-num2)                      	#המרחק בין השני לשלישי
# 	if  (a == 1 or b == 1) and ((b >= 2 and c >= 2) or(a >= 2 and c >= 2)):
# # השוואת המרחקים בין בערכים לפי תנאי המשימה
# 		return True                           #פלט - באם התנאים מתקיימים
# 	else:                                       #אחרת
# 		return False                          #פלט-באם התנאים לא מתקיימים

# distance(0,2,1)                                #קריאה לפונקציה עם השמת ערכים








#                                                            #5.3.6
# def filter_teens(a=13, b=13, c=13):                                     # הגדרת הפונקציה והשמת ערך ברירת מחדל
# 	a = fix_age(a)                                                      #קריאה לפונקציה שמתקנת והשמת הערך הראשון
# 	b = fix_age(b)                                                      #קריאה לפונקציה שמתקנת והשת הערך השני
# 	c = fix_age(c)                                                      #קריאה לפונקציה שמתקנת והשמת הערך השלישי
# 	sum = a+b+c                                                         # סכום הערכים נכנס לתא סאם
# 	#print(sum)                                                          # פלט-סכום שלשת הערכים
# 	return sum
#                                                                         # הפונקציה מקבלת גיל ומתקנת אותו אם צריך
# def fix_age(age):                                                       #הפונקציה המתקנת מקבלת ערך
# 	if (age >= 13 and age <= 19 and age != 15 and age != 16):           #בודקת את התנאים
# 		newAge = 0                                                      #מאפסת -אם צריך
# 	else:                                                               #אחרת
# 		newAge = age                                                    #משאירה את הערך - אם לא צריך לאפסו
# 	return newAge                                                       #מחזירה את הערך של הערך

# def main():                                                             #הגדרת הפונקציה מיין
#     #filter_teens()                                                      #קריאה לפונקציה פילטר טינס מתוך הפונקציה מיין

# if __name__ == "__main__":                                              #סיומת שמורה לשימוש בפונקציה מיין
	# main()




# הפונקציה מקבלת את מספר הקוביות הקטנות,הגדולות ואורך השורה ובודקת אם ניתן לשלבן
# def choclate_maker(small,big,x):

#		five=x//(big*5)
#		spare=x-five*5
#		print("in a row of", x," there is a place for :" ,five, "times of 5 and ",spare ,"times of 1")
# choclate_maker(3,1,9)

	# הפונקציה מקבלת את מספר הקוביות הקטנות,הגדולות ואורך השורה ובודקת אם ניתן לשלבן בדיוק
	# יש ריבועים של יחידה ויש  באורך של 5
# def chocolate_maker(small,big,x):         #הגדרת הפונקציה

#	y=x-big*5                             #כמות המקומות פחות כמות החמישיות
#	if y==0:                              #אם האורך מתחלק בדיוק ל 5
#		print("True")                     #פלט - ניתן להשתמש רק בחמישיות
#	else:                                 #אחרת
#		calc=1*small+5*big                #חישוב כמות החמישיות והיחידות לתא קאלק
#		print(calc==x)                    #בדוק אם אורך השורה וסך כל הריבועים תואם

# chocolate_maker(5,5,17)                   #קריאה לפונקציה עם השמת ערכים






#                                                         # 5.3.7
#                                          # הפונקציה מקבלת את מספר הקוביות הקטנות,הגדולות ואורך השורה ובודקת אם ניתן לשלבן בצורה כלשהיא
# def chocolate_maker(small,big,x):         #הגדרת הפונקציה

# 	if big>0 and x>0:                     #ווידוא ערכים הגיוניים
# 		spare_five = x%5                  # שארית החילוק ב 5
# 		if spare_five > small:            #אם השארית גדולה מהקטן - לא ניתן
# 			return False               #פלט
# 		else:                             #אחרת
# 			return True                #פלט
# 	else:                                 #אחרת
# 		return False                    #פלט

# chocolate_maker(8,1,0)                    #קריאה לפונקציה עם השמת ערכים



# #                                            # 5.4.1
# def func(a, b):                #הגדרת הפונקציה עם 2 משתנים
#     """declare function"""       #תיעוד
#     x = a*b                      #הכפלת הערכים לתוך איקס
#     """multiply a with b"""      #תיעוד
#     y = x*4                      #פעולה נוספת לתוך וואי
#     """multiply x with 4"""      #תיעוד
#     return y                     #החזרת הערך וואי
#     print(y)                     #הדפסת הערך וואי

# def main():                    #הגדרת הפונקציה מיין
#     func(4,5)                 #קריאה לפונקציה פילטר טינס מתוך הפונקציה מיין

# if __name__ == "__main__":     #סיומת שמורה לשימוש בפונקציה מיין
#     main()
#     help (func)



#5.3.4
# def last_early(my_str):            #הגדרת פונקציה
# 	x = my_str.lower()             #מחרוזת באותיות קטנות
# 	end = x[-1]                    #אות אחרונה לתא אנד
# 	rev = x[:-1]                   #כל השאר לתא רוו
# 	if end in rev:                 #בדיקה אם האות האחרונה נמצאת גם לפני
# 		return True                #החזר אמת
# 	else:                          #אחרת
# 		return False               #החזר שקר
# print(last_early("wbsa"))          #פלט-הדפס את תוצאת הפונקציה






                                    #5.5.1

#התכנית בודקת אם הוכנסה יותר מאות אחת או הוכנס תו שהוא לא אות
# def is_valid_input(letter_guessed):       #הגדרת הפונקציה
# 	x = letter_guessed.isalpha()            #בדיקה באם כל התווים הם אותיות
# 	num = len(letter_guessed)               #אורך המחרוזת נכנס לתא נאם
# 	if num == 1 and x == True:              #אם גם הולדה אות אחת וגם היא אות ולא משהו אחר
# 		return True                         #החזר אמת
# 	else:                                   #אחרת
# 		return False                        #החזר שקר
# print(is_valid_input("!"))                #פלט-הדפס את תוצאת הפונקציה

















