#TESTED
#הפונקציה מוחקת מוצר מהרשימה לפי בקשת המשתמש
#משימה 5
def M_5():
    items=input("Please Type What Do You Want to Buy: ")
    splittedItems=items.split(',')
    ques3=input("What Item do you Want to Delet ? ")
    mikum=0
    for x in splittedItems:
        if ques3 == splittedItems[mikum] :
            splittedItems.pop(mikum)
        else:
            mikum+=1
    return(splittedItems)
print(M_5())