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

# Insert new hero
create_hero(Luffy)

# Deleting 
delete_by_Value("Luffy")

create_hero(Luffy)

# Update hero property 
def updateHero(hero, property, newValue): 
    

# Read data 
def render_all():
    select_query = "SELECT * FROM heroes"
    rows = execute_query(select_query)
    for row in rows:
        print(row)

# Call the render
render_all()


