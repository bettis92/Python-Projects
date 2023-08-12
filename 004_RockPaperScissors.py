import random as rdn


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('We are playing Rock, Paper, Scissors! Type "1" for rock, "2" for paper, or "3" for scissors: '))
cpu_choice = rdn.randint(1,3)

if user_choice == 1:
    if cpu_choice == 1:
        print(f'you chose rock\n{rock}\nComputer chose rock\n{rock}\nYou Tied!')
    elif cpu_choice == 2:
        print(f'you chose rock\n{rock}\nComputer chose paper\n{paper}\nYou Lose!')
    else:
        print(f'you chose rock\n{rock}\nComputer chose scissors\n{scissors}\nYou Win!')
elif user_choice == 2:
    if cpu_choice == 1:
        print(f'you chose paper\n{paper}\nComputer chose rock\n{rock}\nYou Win!')
    elif cpu_choice == 2:
        print(f'you chose paper\n{paper}\nComputer chose paper\n{paper}\nYou Tied!')
    else:
        print(f'you chose paper\n{paper}\nComputer chose scissors\n{scissors}\nYou Lose!')
elif user_choice == 3:
    if cpu_choice ==1:
        print(f'you chose scissors\n{scissors}\nComputer chose rock\n{rock}\nYou Lose!')
    elif cpu_choice ==2:
        print(f'you chose scissors\n{scissors}\nComputer chose paper\n{paper}\nYou Win!')
    else:
        print(f'you chose scissors\n{scissors}\nComputer chose scissors\n{scissors}\nYou Tied!')
else:
    print("please type a valid number listed")
    

#lessons learned: try to find a way to use what you have learned in the module, try to simplify the code as much as possible
#for example, you coul have a line that is "if user input == computer input print its a tie"