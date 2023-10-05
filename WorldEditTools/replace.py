from typing import Any
import pyperclip # pyperclip.copy(final_command)

class blockString:

    def __init__(self, block) -> None:
        
        self.block = block

        self.half, self.direction = None, None

        if "stairs" in self.block:

            self.half = input("What half? (B/T): ").lower()

            self.direction = input("what direction? (N/E/S/W):")

        elif "slab" in self.block:

            self.half = input("What half? (B/T): ").lower()




def newCommandSeq(ratios=None, block_type_assign=None):

    print(ratios, block_type_assign)
    
    while True: # Get commands until user says they done

        replacive = blockString(input("Block to replace: ").lower())


