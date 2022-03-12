def M_6():
    items=input("Please Type What Do You Want to Buy: ")
    splittedItems=items.split(',')
    ques4=input("What Item do you Want to Add ? ")
    splittedItems.append(ques4)
    return splittedItems
print(M_6())