#הנדסה אנליטית
#אורך קטע
# import math
# def distance(point1,point2):
#     a=list(point1)
#     b=list(point2)
#     d=math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
#     return d
# print(distance((3,8),(10,2)))

#*********************************************
#אמצע קטע
# import math
# def middle(point1,point2):

#     a=list(point1)
#     b=list(point2)
#     midx=(a[0]+b[0])/2
#     midy=(a[1]+b[1])/2
#     return midx,midy

# print(middle((3,8),(10,2)))

#*********************************************
#שיפוע
# import math
# def incline(point1,point2):

#     a=list(point1)
#     b=list(point2)
#     inc=(a[1]-b[1])/(a[0]-b[0])
#     return inc

# print(incline((4,8),(10,2)))

#*********************************************
#משוואת ישר
# import math
# def line_equation(point1,point2):

#     a=list(point1)
#     b=list(point2)
#     inc=(a[1]-b[1])/(a[0]-b[0])
#     n=a[1]-a[0]*inc
#     print("y=",inc,"x+",n)

#print(line_equation((4,8),(3,8)))


#*********************************************
#הנדסה אנליטית
#היקף משולש
# import math
# def perimeter(point1,point2,point3):
#     a=list(point1)
#     b=list(point2)
#     c=list(point3)
#     dab=math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
#     dac=math.sqrt(math.pow(a[0]-c[0],2)+math.pow(a[1]-c[1],2))
#     dbc=math.sqrt(math.pow(b[0]-c[0],2)+math.pow(b[1]-c[1],2))
#     peri=dab+dac+dbc
#     return peri
# print(perimeter((3,8),(10,2),(12,-2)))

#*********************************************************
#משוואה ריבועית
# import math
# def sqr_equation(a,b,c):
#     x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/2
#     x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/2
#     return x1,x2
# print(sqr_equation(1,-10,21))

#*********************************************************
#משוואת מעגל בהינתן נקודת מרכז מעגל ורדיוס
# import math
# def circle(center,radius):
#     a=list(center)
#     radius2=math.pow(radius,2)
#     print("(x-",a[0],")^2+(y-",a[1],")^2 = ",radius2)
# circle((3,4),5)

#*********************************************************
#משוואת מעגל בהינתן נק' מרכז מעגל ונקודה על המעגל
# import math
# def circle(center,point_on_circle):
#     a=list(center)
#     b=list(point_on_circle)
#     radius2=(math.pow(a[0]-b[0],2))+(math.pow(a[1]-b[1],2))
#     print("(x-",a[0],")^2+(y-",a[1],")^2 = ",radius2)
# circle((-3,4),(0,8))



pressed=input("Which Equation do You Want to Use :  "  )
if pressed=="1":                                    # משוואה ריבועית
    import math
    def sqr_equation(a,b,c):

        x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/2
        x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/2
        return x1,x2

    print(sqr_equation(1,-10,21))

elif pressed == "2":                                #אורך קטע
    import math
    def distance(point1,point2):

        a=list(point1)
        b=list(point2)
        d=math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
        return d

    print(distance((3,8),(10,2)))

elif pressed == "3":                                #אמצע קטע
    import math
    def middle(point1,point2):

        a=list(point1)
        b=list(point2)
        midx=(a[0]+b[0])/2
        midy=(a[1]+b[1])/2
        return midx,midy

    print(middle((3,8),(10,2)))

elif pressed == "4":                                #שיפוע
    import math
    def incline(point1,point2):

        a=list(point1)
        b=list(point2)
        inc=(a[1]-b[1])/(a[0]-b[0])
        return inc

    print(incline((4,8),(10,2)))