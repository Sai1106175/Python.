print("Welcome to KBC")
userName = input("Please enter your Name")
print ("Hello ", userName, "Lets Get started with Questions")

Questions = ["Who is the first PM of India","What is the Calcuation of 5*5*4", "When did india won the first Worldcup"]
print(Questions[0])

userInput = input ("Please answer your time starts now...\n Option A =jawaharlal Nehru \n Option B lal Nehru \n Option C Nehru \n Option D Lal")
if(userInput == "jawaharlal Nehru"):
    sum = 100
    print(f"Its absolutely right answer and you won{sum} ")
else:
    print("It was wrong answer..Thanks for participating!!")

if(sum ==100):
    print(Questions[2])
    userInput2 = int(input("Please answer your time starts now.. \n Option A  = 2001 \n Option B = 2002 \n Option C = 2007 \n Option D 2011"))
    if(userInput2 == 2011):
        sum = sum + 100
        print(f"Its absolutely right answer and you won{sum}")
else:
    print("It was wrong answer..Thanks for participating!!")


    

    

