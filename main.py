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
scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
li = [rock,paper,scissors]
print("Click to run the project")
def func():

        import random
        comp_choice = random.randint(0,2)
        #print(f"computer_chose : {comp_choice}")
        your_choice = int(input("Enter what you want to chose 0 for P,1 for R, 2 for S: "))
        print(f"\t {your_choice}")
        print(f"\t {comp_choice}")
        if your_choice <0 or your_choice>2:
            print("Incorrect entry , enter b/w 0 to 2:\n")
        elif your_choice == comp_choice:
            print(li[your_choice]) #print(game_images[computer_choice])
            print("\t")
            print(li[comp_choice])
            print("\t")
            print("Its a draw")
        elif your_choice==0 and comp_choice==2:
            print(li[your_choice])
            print("\t VS")
            print(li[comp_choice])
            print("\t")
            print("Youu Won!!")
        elif your_choice==2 and comp_choice==0:
            print(li[your_choice])
            print("\t VS")
            print(li[comp_choice])
            print("\t")
            print("Computer_won")
        elif your_choice > comp_choice:
            print(li[your_choice])
            print("\t VS")
            print(li[comp_choice])
            print("\t")
            print("You wonn!")
        else:
            print("Incorrect or something bad happended")


play=True
while(play):
    func()
    if(input("what to play again: to play click:Y\n")=='y'):
        play=True
    else:
        play=False



