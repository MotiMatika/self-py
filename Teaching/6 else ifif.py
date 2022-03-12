                #התכנית מקבלת תו מהמשתמש ומודיעה אם התו נמצא או לא נמצא
#txt = "abcdef"                              #השמת מחרוזת קבועה 
#x=input("enter a letter ")                  # קלט-ניחוש האות ע"י המשתמש
#if x in txt:                                #בדיקה האם התו נמצא במחרוזת הקבועה
#	print("great",x," is in the word")      #פלט-אמת,אם התו נמצא
#else:                                       # אם התו לא נמצא... מ
#	print("sorry",x," isn't in the word")   #פלט- התו לא נמצא

#txt = "12345"                              #השמת מחרוזת קבועה 
#x=input("enter a number ")                  # קלט-ניחוש האות ע"י המשתמש
#if x in txt:                                #בדיקה האם התו נמצא במחרוזת הקבועה
#	print("great",x," is in the string")      #פלט-אמת,אם התו נמצא
#else:                                       # אם התו לא נמצא... מ
#	print("sorry",x," isn't in the string")





                    #התכנית מקבלת את גיל המשתמש ומודיעה על המוסד בו הוא נמצא
age =float( input("what is your age ?  "))
if  12 <= age <18:
	print("you are in high school")
elif 6 <= age <12:	
	print("you are in elemantary school")
elif 4 <= age < 6:	
	print("you are in kindergarden")
elif 0 <= age < 4:	
	print("you are too young ")
elif 18 <= age <=21:	
	print("you are a soldier ")
else:
	print("you are too old ")
	
	                #השפעת טיפוס הערך שהמשתמש מקליד על הפלט
#x=input("enter number or string:")
#print(x)
#y=x+4           	 # נקבל שגיאה כי וואי לא מוגדר לקבל ערך שלא הוגדר
#y=int(x)+4          # זו כתיבה נכונה
#print(y)            #פלט-הסכום עם 4

#התכנית בודקת אם הקלט הוא מספר או מחרוזת ===לא סיימתי
#x=input("enter number or string:")
#print(x)
#if הקלט מסוג מספר או מחרוזת
#y = x+4            	# נקבל שגיאה כי וואי לא מוגדר לקבל ערך שלא הוגדר
#y=int(x)+4          # זו כתיבה נכונה
#print(y)            #פלט-הסכום עם 4



                             #התכנית מקבלת מספר מהמשתמש,ומוציאה הודעה האם הוא קטן/גדול או שווה ל 10 
#print("Choose a Number ",)                        # פלט - הודעה
#choice1 = int(input("What is Your Choice?  "))    #קלט של מספר מהמשתמש
#x=10                                              # השמת ערך בתא איקס
#if choice1 > x:                                   #אם המספר שהקליד המשתמש גדול מ 10 ... אז
#	print("your number is bigger than ",x)         # פלט-המספר שבחרת גדול מ 10
#elif choice1 < x:                                 #אחרת- אם המספר שהקליד המשתמש קטן מ 10 ... אז
#	print("your number is smaller than ",x)        #פלט-המספר שבחרת קטן מ 10
#else:                                             # אחרת
#	print("your number is equal to ",x)            # פלט-המספר שהמשתמש הקליד שווה ל 10
	
	                         #התכנית מקבלת תו מהמשתמש ומוציאה הודעה האם הוא קטן/גדול או שווה לג'יי
#print("Choose a letter ",)                         # פלט - הודעה
#choice1 = (input("What is Your Choice?  "))        #קלט של תו מהמשתמש 
#x=("j")                                            # השמה של תו לתא ג'יי
#if choice1>x:                                      #אם התו שהקליד המשתמש גדול מג'יי ...אז
#	print("your letter is bigger than ",x)         #פלט-התו שבחרת גדול מג'יי
#elif choice1<x:                                    #אחרת-אם התו שהקליד המשתמש קטן מג'יי... אז
#	print("your letter is smaller than ",x)        #פלט-התו שבחרת קטן מג'יי
#else:                                              #אחרת
#	print("your letter is the same as ",x)	       #פלט-התו שבחרת זהה לג'יי

                             #התכנית מקבלת שני מספרים ומוציאה הודעה מי מהם קטן/גדול מהאחר או שווה לו
#print("Choose a Number ")                         # פלט - הודעה
#choice1 = int(input("What is Your Choice?  "))    #קלט - מספר
#print("Choose another Number ")                   #פלט - הודעה
#choice2 = int(input("What is Your Choice?  "))    #קלט - מספר
#if choice1 == choice2:                            #בדיקה הם המספרים שווים
#	print("You Chose the same number")             #אם כן-פלט המספרים שווים
#elif choice2 < choice1:                           #אחרת-אם המספר השניקטן מהראשון
#	print("Your first number is bigger")           #פלט-המספר הראשון גדול יותר 
#elif choice2 >choice1:	                           #אחרת-אם השני גדול יותר
#	print("Your second number is bigger")          #פלט-המספר השני גדול יותר

                        #התכנית מקבלת מספר ומוציאה הודעה מה הוא
#print("Choose a Number Between 1-3")              # פלט - הודעה
#choice = int(input("What is Your Choice?  "))     #קלט מספר
#if choice == 1:                                   #אם הקלט שווה ל 1
#	print("You Chose 1.")                          #פלט-בחרת את המספר 1
#elif choice == 2:                                 #אחרת-אם הקלט שווה ל 2
#	print("You Chose 2.")                          #פלט-בחרת את המספר 2
#elif choice == 3:	                               #אחרת-אם הקלט שווה 3
#	print("You Chose 3.")                          #פלט-בחרת את המספר 3
#else:                                             #אחרת
#	print("You Chose Something Else")              #פלט-בחרת מספר אחר	

                        #התכנית מקבלת תו ומוציאה הודעה מה הוא
#print("Choose a Letter Between a-c")              # פלט - הודעה
#choice = str(input("What is Your Choice?  "))     #קלט מטיפוס מחרוזת
#if choice == "a":                                 #אם הקלט הוא התו איי
#	print("You Chose a.")                          #פלט-בחרת איי
#elif choice == "b":                               #אחרת-אם הקלט הוא בי
#	print("You Chose b.")                          #פלט-בחרת בי
#elif choice == "c":	                           #אחרת-אם בחרת סי
#	print("You Chose c.")                          #פלט-בחרת סי
#else:                                             #אחרת
#	print("You Chose Something Else")              #בחרת תו אחר

                              #AND  OR
#x = input("enter the first  number : ")
#y = input("enter the second number : ")
#z = input("enter the third  number : ")

#if x>y and x>z:
#	print("the greatest number is  :",float(x))
#elif y>x and y>z:
#	print("the greatest number is  :",float(y))	
#else:
#	print("the greatest number is  :",float(z))
#print("the sum is :           ",float(x)+float(y)+float(z))
#print("the multiply is :      ",	float(x)*float(y)*float(z))

#print("Choose a Number ",)
#choice1 = int(input("What is Your Choice?  "))
#x=10
#if choice1>x:
#	print("your number is bigger than ",x)
#elif choice1<x:
#	print("your number is smaller than ",x)
#else:
#	print("your number is equal to ",x)	
	
	
print("Choose a letter ",)
choice1 = (input("What is Your Choice?  "))
x=("j")
if choice1>x:
	print("your letter is bigger than ",x)
elif choice1<x:
	print("your letter is smaller than ",x)
else:
	print("your letter is the same as ",x)	



#print("Choose a Number ")
#choice1 = int(input("What is Your Choice?  "))
#print("Choose another Number ")
#choice2 = int(input("What is Your Choice?  "))
#if choice1 == choice2:
#	print("You Chose the same number")
#elif choice2 < choice1:
#	print("Your first number is bigger")
#elif choice2 >choice1:	
#	print("Your second number is bigger")


#print("Choose a Number Between 1-3")
#choice = int(input("What is Your Choice?  "))
#if choice == 1:
#	print("You Chose 1.")
#elif choice == 2:
#	print("You Chose 2.")
#elif choice == 3:	
#	print("You Chose 3.")
#else:
#	print("You Chose Something Else")	


#print("Choose a Letter Between a-c")
#choice = str(input("What is Your Choice?  "))
#if choice == "a":
#	print("You Chose a.")
#elif choice == "b":
#	print("You Chose b.")
#elif choice == "c":	
#	print("You Chose c.")
#else:
#	print("You Chose Something Else")