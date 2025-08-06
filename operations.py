from datetime import datetime
def displayingStock(nl):
    """
    function: It is used to give id to each product and display contact details and loctaion.
    parameters: nl list (a list where each inner list contains product details)
    returns: none
    """
    item_id=1                       #declaring a new variable and assigning a value to it
    for each in (nl):               #to access the 2D list
        print(item_id,end="\t")     #to give id for each product
        for j in each:
            print(j,end="\t")       #print method had \n as a default so end with \t
        print()                     #to go to a new line so that all of the elements doesnot stay in the same line
        item_id=item_id+1           #to increase the id number
    print("_"*70)                   #puts 70 underscores "_" after the table
                                    #/t helps to fix the position of the element and \n helps to print in a new line
    print("\n\t\t\t\t\tContact Us: 981846534\n\t\t\t\t\tLocation: Budhanilkantha\n\t\t\t\t\tPhone: 01-4373542")

def displaying_user(nl):
    """
    function: It is used to iterate and convert the price from wholesale price to retail price
              and display the details of the products to the user
    parameters: nl list (a list where each inner list contains product details)
    returns: none
    """
    item_id=1
    for i in range(len(nl)):    
        print(item_id,end="\t")
        for j in range(len(nl[i])):
            if j==3:
                print(int(nl[i][j])*2,end="\t")             #converting wholesale price to retail price
            else:
                print(nl[i][j],end="\t")
        print("\n")
        item_id=item_id+1
    print("_"*69)

def access_values(nl,item_input_id):
    """
    function: It is used to access the values from the list and store in a new variable
    parameters: nl list and item_input_id
    returns: total_quantity_of_selected_item and item_name
    """
    '''if the user inputs id 2 then the product is at index
        1 therefore, to get access to that product -1 is done'''
    total_quantity_of_selected_item=nl[item_input_id-1][2]  #accessing the total quantity from the list
    item_name=nl[item_input_id-1][0]                        #accessing the name from the list
    return total_quantity_of_selected_item, item_name

def checking_free_items(nl,item_name,item_input_id,purchases):
    """
    function: In this function,number of quantity the customer wants to purchase is taken and validated
              then in a dictionary, the item name and input quantity is added. Free items is then calculated
              and total items with free items is calculated and if the total items with free items is less
              than 0 or greater than the total quantity in the list then an invalid request message is sent
    parameters: nl list(a list where each inner list contains product details),item name, item input id,
                purchases(a new dictionary made to add item name and quantity)
    returns: free items,total quantity with free items and item input id
    """
    #Taking the item quantity
    try_loop=True
    while try_loop==True:
        try:
            item_input_quantity=int(input("Enter the number of items that you want to purchase: "))
            if item_input_quantity<=0:
                print("Invalid input. Please enter a valid input.")
                try_loop=True
            else:
                try_loop=False
        except:
            print("Invalid input.")
            try_loop=True
    
    #if the item name is already present in the dictionary then the new input quantity is updated
    if item_name in purchases:
        purchases[item_name]=purchases[item_name]+item_input_quantity
        
    #else the name and quantity is added in the dictionary
    else:
        purchases[item_name]=item_input_quantity
        
    #calculating how much free items should be given according to the items purchased quantity
    for item, total_quantity in purchases.items():
        free_items=total_quantity//3

    #if the user inputs id 2 then the product is at index 1 therefore, to get access to that product -1 is done
    total_quantity_of_selected_item=nl[item_input_id-1][2]  #accessing the total quantity from the list
    total_quantity_with_free_items=item_input_quantity + free_items

    #continuing the loop until the user doesnot enter a valid number of quantity
    while item_input_quantity <= 0 or total_quantity_with_free_items > int(total_quantity_of_selected_item):
        print("The items input must be greater than 0 or within our stock quantity.")
        item_input_quantity=int(input("Enter the number of items that you want to purchase: "))
        free_items=item_input_quantity//3
        total_quantity_with_free_items=item_input_quantity + free_items
    print("Dear customer, Since purchasing 3 or more than 3 number of a specific products you get free items.\nYou have received ",free_items," free items.")    
    return free_items,total_quantity_with_free_items,item_input_quantity

def updating_stock(nl,item_input_id,total_quantity_with_free_items):
    """
    function: In this function the stock is updated after selling to the customer
    parameters: nl list, item_input_id, total_quantity_with_free_items
    returns: nl list (a list where each inner list contains product details),item_input_id
    """
    #updating the number of items after selling
    nl[item_input_id-1][2]= str(int(nl[item_input_id-1][2])-total_quantity_with_free_items)
    print("\n")
    return nl,item_input_id

def bill_calculation(nl,item_input_id,item_input_quantity,user_sell_items,free_items,total):
    """
    function: In this function,the bill is calculated and added
              in the user_sell_items list also total price is calculated
    parameters: nl list(a list where each inner list contains product details),item_input_id,
                item_input_quantity,user_sell_items,free_items,total
    returns: total,user_sell_items
    """
    item_name=nl[item_input_id-1][0]                #accessing the name from the list
    price_per_item=int(nl[item_input_id-1][3])*2    #changing the CP by multiplying by 2
    total_price=price_per_item*item_input_quantity  #total price for the products selected
                                                    #Storing the purchased items in a new list
    user_sell_items.append([item_name,item_input_quantity,free_items,price_per_item,total_price])
    total=total+total_price
    return total,user_sell_items

def shipping_price(shipping_cost,total):
    """
    function: In this function the user is asked if they want to ship their items or
              not and total price with shipping is calculated
    parameters: shipping_cost,total
    returns: shipping_cost,total_price_with_shipping
    """
    #asking the user if the user wants to ship their item
    print("Answer 'y' for yes or 'n' for no.")
    shipping_answer=input("Do you want to ship the items?:").lower()
    if shipping_answer=="y":
        shipping_cost=500
        
    #adding shipping price to total
    total_price_with_shipping=total+shipping_cost
    return shipping_cost,total_price_with_shipping

def display_stock_option2(nl,item_id):
    """
    function: In this function the product details is shown to the admin
    parameters: nl,item_id
    returns: none
    """
    for each in (nl):                               #to access the 2D list
        print(item_id,end="\t")                     #to give id for each product
        for j in each:
            print(j,end="\t")                       #print method had \n as a default so end with \t
        print()                                     #to go to a new line so that all of the elements doesnot stay in the same line
        item_id=item_id+1                           #to increase the id number
    print("_"*70)

def update_stock_in_list(restock_id,nl,restock_quantity):
    """
    function: In this function the current stock is updated in the list
    parameters: restock_id,nl,restock_quantity
    returns: nl list
    """
    #updating the current stock in the list
    nl[restock_id-1][2]=str(int(nl[restock_id-1][2])+restock_quantity)
    return nl

def restock_bill(restock_id,restock_quantity,nl,restock_list,restock_total):
    """
    function: In this function the values are accessed from the list and are appended in a new list
              the total money is also calculated here
    parameters: restock_id,restock_quantity,nl,restock_list,restock_total
    returns: restock_total,restock_list
    """
    restock_name=nl[restock_id-1][0]
    restock_price_per_item=int(nl[restock_id-1][3])
    total=restock_price_per_item*restock_quantity
    restock_total=restock_total+total
    restock_list.append([restock_name,restock_quantity,restock_price_per_item,total])
    return restock_total,restock_list

def enter_credentials():
    """
    function: In this function the credentials of the customer is taken and validated
    parameters: none
    returns: name,phoneNumber
    """
    print("-"*45)
    print("Enter your details for bill generation.")
    name=input("Enter the full name of the customer: ")                         #taking customer's details
    while name=="":
        print("Invalid input.")
        name=input("Enter the full name of the customer: ")
    phoneNumber=input("Enter the phone number of the customer: ")
    while len(phoneNumber)!=10:
        print("Invalid phone number. Enter 10-digit phone number.")
        phoneNumber=input("Enter the phone number of the customer: ")
    print("-"*50)
    return name,phoneNumber

def choose_option_input():
    """
    function: In this function the option chosen is validated
    parameters: none
    returns: option_input,try_loop
    """
    try_loop=False
    while try_loop==False:
        try:
            option_input= int(input("Enter the option you want to choose:"))   #choosing the option from the user
            try_loop=True
        except:
            print("Please enter a valid number.")
            try_loop=False
    return option_input,try_loop

def declaring_values():
    """
    function: In this function there are declarations only
    parameters: none
    returns: user_sell_items,total,final_total,shipping_cost,loop_sell,purchases
    """
    user_sell_items=[]                  #list where the purchased items are stored
    total=0                             #total bill amount without adding shipping amount
    final_total=0                       #final amount
    shipping_cost=0
    loop_sell=True
    purchases={}
    return user_sell_items,total,final_total,shipping_cost,loop_sell,purchases

def input_user_id(nl):
    """
    function: It is a function where an id is taken from the user and validated
    parameter: nl list
    returns: item_input_id
    """
    #Taking item Id from the consumer
    try_loop=False
    while try_loop==False:                  
        try:                                                        #if error occurs in try block the except is executed
            item_input_id=int(input("Please input the id of the product you want to purchase:  "))
            if item_input_id<=0 or item_input_id>len(nl):           #keep looping until user inputs a valid input
                print("Invalid input.")
                try_loop=False
            else:                                                   #if valid input, continue
                try_loop=True
        except:
            print("Invalid input.")
            try_loop=False
    return item_input_id

def purchase_more_items(loop_sell):
    """
    function: In this function a ans value is taken from the user which determines
              if the loop is continued or breaked
    parameters: loop_sell
    returns: loop_sell
    """
    print("Answer 'y' or 'yes' for continuing and answer 'n' or 'no' for discontinuing")
    answer=input("Do you want to purchase more items?:").lower()        
    if answer=="y" or answer=="yes":
        loop_sell=True
    elif answer=="n" or answer=="no":
        loop_sell=False
    else:
        print("\n")
        print("Invalid input.")
        loop_sell=False
    return(loop_sell)

def display_bill_details(user_sell_items,name,shipping_cost,total_price_with_shipping):
    """
    function: In this function the bill details is displayed by accessing the user_sell_items list
              and total price is also displayed
    parameters: user_sell_items,name,shipping_cost,total_price_with_shipping
    returns: name,user_sell_items,shipping_cost,total_price_with_shipping
    """
    #Displaying the details in bill in the console
    for i in range(len(user_sell_items)) :
        print(user_sell_items[i][0]+"\t\t"+str(user_sell_items[i][1])+"\t\t"+str(user_sell_items[i][2])+"\t\t$"+str(user_sell_items[i][3])+"\t\t$"+str(user_sell_items[i][4])+"\n")
    print("_"*90)
    print("Customer Name: ",name)
    if shipping_cost>0:
        print("Shipping Price: $"+str(shipping_cost))
    print("Total cost with shipping: $"+str(total_price_with_shipping))
    print("\n")
    return name,user_sell_items,shipping_cost,total_price_with_shipping

def option_two_declare():
    """
    function: In this function there are declarations of variables,list and date and time
    parameters: none
    returns: restock_total,current_date_and_time,restock_list,item_id,restock_loop
    """
    restock_total=0
    current_date_and_time = datetime.now()
    restock_list=[]
    item_id=1                                #declaring a new variable and assigning a value to it
    restock_loop=True
    return restock_total,current_date_and_time,restock_list,item_id,restock_loop

def restocking(nl):
    """
    function: In this function restock id and product quantity is taken and validated
    parameters: nl list
    returns: restock_id,restock_quantity
    """
    try_loop=False
    while try_loop==False:                  
        try:                                                        #if error occurs in try block the except is executed
            restock_id=int(input("Enter the id of the item to restock: "))
            if restock_id<=0 or restock_id>len(nl):                 #keep looping until user inputs a valid input
                print("Invalid input.")
                try_loop=False
            else:                                                   #if valid input, continue
                try_loop=True
        except:
            print("Invalid input.")
            try_loop=False

    #taking product quantity to restock
    try_loop=False
    while try_loop==False:                  
        try:
            restock_quantity=int(input("Enter the amount of quantity to restock: "))
            if restock_quantity<=0:
                print("Invalid input.")
                try_loop=False
            else:
                try_loop=True
        except:
            print("Invalid input. Please enter valid input.")
            try_loop=False
    return restock_id,restock_quantity

def restock_more(restock_loop):
    """
    function: In this function ans is taken and loop continue or break is determined
    parameters: restock_loop
    returns: restock_loop
    """
    print("Enter 'y' for restocking more or enter 'n' for printing the bill.")
    ans=input("Do you want to restock more items?").lower()
    if ans=="y" or ans=="yes":
        restock_loop==True
    elif ans=="n" or ans=="no":
        restock_loop=False
    else:
        restock_loop=False
    return restock_loop

def restock_bill_details(restock_list,restock_total):
    """
    function: In this function the bill details for the restock is displayed using restock_list
              total cost is also displayed
    parameters: restock_list,restock_total
    returns: none
    """
    for each in range(len(restock_list)):
        print(restock_list[each][0]+"\t\t    "+str(restock_list[each][1])+"\t\t    $"+str(restock_list[each][2])+"\t\t  $"+str(restock_list[each][3]))
    print("_"*90)
    print("Total Cost: $"+str(restock_total)+"\n")

def restock_file_name(datetime):
    """
    function: In this function, a new unique named txt file is created where the bill is stored
    parameters: datetime
    returns: date_and_time
    """
    #generating restock bill in a txt file
    year=str(datetime.now().year)
    month=str(datetime.now().month)
    day=str(datetime.now().day)
    hour=str(datetime.now().hour)
    minute=str(datetime.now().minute)
    sec=str(datetime.now().second)
    date_and_time=year+"."+month+"."+day+"."+hour+"."+minute+"."+sec
    return date_and_time
    
