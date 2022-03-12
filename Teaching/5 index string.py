#word=str(input("enter a word  "))  #קלט של מחרוזת
#print(word[0])                     # פלט - התו הראשון משמאל
#print(word[-2])                    #פלט-התו השני מימין

#Word=input("Enter a String  ")    #קלט של מחרוזת
#print(Word[0:2])                  #יציג את האות במקום הראשון וגם השני
#print(Word[0:5:2])                #ללא קשר לאורך המחרוזת,יחתוך עד מיקום 5 וירשום קפיצות של 2
#print(Word[:])                    #הצגת כל המחרוזת
#print(Word[::4])                  #לא קשר לאורך המחרוזת,פלט של האות במקום האפס ובקפיצות של 4
#print(Word[::1])                  #ללא קשר לאורך הקלט - הצגת כל האותיות- כי הקפיצה ב1
#print(Word[1:3])                  #יציג את האות במיקום 1  וגם 2
#print(Word[::-1])                 #יציג את המחרוזת הפוכה-מימין לשמאל ללא דילוגים כי מינוס 1
#print(Word[-2::-4])               #יתחיל מהמקום השני מימין ,ירשום אותו וידלג כל ארבעה מקומות
#print(Word.find('12'))            #יחפש את הצירוף המצויין.אם ימצא,יציין את המיקום ההתחלתי.אם לא - ירשום מינוס 1

#encrypted_message="lxgxnxixcxixlxsx xnxoxhxtxyxpx xgxnxixnxrxaxexlx xmxax xi" #הכנסת צופן
#print(encrypted_message[-1::-2])                                           # כל אות שנייה מימין לשאל נחשפת ומתקבל משפט

#encrypted_message="lxgxnxixcxixlxsx xnxoxhxtxyxpx xgxnxixnxrxaxexlx xmxax xi" #הכנסת צופן
#x=len (encrypted_message)                                                     #ספירת תווים במחרוזת
#print(x) 		                                                               #פלט של מספר התווים במחרוזת

#encrypted_message="mxxoxxtxxixx xxyxxaxxixxr"     #הכנסת צופן
#print(encrypted_message[0::3])                    # חשיפת הקוד בקפיצות של 3 תווים מהמקום הראשון ועד לסוף המחרוזת

#encrypted_message="mxxoxxtxxixx xxyxxaxxixxr"      #הכנסת צופן
#x=len (encrypted_message)                          #ספירת כמות התווים בקוד
#print("Your Code is : ",x,"Charecter Long")        #פלט הודעה של כמות התווים
#print("The Code is :",encrypted_message[0::3])     #פלט - חשיפת הקוד







#3.4.2

#                              #לזהות מהו התו הראשון ולהחליפו ב אי
# txt=input("please enter a string : ")   #קלט של מחרוזת
# tav1=txt[0]                             #זיהוי התו הראשון
# x=txt[1:]                               #המחרוזת ללא התו הראשון
# y=tav1+x.replace(tav1,"e")              #צירוף התו הראשון והחלפת כל התווים שבהמשך לאות אי
# print(y)
# #פלט-המחרוזת שכלה מופעים של התו הראשון,יתחלפן לאי חוץ מהתו הראשון






#3.4.3
#קליטת מחרוזת,חלוקתה לשניים .מחצית ראשונה אותיות קטנות ומחצית שניה אותיות גדולות
#אם מספר האותיות אינו זוגי,החלק הראשון יהיה קטן יותר

# txt=input("please enter a string : ")                                  #קלט של מחרוזת
# count_num = len(txt)                                                   #אורך המחרוזת
# half1 = count_num//2                                                   #מונה את מספר התווים בחצי הראשון של המחרוזת
# print("you typed a string with :", count_num, "letters")               #פלט-מציין את אורך המחרוזת
# half2 = count_num-half1                                                #מחשב את מספר התווים במחצית השניה
# print ("the 1st half of your string is  :",int(half1),"letter(s)")     #פלט - כמה אותיות בחצי הראשון
# print ("the 2nd half of your string is  :",int(half2),"letter(s)")     #פלט- כמה אותיות בחצי השני
# half11 = txt[:half1]                                                   #מעתיק את המחצית הראשונה
# half12 = txt[half1:]                                                   #מעתיק את המחצית השניה
# print(half11.lower() + half12.upper())                                 #הופך את המחצית הראשונה לאותיות קטנות ואת המחצית השניה לאותיות גדולות
                                                                       #ומצמיד את 2 החצאים



#3.5.2
# txt=input("please enter a word : ")                                  #קלט של מחרוזת
# count_num = len(txt)                                                 #אורך המחרוזת
# print("_ " * count_num)

#3.5.1
txt=input("please enter a string : ")      #קלט של מחרוזת
print(txt.lower())
l1=list(txt)                       #ממיר כל אות שנקלטת ל אות קטנה
print(l1.sort())







# l1=input(" enter a list : ")      #קלט של מחרוזת




