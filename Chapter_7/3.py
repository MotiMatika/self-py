#הפונקציה קולטת את המוצרים ומאפשרת למשתמש לבדוק אם קיים מוצר כלשהו ברשימה

def M_3():
    items=input("Please Type What Do You Want to Buy: ")
    splittedItems=items.split(",")
    ques1=input("Is the Item is in the List ?")
    if ques1 in splittedItems:
        print("Yes",ques1,"is in the List")
    else:
        print("No",ques1,"isn't in the List")
M_3()