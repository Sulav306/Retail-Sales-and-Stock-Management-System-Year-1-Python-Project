#Importing date and time
from datetime import datetime
from read import readFile
from operations import displayingStock,displaying_user,access_values,checking_free_items,updating_stock,bill_calculation,shipping_price,display_stock_option2,update_stock_in_list,restock_bill,enter_credentials,declaring_values,choose_option_input,purchase_more_items,display_bill_details,option_two_declare,restocking,restock_more,restock_bill_details,restock_file_name,input_user_id
from write import update_stock_in_file,save_bill_in_file,updating_the_file,save_stock_bill_in_file,display_heading_in_option1,choose_options,label_above_product_details,display_label_bill,heading_option2,print_restock_bill,option_three,invalid_input

display_heading_in_option1()
nl=readFile()       #calling functions
displayingStock(nl)

loop=True           #declaring a loop for admin
while loop== True: #while loop implementation
    choose_options()
    option_input,try_loop=choose_option_input()

    if option_input==1: #if statement which will be used after the user inputs the value 
        name,phoneNumber=enter_credentials()
        user_sell_items,total,final_total,shipping_cost,loop_sell,purchases=declaring_values()

        while loop_sell==True:
            label_above_product_details() #calling respective functions     
            displaying_user(nl)
            item_input_id=input_user_id(nl)
            total_quantity_of_selected_item,item_name=access_values(nl,item_input_id)
            free_items,total_quantity_with_free_items,item_input_quantity=checking_free_items(nl,item_name,item_input_id,purchases)     
            nl,item_input_id=updating_stock(nl,item_input_id,total_quantity_with_free_items)
            total,user_sell_items=bill_calculation(nl,item_input_id,item_input_quantity,user_sell_items,free_items,total)
            loop_sell=purchase_more_items(loop_sell)
        shipping_cost,total_price_with_shipping=shipping_price(shipping_cost,total)

        current_date_and_time=datetime.now()    #accessing the current date and time
        nl=update_stock_in_file(nl)
        display_label_bill()
        name,user_sell_items,shipping_cost,total_price_with_shipping=display_bill_details(user_sell_items,name,shipping_cost,total_price_with_shipping)
        save_bill_in_file(total_price_with_shipping,shipping_cost,name,phoneNumber,current_date_and_time,user_sell_items)
        
    elif option_input==2:                                #to restock the items as a store owner
        restock_total,current_date_and_time,restock_list,item_id,restock_loop=option_two_declare()
        while restock_loop==True:
            heading_option2()
            display_stock_option2(nl,item_id)
            restock_id,restock_quantity=restocking(nl)
            restock_total,restock_list=restock_bill(restock_id,restock_quantity,nl,restock_list,restock_total)
            nl=update_stock_in_list(restock_id,nl,restock_quantity)
            updating_the_file(nl)
            restock_loop=restock_more(restock_loop)

        print_restock_bill()
        restock_bill_details(restock_list,restock_total)
        date_and_time=restock_file_name(datetime)
        save_stock_bill_in_file(date_and_time,restock_list,current_date_and_time,restock_total)
                
    elif option_input==3:
        option_three()
        break
    else:
       invalid_input()  

        
    
