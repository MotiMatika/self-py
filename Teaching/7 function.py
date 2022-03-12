                                            #פונקציות
# def moti():          #הגדרת הפונקציה עם שם
# 	print("wow")     # מה הפונקציה תבצע
# #moti()              #קריאה לפונקציה לבצע


# def squre(number):             #הגדרת הפונקציה עם שם ופרמטר
# 	print(number**2)           #הפונקציה תעלה בריבוע מספר שנקליד
# #squre(3)                      #הפונקציה מקבלת את הפרמטר 3

#def mystery(index):           #הגדרת הפונקציה עם שם ופרמטר
#    print("z" * len(index))   #פלט - כתיבת האות זד כאורך המחרוזת שתקבל,כי לן מתכוון רק למחרוזת
#mystery("111111")             # מוכנס לפרמטר מחרוזת באורך 6 תווים-הפלט יהיה האות זד נכתבת 6 פעמים ברצף
#func = mystery                #משתנה פנק שמקבל את הפונקציה מיסטרי
#func("python")                #מחרוזת באורך 6 תוים-הפלט יהיה האות זד 6 פעמים
	
	              #התכנית בוחרת באופן אקראי אחת משלש המילים
#import random                                # קריאה לספריה רנדום                      
#def pick_a_fruit():                          # הגדרת פונקציה 
#	fruit_list = ["banana","apple","orange"]  #הכנסת 3 מחרוזות מהן תיעשה הבחירה
#	print(random.choice(fruit_list))          #פלט-אחת משלש המחרוזות
#pick_a_fruit()                               #קריאה לפונקציה

                              #תכנית שמחשבת סכום של 2 מספרים
#def cal(n,j):                        #הגדרת פונקציה עם 2 פרמטרים
#	x = n+j                           #הסכום נכנס לתא איקס
#	return x                          #הפונקציה מחזירה את ערך איקס
#t=cal(5,7)                           #השמת ערכים לפרמטרים וכל הפונקציה נכנסת לתא טי
#print(t)                             #פלט-הסכום

                                             #תכנית שמחשבת שורשים של משוואה ריבועית
#import math                               #קריאה לספריית מאט
#def mishvaa_ribuit(a,b,c):                #הגדרת פונקציה עם שלשה פרמטרים
#	x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)  #הנוסחה לשורש הראשון
#	x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)  #הנוסחה לשורש השני
#	return x1,x2                           #החזרת 2 השורשים
#a_b_c = mishvaa_ribuit(1,2,1)             #השמת ערכים לפרמטרים וכל הפונקציה נכנסת לתא אייביסי
#print (a_b_c)                             #פלט-2 השורשים

#def chocolate_maker(small, big, x):
#	result = int(((x-big*5)%small))
#	print(result)
#chocolate_maker(3,2,10)

#def last_early(my_str):        #ודקת אם התו האחרון מופיע גם קודם
#	q = my_str.lower()               #מחליף את כל האותיות במחרוזת לקטנות
#	last = q[-1]                     #התו האחרון במחרוזת נכנס לתא לאסט
#	last_b = q[-2::-1]               #כל התווים מהמקום השני מימין נכנסים לתא לאסטבי
#	if last in last_b:               #בודק אם התו האחרון מופיע גם קודם
#		print("True")                #אם כן- מדפיס כן
#	else:                            #אחרת
#		print("False")               #אם לא מופיע ,מדפיס לא
#last_early("X")

#התכנית מקבלת 3 מספרים שלמים ומוציאה אמת אם גם יש מרחק של 1 בין השניים האחרים וגם שאחד מהם רחוק מהאחרים יותר מ2
#def distance(num1, num2, num3):
#	if(abs(num2-num1) == 1 or abs(num3-num1) == 1)and (abs(num2-num1) >= 2 and abs(num2-num3) >= 2 or abs(num3-num1) >= 2 and abs(num3-num2) >= 2 ): 	
#		print("True")
#	else:	
#		print("False")
#distance(0,2,1)                    #פלט - שקר

                        #הגדרת פונקציה וקריאה לה
#def water():
#     fish_view = "I can only live within the water scope!"
#     print(fish_view)

#water()

                                #ההבדל בין משתנה גלובלי למשתנה לוקאלי
#a = 0                      # איי משתנה גלובלי
#def my_function():         #הגדרת פונקציה
#    a = 3                  #איי הוא משתנה לוקאלי
#    print(a)               # פלט ערך איי

#my_function()              # קריאה לפונקציה - שתדפיס את ערך איי הלוקאלי שלה
#print(a)                   #פלט-איי הגלובלי
                            #הפלט יהיה 2 שורות:הראשונה 3 מהפונקציה והשנייה 0 מהגלובלי
	
                           #שינוי ערך למשתנה גלובלי	
#d = 1                  #די הוא משתנה גלובלי
#def foo4():            #הגדרת פונקציה
#	global d            #קריאה למשתנה הגלובלי 
#	d = 2               #שינוי ערכו של המשתנה הגלובלי
#	print(d)            #פלט-של תא די 
#foo4()                 #פלט-הפונקציה
#print(d)	            #פלט-ערך המשתנה הגלובלי,ששינה את ערכו בתוך הפונקציה	

                        #שימוש בערך שהפונקציה מחזירה	 
#def add(num1, num2):    #הגדרת פונקציה
#	return num1 + num2   #חישוב הסכום
#sum = add(16,14)        #השמת2 המחוברים לתא סאם
#print(sum)              #פלט -הערך 30


#def add(num1, num2):    #הגדרת פונקציה
#	sum = num1 + num2
#	return sum           #חישוב הסכום
#add(16,14)              #השמת2 המחוברים לתא סאם
#print (sum)           

                  #שימוש בפונקציה מיין
def a():                    #הגדרת פונקציה 
	print("moti")           #
	
def b():                    #הגדרת פונקציה
	print("yair")           #
	
def c():                    #הגדרת פונקציה
	print("is a teacher")   
	           
def moti():          #הגדרת הפונקציה עם שם
	print("wow")     # מה הפונקציה תבצע
   

def squre(number):             #הגדרת הפונקציה עם שם ופרמטר
	print(number**2)           #הפונקציה תעלה בריבוע מספר שנקליד
		
def main():                 #הגדרת הפונקציה מיין שמכילה את כל הפונקציות שרוצים להריץ
	a()                     #הפונקציה איי
	b()                     #הפונקציה בי
	c()                     #הפונקציה סי
	moti()                  #הפונקציה מוטי
	squre(4)                #הפונקציה סקוור עם פרמטר 4 שיעלה בריבוע
	
if __name__ == "__main__":  #תחביר מורכב לביצוע כל 5 הפונקציות שכלולות במיין
	main()                  #קריאה לפונקציה מיין שתבצע את עצמה


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



def a(old_gussed_letters,secret_word):
    x = len(old_gussed_letters)

def b(old_gussed_letters,secret_word):
    z = old_gussed_letters.count("b")

def c(old_gussed_letters,secret_word):	
    y = len(secret_word)

def d(old_gussed_letters,secret_word):
    t = secret_word.capitalize()

def main():                 #הגדרת הפונקציה מיין שמכילה את כל הפונקציות שרוצים להריץ
	a()                     #הפונקציה איי
	b()                     #הפונקציה בי
	c()                     #הפונקציה סי
	d()                  #הפונקציה מוטי
	                #הפונקציה סקוור עם פרמטר 4 שיעלה בריבוע
	
if __name__ == "__main__":  #תחביר מורכב לביצוע כל 5 הפונקציות שכלולות במיין
	main()                  #קריאה לפונקציה מיין שתבצע את עצמה






    #return x,y,z,t
    
print(li(["c","b","p","c"],"moti yair"))  










