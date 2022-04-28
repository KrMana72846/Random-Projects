import random

def generate_role(homes,allies,allegiance, human, pet):
    home = random.choice(homes)
    ally = random.choice(allies)
    faction = random.choice(allegiance)
    if ally == "Double":
        
        ally1 = random.choice(human)
        ally2 = random.choice(pet)
        
    print("Home:",home)
    if ally == "Double":
        print("Your rolled double companions!")
        print("Ally 1:",ally1)
        print("Ally 2:",ally2)
    else:
        print("Ally:",ally)
    print("Allegence:",faction)

def generate_profession(role):
    role1 = open("Fallout Roles.txt",'r')
    role2 = open("Fallout Roles Male.txt",'r')
    role3 = open("Fallout Roles Female.txt",'r')

    if role == 0:
        i = -7
    else:
        i = 0
        
    j = (role-1)*8
    while i < j:
        role1.readline()
        role2.readline()
        role3.readline()
        i+= 1
    k = i    

    lines = 8
    if role == 1 or role == 2 or role == 4 or role == 8:
        lines -= 1
    elif role == 6:
        lines -= 2

    print("You:")
    while i < j+lines:
        roleplay = role1.readline()
        print(roleplay)
        i+= 1
    if role == 10:
        roleplay = role1.readline()
        print(roleplay)
        
    i = k
    lines = 8
    if role == 1 or role == 7:
        lines -= 1
    elif role == 3 or role == 5 or role == 6 or role == 8 or role == 9: 
        lines -= 2
        
    print("You Male Alternative:")    
    while i < j+lines:
        roleplay = role2.readline()
        print(roleplay)
        i+= 1
    if role == 10:
        roleplay = role2.readline()
        print(roleplay)

    i = k
    lines = 8
    if role == 1:
        lines -= 1
    elif role == 2 or role == 3 or role == 4 or role == 5 or role == 7 or role == 8: 
        lines -= 2

    print("You Female Alternative:")    
    while i < j+lines:
        roleplay = role3.readline()
        print(roleplay)
        i+= 1
    if role == 10:
        roleplay = role3.readline()
        print(roleplay)    

    
    



homes = ["Wanderer","Dino Dee-lite motel","Bon Vivant suitez","Victor's Shack","Lucky 38 suite","Wolfhorn Ranch","Faction Housing","Vault 21","Harper's Shack","The Tops Suite"]
allies = ["Double","Gannon","Raul","Boone","Cass","Rex","Veronica","Lily","ED-E","Loner","Willow","Joana","Sunny Smile"]
allegiance = ["House","Legion","NCR","Independant"]
human = ["Gannon","Raul","Boone","Cass","Veronica","Lily"]
pet = ["ED-E","Rex"]


answer = 'yes'
while answer == 'yes' or answer == 'y':
    total = 41
    while total > 40:
        s = random.randint(1,10)
        p = random.randint(1,10)
        e = random.randint(1,10)
        c = random.randint(1,10)
        i = random.randint(1,10)
        a = random.randint(1,10)
        l = random.randint(1,10)
        total = s + p + e + c + i + a + l
        remainder = 40 - total

    generate_role(homes,allies,allegiance, human, pet)
    role = random.randint(1,10)
    print("Special Stats")
    print("S:",s)
    print("P:",p)
    print("E:",e)
    print("C:",c)
    print("I:",i)
    print("A:",a)
    print("L:",l)
    if remainder > 0:
        print("Remaining S.P.E.C.I.A.L points:",remainder)
    print("")
    print("Roles to play")
    print("")
    show = input("Show roles? type y or yes ")
    if show == 'yes' or show == 'y':
        generate_profession(role)
    
    
    answer = input('Would you like to roll again? type y or yes ')
    print("")

input('press enter to exit')



