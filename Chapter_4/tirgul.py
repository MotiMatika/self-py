txt=input("please enter a string : ")      #קלט של מחרוזת
First_Letter = txt[0]
print(First_Letter)
Last_Letter = txt[-1]
print(Last_Letter)
if First_Letter ==  Last_Letter:
    print("OK")
elif (First_Letter+1) == (Last_Letter-1):
    print("OK")
else:
    print("NOT")
