import ast
def insert_customer():
    #inserting customer function
    c_name = input("Enter the customer name:")
    c_address = input("Enter the customer address:")
    c_id = input("Enter a unique id:")
    dict = {"name": c_name, "address": c_address, "customer_id": c_id}
    return dict


def delete_customer(customer_list):
    #deleting customer  using customer id
    c_id = input("Enter the customer Id:")
    for i in range(len(customer_list)-1):
        id=customer_list[i]['customer_id']
        if id==c_id:
            customer_list.remove(customer_list[i])
    return customer_list


def update_customer_data(customer_list):
    #updating customer data with either name or address
    c_id = input("Enter the customer Id:")
    cchoice=int(input("enter your choice"))
    for i in range(len(customer_list)):
        id = customer_list[i]['customer_id']
        if id == c_id:
            if cchoice==1:
                name=input('enter the name change')
                customer_list[i]['name']=name
            elif cchoice==2:
                address=input("enter the address")
                customer_list[i]['address']=address
    return customer_list

#product functions
def insert_product():
    p_name = input("Enter the product name:")
    p_amount = int(input("Enter the number of product:"))
    p_price=float(input("Enter product price"))
    p_id = str(id(p_name))
    dict = {"name": p_name, "amount": p_amount, "price": p_price,"product_id":p_id}
    return dict


def delete_product(product_list):
    p_id = input("Enter the product Id:")
    for i in range(len(product_list) - 1):
        id = product_list[i]['product_id']
        if id == p_id:
            product_list.remove(product_list[i])
    return product_list


def update_product_data(product_list):
    p_id = input("Enter the product Id:")
    cchoice = int(input("enter your choice"))
    for i in range(len(product_list)):
        id = product_list[i]['product_id']
        if id == p_id:
            if cchoice == 1:
                name = input('enter the name change')
                product_list[i]['name'] = name
            elif cchoice == 2:
                amount = int(input("enter the new amount"))
                product_list[i]['amount'] = amount
            elif cchoice == 3:
                price = float(input("enter the new price"))
                product_list[i]['price'] = price
    return product_list


def search_product(product_list):
    #searching for a product using product  id
    p_id = input("Enter the product Id:")
    for i in range(len(product_list)):
        id = product_list[i]['product_id']
        if id == p_id:
            name=product_list[i]['name']
            amount=product_list[i]['amount']
            price=product_list[i]['price']
    dict={"product_name":name,"product_amount":amount,"product_price":price}
    return dict


def amount_purchased(product_data_list):
    #List a customer's (customer id will be given) and give the name of customer, product price ,amount and total amount paid
    productamount=[]#list that cointains product amount and product name
    total=0
    c_id = input("Enter the customer Id:")
    for i in range(len(product_data_list)):
        id = product_data_list[i]['customerid']
        if id==c_id:
            cname=product_data_list[i]["customer name"]
            price = product_data_list[i]["product_price"]
            name=product_data_list[i]["product_name"]
            amount=product_data_list[i]["productamount"]
            tprice=price*amount
            product={"product_name":name,"amount":amount}
            productamount.append(product)
            total=total+tprice
    print(cname,"bought",productamount,"at a total price of",total)


def purchase(customer_list,product_list,):

    p_id = input("Enter the product Id:")
    c_id=input("enter the customer id")
    c_amount = int(input("enter the amount purchased"))
    for i in range(len(customer_list)):
        name = customer_list[i]['name']
        if c_id ==customer_list[i]['customer_id']:
            for i in range(len(product_list)):
                print(product_list)
                if p_id==product_list[i]['product_id']:
                    price = product_list[i]["price"]
                    pname = product_list[i]["name"]
                    if c_amount<=product_list[i]['amount']:
                        amount=product_list[i]['amount']-c_amount
                        product_list[i]['amount']=amount
                    else:
                        print("out of stock")
    dict = {"customerid": c_id, "customer name": name, "productid": p_id, "product_name": pname,
                        "productamount": c_amount, "product_price": price}
    return dict



if __name__ == '__main__':

        customer_list=[]
        product_list=[]
        product_data_list=[]
        customer = open("customer_info.txt", "r")
        fcustomer = open("customer_info.txt", "a")
        for s in customer:
            data = ast.literal_eval(s)
            customer_list.append(data)
        product = open("product_info.txt", "r")
        fproduct = open("product_info.txt", "a")

        for s in product:
            data = ast.literal_eval(s)
            product_list.append(data)
        pdata=open("customerproductdata.txt","r")
        fdata = open("customerproductdata.txt", "a")
        for s in pdata:
            data=ast.literal_eval(s)
            product_data_list.append(data)

        print("""
                    What would you want  to update
                     1.Customer
                     2.Product
                     """)
        choice = int(input("Enter the choice"))
        if choice==1:
            print("""
                         What would operation would you like to do
                          1. Insert a New Customer
                          2. Delete a Customer
                          3. Update Customer Data
                          4.list customers
                          """)
            option=int(input("enter the operation you wish to perform"))
            if option==1:
                print(insert_customer(),file=fcustomer)
            elif option == 2:
                j = delete_customer(customer_list)
                with open('customer_info.txt', "w") as myfile:
                    for i in range(len(j)):
                        print(j[i],file=myfile)
            elif option==3:
                j=update_customer_data(customer_list)
                with open('customer_info.txt', "w") as myfile:
                    for i in range(len(j)):
                        print(j[i],file=myfile)
            elif option==4:
                print(customer_list)
        elif choice==2:
            print("""
                                 What would operation would you like to do
                                  1. Insert a New Product
                                  2. Delete a Product
                                  3. Update Product Data
                                  4. purchase product
                                  5. lists products
                                  6. search product
                                  7.list customer name and total amount spent
                                  """)
            option = int(input("enter the operation you wish to perform"))
            if option==1:
                print(insert_product(),file=fproduct)
            elif option==2:
                j=delete_product(product_list)
                with open('product_info.txt', "w") as myfile:
                    for i in range(len(j)):
                        print(j[i],file=myfile)
            elif option==3:
                j =update_product_data(product_list)
                with open('product_info.txt', "w") as myfile:
                    for i in range(len(j)):
                        print(j[i],file=myfile)

            elif option==4:
               j = purchase(customer_list,product_list)
               print(j,file=fdata)
               with open('product_info.txt', "w") as myfile:
                   for i in range(len(product_list)):
                       print(product_list[i], file=myfile)
            elif option==5:
                print(product_list)
            elif option==6:
                print(search_product(product_list))
            elif option==7:
                amount_purchased(product_data_list)

