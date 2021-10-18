customer_list=[{'name': 'brenda', 'address': '345', 'customer_id': '45'},
{'name': 'juma', 'address': '1234', 'customer_id': 3115163323632},
{'name': 'brenda', 'address': '1234j', 'customer_id': 1576011607984}
]
product_list=[{'name': 'blue', 'amount': 34, 'price': 340.0, 'product_id': 45},
              {'name': 'brown', 'amount': 364, 'price': 340.0, 'product_id': 2429025611856}]
def insert_customer():
    c_name = input("Enter the customer name:")
    c_address = input("Enter the customer address:")
    c_id = id(c_name)
    dict = {"name": c_name, "address": c_address, "customer_id": c_id}
    return dict
def delete_customer(customer_list):
    c_id = input("Enter the customer Id:")
    for i in range(len(customer_list)-1):
        id=customer_list[i]['customer_id']
        if id==c_id:
            customer_list.remove(customer_list[i])
    return customer_list
def update_customer_data(customer_list):
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

def insert_product():
    p_name = input("Enter the product name:")
    p_amount = int(input("Enter the number of product:"))
    p_price=float(input("Enter product price"))
    p_id = id(p_name)
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


def purchase(customer_list,product_list):
    p_id = input("Enter the product Id:")
    c_id=input("enter the customer id")
    c_amount=input("enter the amount purchased")
    for i in range(len(product_list)):
        if p_id==product_list[i]['product_id']:
            if c_amount<=product_list[i]['amount']:
                product_list[i]['amount']=c_amount
            else:
                print("out of stock")








if __name__ == '__main__':
    print("""
             What would you want  to update
              1.Customer
              2.Product
              """)
    choice = int(input("Enter the choice"))
    if choice == 1:
        print("""
                 What would operation would you like to do
                  1. Insert a New Customer
                  2. Delete a Customer
                  3. Update Customer Data
                  """)
        customer_operation=int(input("enter the what operation to perform on customer"))
        if customer_operation==1:
            customer_list.append(insert_customer())
        elif customer_operation==2:
            delete_customer(customer_list)
        elif customer_operation==3:
            update_customer_data(customer_list)




    elif choice == 2:
        print("""
                     What would you like to do
                      1. Insert a New Product
                      2. Delete a Product
                      3. Update Product Data
                     """)
        product_operation = int(input("enter the what operation to perform on product"))
        if product_operation == 1:
            product_list.append(insert_product())
            print(product_list)
        elif product_operation == 2:
            delete_product(product_list)
            print(product_list)
        elif product_operation == 3:
            print(update_product_data(product_list))
    else:
        print("invalid choice")
