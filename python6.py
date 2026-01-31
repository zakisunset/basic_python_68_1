"""
#
#Part : Functions
#
"""
def myFullName(firstName="Unknown", lastName="Donut"):
    return firstName + " " + lastName

print(myFullName("John", "Doe"))
print(myFullName("Rose"))
print(myFullName())
print(myFullname(lastName="Smith"))
print(myFullName("Alice","Johnson"))

def redPotion(hp):
    return hp + 50
def bluePotion(mp):
    return mp + 30

current_hp = 70
print("Current HP:", current_hp)
current_hp = redPotion(current_hp)
print("After using Red Potion, HP:", current_hp)