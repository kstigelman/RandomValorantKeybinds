"""
    This script randomizes a list of given controls with
    a list of keybinds so that you can play video games
    with a new, agonizing challenge.

    Written by Kyler Stigelman 7/5/23
"""
import keyboard
import random


# Outputs a file of given filename with the set of mapped controls.
def randomize_controls (filename):
    controls = open ("controls.txt")
    keys = open ("keys.txt")
    binds = open (filename, "w+")
    keyLines = keys.readlines()
    for line in controls.readlines ():
        n = random.randint(0, len (keyLines) - 1)
        # usedKeys.append (keys[n])
        binds.write (line.replace ('\n', '') + " -> " + keyLines[n] + "\n")
        keyLines.remove (keyLines[n])
    binds.close ()
    controls.close ()
    keys.close()
    

exit = False

print ("\nType 'exit' to quit the application.\n\n")
while (exit == False):
    name = input ("Enter a name for this bind set: ").replace ('\n','')

    if (name == "exit"):
        exit = True

    randomize_controls (name + ".txt")
    
#amount = input ('How many bind sets do you need? ').replace ('\n','')
#for i in range (0, int (amount)):
#    print ("Creating file " + str (i + 1))
#    randomize_controls ("binds_" + str(i + 1)+ ".txt")


# Method used to get the names of all keyboard characters.
def get_keys ():
    f = open ("keys.txt", "r")

    running = True

    while running:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == "up":
            continue

        if key_event.name == "esc":
            running = False
        else:
            f.write (key_event.name + '\n')
    f.close ()