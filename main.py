
# Welcoming the user
def welcome() :
    print("*********Welcome Satran billing system*********")
    global sn 
    sn = input("Enter the name of your Shop:")
    chose()
        
# initialising
def chose():
    o = int(input("Enter 0 to exit and 1 to create a bill:"))
    if o==0:
        print("\t\t****Thank you for using us****")
        exit()
    else:
        add()
    
# Function of adding the details
def add():
    name = input("Enter the Name of the customer:")
    item = input("Enter the name of the item:")
    items = []
    items.append(item)

    price = int(input("Enter the Price of the item:"))
    prices = []
    prices.append(price)
    cont = input("Do you want to add more items(Y/N):")
    if cont=="Y":
        append(items,prices,name)
    elif cont=="N":
        display(items,prices,name)
def append(items,prices,name):
    item = input("Enter the name of the item:")
    items.append(item)
    
    price = int(input("Enter the Price of the item:"))
    prices.append(price)

    cont = input("Do you want to add more items(Y/N):")
    if cont=="Y":
        append(items,prices,name)
    elif cont=="N":
        display(items,prices,name)



    
# Displaying the invoice
def display(items,prices,name):
    print(f"\t\t {sn}")
    print("")
    print(f"\t\tName:{name}")
    tp = 0
    li = len(prices)
    for i in range(li):
        print(f"\t\t{items[i]}:Rs.{prices[i]}")
        p = prices[i]
        tp = tp+p
        
    print(f"\t\tTotal:Rs.{tp}")
    print("\t\t****Thank you for using us****")
    exit()

#main program
welcome()




        
