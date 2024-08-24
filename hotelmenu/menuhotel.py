#define the menu of hotel 
menu={
    'pizza':40,
    'chill-chicken':170,
    'C-momo':250,
    'chowmein':225,
    'thukpa':200,
    'coffee':80,
}
#greet
print("Welcome to NayaSathi hotel")
print("pizza:Rs40\nchill-chicken:Rs170\nc-momo:250\nchowmein:Rs225\nthukpa:Rs200\ncoffee:Rs80")
order_total=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not avaialable yet!")

another_order= input("Do you want to add another item?(Yes/No)")
if another_order=="yes":
        item_2=input("Enter the name of second item=")
        if item_2 in menu:
            order_total +=menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item{item_2} is not available")
            print(f"The total amount of items to pay is{order_total}")
