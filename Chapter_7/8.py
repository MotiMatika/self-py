#הפונקציה מוחקת כפילויות
#משימה 8
#TESTED
def M_8():
    items=input("Please Type What Do You Want to Buy: ")
    splittedItems=items.split(',')
    new_items = []

    def isInArray(item, array):    #הגדרת פונקציה שבודקת אם אובייקט נמצא ברשימה ומחזירה אמת -אם נמצא או שקר-אם לא נמצא
        result = item in array     #משתנה ריזולט שמקבל אמת או שקר
        return result              #החזרת התוצאה של הפונקציה

    for item in splittedItems:
        if(isInArray(item, new_items)):    #בודקת אם המוצר נמצא כבר ברשימה המעודכנת
            continue                       #אם נמצא , מתעלמת
        else:                              #אם לא נמצא
            new_items.append(item)         #מעדכנת את הרשימה

    return(new_items)                       #הדפס את הרשימה המעודכנת
print(M_8())