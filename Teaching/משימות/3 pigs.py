briks=input("enter 3 digits - each for one pig "  )      #הכנסת מספר תלת ספרתי
pig1=int(int(briks)/100)                                 #הפרדת ספרת המאות שמציינת את מספר הלבנים שאסף חזיר ראשון
pig2=int((int(briks)/10-pig1*10))                        #הפרדת ספרת העשרות שמציינת את מספר הלבנים שאסף חזיר שני
pig3=int(briks)-(pig1*100+pig2*10)                       #הפרדת ספרת האחדות שמציינת את מספר הלבנים שאסף חזיר שלישי
sum=pig1+pig2+pig3                                       #חישוב סכום הלבנים שאספו שלשת החזירים
print("sum of briks collected :",sum)                    #הדפסת הסכום
get=int(sum/3)
print("each pig gets :", get," briks")                   #חלוקה שווה של הלבנים - ללא שארית
spare=sum-get*3
print("spare of brick after dividing :",spare)           # פלט לשארית שנותרה לאחר החלוקה
x=True
x=spare==0                                               #בודק האם יש שארית.שאלתי האם השארית שווה לאפס
print(x)                                                 #פלט של השאלה תלוי בסכום הלבנים
