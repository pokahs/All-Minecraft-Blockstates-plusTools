from typing import Any
import pyperclip

class blockString:

    def __init__(self) -> None:
        pass

def newCommandSeq(type):
    
    while True: # Get commands until user says they done

        replacive = blockString()


final_command = "//rep "

def add(blah):
    global final_command
    final_command += blah

target = input("Block to replace: ")

add(target + " ")


facing_info = [["N", "E", "S", "W"]]

if "stairs" in target:

    target_facing = input("Facing? (N, E, S, W, Addall): ")

    target_half = input("Type? (Bot, Top): ")

    if target_facing or target_half:

        add("[")

        if target_facing



    




if "slab" in target:
    target_type = input("Type? (Bot, Top): ")



pyperclip.copy(final_command)
