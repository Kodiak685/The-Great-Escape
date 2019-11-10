print('\n' * 100)
print('You wake up in a dark room with no memory of how you got there. Your head is throbbing.')
name = input('Now what was your name again?\n')
print('\nAh yes of course, your name is {}!'.format(name), '\nThe only other thing you can remember',
      "is that you can pick up an item by saying 'pick up (item name)', use an item by saying 'use (item name)', and go to an adjacent room by saying 'go to (room name)'")

gameEnd = False

items = []
roomDesc = {'closet': "It is dark and damp, you feel around and find what appears to be a match.",
            'kitchen': "The kitchen looks old and has a fine layer of dust. There is a crowbar laying on the counter and an unlocked door on the other side of the room that appears to lead to a store room. There appears to be something written on the wall but it is covered up by years of grease and grime.",
            'store room': "The storage room is covered with a layer of dust, but in the corner there is just about the most massively useful thing that any interstellar hitchhiker can carry, a towel. The room also has another door that appears to be jammed. The kitchen is behind you.",
            'parlor': "The parlor is a large room that has obviously been out of use for a long time. There are three doors including the one you just entered through. One door leads outside but is locked and the other door is unlocked and looks like it to goes to a glowing room. There is a battery laying on the floor. The store room is behind you.",
            'glowing room': "The mysterious glowing room is filled with a pulsing green light. It radiates from a pillar in the middle of the room. The pillar has a keypad on it. The parlor is behind you."}
roomItem = {'closet': "match", 'kitchen': "crowbar", 'store room': "towel", 'parlor': "battery",
            'glowing room': "No item seen"}
itemUse = {'match': "You strike the match and light up the closet revealing a door that appears to go to a kitchen.",
           'crowbar': "You manage to unstick the door so it is now useable, on the other side is a parlor.",
           'towel': "You wipe the grime off the wall revealing 4 numbers written behind, 8253",
           'battery': "As you place the battery into the slot the pillar begins to hum and tremble. A slot on the pillar opens and a small key falls out.",
           'key': "As you place the key into the door lock and turn it you can hear the pins click into place and the door unlocks."}
itemRoom = {'closet': "match", 'kitchen': "towel", 'store room': "crowbar", 'parlor': "key", 'glowing room': "battery"}

nexRoom = {'closet': 'kitchen', 'kitchen': ['closet', 'store room'], 'store room': ['kitchen', 'parlor'],
           'parlor': ['store room', 'glowing room', 'outside'], 'glowing room': 'parlor'}

curRoom = 'closet'
keypad = 8253

while gameEnd == False:
    print('------------------------------------------------------')
    print("{}'s stats: \n".format(name), "Items: {}\n".format(items), "Room: {}\n".format(curRoom),
          "Room Description: {}\n".format(roomDesc[curRoom]),
          "Items in room: {}\n".format(roomItem[curRoom]))
    action = input('What do you want to do?\n')
    print('')
    if action == 'use battery':
        print("That item can't be used here. Please try another command.")
        continue
    if action == 'use keypad':
        print('The keypads butons glow as they await an input.')
        userkey = int(input('Enter a 4 digit code.'))
        if userkey == keypad:
            print(
                'The keypad chimes in acceptance as you enter the right number. A small slot opened where it looks like you can put something in')
            tempAction = input('What do you want to do?')
            if tempAction == 'use battery':
                if 'battery' in items:
                    print(itemUse['battery'])
                    tempAction2 = input('What do you want to do?')
                    if tempAction2 == 'pick up key':
                        items.append('key')
                        continue
                    else:
                        continue
                else:
                    print('You do not have that item!')
                continue
            else:
                continue
        else:
            print('The keypad buzzes as the wrong code is entered')
            continue

    elif action == 'use key':
        if 'key' in items:
            if curRoom == 'parlor':
                print(
                    "As you place the key into the door lock and turn it, you can hear the pins click into place and the door unlocks. You open the door and walk outside.")
                gameEnd = True
            else:
                print('You can not use that item here.')
                continue
        else:
            print('You do not have that item.')
            continue
    elif action == 'go to outside':
        print("The door is locked shut and needs a key")
        continue
    else:
        if action == "pick up " + str(roomItem[curRoom]):
            items.append(roomItem[curRoom])
            roomItem[curRoom] = 'No items'
            continue
        if "use " in action:
            if itemRoom[curRoom] in action:
                if itemRoom[curRoom] in items:
                    print(itemUse[str(action[4:])])
                    continue
            if itemRoom[curRoom] not in items:
                print('You do not have that item or you can not use it here!')
                continue
        if 'go to ' in action:
            if str(action[6:]) in nexRoom[curRoom]:
                curRoom = action[6:]
                continue
            else:
                print("That room isn't adjacent to the current room")
                continue
        else:
            print(
                "That is not an accepted command. Remember the commands are 'pick up (item)', 'use (item)', and 'go to (room)'")

print('Congratulations! You have successfully escaped!')

