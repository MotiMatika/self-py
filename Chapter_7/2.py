def M_2():
    items=input("please type what do you want to buy: ")
    splittedItems=items.split(',')
    num_comma=items.count(",")+1
    print("there are ",num_comma," items in your list")
M_2()