#הפונקציה מדפיסה את כל המוצרים שאינם חוקיים
# מוצר אינו חוקי אם אורכו קטן מ-3 או שהוא כולל תווים שאינם אותיות
#משימה 7
def M_7():
    items=input("Please Type What Do You Want to Buy: ")
    splittedItems=items.split(",")
    for x in splittedItems:
        length_item=len(x)
        if length_item > 3 and x.isalpha():
            continue
        else:
            print(x)
M_7()