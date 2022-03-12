#הפונקציה סופרת כמה פעמים המוצר קיים
#משימה 4
# def M_4():
hofaot=0
mikum=0
items=input("Please Type What Do You Want to Buy: ")
splittedItems=items.split(',')
ques2=input("How Many Times the Item Appears in the List ?")
for x in splittedItems:
    if ques2 == splittedItems[mikum] :
        hofaot+=1
        mikum+=1
    else:
        mikum+=1
print(ques2," appears",hofaot, "times")
# print(M_4())