def update_stock_in_file(nl):
    """
    function: It is used to update the products stock in the .txt file and after
              each element a comma "," is added except after the last element
    parameters: nl list (a list where each inner list contains product details)
    returns: the updated nl list(The same list that was written to the file.)
    """
    file=open("coursework.txt","w")
    for i in range(len(nl)):
        for j in range(len(nl[i])):
            file.write(nl[i][j])
            if j!=len(nl[i])-1: #putting "," in between of each element in each list
                file.write(",")
        file.write("\n")
    file.close()
    return nl

def save_bill_in_file(total_price_with_shipping,shipping_cost,name,phoneNumber,current_date_and_time,user_sell_items):
    """
    function: It is used to save and display the bill in a new .txt file
              and respective details are added in it
    parameters: total price including shipping, shipping cost, name of the customer,
                phone number of the customer, present date and time,
                user_sell_items list which contains the details about the purchases made
    returns: none
    """
    file=open(name+str(phoneNumber)+".txt","w")
    file.write("\n\t\tWecare Wholesale")
    file.write("\n\t\tBudhanilkantha, Kathmandu")
    file.write("\n\tContact: 01-4373542 E-mail: wecarepvt@gmail.com\n")
    file.write("-"*60)
    file.write("\nCustomer Name: "+name)
    file.write("\nCustomer Phone Number: "+phoneNumber)
    file.write("\nDate and Time: "+str(current_date_and_time)+"\n\n")
    file.write("_"*90)
    file.write("\n\t\t\t\tPurchase Details\n")
    file.write("_"*90)
    file.write("\n\tItem\t\t   Quantity\t Free Items\t Price Per Item\t\t Total\n")
    file.write("_"*90)

    #displaying the details of the bill in the txt file
    for i in range(len(user_sell_items)) :
        file.write("\n"+user_sell_items[i][0]+"\t\t\t"+str(user_sell_items[i][1])+"\t\t"+str(user_sell_items[i][2])+"\t\t"+str(user_sell_items[i][3])+"\t\t"+str(user_sell_items[i][4])+"\n")
    file.write("_"*90)
    if shipping_cost>0:
        file.write("\nShipping Price: $"+str(shipping_cost))
    file.write("\nTotal cost with shipping: $"+str(total_price_with_shipping))
    file.close()

def updating_the_file(nl):
    """
    function: It is used to update the coursework.txt where all the details are stored.
    parameters: nl list (a list where each inner list contains product details)
    returns: none
    """
    file=open("coursework.txt","w")
    for i in range(len(nl)):
        file.write(nl[i][0]+","+nl[i][1]+","+nl[i][2]+","+nl[i][3]+","+nl[i][4]+"\n")
    file.close()

def save_stock_bill_in_file(date_and_time,restock_list,current_date_and_time,restock_total):
    """
    function: It saves and displays the bill of restock in a new .txt file.
    parameters:current date and time, restock list which contains the details of restocked items
               restock total the total amount of money
    returns: none
    """
    #Saving the bill to a new .txt file with a unique name
    file=open(date_and_time+".txt","w")
    file.write("\n\t\tWecare Wholesale")
    file.write("\n\t\tBudhanilkantha, Kathmandu")
    file.write("\n\tContact: 01-4373542 E-mail: wecarepvt@gmail.com\n")
    file.write("-"*60)
    file.write("\nReceiver Name: Wecare Wholesale ")
    file.write("\nPAN number:103458 ")
    file.write("\nDate and Time: "+str(current_date_and_time)+"\n\n")
    file.write("_"*90)
    file.write("\n\t\t\t\t Bill\n")
    file.write("_"*90)
    file.write("\nItem \t\t\t Quantity\t Price Per Item \tTotal Amount\n")
    file.write("_"*90)

    #displaying the details of the bill in the txt file
    for each in range(len(restock_list)) :
        file.write("\n"+restock_list[each][0]+"\t\t    "+str(restock_list[each][1])+"\t\t    $"+str(restock_list[each][2])+"\t\t  $"+str(restock_list[each][3])+"\n")
    file.write("_"*90)
    file.write("\nTotal Amount: $"+str(restock_total))
    file.close()

def display_heading_in_option1():
    """
    function: In this function, the title is displayed
    parameters: none
    returns: none
    """
    print("\n\t\t\tWecare Wholesale Store")
    print("_"*70)       #puts 70 underscores "_" above the label
    print("ID\tName\t\tBrand\t\tQty\tPrice\tOrigin") #this print is to give labels above the product details,multiple \t to maintain spacing
    print("_"*70)       #puts 70 underscores "_" below the label

def choose_options():
    """
    function: In this function, the options is displayed
              on the screen with small descriptions each
    parameters: none
    returns: none
    """
    print("-"*45)
    print("Please press the suitable option for you")
    print("-"*45)
    print("Press 1 to sell the products.")
    print("Press 2 to restock the products.")
    print("Press 3 to exit.")
    print("-"*45)

def label_above_product_details():
    """
    function: In this function, the label is displayed
              on the terminal
    parameters: none
    returns: none
    """
    print("_"*69)
    print("ID\tName\t\tBrand\t\tQty\tPrice\tOrigin") #this print is to give labels above the product details,multiple \t to maintain spacing
    print("_"*69)

def display_label_bill():
    """
    function: In this function, the necessary components
              to create a bill is displayed
    parameters: none
    returns: none
    """
    #Displaying the bill in the console
    print("\n\t\t\t We Care Wholesale")
    print("\t\t\t Budhanilkantha,Kathmandu")
    print("\t\t Phone: 01-4373542 E-mail: wecarepvt@gmail.com")
    print("_"*90)
    print("\t\t\t\t Purchase Details")
    print("_"*90)
    print("Item \t\t Quantity\t Free Items\t Price Per Item \tTotal Amount")
    print("_"*90)

def heading_option2():
    """
    function: In this function, the title and label for option 2
              is displayed on the terminal
    parameters: none
    returns: none
    """
    print("\n")
    print("Welcome Back Admin,")
    print("_"*70)
    print("ID\tName\t\tBrand\t\tQty\tPrice\tOrigin") #this print is to give labels above the product details,multiple \t to maintain spacing
    print("_"*70)                                    #puts 70 underscores "_" below the label
 
def print_restock_bill():
    """
    function: In this function, the necessary components needed to
              complete a bill structure is displayed
    parameters: none
    returns: none
    """
    print("\n\t\t\t We Care Wholesale")
    print("\t\t\t Budhanilkantha,Kathmandu")
    print("\t\t Phone: 01-4373542 E-mail: wecarepvt@gmail.com")
    print("_"*90)
    print("\t\t\t\t  Bill")
    print("_"*90)
    print("Item \t\t\t Quantity\t Price Per Item \tTotal Amount")
    print("_"*90)

def option_three():
    """
    function: In this function, the message is displayed
    parameters: none
    returns: none
    """
    print("Thankyou for choosing us for your skin.")

def invalid_input():
    """
    function: In this function, the message is displayed
    parameters: none
    returns: none
    """
    print("\nThe input is invalid. Please choose from the options 1, 2 or 3.")
          



