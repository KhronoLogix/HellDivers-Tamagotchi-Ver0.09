#BluPrint Games
#LeadDev: Logix
#BugTester: Hanahaki

import random
class Tomagotchi(object):  
    #what he is who he feels like
    def __init__(self, name, tired = 10, hunger = 10, boredom = 10, thirst = 10, hp = 20, immortal = 0, ammoPrim = 8, ammoSecon = 4, ammoHeavy = 2):
        self.name = name
        self.hp = hp
        self.hun = hunger
        self.thirst = thirst
        self.tired = tired 
        self.bore = boredom
        self.ammoPrim = ammoPrim
        self.ammoSecon = ammoSecon
        self.ammoHev = ammoHeavy
        self.immortal = immortal
    
    #the passage of time
    def passTime(self):
        self.hun = self.hun - 1
        self.bore = self.bore - 1
        self.tired = self.tired - 1
        self.thirst = self.thirst - 1
    
    def talk(self):
        talkChoice = 1
        while talkChoice == 1:
            print('''
                 What do you want to talk to me about?
                  ╔═══════════════════════════════════╗
                  ║ 1: How are you feeling?           ║
                  ╠═══════════════════════════════════╣
                  ║ 2: How hungry are you?            ║
                  ╠═══════════════════════════════════╣
                  ║ 3: How Thirsty are you?           ║
                  ╠═══════════════════════════════════╣
                  ║ 4: Are you bored or tired?        ║
                  ╠═══════════════════════════════════╣
                  ║ 5: Check your HP for me           ║
                  ╠═══════════════════════════════════╣
                  ║ 6: Check your ammo for me         ║
                  ╠═══════════════════════════════════╣
                  ║ 7: Whats your opinion on Freedom? ║ 
                  ╠═══════════════════════════════════╣
                  ║ 8: Time for a helldive.           ║
                  ╠═══════════════════════════════════╣
                  ║ 0: Never Mind                     ║
                  ╚═══════════════════════════════════╝
                  ''')
            talkChoice = input("I want to talk about: ")
            if talkChoice == "1":
                print(f"im feeling {self.mood}")
            elif talkChoice == "2":
                if self.hun == 1 or 2:
                    print("im not that hungry right now but im sure i could use a bite later!")
                elif self.hun == 3 or 4:
                    print("im getting pretty hungry i would like something to eat")
                elif self.hun == 5 or 6:
                    print("please give me something im so hungry")
                elif self.hun >= 7:
                    print("im starving to death...")
            elif talkChoice == "3":
                if self.thirst == 1 or 2:
                    print("im not thirsty right now :D")
                elif self.thirst == 3 or 4:
                    print("i could use a cup of water right now")
                elif self.thirst == 5 or 6:
                    print("please give me water im so dry")
                elif self.thirst >= 7:
                    print("sweet liberty give me water...")
            elif talkChoice == "4":
                if self.bore == 1 or 2:
                    print("im not bored, i wouldnt mind a quick game though!")
                elif self.bore == 3 or 4:
                    print("im decently bored can we play a game together?")
                elif self.bore == 5 or 6:
                    print("please play with me")
                elif self.bore >= 7:
                    print("am i not fun? please hangout with me...")
                if self.tired == 1 or 2:
                    print("im not sleepy")
                elif self.tired == 3 or 4:
                    print("a small nap would be nice")
                elif self.tired == 5 or 6:
                    print("im suprised i havent fallen asleep im so tired")
                elif self.tired >= 7:
                    print("please let me sleep...") 
            elif talkChoice == "5":
                print(f"my hp is {self.hp}/20")
                if self.hp == 20:
                    print("im good as a new helldiver!")
                elif self.hp >= 15:
                    print("i got some scrapes and bruses but i can walk it off")
                elif self.hp >= 10:
                    print("im in pain, im bleeding i think?")
                elif self.hp >= 5:
                    print("I NEED A STIM.")
            elif talkChoice == "6":
                print(f'''
                      i have {self.ammoPrim}/8 Primary Mags
                      i have {self.ammoSecon}/4 Secondary Mags
                      i have {self.ammoHev}/2 Stratagem Mags
                      ''')
            elif talkChoice == "7":
                randomPhrase = random.randint(1,5)
                if randomPhrase == 1:
                    print("Liberty is perfection.")
                elif randomPhrase == 2:
                    print("Like those socialist bots need to go! Spill oil!")
                elif randomPhrase == 3:
                    print("Like those Divers on Erata Prime need to get they're guns together and beat back those bugs!")
                elif randomPhrase == 4:
                    print("That we havent spread Freedom to enough planets, Free all Sectors!")
                elif randomPhrase == 5:
                    print("MY LIFE FOR SUPER EARTH!")
            elif talkChoice == "8":
                lifeRNG = random.randint(1,20)
                diff = input('''
                Dont forget to choose your difficulty
                ╔═══════════════════════════════════╗
                ║ 1: Trivial                        ║
                ╠═══════════════════════════════════╣
                ║ 2: Easy                           ║
                ╠═══════════════════════════════════╣
                ║ 3: Medium                         ║
                ╠═══════════════════════════════════╣
                ║ 4: Challenging                    ║
                ╠═══════════════════════════════════╣
                ║ 5: Hard                           ║
                ╠═══════════════════════════════════╣
                ║ 6: Extreme                        ║
                ╠═══════════════════════════════════╣
                ║ 7: Suicide Mission                ║ 
                ╠═══════════════════════════════════╣
                ║ 8: Impossible                     ║
                ╠═══════════════════════════════════╣
                ║ 9: Helldive                       ║
                ╠═══════════════════════════════════╣
                ║ 0: I dont want to dive anymore    ║
                ╚═══════════════════════════════════╝
                ''')
                #The RNG behind the difficulty
                trivialDive = random.randint(1,4)
                easyDive = random.randint(1,10)
                mediumDive = random.randint(5,10)
                challengingDive = random.randint(10,15)
                hardDive = random.randint(10,19)
                extremeDive = random.randint(15,19)
                smDive = random.randint(10,20)
                impossibleDive = random.randint(15,20)
                hellDive = random.randint(18,30)

                if diff == "1":
                    print(f"My name is {self.name} im diving on tivial, im Extremely likely to come back. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= trivialDive
                    self.ammoPrim -= 1
                    print(f"Your diver lost {trivialDive} HP")
                elif diff == "2":
                    print(f"My name is {self.name} im diving on Easy, im Highly likely to come back. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= easyDive
                    self.ammoPrim -= 1
                    self.ammoSecon -= 1
                    self.ammoHev -= 1
                    print(f"Your diver lost {easyDive} HP")
                elif diff == "3":
                    print(f"My name is {self.name} im diving on Medium, im more likely to come back. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= mediumDive
                    self.ammoPrim -= 2
                    self.ammoSecon -= 1
                    self.ammoHev -= 1
                    print(f"Your diver lost {mediumDive} HP")
                elif diff == "4":
                    print(f"My name is {self.name} im diving on Challenging, im likely to come back. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= challengingDive
                    self.ammoPrim -= 3
                    self.ammoSecon -= 4
                    self.ammoHev -= 2
                    print(f"Your diver lost {challengingDive} HP")
                elif diff == "5":
                    print(f"My name is {self.name} im diving on Hard, i may not come back. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= hardDive
                    self.ammoPrim -= 4
                    self.ammoSecon -= 4
                    self.ammoHev -= 2
                    print(f"Your diver lost {hardDive} HP")
                elif diff == "6":
                    print(f"My name is {self.name} im diving on Extreme, im likely to die. i will miss you. i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= extremeDive
                    self.ammoPrim -= 5
                    self.ammoSecon -= 4
                    self.ammoHev -= random.randint(1,2)
                    print(f"i called in {random.randint(1,3)} resuplies")
                    print(f"Your diver lost {extremeDive} HP")
                elif diff == "7":
                    print(f"My name is {self.name} im diving on a Suicide Misson, dont wait up... i am a helldiver and i understand i may die. FOR DEMOCROCY!")
                    self.hp -= smDive
                    self.ammoPrim -= random.randint(3,8)
                    self.ammoSecon -= random.randint(2,4)
                    self.ammoHev -= random.randint(1,2)
                    print(f"i called in {random.randint(1,5)} resuplies")
                    print(f"Your diver lost {smDive} HP")
                elif diff == "8":
                    print(f"My name is {self.name} im diving on Impossible, remember me. i am a helldiver and i understand i will die. FOR DEMOCROCY!")
                    self.hp -= impossibleDive
                    self.ammoPrim -= random.randint(5,8)
                    self.ammoSecon -= random.randint(2,4)
                    self.ammoHev -= 2
                    print(f"i called in {random.randint(2,6)} resuplies")
                    print(f"Your diver lost {impossibleDive} HP")
                elif diff == "9":
                    print(f"My name is {self.name} im diving on Helldive, not coming back... will you miss me? ... FOR DEMOCROCY.")
                    self.hp -= hellDive
                    self.ammoPrim -= 8
                    self.ammoSecon -= 4
                    self.ammoHev -= 2
                    print(f"i called in {random.randint(2,8)} resuplies")
                    print(f"Your diver lost {hellDive} HP")
                elif diff == "0":
                    print("your helldiver steps back into the ship: ","hey what gives?")
                else:
                    print("\nSorry ",diff," isnt a valid option")
            elif talkChoice == "0":
                print("thanks for talking to me!")
                talkChoice = 0
            else:
                print("\nSorry ",talkChoice," isnt a valid option")
        self.passTime()

    #property is a getter, its sure something
    #the feelings of its feewings 
    @property
    def mood(self):
        sadness = (self.hun + self.bore + self.thirst + self.tired) - 40
        if sadness == 40:
            m = "Democratic"
        elif 39 >= sadness >= 30:
            m = "Feeling Meiocre"
        elif 29 >= sadness >= 20:
            m = "Sad"
        elif 19 >= sadness >= 10:
            m = "PTSD Riddled"
        elif 9 >= sadness >= 1:
            m = "Niegh Dead"
        elif sadness == 0:
            m = "Dead."
        return m

    
  
    def health(self, medkit = 10, medpack = 20):
        if self.hp < 10:
            oldHP = self.hp
            self.hp += medpack
            if self.hp > 20:
                self.hp = 20
                self.tired -= 5
            print(f"the helldivr was at {oldHP} we gave them a medpack, now they have {self.hp}/20")
        elif self.hp < 15:
            oldHP = self.hp
            self.hp += medkit
            if self.hp > 20:
                self.hp = 20
                self.tired -= 1
            print(f"the helldiver was at {oldHP}, we gave them a medkit, now they have {self.hp}/20")
        else:
            print("I dont need to heal right now")
        return self.hp
    
    #the eating food of the food function
    def eat(self,food = 7):
        print("That was good thank you!")
        self.hun += food
        if self.hun == 0:
            self.hp -= 1
            print("this hurts im so hungry, I CANT DROP LIKE THIS!")
            self.hun = 0
        self.passTime()
    
    #pretty much the same as the food but for water
    def drink(self,drink = 7):
        print("refreshing!")
        self.thirst += drink
        if self.thirst < 0:
            self.hp -= 1
            print("i need something to drink, im dehydrated please.")
            self.thirst = 0
    def sleep(self, sleep = 7):
        print("dormir")
        self.tired += sleep
        if self.tired < 0:
            self.hp -= 1
            print("LET ME SLEEEP...")
            self.tired = 0


    #play with your diver
    def play(self, fun = 7):
        print("Sweet Liberty that was nice")
        self.bore += fun
        if self.bore <0:
            print("please do something...")
            self.bore = 0
            self.tired += 1
        self.passTime()
    
    def ammo(self, resup = 8):
        print("Ammo against the ailens!")
        self.ammoPrim += resup
        self.ammoSecon += resup
        self.ammoHev += resup
        if self.ammoPrim > 8:
            self.ammoPrim = 8
        if self.ammoSecon > 4:
            self.ammoSecon = 4
        if self.ammoHev > 2:
            self.ammoHev = 2
        print(f"i have {self.ammoPrim}/8 Primary Mags\ni have {self.ammoSecon}/4 Pistol Mags\nI have {self.ammoHev}/2 Stratagem Mags")

    def dead(self):
        if self.hp == 0:
            dead = 1
        return dead
    def immortall(self):
        if self.dead == 1:
            self.dead = 0
            self.hp = 20
            self.hun = 10
            self.thirst = 10
            self.tired = 10
            self.bore = 10
            print("how am i still alive?")
    def dev(self):
        print('''
            ╔════════════════════════════════════════╗
            ║ This is a dev board. Ver. 0.08         ║
            ╠════════════════════════════════════════╣
            ║ 1. Print all stats                     ║
            ╠════════════════════════════════════════╣
            ║ 2. Immortal Diver                      ║
            ╠════════════════════════════════════════╣
            ║ 3. Roadmap + devlog                    ║
            ╠════════════════════════════════════════╣
            ║ 4. Exit The program                    ║
            ╚════════════════════════════════════════╝
              ''')
        devInput = input("Choice: ")
        
        if devInput == "1":
            print(f'''
            Name : {self.name} 
            ╔═══════════════════════════════════╗
            ║HP: {self.hp}                               ║
            ╠═══════════════════════════════════╣
            ║Hunger: {self.hun}                          ║
            ╠═══════════════════════════════════╣
            ║Thirst: {self.thirst}                          ║
            ╠═══════════════════════════════════╣
            ║Sleepy: {self.tired}                          ║
            ╠═══════════════════════════════════╣
            ║Bored: {self.bore}                           ║
            ╠═══════════════════════════════════╣
            ║AmmoPrim: {self.ammoPrim}                        ║
            ╠═══════════════════════════════════╣
            ║AmmoSecon: {self.ammoSecon}                       ║
            ╠═══════════════════════════════════╣
            ║AmmoHev: {self.ammoHev}                         ║
            ╚═══════════════════════════════════╝
                  ''')
            print("time pass")
            self.passTime()
            print(f'''
            Name : {self.name} 
            ╔═══════════════════════════════════╗
            ║HP: {self.hp}                               ║
            ╠═══════════════════════════════════╣
            ║Hunger: {self.hun}                          ║
            ╠═══════════════════════════════════╣
            ║Thirst: {self.thirst}                          ║
            ╠═══════════════════════════════════╣
            ║Sleepy: {self.tired}                          ║
            ╠═══════════════════════════════════╣
            ║Bored: {self.bore}                           ║
            ╠═══════════════════════════════════╣
            ║AmmoPrim: {self.ammoPrim}                        ║
            ╠═══════════════════════════════════╣
            ║AmmoSecon: {self.ammoSecon}                       ║
            ╠═══════════════════════════════════╣
            ║AmmoHev: {self.ammoHev}                         ║
            ╚═══════════════════════════════════╝
                  ''')
        elif devInput == "2":
            print(f"{self.name} cant die now your welcome! Weakling...")
            self.immortal = 1
        elif devInput == "3":
            print('''
                  Hi, my name is Khronologix
                  This is the most bear bones Tomagotchi for my current fav game, Helldivers
                  its a love letter to the dev team i wont be entirely finished for a while
                  
                  Update 0.01 - 0.07
                  so many functions....
                  Such as Hunger, Thirst, Ammo of all types (has no use now), Bored.
                  Update 0.08
                  Added Death
                  Added Immortality
                  
                  Update 0.09
                  Added Sleep 
                  fixed so many bugs with my good friend and Co-Founder Hanahaki
                  
                  Next Update 0.1
                  wait for helldiver dev to say its ok to make this a thing THEN
                  Add a reason to helldive, Add equipment, Add bleeding / other status effects
                  upgrade living status overall add more features.
                  amazing passion project
                  ''')
        else:
            print("why are you in the dev section \nif you dont even know how to type a single number?")
        return self.immortal

#main function runs everything
def main():
    critName = input("Name them: ")
    
    print('''
          
██╗░░░██╗░█████╗░██╗░░░██╗██████╗░  ░█████╗░░██╗░░░░░░░██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗  ██╔══██╗░██║░░██╗░░██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║██████╔╝  ██║░░██║░╚██╗████╗██╔╝██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗  ██║░░██║░░████╔═████║░██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║  ╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝  ░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝

██╗░░██╗███████╗██╗░░░░░██╗░░░░░██████╗░██╗██╗░░░██╗███████╗██████╗░
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██║██║░░░██║██╔════╝██╔══██╗
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║██║╚██╗░██╔╝█████╗░░██████╔╝
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░██║███████╗███████╗███████╗██████╔╝██║░░╚██╔╝░░███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
          ''')
    
    crit = Tomagotchi(critName)
    choice = None
    while choice != 0:
        print('''
              ╔═══════════════════════════════╗
              ║ 1: Talk to your Helldiver     ║
              ╠═══════════════════════════════╣
              ║ 2: Let your Helldiver Eat     ║
              ╠═══════════════════════════════╣
              ║ 3: Let your Helldiver Drink   ║
              ╠═══════════════════════════════╣
              ║ 4: Let your Helldiver Sleep   ║
              ╠═══════════════════════════════╣
              ║ 5: Play with your Helldiver   ║
              ╠═══════════════════════════════╣
              ║ 6: Check your Divers Ammo     ║
              ╠═══════════════════════════════╣
              ║ 7: Check HP and Heal          ║
              ╠═══════════════════════════════╣
              ║ 0: Quit The Program           ║
              ╚═══════════════════════════════╝
              ''')

        choice = input("Choice: ")
        
        while crit.dead != 1:
            if choice == "1":
                crit.talk()
                break
            elif choice == "2":
                crit.eat()
                break
            elif choice == "3":
                crit.drink()
                break
            elif choice == "4":
                crit.sleep()
                break
            elif choice == "5":
                crit.play()
                break
            elif choice == "6":
                crit.ammo()
                break
            elif choice == "7":
                crit.health()
                break
            elif choice == "0":
                print("Bye")
                choice = 0
                break
            elif choice == 1:
                print("your helldiver is dead.")
                choice = 0
            elif choice == "0703":
                crit.dev()
                break
            else:
                print("\nSorry ",choice," isnt a valid option")
            if crit.dev != 1:
                if crit.dead == 1:
                    print(f"im sorry your helldiver is dead...")
                    break
            else:
                if crit.dead == 1:
                    crit.dead = 0
                    crit.immortall()
                    break

main()
input("have a good day!.\nPress anything to exit: ")
exit()