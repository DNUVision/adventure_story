from player import Player
import world
#from collections import OrderedDict



def play():
    print("Sinbad and the Roc")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        #choose_action(room, player)
        action_input = get_player_command()
        if action_input in ["n", "N"]:
            player.move_north()
        elif action_input in ["s", "S"]:
            player.move_south()
        elif action_input in ["e", "E"]:
            player.move_east()
        elif action_input in ["w", "W"]:
            player.move_west()
        elif action_input in ["i", "I"]:
            player.print_inventory()
        elif action_input in ["a", "A"]:
            player.attack()
        elif action_input in ["h", "H"]:
            player.heal()
        else:
            print("Invalid Action!")

def get_player_command():
   return input("Action: ")


play()

'''
actions = OrderedDict()
if player.inventory:
    actions["i"] = player.print_inventory
    actions["I"] = player.print_inventory
    print("i: view inventory")

def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Print Inventory")
    if isinstance(room, world.EnemyTile) and room.enenmy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action.adder(actions, "n", player.move.north, "Go North")
        if world.tile_at(room.x, room.y + 1):
            action.adder(actions, "n", player.move.south, "Go South")
        if world.tile_at(room.x + 1, room.y):
            action.adder(actions, "e", player.move.east, "Go East")
        if world.tile_at(room.x - 1, room.y):
            action.adder(actions, "w", player.move.east, "Go West")
    if player.hp < 100:
        action.adder(actions, "h", player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid Action!")
'''