from typing import Any
import pyperclip # pyperclip.copy(final_command)


# User will start a session of creating commands. While they can just create singular ones directly, this doesnt work well for multi-line commands.
# When commands are done, they will be saved to a text file. For now you just delete them manually, and starting a new command session will just add
# onto the end of the text file. A function to essentially print them all (in game chat) will go through the entire text file and print each command.

# static block - normal block with no direction/tags

# dynamic block - blocks with defining features (stairs, slabs, walls, etc)

# Different types of commands and how they go:

# tags:

# replacer_tags_universal

# if the target is a static block, the only concern is checking the replacers. if replacer_tags_universal, then whenever a new tag is asked for 
# a replacer, the tag is saved and used for the default on any new replacers. if not, then simply any replacer will ask for the needed tags for itself

# if target is a replacer block, the treatment is the exact same except any tags defined for the target block will be used immediately for the
# replacer_tags_universal tag assigning system.

# auto_ratios

# ratios work the same for any dif blocks used, whateva. if auto_ratios, no replacer block will be asked for a ratio. the ratio for each will be simply
# parsed in the final print via 1/num_of_replacers. if not auto_ratios, each block will gain an attribute via user input of its ratio/percentage. 
# each block ratio is simply a whole number, which then turns into a percentage when printing via all 1/block numbers together*the number of a block

# Timeline of a command creation

# Get target block

# Asks if target block will be a replacer as well

# Asks for replacers (loop until broken via user sayinig no more replacers)

# Now done, can use print command anytime to parse.

# NOTE that using a simple command creation is rly only ever gonna be used for debugging kinda. not meant to like print and save automatically


# Timeline of newSet function

# Starts loop of creating commands

# for each command, inputs appropiate tags like replacer_tags_universal and auto_ratios

# when a command's innit is done, the commands print function is called to save its final form as a command (or multiple if very long)

# asks if wanna do another command. if yes, then like another iter of loop. if naw, goes through the list of commands and adds em all to the
# designated command text file (name should be in function parameters). if text file with name already exists, it will add onto it.


# new function seperate from class: File to in game printer.
# will go through a specificed text file name (in this case prob a replace command text file) and for each line:
# copy it, open chat, paste, and enter.
# would be good/necessary for the actual print to be activated by a specified key press (optimal) or timer.

class replaceCommand:

    def __init__(self, auto_ratios=True, auto_block_type_assign=True) -> None:
        
        self.auto_ratios = auto_ratios
        self.auto_block_type_assign = auto_block_type_assign

        self.replacive = blockString(block=input("Block to replace: ").lower())

        self.replacer_count = 0

        self.replacers = []

        while True:

            self.replacers.append(blockString(block=input("Replacer block: ").lower(), parent_block=self.replacive))
            if not self.auto_ratios:

                self.replacers[self.replacer_count].ratio = input(int("Ratio for this replace (As a whole number as part of a future total): "))

            self.replacer_count += 1

            if input("Add another replacer block (Y/[anything else]): ").lower() != "y":
                break

    @classmethod
    def newSet(cls, auto_ratios=True, auto_block_type_assign=True):

        pass

    def parseCommand(self):

        # If any attributes of the 
        pass


class blockString:

    def __init__(self, block, parent_block=False, stair_half=None, slab_half = None, direction=None) -> None:
        
        self.block = block

        if parent_block:

            for attr_name, attr_value in vars(parent_block).items():

                if not attr_value:
                    
                    setattr(self, attr_name, attr_value)

        



    