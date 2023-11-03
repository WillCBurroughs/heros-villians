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

# Clear off screen 
def clear_screen():
    import os
    os.system('clear')

# Prints out frames from rick roll
def print_frame(frame):
    clear_screen()
    for _ in range(40):
        print()
    for row in frame:
        padding = ' ' * 30  # Adjust padding for centering
        print(padding + row)

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

rick_dance = [
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
            """,
"""
:dddoooooooooooooodddxxddddooooooooolllllllllllllooddddooloolllllllclllllllloooooooooooooolllllllloc
cxxxddddddddddddxxxkkkxdxkkxkkkkkkxddoooddddoooodxkkkkkxxdddddddoolloooddddxxkkkxxkkxddddddooooooodl
cxxxxxxxxxxxxxxxkkOOkxxxkkkkOOOOOkkxdddddxxxdddxkkkkkOOOkkxdxxxxdoooodxxxkkkkOOOkxkkOkkxxddooodddddo
cxxxxxxxxxxxkkkkxxkkxxkOOOOOOOkkxkkkxxxxddddddddxkkOOOOOkxxxxxdddddoodddxxkOOO0OOkxkOOOkxdoooodddddo
cxxxxxxxxxkOOOOOkxxxxkOOOOkkkkxxxkOkxxxxdxxddolcloodkkkkxxxkkkxddddoodxddddxkkOO0Okxkkxddxxddddddddo
cxxxxxxxkkO00000OkkxxOOOkxxkOOkkkOOkxxxxxdl:;,,,',,;:loxkkkOOkkxddooddxxdddddxxkOOOkxdddxkkkxxxxxxxo
cxxxxxxkOO0000000OkxxxkxxxxkOOOkkkkkxxxxxo:,''''',,,,,;okkkkkkkkxdooodxdddxxxddxkOOkddxkkkOOOkkxxxxo
cxxxxxxkOO0000000OkxxxxkOkkkkOkkkOkxxxxxdl::::::cclc:;,lxkkkkkkkxddoodddddxxxddxxxddddkkkOOOOOOOkxxo
cxxkkkkkOO0000000OkxkOkxkkkkkkkO00Okxxxdlcccccllllool:;cdxxkkkkkxddoodxkxddddddxxxxdddkkOO000000Okkd
ckkkkkxxkkOOOOOkkxxxkOOkkxkO0OOO00Okxxxxocc:::cccccclc:lddddxxxddddoodxkkxxxxxdddxxxddxOO0000000Okkx
cxkxxxxxxxkOOOkxxxxxxxxxxxkOO0OOO0Okxxxxdol::::llcclllcoxxdddddddddoodxkkxxkOkxdxxkxxdxxkO000OOOkkOk
cxkOOkkkkkkxxxkkkkkkkkkxxkxxkOOkOOOkxxxxdolc:::cllllllldxxxddxkxddooodxkxxkOOkxdddxddxxxxkOOOkkkkkkx
cxkOOOOOOkkxxkkOOOOOOkxxkkkxxkkkkkkxxxxkkdoc:::clllllodddddddxxkxxdooddxddkkkxkkxxkkkkOOOkkkkkOOOOOk
cxkkOOOkkkxxxkkOkkOOkkxxxxxddxxkkkkxdddxxxol::ccllllloddddxkxddxxxdoooddxddxxxkkxdxkOOOO0OkxxkO0000k
cxxkkkkkkkkxxkkkkkkkkxddxxdddddkkkkxdddddool:cccclllloddxxkkkxdoddoooodxkxddddxxdddxkOOOOOOxxkO0000k
cxxdddxxxkxxxkxxddddddxkkkxddddxkkxdddddoool:c::cllllllcldxkkxxdodoooodxxxdddxxkxdddxxxkkOOkkk000OOx
lkxxxxxxxddddddxxxxddxkkkkxxxxddxkxddoolc:cl:::;:lllclc''',;:clloddooodxxdodddxkkkkxddddxxkkxkkkkkxd
cxdxkkkkkxddxxxkkkxddxkkkxxxkxdddxdlc;,'..:olc:::::cldc'.......',;cloodxdoodxddxkOOkxxxxxxddddxkkOOx
:ddxkkkkkxddxkkkkkxdodxkkxxkxdool:;'......;loollcclodd:'...........':odddoodxxdxkOkxdxkkkkkxddkOOOOx
cxxdxkkkxdddddxxxddddddxxddddo:'..........':cllolclll:'.............,lddddooddddkkxxxxkkkkkxddxOOOOx
ckkxxxxxxxxxxddddddxxxxdddddxl'.............';clc:;;,...............'cdddddddoodxxxkkxxxkkxdddxxkOkd
cxxxxddxxxxxxxdoddxxxxxdddxxx:...............;::;;;;'................:dddxxxxxdddxkOOkkxxxxxkkkkxxkd
ckkkxxdxkkxxxxdodxxxxxxxdddxd;...............,;;;;,,'.',,'...........;oddxxxkkxdxkkkkkkxxxxkkxkkkxkx
ckkkxddxkkkkkxdodxxxxxxxdoddl,...............';;,,,'.';:c:;,.........;odddxxxxddxkOOOOOkxxkkkkkOkxxx
cxxxxddxxxxxxdooodxdddxdoddol,................,;,,'..':::::,.........;odoooddddodxkkOOOkxxxkkxkkkxxd
cxxxdoddxxxxxdolodddddddodddl,................',,''...';::;'.........;odoooooddodxkkkkkkddxxxxxkxddd
:dddoooodooodolloooooddoooddc,.................,,'......,;;'.........,looolloddoodxxxxxdoodxddxxxddo
:dddoooooooooolloodddddooool:'.................,''.... ...............;lolllloooooddddddoooddddxdooo
:odoolooddoooolloooooddoolll:'.................''......................,llooollllodddddolloododddool
;loolllooooollcllooooooolllc:;;'...............''......  ..............;lloolllcllooolllllloooooooll
;llllllllllllccccllllllllc:::::;,...... .......''.......    .........':llllllllcclllllllcccllllllllc
,clcccclccccccccccccccllcc;,;;;:,...     .................   .......,cllllllllccccccccccccccclllllc:
,cccccccccccccccccccccccccc;,,;,..         ................ ..,;;;:cclccllllccccccccccccccccccccccc:
,::::::::::::::::::::cccccc:,....            .................;ccccccccccccccccccccccccccccccccccc::
,:::::::::::::::::::::::::c::,,...           ..,,,''..........,ccccccccccccccccccccccccccccccccc:::;
,:::::::::::::::::::::::::::::;......        ..,,,,,'.........':cccccccccccccccccccccccccccccccc:::;
""",
"""
dddddddddddoddddddxxkkxdxxxdxxxxxddooooooooooollodxxxxxdooooollollllllllloooddxdddxddooooooolloooooc
xxxxxdddddddddxxkkkkkxxxkkkkkkOOOkxddoodxxxddoodxxxdxxxxxddddxddoooooodxxxxkkkOkxkkkkxxxdddooooddddl
xxxxxxxxxxxxxkxxkkkkxxkkOOOOOOOkkkxxddddddddddddl:::::;;:loddddddooooodxxkkkOOOOkxxkOOOkxddooodddddl
xxxxxxxxxxkkOOOkxxxxxkOOOOkkkkxxxkkkxxxxddxxxdoc,'''..''',;coddoddooodddddxkkOO0OkxxkOkxdddooodddddl
xxxxxxxxxkO0000OkxxxkOOOOkxkkkxxkOOkxxxxxkkkxoc:;,,,,,;;;;,;oxxdooooodxddoddxxkOOOkxxxddxxxxdddddddl
xxxxxxxkOO000000OOkxkkkkxxkOOOOkkkOkxxxxkkkkxl;::cccllllll:;lxxxddooodxxddxxddxkOOOkxddxkkkkkxxxxxxo
xxxxxxkOOO000000OOkxxxxkkxkOOOkkkkkxxxxkkkOkxc;:::::clllllc:oxkxxdooodddddxxxdddxxxxdxxkkOOOOOkkxxxo
xxxkkxkOOO000000OOkxkkkkOkkkkkkOOOkxxxxxkkkkxlc::::::cccclclxkkkxdooodxxdddxdddxxdddddkkOOOOOOOOkxxo
xkkOkxkkOOOOOOOOOkxkOOkkxkkOOkkO00Okxxxxdxkxollc:::::cllllloxkxdddooodxkkxdddddxddxxddkOOO000000Okkd
xkkkxxxxxkOOOOkxxxxxxkkkxxkO0OkO00Okxxxxddddollc:::::clllllodddodddoodxkkxxkkxdddxkxddxkOO0000OOOkOx
xkkkkkkkkkkkkkxxxxxxxxxxxxxkOOOkOOkxxdddxxxxddoc:::::clllodddxddooooodxkxxkOOkddxxxdddxxxkO0OOkkkkkd
xkOOOOOkOkxxxkkOkkOOOkxxkkxxkOkkkkkxxdxxkkxxdolc::::cclloddddxxxxdooodxxdxkOkxxxddxxxxkkkkkkkkkkkkkd
dxkOOOOkkkxdxkkOkkOOkxxxkxxxxxxkkxxdddxkkxdoddl::::::ccloddxdddxxxdoooddddxxxxkkxdxkOOOO0OkxxkO0000x
dxkOkkkkkkxxxkkkkkkkkxddddddddxkkkxdddooolcloolcc:::cllllcldddodddoooodxxddddxxxdddkkOOOOOkxxkO0000x
dxxxxxxkkkxxkkkkxxxxdddxxxdddddxxxdllc;,''';ll:::c::ccclc,'';;:loooooodxxxddddxxdodxkkkOOOOkxk00000x
xxxdxxxxxxddxxxxdddddxkkkxddxdooc;,'.......,ll:;:cccclodc'......';:clodxddodddxxxxddddddxkkkxkOOOkkd
xxxxkkkkxddddxxxkkxdxkkkkxxxkdoc,..........';:;;:ccloddc,...........';lddoodxddxkOkxdddxxddxxxxkkkko
dddkkkkkkxdxxkkkkkxddxkkkxxkxdo;.............';:::::cl:'..............,ldoddxddxkOkxdxxkkkxdddkOOOOd
dddxkkkkxdddxxkxxxddddxxxdxxdo:'.............':lc::::;'..........';;,'':ddoddddxkkxddxkkkkkxddkOOOOx
xkxxxxxxddxdddxddddxxxdddddddc'..............'cl::::;,...........;ccc:,:ddddooodxxxxxxxxkkxdddxkOOOd
xkxxxdxxxxxxxddoddxxxxxddddxd:...............';:;;;;;'..........';cccc;cdxxxddoddxkOOkxxxxdxxxxxxkko
xxxxxdxxxxxxxddodxxxxxxdddxxo;................,;;;;;,'...........,:cc;,:dxxxxxdddxkkkkkxdxxkxxkkxxxd
xkkkxdxkkkkkkxoodxxxxxxdoddoc'...............',;;,,,'............';::'.:ddxxxxdddxkkkkkxdxxkkxkkkxxd
xkkxdddxxxxxxdoodxxdxxxdol:,'...........';;;,,,,;,,,..............';;'.,lddddooodxkkkOOkdxkkkkkkkxxd
xxxxdddxxxxxxdoodddddddol;.............';;;;,'',,,,'....................;loooddodxkkkkkxddxkxxxkxddo
ddddoodddddddoloodoodddol;.............,,;;,,..'''''.............  ......,:lodooodxxxxxxdodxxxxkxddo
ddddoooooooooolloooooddooc,....................''''.............     ......,loolloddddddoodddddxdool
oddoooooddoooolooooddddoll:'.............. ....''..............       .....,cllllodddddolloddodddool
looollooooooollloooooddollolc:;,,,,'...........''..............       ....,clllclloooooolllooooddooc
llllllllllllllcllllllollllooollllcc,............................       ..'clllllllllllllllllllllollc
clllccllllllcccccccccllllllllllllc:,...................................';clllllllllllllllllllllllcc:
ccccccccccccccccccccccllllllllllcc:'........ ......................':ccclllllllllllccccccccccllcccc:
:cc:::ccc:::::::::::cccccclllcccc::'.......  ....','................';ccclccllccccccccccccccccccccc;
::::::::::::::::::::::cccccccccc::;.......   ....''.......     ......':ccccccccccccccccccccccccc:::;
:::::::::::::::::::::::::ccc::::::;........  ....''........     ......;ccccccccccccccccccccccccc:::;
""",
"""
oddddddddooooooddddxkkxddxxdxxxxdddooooooooooollodxxxxxddoddolllllllllllloooodxdddxdddoddooolloooool
dxxddddddddddddxxxkkkxxdxkkxkkkkkkxddooodxddooodxxkkkkkkxxddddddoooloodddxxxxkkkxxkkxxdxxddooooooddo
dxxxxxxxxxxxxxxxkkkkxxxkkOkkOOOOkkxxdddddxxxdddxkkkOOOOOkkxxxxxxdoooodxxkkkkOOOOkxkkOOkkxddooodddddo
dxxxxxxxxxxkOOkxxxxxxxkOOOOkkkkxxkkkxxxxdddxxdddxkOOOOOkkxxxxxdddddooddddxkOOO00OkxkkOOkxddooodddddo
dxxxxxxxxkOOOOOOkxxxxkOOOkkxkxxxkOOkxxxxxxkkkkxxxxkkOOkkxxkOkkxdddddddxddddxxkOOOOkxxxxddxxddddxxxdd
dxxxxxxkkOO00000OkxxkOOkkxxkOOkkkOOkxxxxkkkkkOkkkkxxxxxkkOOOOkkxxddodxkxdddxddxkO0Okxddxxkkkxxxxxxxd
dxxxxxxkOO000000OOkxxxxxxxkOOOOkkkkxxxxxxxddooddkkkkxxkOOOOOkkkkxddoodxddxxkxddxkkkxxdxkkOOOOOkkxxxd
dxxkxxkOOO000000OOkxxkxkOkkkkkkkOOkxxxddl:;;,,,;:lloddxkkkkkkkkkkddooddxddxxxddxxxddddxkOOOO00OOkxxd
dxkOkxkOOO0OO0OOOkxxkOkxkkkOkkkO00Okxxdo:,''''''',,,:dxxddxkkkkxdddoodxkkxdddddxxxxxddkkOO000000Okkx
dkkkkxxxkkOOOOkkxxxxkOkkxxkO0OOO00Okxxddl::;:::;;''',cxxddddxxxddddoodkkkxxkkxdddxkkxxxOO0000000Okkk
dxxxxxxxxxkOOkxxxxxxxxxxxxkOOOOOO0Okxddoccclllooc;,',lxkkxxddxddddddodxkkxkOOkxdxxxxxdxxkO000OOkkkOk
dkkOOkkkkkxxxxkkkkkkkkxxkkxkOOOkOOkxxdoc::ccccllc;,,:dkkxxxdxkkkxdooodxkxxkOOkxxddxxxxxkkkOOOkkkkkkx
dxkOOOOOOkxxxkOOkkOOkkxxkkxxxkkkkkxxxdlc:cccc:clc;,;lxkxddxxxxxkkxddoddxdxkkkxkkxxkkOOOOOOkkkkOOOOOO
dxkOOOkkkkxdxkkkkkkkkxdxxxddddxkkkxxdol::clllllllc:coddddxkOkxdxxxdooodxxxxxxxkkxdxkOOOO00OkxkO0000O
dxxkkkkkkkxxxkkkxxxxxddxxxddddxkkkkxdol:::cccccccloooodxkkOOOkddddooodxkkkxddxxxdddxkOOOOOOkxkO0000O
xxddddxxxxxdxxxxdddddxxkkxdddddxkkxddol:::cccc:::odddoxkkkOOOkxdddooooxxxxdddxkkxdddxxxxkOOkkk000OOk
xxxxxkxxxdddddxxxxxdxxkkkxdxxdddxkxdool::::ccc:::lddooodxxkkkxdddxdooodxxddxxdxkOOkxddddxxxxxkkkkkkd
dddxkkkkkxddxxxxxkxddxkkkxxxkxdooolcclc;;;;:ccc:codddododdxxddooddoooodxdodxkxxkOOOkxxkkkxxdddxkOOOx
oddxkkkkkxddxxkxxxdoodxkxdddoc:;,''.,cl:;;;:cccll::clodddoooddoooodoooddddodxxdxOOkxxxkkkkkxddkOOO0k
dxxdxkkxddddddxxdddddddol:;,'.......,lolc:::ccloc,..',;cooddddddoddooooooddodddxkkxxxxkkkOkxddxkOOOk
xkxxddxxxxxxddddoddxxxo:'...........,clollcclooo:'......',;codxxddooooooodxxddddxxkOOkxxkxxxxxxxkkkx
dxxxxddxxxxxxdooddddddc'..............';::clodo:'...........,cdxxddoooodxxxkkxxdxkOOOOkxxxxkkkkkxxkx
xkkkxdxxkxxxxxoodddddo;................,;;;::c:;'............,lxxddooooodxxkkkxdxkOOOOkkxxkkkkkkkxkx
dkkxdddxxxxxxdoodddddl'.................;;;:::;,'.............cddoooooooodxkkxddxkOOOOOkxxkOkkkOkxxx
dxxxdddxxxxxxdoooddddc'.............'',,;;;;;;,,'.............cdoooooooooodddddddxkOOOOkxxxkkkkkkxxx
dxxdoodddddddollodddl;.............';::::;,,;,,,.............'coodoooloooooodxxddxkkkkkkddxxxxxkkddd
odddoooooooooolloooo:..............,;;:::;,,,,,'.............'coooooollooooooddoodxxxxxxdodxxddxxddo
oddoolooooooollloool,..............,,;;,''''''''.............,looooollllllloooooodddddddooodddddddoo
looollooooooolllool:................'......'''''.............'collllllllllooollllodddddolloododddooo
clllllllllllllclllc'.................. ....'''''..............:llllllccclloolllccloollllllllooooooll
clllccllllcccccccc,..................  .....''''.. ...........':llc:;,,;clllllcccclllccccccllllllllc
cccccccccccccccccc;..............       ..........  ...........';;,,'',;:cllccccccccccccccccccllllcc
:cccccccccccc::cccc,..........          ...........  ...       ...'''',;:cccccccccccccccccccccccccc:
::::::::::::::::::c:;'.....''.          ............  .        ...'''',;ccccccccccccccccccccccccccc:
:::::::::::::::::::::::;;:::;..          ............           ......,:cccccccccccccccccccccccc::::
;:::::::::::::::::::::::::::,..          ............              ...,ccccccccccccccccccccccccc:::;
""",
"""
dxxxxxxxxxxxxxxxkkOkxxxkOOkOOOOOkkxxdddddxxxdddxkkOOOOOOOkxxxxxxdoooodxkkkkOOOOOkxkkOOOkxxddoodddddo
dxxxxxxxxxxkkkkxxxkxxxkOOOkkOkkxxxkxxdxddddddddxxkOOOOOOkxxxxxdddddoodddxxkOOO00OkxkOOOkxddooodddddo
dxxxxxxxxxkOOOOkxxxxxkOOOOkxxxxxkOOkddolcccclllodxkkOOkkxxkkkkxddddoddxdddxxkkOOOOkxkkxxdxxddddxdddo
dxxxxxxkkOO0000OOkxxkOOOkxxkOOkxkOkxol:,'''''',:oxxxxxxkkkOOOkkxddoodxkxdddddxkOOOOkxddxxkkkxxxxxxxo
dxxxxxxkOOO00000OOkxxxxxxxkOOOOkxxoc;,'''''''',;okkxxxkOOkkOkkkkxdooddxddxxxxddxkOOkxxxkkkOOOkkkxxxo
dxxxxxkOOO000000OOkxxxxkOkxkkkkkkxc,'',;;::ccclcldxxxxxkkkkkkkkkxdddodddddxkxddxxxxddxkkOOOOO0OOkxxd
dxkkkxkOOO0OO000OOkxkOkxkkkkkkkOOOo;'';:ccllooolodxxkkxxxxxkkkkkxddoodxkxxddddxxxxxdddkOOO000000Okkd
xkkkkxxxkkOOOOOkxxxkkOkkxxkO0OkOOOo;',;:::cccllloxkkOkkxdddxxkxddddoodkkkxxkkxdddxkxddkOO0000000OkOx
dxxxxxxxxxkOOkxxxxxxxxxxxxkOOOkkOOd:;;:::ccc:clldkkkkkkkkxxddddddddoodkkkxkOOkxdxxkxxdxxkO0000OOkkOk
dkkOkkkkkkxxxxkkkkkkkkxxxxxxOOOkkOxl:::::ccc:clodxkkkkkkkxxdxkkkddooodxkxxkOOkxxddxxxxxxkkO0OOkkkkkx
dxkOOOOkOkxxxkOOkkOOOkxxkkxxxkkxkxxdoc::::cccclodxxxkkkxdddxxxkkkxdooddxdxkOkxkkxxkkkkOOOOkkkkOOOOOk
dxkkkOkkkkxxxkkOkkkkkxdxxxddddxkkkxddl:;::::ccloddddxxdddxkkkxdxkxdooddxxxxxxxkkxdxkOOO000OxxkO0000k
dxxkkkkkkkxxxkkkkxkxxdddxxdooddxkkxooc:;;;;:ccccloddoodxxkkOOxddddooodxkkxddxxxxdddkOOOO0OOkxkO0000k
dxddddxxxxxxxxxxddddddxkkxdddoodxdc;,::;;;;:cc:::::;:cldxxkkkkxdodooooxxxxdddxkkxdddxxxkOOOkkO000OOk
xxxxxxxxxddddddxxxddxxkkkxdxxoc:;'...;cc:::cc:;;:,'....';:ldxxdodddoooxxxddxxdxkkkkxddddxxkkxkOOkkkd
dddxkkkkkxddxxkxxxxddxkkxdoc:,'......'colccc:cc:;'.........,coooddoooodxdodxxdxkOOOkxxxkkxxdddxkOOOx
oddxkkkkkxddxkkxxxdooodoc;'...........;odolccloc;...........;odoooooooddddodxxdxOOkxxxkkkkkxddkOOO0k
dxxdxkkxddddddxxddodddl;..............';ccccccll;...........,lddoddoooooddoodxdxkkxxxxkkkOkxddxOOO0k
xkxxxxxxxxxxddddoddxxdc'................,::cc::c,...........,lxxddooooooodxxddddxxkOOkxxkkxxxxxxkOkd
dxxxxdxxxxxxxdoooddddo;.................';:::;;,............'cdxxdoooooddxxkkxxdxkOOOOkxxxxkkkkkxxkx
xkkxxdxxxxxxxdoodddddl,..................,::;;;,.............:dxxddooooddxxkkkxdxkOOOOkkxxkkkkkkkxkx
xkkxdddxxxxxxdoodddddc...................';;,,,,'............;oddoooooooodxkkxddxkOOOOOkxxkOkkkOkxkx
dxxxdddxxxxxxdolodddo;....................',,',,;;:;;,.......,ldoooooloooodddddddkOOOOOkxxkkkkkkkxxd
dxxdoodddddddollodddc'.....................'''',;;::::'......'looooolloodooodxxddxkkkOOkddxkxxxkxddd
odddoooooooooolloooo:......................''''',;;::;'.......;loooolllooooodxdoodxxxxxxdodxxdxxxddo
oddoolooooooollloool;.............. ........'......',,........':ooolllllllooooooodddddddoodddddxddoo
looolloooooolllloool,..............  .......'....  ..........':lllllllllllodollllodddddolloododddool
cllllllllollllcllll:'......,;;'...     .....'...............'cllllllllllllooollcllooolllllloooooooll
clllcclllccccccclll:......,;;;;,..      .................',;cllllllllcclllllllcccclllccccccllllllllc
cccccccccccccccccccc;.....'',;;;'.       ........... ..;ccllllllllllccccccccccccccccccccccccccllllc:
:ccc::ccccccc::ccccc:,......',,,..        .............:lllcccccccccccccccccccccccccccccccccccccccc:
:::::::::::::::::::::::,........          .',''........,:cccccccccccccccccccccccccccccccccccccccccc:
:::::::::::::::::::::::'....              .',,'.........;ccccccccccccccccccccccccccccccccccccccc:::;
;:::::::::::::::::::::;..                 .',,,'........,ccccccccccccccccccccccccccccccccccccccc:::;""",
"""
ddddddoooooooooooddxkxdddxxddxxdddoollllllllllllodxxxxxdooodolllllllllllloooddxddxxddddoddoolloooooc
ddddddddddddddddxxkkkxddxkxxkkkkkkxdooooolllllooxxxkkkkkxdddddddoooooodddxxxxkkkxkkkxxxxdddooooooddl
dxxxxxxddddxxxxxkkkkxxxkkkkkOOOkkxxdolc;;,',,,;cdkkkkkOkkkxdxxxxdoooodxkkkkkOOOOkxkOOkkkxddooodddddl
dxxxxxxxxxxkkOkxxxxxxxkOOOkkkkxxxxdl:;'.....''''cxkkOOOkxxxxxddddddooddddxkOOO00OkxkOOOkxddooodddddl
dxxxxxxxxkOOOOOOkxxxxkOOOkxxxxxxxo:,'.'''',,,,,;lxxkkkkxxxkkkkxddddodxxddddxxkOOOOkxxxxddxxddddddddl
xxxxxxxkkOO0000OOkxxkkkkxxxkOkkxo:'..''';:cllllodxxxxxxkkkOOOkkxddoodxkxdddxddxkOOOkxddxkkkkxxxxxxxo
xxxxxxxkOOO0O000OkxxxxxxxxxkOOkxl;...'',:ccllllodkkxdxkkOkOkkkkkxddoddxddxxkxddxkkkxxxxkkOOOOOkkxxxo
xxxxxxkOOO00000OOkxxxxxkkkxxkkxxl,''''';:ccccclloxxxddxkkkkkkkkkxddooddxddxxxddxxxdddxkkOOOO00OOkxxo
xxkOkxkOOOOOOOOOOkxxkkxxxxkkkxkkd:,;:;;;:ccllllloxxkkkxxdxxkkkkxdddoddkkkxdddddxxxxddxkOOO000000Okkd
xkkkkxxxkkOOOOkxxxxxkkkxxxkOOkkOko:;::::::cclllldxkkkkkxddddxxxddddooxkkkxxkkxdddxkxddkOO0000000OkOx
xxxxxxxxxxkkkkxxxddxxxxdddxkOOkkOko::::::::cllloxkkkkkkkkxxddxdddddoodkkkxkOOkxdxxxxxdxxkO000OOkkkOx
xkOOkkkkkkxxxxkkkkkkkkxxxxdxkkkxxxoc::::::::clloxxxkkkkkxxddxkkkddooodxkxxkOOkxxdxxxxxxkkkO0Okkkkkkd
dxkOOOOkkkxdxkkkkkkkkxdxxxxddxoc::c::::::::cooooodxxkkxxddxxxxxkkxddodxxdxkkxxkkxxkkkOOOOOkkkkOOOO0x
dxkkkkkkkkxdxxkkkkkkxdoddolc:;'..'cc::cccccllloooooddddodxkkkddxxxdooodxxxxxxxkkxdxkOOOO0OkxxkO0000k
dxxxxxkkkkxdxkkxxxxxdolc;,'.......;llccccccol;;::::;:codxkkkkxdddoooodxkkxdddxxxdddkkOOOOOkkxkO0000x
xxdddddxxxddxxdddooc;,'...........,ldollccldo:;;:;,'.',:oxkkkkdoodooodxxxxdddxkkxdddxxxkkOOkkO000OOx
xxdxxxxxddddddddddc,...............;cllcclol:,;;:,'.....;dkkxddodxdoooxxxddxxdxkOkkxddddxxxxxkkkkkko
dddxkkkkxddddxxxdo;.................';:::::;'.,;;'......'lxddoooddoooodxdodxxxxkOOOkxxkkkxxdddxkOOOd
dddxkkkkxdoodxxddl'..................,:::::,..,c:'......'codddooooooooddddodxxdxOOkxxkkkkkkxddkOO00x
xxddxxxxdoooodddo;....................;::::,..;l:'.......:odddddoddooooooddodxdxkkxxxkkkOOkxddxOO00x
xkxddddddxxddooo:'....................';:::,..':;........;odddxxddooooooddxxddddxxkOOkxxkkxxxxxxkOkd
xxxxdddxxxddddol,......................';;;'...''........,oddxxxxddoooodxxxkkxxdxkOOOOkxxxxkkkkkxxkd
xkkxdddxxxxxxdo:........................,;;,...''........'cddxxxxddooooddxkkkkxdxkOOOkkkxxkkkkkkkxkd
xkxxdodxxxxxxdl,.......................',::;,'''..........;ooddddoooooooodxkkxddxkOOOOOkxxkOkkkOkxxd
xxxxdodxxddddol,.....................',,;::;,..'..........,looooooooooooooddddddxkkOOOOkxxkkkkkkkxxd
dxxdoooddddddoc'.....................',,;::;'..'..........'ldooooooooloodooodxdddxkkkkkxddxkxxxkxddo
oddooooooooooo:.......................'''''................';cclooollooooooodddoodxxxxxdoodxddxxxddl
oddolloooollooc'................................................,;;;:cllllllooooodddddddoooddddddool
oooolloooooolll:'..................... ................        ..'',,,,;:cclllllloddddoolloododddool
lllllllllllllcclc::;;,,'.....           ..................     ...',,,,,;:ccclcclloolllllllooooooolc
clccccccccccccccllllllc;.........        .............,::;,'........',;;:::cccccclllllcccccllllllll:
ccccccccccccccccccccccc,..........        .......... .,cllllcc::;,,';cccccccllcccccccccccccccllllll:
:cc:::ccccccc::ccccccc:,.........         .......... .'cllllllllllllccccccccccccccccccccccccccccccc:
:::::::::::::::::::ccc:,........          ..'....... ..:cccccccccccccccccccccccccccccccccccccccccc:;
::::::::::::::::::::cc:'........           .'.......  .:cccccccccccccccccccccccccccccccccccccccc:::;
""",

"""
dxxxxddddddddddxxxkkkxddxkkxkkkkkkkddooodxxdooodxxkkkkkkxdddddddoollooodddxxxkkkxxOkxxddxdddoooooooo
xxxxxxxxxxxxxxxxkkOkkxxxkkkkkOOOOkxxddddxxxxdddxkkkkkkOOkkxdxxxxdoooodxxxkkkkOOOkxkOkkkxxxddoooddddd
xxxxxxxxxxxxkkkxxkkkxxkOOOOOOOkkxkkxxxxxdddddddxxkOOOOOOkxxdxxdddddoodddxxkOOO0OOkxkOOOOxddooodddddd
xxxxxxxxxxkOOOOkxxxxxkOOOOkkkxxxkOOkxxxxdxxkkkxdxkkkOOOkxxkkkkxddddoddddddxxkkOOOOkxkkkxxddddoddxddd
xxxxxxxxkkO0000OOkxxkOOOkxxkkkkxkOOkxxxxkkkkkOkkxxkxkkkkkkOOOOkxdddodxkxdddddxkOOOOkxxddxkkkxddxxxxd
xxxxxxkkOO000000OOkxxkkxxxkOOOOkxkkkxxxxkkkkkkkkOkkkxxxOOOOOOkkkxddoddxxdxxxxddxkOOkxxxxkkkkOkxxxxxd
xxxxxxkOOO0000000OkxxxxkkkkkOOkkkkkxxxxddolccccldxxxxxxkOkkkkkkkkddoddddddxkxxddxxxxdxxkkOOOOOOOkxxx
xxkkkxkOO00000000OkxkkkkkkkkkkkO00Okxxoc;,,,''',;::coxxxxxkkkkkkxdddddxkxddxdddxxxddddxkOOOO0000Okkx
xkkOkxxkkOOOOOOOkkxkOOOkxxO00OOO00Okxdo:,'',,;;;;,,,cxkxdddxkkkxddddddkkkxxxxxdddxxxddxOO0000000Okkk
xxxxxxxxxkOOOkkxxxxxxkkxxxkO0OOO00Okxdlc::cccllll:;,:dkkxxddddddddddodkkkxxOOkxdxkkkxdxkkO0000OOOkOO
xkkkkkkkkkkkkkkkkkkkkkxxxxxkO0OkOOOxxoccc:cclllllcc;:dkkkxxdxkkxdddoodxkkxkOOkxxdxxdddxxxkO00Okkkkkk
dkOOOOOOOkxxxkOOOOOOOkxxkkkxkOkkkkkxxdlc:;;:ccccllc:cxkxxdddxxkkkxdoodxxdxkOkxkkxxkkkkkOOkkkkkOOOOOO
dxkOOOOkkkxxxkkOkkOOkxxxxxxxdxxkkkxxxdolc:::cllllllllddddxkkxdxxkxdoodddddxxxxkOxdxkOOOO0OOkxkO0000O
dxkkkkkkkkxxkkkkkkkkkxddxxddddxkOkkxddolc:::ccccclllloddxkkOOxdddddoodxxkxdddxxxxddkkOOO0OOkxkO0000O
xxdxxxxxkkxxxkkxddxdddxkkxxddddxkkxxddddl:;;:c:::lododxxkkkOOkxdooooooxxxxdddxxkxddxxkkkOOOkkkO000OO
xkxxxxxxxxddddxxxxddxkkkkxxxxdddxkxddddxoc:;:c:;:loooodxxxkkkxdddddooodxxdddxdxkkkxxddddxxkkxkOOOkkx
xxdxkkkkkxddxxkxkkxddxkkkxxkkxddxkxdddddo::;;:c::looooooddxxddoodddooodxdodxxddkkOOkxxxxxxdddxxxkkkk
dddxkkkkkxddxkkkkkxdodxkkxxkxxxxdxdoollol:;;;:clllll:;clooddddooddoooodddoodxxdxkOkxxxkkkkkxddxkOO0O
dxdxkkkkxddddxkxxddddddxxdxxddddolc;,,;cl:;;;:collol;...',;:cloooddoooooddoodxdxkkkxxxkkkkkkddxOOO0O
xkxxxxxxxxxxdddddddxxxddddddolc;,'....'cdl::::cloodl,........',;clddooooodddddddxxkkkxxxkkxddddxkOOk
xxxxddxxxxxxxdooddxxxxdddddl,'........'coolcccccloo:'............,cddooodxxkxdddxxOOOOkxxxxxkkxxxkkx
xkkxxdxxxxxxxxdodxxxxxxdodo;...........',;:::cccc:;'..............;odoodxxxkkkxdxkkOkkkxxxxkkxxkkxxk
xkkxxdxkkkkkxxoodxxxxxxdooc'.............',;;;;;;,'...............'ldoooddxkkxddxkOOOOOkxxkkkkkOkxxk
xkkxdddxxxxxxdoodxxdddddoo;...............,;;;;;,'.................;odoooodddddddxkOOOOkxxkkkkkkkxxk
xxxxdodxxxxxxdoodddddddool,..........',,,',;;;;;,'.................'cooooooooddddxkkkkOkxdxkkxxkkxdx
ddddoodddddddolloooooooolc'........,;;;;,',;;,,,,'..................;ooooooldddoodxxxxxxdodxxxxxxddd
ddddoooooooooolloooooooolc'.......,;;,;,,',,,,,,,'..................'cooolllloooodddddddooodddddddod
oddolooddoooolllooooodool:'.......,;;;;,'..',,',''...................;loolooollllodddddooloddddddooo
looolloooooollclooooooolc,........,,,''.....'''''....................':lllooollclloooooolllooooodoll
lllllllllllllccclllllllc,............. ......''''.....................'clllllllcclllllllccllllllllll
clllccllllclccccccccccc:'............  .......'''..............   .....:lllllllcccllccclcccclllllllc
cccccccccccccccccccccccc;...........   ........''..............  ......:llllllccccccccccccccccclcccc
:cc:::ccc::::::::::::ccc:,........     ........'..............      ...;ccccccccccccccccccccccccccc:
::::::::::::::::::::::::::;,,'',,..    .....................        ...',;:cccccccccccccccccccccc:::
::::::::::::::::::::::::::::::::;.....  .................. .        ....'',;::cccccccccccccccccc::::
;:::::::::::::::::::::::::::::::,...     ..........'','...         .......'';:cccccccccccccccccc::::
""",
"""
lxxxxxdxdddddxxxkkkkkxxxkkkkkOOOOkkxdddddxxxdddxkkkkOkOOkkxxxxxxdoooodxxkkkkOOOkkkOOkkkxxddoooddddd:
lxxxxxxxxxxxkkkxxxkkxxkkOOkkOOkkxxkxxdxxdddddddxxkOOOOOOkxxxxxdddddooddxxkkOOO0OOkxkOOOkxddoooddddd:
lxxxxxxxxxkOOOOOkxxxxkOOOOkxxxxxxkOkxxxxdxxkkkxdxkkOOOOkxxkkkxxddddoddddddxkkOO0Okxxkkxxxxddodddddd:
lxxxxxxxkkO0000OOkxxxOOOkkxkkkkxxkOxdddoodxxkkkkxxxkkkkkkkOOOkkxddoodxkxdddddxkOOOkxxxdxkkkxxddxxxd:
lxxxxxxkOOO00000OOkxxxkxxxxkOOOkxxdlcc:;,;;:codkkkkxxxkOOOOOkkkkxdoodxxddxxxxddxkOOxdxxkkkOOkkxxxxx:
lxxxxxxkOO0000000OkxxxxkkkkkkOkkkxl;''''''',,,;oxkxxxxkkkkkkkkkkxddooddddxxxxddxxxxddxkkOOOOOOOOkxx:
lxxkkxkkOO000000OOkxkkkxkkkkkkkOOxl:,,,;;:::;,,cdxxxkkxxxxkkkkkkxdodddxkxdddddxxxxxddxkOOO00000Okkkc
lkkkkkxxkkOOOOOkkxxxkOOkxxkOOOkOOdccccclllool:,:dxkkOOkxdddxkkxddddodxkkkxxxxxdddxkxdxkOO0000000Okkl
lxxxxxxxxxkOOkkxxxxxxxxxxxkOOOkkOxlc:::ccccllc;cxkkkkkkkxxdddddddddoodkkkxkOOkxdxkkxxdxkOO000OOOkkOl
lxkkkkkkkkkxxxkkkkkkkkxxxxxxkOOkkkdc:;:cccccllclxxkkkkkkkxxdxkkxdoooodkkxxkOkxxddxxddxxxkkO0Okkkkkkc
lxkOOOOkOkxxxkkOkkOOOkxxkkxxxkkkxdol::::lllllllodxxkkkkxdddxxxkkkxdoodxxdxkkxxkkxxkkkkOOOkkkkkOOOOOl
cxkkOOOkkkxdxxkOkkkkkxddxxddddxkkxdlc:::clllllooodddxxdddxkkxddxkxdooddxxdxxxxkkxdxkOOO00OkxkOO0000l
cxxkkkkkkkxxxkkkkxkkxdddxxdddddxkkxdl:::cccclc:ccoddooddxkkOkxddddooodxkkxdddxxxddxkOOOO0OkxxOO0000l
lxxddddxxkxxxxxxddddddxkkxxddddxxkxdlc:::ccccc:;coxdoodxxkkkkkxdooooooxkxddddxkkxddxxxxkOOOkkO000OOl
lkxxxxxxxddddddxxxxddxkkkxxxxdddxxdolc;;;:cclc;;:c:::cloddxkxxdoddooodxxxddxddxkkkxdddddxxkxxkOkkkxc
lxdxkkkkkxddxxxxxkxddxkkkxdxkxdolc;,:c:;;;:cccc:;'.....'',:cclooddoooodxdodxxdxkOOOxxxxkkxdddxxkOOkc
cddxkkkkkxddxxkxxxxdooxkxdxxdl:,'...;ll::::::lol;............,cooooooodddoodxxdxOOkxxkkkkkkxdxkOO0Ol
lxxdxkkxxdddddxxxddddddddol:,'......'coolc::lddo;.............,loddoooooddoodddxkkxxxkkkOkkxddkOO0Ol
lkkxddxxxxxxxdddoddxxxdl:'...........;cllc:clllc,..............:dddoooooddxxddddxxkOkxxxkxxxxdxkOOkc
lxxxxddxxxxxxddoodxddddc'..............,;;;:::;,...............;oddoooodxxxkkxddxkOOOkkxxxkkkkxkxxkc
lkkkxddxkkxxxxdoddxddddc................,;:::;;,...............'ldddoooddxxkkkxdxkOOOOkxxxkkkkkkkxkc
lkkxxddxkxxxxxooddxdddd:................';;;;,,,................:odoooooodxkxxddxkOOOOOkxxkOkkOOkxkl
lxxxdodxxxxxxdooodddddo;.................,;;,,,'................,looooooooddddddxkOOOOOkxxkkkkkkxdxc
cxxddodddddddollodddddo;..................,,,,,'................'coooooooooodxdddxkkkkkxddxkxxxkxdxc
cdddoooooooooollooooool;...................'''''.......,;;,,'...':looloooolodddoddxxxxxdoddxddxxddd:
cdddoloooooooollooooool;...................'''''......',;;:::,....,clllllllooooooddddddooodddddddoo:
:ooollooddooolllooooool:,'.... .............'''........',;;::;....,cllllllooolllooddddoolloooodddoo;
;lllllllllllllcllllllll:;;;;'.. ... ........'''...    ....,,,'...,clllllllllllcclloolllllllloloooll;
;lllcclllcccccccccccccc:;:::;'.      ........''....      .......'cllllclllllllccccllcccccccllllllll,
;cccccccccccccccccccccc:;;::;,.        ... ..'''......   ....',:cllllccccccccccccccccccccccccclllcc,
,cccc:ccccccc::::cccccc:;,;,,..         ...............  .';:ccllcccccccccccccccccccccccccccccccccc,
,:::::::::::::::::::::::,'....           .................':ccccccccccccccccccccccccccccccccccccc::'
,:::::::::::::::::::::::;'''..            .................;cccccccccccccccccccccccccccccccccccc:::'
"""
  ]


user_continue = True

while(user_continue): 

    user_Actions = ["create", "read", "update", "delete", "rick"]

    userChoice = input("Hello What Would you like to do?: (*Create, Read, Update, Delete, Rick*) ").lower()

    # Action that can not be done 
    if(userChoice not in user_Actions): 
        print("That is not a supported action. Supported actions are: create, read, update, delete, and rick")

    # delete functionality
    elif(userChoice == "delete"):
        see_list = input("Would you like to see the current list of heroes? (y/n) ").lower()
        if(see_list == "y"):
            render_names()
        choice_delete = input("Which user would you like to delete? ")
        delete_by_Value(choice_delete)


    # Updating value within table
    elif(userChoice == "update"): 
        see_list = input("Would you like to see the current list of heroes? (y/n) ").lower()

        if(see_list == "y"):
            render_names()
        
        possible_properties = ["biography", "name", "about_me"]
        selected_character = input("What character would you like to update? ")

        

        selected_property = input("What property would you like to change(biography, name, about_me) ")

        # Making sure value is acceptable value 
        while(selected_property not in possible_properties):
            print("Selected property not available")
            selected_property = input("What property would you like to change(biography, name, about_me) ")

        newValue = input("What new value would you like to add? ")

        updateHero(selected_character, selected_property, newValue)
        print(f"{selected_character} {selected_property} changed to {newValue} ")

    # Create new value for table 
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
        
    # Rick the table 
    elif userChoice == "rick":
        for _ in range(3):  # Repeat the dance three times
            for frame in rick_dance:
                print_frame([frame.center(100)])
                time.sleep(0.2) 

        
    # Render current table for user 
    elif userChoice == "read":
        render_all()
        continue_input = input("Would you like to continue? (y,n) ").lower()

        if(continue_input == "n"):
            user_continue = False
    
    


