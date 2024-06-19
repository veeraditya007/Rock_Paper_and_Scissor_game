import random
rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissior='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

user_choice=int(input("what do you chose?\n1-> 0 for rock\n2-> 1 for paper\n3-> 2 for scissor\n"))
if user_choice==0:
    print("You choose  rock\n\n",rock)
elif user_choice==1:
    print("You choose paper\n\n",paper)
elif user_choice==2:
    print("You choose scissior\n\n",scissior)  
else:
    print("You chose wrong character\n\n")          
computer_choice=random.randint(0,2)

if computer_choice==0:
    print("computer choose rock\n",rock)
elif computer_choice==1:
    print("computer choose paper\n",paper)
else:
    print("computer choose scissior\n",scissior) 


if user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==2 and computer_choice==0:
    print("You loose!")    
elif computer_choice>user_choice:
    print("You loose!") 
elif computer_choice==user_choice:
    print("It's a draw ")       
else:
    print("You chose an invalid character ,You Losee!")    