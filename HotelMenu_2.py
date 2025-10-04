menu= {
    'pizza':80,
    'pasta':50,
    'coffee':40,
    'maggie':50,
    'salad':70,
    'burgur':90,
}
cart=[]
total=0
print("----WELCOME TO OUR RESTAURENT----")

for key, value in menu.items():
    print(f"{key:10}:{value:.2f}/-")

print("---------------------------------")
while True:
    choices=input("ENTER THE FOOD YOU WANT: ").lower()
    
    if choices == 'q':
        break 
    elif menu.get(choices) is not None:
        cart.append(choices)       
print("----------------------------------") 

for choices in cart :
    total += menu.get(choices)
    print(choices, end=" ")

print()
print(f"TOTAL COST: {total}rs")
print("----------------------------------") 

