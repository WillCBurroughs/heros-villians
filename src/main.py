import time
from database.db_connection import execute_query, execute_modify


# Function to delete (Delete)
def delete_by_Value(name): 
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))
    
    if result:
        delete_query = "DELETE FROM heroes WHERE name = %s;"
        execute_modify(delete_query, (name,))
        print(f"Deleted hero: {name}")
    else:
        print(f"Hero not found with name: {name}")

# Defining Hero class 
class Hero:
    def __init__(self, name, bio, description):
        self.name = name
        self.bio = bio
        self.description = description

# Create new hero (Create)
def create_hero(hero):

    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (hero.name,))

    if result:
        print(f"Hero already present: {hero.name}")
    else:
        print(f"Hero not found with name: {hero.name}")
        insert_query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s);"
        execute_modify(insert_query, (hero.name, hero.bio, hero.description))

# Adding new ability
Luffy = Hero("Luffy", "King of the pirates", "He is Dylan")

# Update hero property (Update)
def updateHero(name, property, newValue):
    check_query = "SELECT id FROM heroes WHERE name = %s;"
    result = execute_query(check_query, (name,))
    possible_properties = ["biography", "name", "about_me"]


    if property not in possible_properties:
        print(f"Hero {name}: does not contain {property} possible properties are (biography, name, about_me)")
    elif result and property in possible_properties:
        print(f"Hero exists: {name}")
        # Build the update query with string concatenation
        update_query = f"UPDATE heroes SET {property} = %s WHERE name = %s;"
        execute_modify(update_query, (newValue, name))
    else:
        print(f"Hero not found with name: {name}")

updateHero("Chill Woman", "name", "Super Chill Woman")

# Read data 
def render_all():
    select_query = "SELECT * FROM heroes"
    rows = execute_query(select_query)
    for row in rows:
        print(row)

# Allows for seeing names of characters 
def render_names(): 
    select_query = "SELECT * FROM heroes"
    rows = execute_query(select_query)
    for row in rows:
        print(row[1])



user_continue = True

while(user_continue): 

    user_Actions = ["create", "read", "update", "delete", "rick"]

    userChoice = input("Hello What Would you like to do?: (*Create, Read, Update, Delete, Rick*) ").lower()

    if(userChoice not in user_Actions): 
        print("That is not a supported action. Supported actions are: create, read, update, delete, and rick")

    elif(userChoice == "update"): 
        see_list = input("Would you like to see the current list of heroes? (y/n) ").lower()

        if(see_list == "y"):
            render_names()
        
        possible_properties = ["biography", "name", "about_me"]
        selected_character = input("What character would you like to update? ")
        selected_property = input("What property would you like to change(biography, name, about_me) ")

        while(selected_property not in possible_properties):
            print("Selected property not available")
            selected_property = input("What property would you like to change(biography, name, about_me) ")



    elif(userChoice == "create"):
        
        finished_Character = False

        while(not finished_Character):
            name = input("What is your name? ")
            about_me = input("Can you give us a quick description of yourself? ")
            biography = input("Can you give us your background? ")
            new_Hero = Hero(name, about_me, biography)
            create_hero(new_Hero)
            done = input(f"""
Is this how you would like your character (y/n)?  
Name: {name}
About Me: {about_me}
Biography: {biography}
""")
            if(done == "y"):
                finished_Character = True
                print("Character created and added")
        

    elif userChoice == "rick":
        print(
            """
00000000000KKKKK0KKKXKK0OOOOOOO0KXXXKK0000O00OkkkkOOKKXKXXXXKKK00OkxkkxkkkO00KKKKKKK000000000OOOOOkx
000000KKK0KKKKK00000000O000O0000KK000OkkkkkkkkkkkkkkkkkO00000KKKK0Okkkxkkkk0KKKKKKKKK000000000000Okk
000KXXXXK0KNNXXKKKK00000000000000OOkkkOOOkkkkkdcc::::;;:loxOOOOOOOOkxxkkkkkkOOO00000000000000000OOkk
KKKXXXK000XNXXXXXXXXXXXXK0000000KK000OOOOOkkkdc,''''',,',;:okkkkkkkxxxkkkkkkkO0000KXXXXKKXXXK00OOkkk
XXXXKK00KKXNXXXXXXXXXNNXKK00000KKXXXKK0OOOOOxo:;;;;,,;;;,,,;oOK00OkkkkkkkO000KXXXXXNNNNKKKXNXKOkkkkk
XXXXKKKKXXNNXXXNNXXXKKKKK0000KKKKK0000OOOOOolooooddddddddl;,lO00OOkkkkkkkk0KKKKKXXXXNNXK0000000OOkkk
0KKK00KXNNNNXXKKKK0000KKXK000KKK0000000OOkxlldolooddxxxxkdc;okkkxkkOOkxkkkkkOO00KXXXNNNXKK0OOO0KK0OO
0000KXNNNNNXK00000000KXXNK0000K000KXXXXXKOkxdoc:cllodoooddc:x0OkkkkOOkxkkOOkxkkk000KXXNNXK0OkOO00OOO
K000XNNNNXK000KXXK000KNNNXK000KKXXNNNXXNXOxkxollccloxdooddlxKKKKOkkkkkkkk000OkkkkkkO0KXXXK0OkkOOOO0K
XK00KKKK00000KXXNNXXKKXNNXKKKKKXNNNNNXXXXOdkkolllllodxxxxddkKKKK00Okkkkkk0K0OkkkO0OOkOO0KKKKOOOO00KN
X0000000KK000KXXNXKKKKKKKKKKK0KXNNNNNXXXXKOOkollcloodxxxxxk0KKKKKK0kkkkkk00OkO000K0OkkkkOO0K0OO0KXNN
X000KK00KXXK000KXK00KXXXKK0KK0KNWWNNNXXXXKKKkollcllodddxkO0KKKKKK00kxkkkkkkOkkO00KK0OkkkkkkOOO0KXNNN
X00KXXK00KK00KK0000XNNNNXK00000KXXNNNXXXK0OOxolllooddddxO0KK0K0K000OkxxkkkO00OkO0K0OkkO00OkO0000XNWW
000KNNXK0000KXXXK00XNNNNX0000KK00KKXXXX0OkkkdllccllooddxxxO0KKK00kkkkkkxxO0KKK0OOOOOOkO0OOOKXK0KXNWW
0000KKKKK0O0KNNNNK0KNNNNK000KXXK0OO00OOOkOOxdlllodddddxxc,cdkOOOOkkOOkkkkO0KKXKO0KXK0OkkkO0XNK00KXNN
OO00000OOOOO0KXXXX00XXXXK00000000000OkxxkOkdooollooodxOd;...';:clodxxkkkkk00KK0OKXXKKOkkO0XXXXK000KK
00KKKK0OO0K0OOKXXX00KXXK0OOOOOO000Oxoc:cxOkdooollodxk0kc............';:coxO000OOKXXK0kkkkkOOOO0OO000
XXXXXK0O0XXK0OOKXK0OO000OkkOOkxdlc;'...;dkkoccldxOOOOx:..................;x00OkOKKK0kkOkkkO0000000KK
XXXXK0OO0XKK0OO0000000OOOkkkkl,'.......':cllcclddxxxo;....................lOOkkk00OkkO00OkkOKKKKKKXX
XXXXKOOOOOOOOOkkOOKXXXX0OOkkx;............:c::lollll;.....................,okOOkkkkxkO0K0kxk0KKKKKXX
XKKK0OkOO00OOkkkkOKXXXNKOOOkd,............;cllcclcc:'......................;k0OOkkxxxkkOOOkkOKKKKKXX
0OOkkOO0KK00OkkkkO0KXKXKOkkkd,............;cddc:c::,.......................,dO0OkkxxkO00OkkkO00KKKKK
OkkO0KKKKK0Okk0OkkO0KXXKOkkko,............;lxdc::;,.........................,dOOkkkkkOKXK0OOkkkOOOOO
0Ok0KKKKK0OkkOK0OkkOKXX0OOkkl.............;lddc::,...................   .....,coxkO0kOKXXXXK0Okkkkkk
0OkO0KKKK0OkO0K00OOO0KX0OOkkl.............,:c:::;'......,:::;;;,.....  .........,lk0OO0XXXNNXKOOO00O
0kkkk0KKK0kk0K0OOO00O0K0Okkkl'............';:::;,.......;cclloolc'...   .  ........:okO0XXXXXKOO0K00
OxkkkO000OkO00kkkk0KOO00kkkkd'... .........,::;;'........,:clllloc'..... ...........'okO0KXK0OkO0K00
kkOOkkxkkxxkkxxOOOOOOOOOkkxko'...  ........,;;;,..........,:cllloo:..................lkkOKK0OkkOO000
O0000kxxxxxxxxO00KKOkkkkkkxxl'...   .......,;;,'.......  .....';cl:'.................:xxkOOkOOOOkkkk
OOOO0OkxddxxkO000KKK0Okkkxxxc'.....',,,,''.,;;,'.   ..         ..... ..''............,oxxxxk0000Oxdd
kkkkkkkxddxkkkOO000000Okkxxxo;..':clllc:;..,;,,..                    ...'...........,ldddxxkOOOOOkxd
OOOkkOkxdddxkkOO00000Okkxxxxd,.',,::;;;;,..';,'.                       .,''..'',,;coxxddddxxkkkkkkxd
kkkkkkkdoooodxkOO0Okkxxxxxdxdl;'..';;;;;'..',,'.           ...         ;dddddddxxkkkxxdoodxkkkkkkkxx
kkkkkkxdooddodxkOkxxxxxxxxddxdl:;...,,,'. .'',..                       'oxxxddddxxxxdooooodxxxxxxkxx
xxxxxxxooodxdooddddxkkxdddddxxdooc,'....   .''.                   ......cddddddddddddddooodxxxxxxxxd
xxxxxxdooodxxddodxkkOkxdddddxkkxdolol;......'..                  .......:odddddddddoddddooddxddxdxxd
ddddddolloddddoodxkkkxddddddxkkxdolol,....,;,'.                   ......'ldodddddddddddooooddddddddd
ooooooolloddooooodxkkxdddooodxxdolll:'....,;,'..                  .......:ooodoooooooddooooodddddddd
            """)
    elif userChoice == "read":
        render_all()
        continue_input = input("Would you like to continue?")
    
    

# user_continue = False÷
