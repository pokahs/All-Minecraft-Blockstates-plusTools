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

    def __init__(self, auto_ratios=True, replacer_tags_universal=True) -> None:
        
        self.target = block(block_name=input("Block to replace: ").lower())

        self.replacers = []

    @classmethod
    def newSet(cls, auto_ratios=True, replacer_tags_univeral=True):

        pass

    def parseCommand(self):

        # If any attributes of the 
        pass




class block:

    def __init__(self, block_name, checkvalidity=True, tag_filling=False) -> None:
        
        self.block_name = block_name # Add check in json for the name if checkvalidity is True

        # After the block_name has been verified as legimiate, or not due to optimizations, it will now create its own dict var
        # to save and store its tags and the value for each tag. if tag_filling actually is something, it should be a dict for tags.
        # for each tag this block has, it will check if it used in the tag_filling, and if it is make it match to the tags here.

        # if there are still tags for this block that are empty after this potential filling process, the user will be asked to fill em out.
        # The new tags that are filled out for this block will then be returned/saved to update the global tag_filling dict that is used for
        # block creation. NOTE if the group system is in use here, it should only change the tags in the tag_filling dict for the block's group.

        # NOTE that the tag_filling system should def include an option (prob as the default) to only fill tags for block with same group.
        # As in if this block is a stair, it should only check for defined tags for the stair group in the tag_filling.


class replacer(block):

    def __init__(self, block_name, auto_ratio, tag_filling=False):

        super().__init__(input("Name of replacer block: "), tag_filling=tag_filling)

        if auto_ratio:

            self.ratio = False

        else:

            self.ratio = float(input("Put the ratio of how much this block should replace as part of a whole: "))

    