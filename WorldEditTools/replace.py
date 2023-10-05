from typing import Any
import pyperclip # pyperclip.copy(final_command)

class replaceCommand:

    def __init__(self, ratios=None, block_type_assign=None, self_start=None) -> None:
        
        self.ratios = ratios
        
        self.block_type_assign = block_type_assign

        self.self_start = self_start

        if self.self_start:
            
            self.sequence()

    def sequence():

        replacive = blockString(input("Block to replace: ").lower())

        replacer = blockString(input("Replacer block: ").lower())

class blockString:

    def __init__(self, block, half=None, direction=None) -> None:
        
        self.block = block

        self.half = half
        
        direction = direction

        if "stairs" in self.block and not self.half and not self.direction:

            self.half = input("What half? (B/T): ").lower()

            self.direction = input("what direction? (N/E/S/W):")

        elif "slab" in self.block and not self.half:

            self.half = input("What half? (B/T): ").lower()
