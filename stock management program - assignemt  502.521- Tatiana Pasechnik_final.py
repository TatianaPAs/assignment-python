#program stores 6 atributes for dresses: Code, Name, Size, Price, Color and Quantity
code_list=["1001","1002","1003"]
name_list=["Bella", "Victoria", "Magnolia"]
size_list=["Large", "Small", "Medium"]
price_list=[100.50, 85.50, 90]
colour_list=["White", "Blue", "Red"]
quantity_list=[15,30,42]


def addProduct():
    product_code=input("Enter unique dress ID ")
    
    if product_code not in code_list:
        code_list.append(product_code)
        product_name=input("Please enter the name of a dress model ")
        name_list.append(product_name)
        product_size=input("Enter dress size ")
        size_list.append(product_size)
        product_colour=input("Enter dress colour ")
        colour_list.append(product_colour)
        product_price=float(input("Enter dress price "))
        price_list.append(product_price)
        product_quantity=int(input("Enter dress quantity "))
        while product_quantity <10 or product_quantity>50:
            print("Dress quantity must be minimum 10 and maximum 50 ")
            product_quantity=int(input("Enter dress quantity "))
        if 10<=product_quantity<=50:
            quantity_list.append(product_quantity)      
        add_more=input("Do you want to add more dresses to record, enter yes or no: ").lower()
        if add_more=="yes":
            addProduct()     
    else:
        print("Dress ID already exists, please enter another ID ")
        addProduct()

def checkProduct(code):
#function returns boolean value
    x= code in code_list
    return x
   
def searchProduct(prompt):
    global index
    check=checkProduct(prompt)
#fisrt checking if code in the list    
    while(1):
        if check==False:
            print("Dress with this ID does not exist")
            prompt=input("Enter unique dress ID ")
            check=checkProduct(prompt)
        
        if check==True:
            index=code_list.index(prompt)
# finds index of a product code, to use it for other lists
            print("Dress details: ")
            print("Dress unique ID: ",code_list[index])
            print("Name of a dress model: ",name_list[index])
            print("Dress size: ",size_list[index])
            print("Dress colour: ",colour_list[index])
            print("Dress price: ",price_list[index])
            print("Dress quantity: ",quantity_list[index])
            break
  
    
def updateProduct(product_code):
    searchProduct(product_code)
#have to declare what is new product_code, otherwise migth run into error, by storing wrong code
    product_code=code_list[index]
 
#updating details starts       
    product_name_update=input("Do you want to update dress model name, enter yes or no: ").lower()
    if product_name_update=="yes":
        product_name=input("Please enter the new dress model name: ")
        name_list[code_list.index(product_code)]=product_name
    
    product_size_update=input("Do you want to update dress size, enter yes or no: ").lower()
    if product_size_update=="yes":
        product_size=input("Please enter the new dress size: ")
        size_list[code_list.index(product_code)]=product_size
        
    product_colour_update=input("Do you want to update dress colour, enter yes or no: ").lower()
    if product_colour_update=="yes":
        product_colour=input("Please enter the new dress colour: ")
        colour_list[code_list.index(product_code)]=product_colour
    
    product_price_update=input("Do you want to update dress price, enter yes or no: ").lower()
    if product_price_update=="yes":
        product_price=int(input("Please enter the new dress price: "))
        price_list[code_list.index(product_code)]=product_price
        
    product_quantity_update=input("Do you want to update dress quantity, enter yes or no: ").lower()
    if product_quantity_update=="yes":
        product_quantity=int(input("Enter dress quantity "))
#check if quantity within 10-50        
        while product_quantity<10 or product_quantity>50:
            print("Dress quantity must be minimum 10 and maximum 50 ")
            product_quantity=int(input("Enter new dress quantity "))
        
        if 10<=product_quantity<=50:
            quantity_list[code_list.index(product_code)]=product_quantity
        
    
def buyProduct(product_code, product_quantity):
    searchProduct(product_code)
#first check if code in the code list and display details 
#need to redifine the code in case there was not existing code before
    product_code=code_list[index]
    
    quantity=quantity_list[code_list.index(product_code)]
#check quantity if store has enough in database

    while product_quantity>quantity:
        print("There are only ",quantity, "available")
        product_quantity=int(input("Enter quantity of dresses you want to buy "))
    
    if product_quantity<=quantity:
        new_quantity=quantity_list[code_list.index(product_code)]-product_quantity
        quantity_list[code_list.index(product_code)]=new_quantity
        sell_quantity=product_quantity
        print("You want to buy dress ID ",product_code,"-", sell_quantity,"items")
#calculate total and discount
        if sell_quantity<10:
            Total_price=(sell_quantity*price_list[index])*1.15
            print("Total price to pay including GST is: ","{:.2f}".format(Total_price),"NZ Dollars")         
        elif 10<=quantity<20:
            Total_price=((sell_quantity*price_list[index])*1.15)*0.9
            print("Total price to pay including GST  and 10% discount is: ","{:.2f}".format(Total_price),"NZ Dollars")   
        elif 20<=quantity<=30:
            Total_price=((sell_quantity*price_list[index])*1.15)*0.8
            print("Total price to pay including GST  and 20% discount is: ","{:.2f}".format(Total_price),"NZ Dollars")
        elif 30<quantity:
            Total_price=((sell_quantity*price_list[index])*1.15)*0.7
            print("Total price to pay including GST  and 30% discount is: ","{:.2f}".format(Total_price),"NZ Dollars")
        
            
#main program starts
while(1):
    
    print("Please select one of the following options: ")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update product")
    print("4. Buy product")
    print("5. Exit")

    choice=int(input("Please enter 1,2,3,4,or 5: "))
    if choice ==1:
        print("To add a new dress, please provide information bellow: ")
        addProduct();
        
    elif choice==2:
        print("With this option, you can check the dress details from the database")
        prompt=input("Enter unique dress ID ")
        searchProduct(prompt);
        
    elif choice==3:
        print("To update dress details in the database, please provide information bellow: ")
        product_code=input("Enter unique dress ID ")
        updateProduct(product_code)
        
    elif choice==4:
        print("With this option you can buy dresses")
        print("We have a special offer for you: ")
        print("If you buy 10-19 dresses in one trasaction, you will get a 10% discount ")
        print("If you buy 20-30 dresses in one trasaction, you will get a 20% discount")
        print("If you buy more than 30 dresses in one transaction, you will get a 30% discount")
        product_code=input("Enter unique dress ID which you want to buy ")
        product_quantity=int(input("Enter quantity of dresses you want to buy ")) 
        buyProduct(product_code, product_quantity )
     
    if choice==5:
        print("Exit")
        break

