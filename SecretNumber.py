import random 
low=0
high=100
number=random.randint(low,high)
guesses=0
print("Welcome to the Secret Number Game!")
guessing=True
while guessing:
    guess=int(input("Enter Your Number: "))
    guesses +=1

    if guess<low or guess>100:
        print(f"Please Enter A valid Number Between {low} and {high}")
    
    elif guess>number :
        print(f"The Number Is Too High, Try Decreasing The Count")
    
    elif guess<number:
        print("The Number Is Too Low, try Increasing The Count")

    else:
        print(f"Yes You Guessed It Right You Took {guesses} Guesses")
        guessing=False
