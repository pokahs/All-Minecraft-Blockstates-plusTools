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

import json

group_data_json = "group_data.json"
block_data_json = "block_data.json"

block_data, group_data = None, None

try:
    
    with open(block_data_json, 'r') as json_file:
            block_data = json.load(json_file)

except FileNotFoundError:
    print(f"BIG WARNING! Data file not found: {block_data_json}")

except json.JSONDecodeError:
    print(f"BIG WARNING! Data in json file formatted wrong: {block_data_json}")


try:
    
    with open(group_data_json, 'r') as json_file:
            group_data = json.load(json_file)

except FileNotFoundError:
    print(f"BIG WARNING! Data file not found: {group_data_json}")

except json.JSONDecodeError:
    print(f"BIG WARNING! Data in json file formatted wrong: {group_data_json}")

# How will program handle a brick stair being replaced by oak stair

# Since they are both stairs, sharing tags via group or not doesnt matter.

# The dif b/w sharing tags or not is big as either:
# - No share : you just ask for tags both individually, and it turns into 1 command.
# - Share : the tags you got for the brick stair will carry over to the oak stair, and it turns into 1 command.

# However, say we wanna do all the values of tag end-to-end, or we want to leave one tag as a default/not defining it.
# This problem leads to the solution of any tag being able to have the value of "all" or "none".
# The rest of the program doesnt change much; the "all" or "none" values if they come up will be treaten as any other value,
# meaning they can be part of the tag sharing system or can be used when a user defines a tag value directly.

# The signifigance of the "all" and "none" tags only come out at the time or parsing. While the "none" tag is easy;
# the tag is simply ignored.
'''
Making group sharing default since realized errors and weird shit occurs if one group has a num of values for a tag but other group has a different
num of values for the same tag. A block might be assigned a tag value that it actually cant have.


if block's defined group in shared_tags:

    for each tag in group:
    
        make block's own tag = defined tag

else:

    ask user for each tag, and return new info to update global shared_tags


'''


class replaceCommand:

    def __init__(self, auto_ratios=True, shared_tags=True) -> None:
        
        self.target = block(block_name=input("Block to replace: ").lower())

        self.shared_tags = shared_tags

        if not type(self.shared_tags) is dict: # Will happen unless user inputted a dictionary with tags values already

            self.shared_tags = {}



        self.replacers = []

    @classmethod
    def newSet(cls, auto_ratios=True, shared_tags=True):

        pass

    def parseCommand(self):

        # If any attributes of the 
        pass




class block:

    def __init__(self, block_name, checkvalidity=True, shared_tags=False) -> None:
        
        self.block_name = block_name # Add check in json for the name if checkvalidity is True

        self.tag_info = {}

        if (checkvalidity and self.block_name in block_data) or (not checkvalidity):

            
            # We have now verified the block to be a valid block. (or it isnt but checkvalidity was off)

            # The next step depends on if there is merging tag info, and if it group based or not.
            # NOTE I gotta add a group attr to each block in block_data for this shit to work
            if shared_tags:

                cur_block_group = block_data[self.block_name]["group"] # just saving group of this block since used so much

                if cur_block_group in shared_tags:
                    for tag in shared_tags[cur_block_group]:
                        # Not sure exactl what "tag" will be, if its like half : top or just like half or whatever
                        # but in this state you just add each tag to the current tag_info, since rn every single tag will be defined
                        # with this system if we entered this stage we dont need to ask user for anything
                        print(tag) # for now just printing to check ltr, but gotta add it to tag_info

                else: # The group's tags hasnt been defined, so now we ask user for each.
                    
                    for base_tag in group_data[cur_block_group]["tags"]:
                        print(base_tag) # Me not know how to handle json but we need the name of tag here, then we ask user what
                        # they want for it and then we save it. NOTE we also gotta figure out how to return the new data here.

                

            # If no merging tag info, we just go and start asking user for what each tag should be.

            # If tag info but not grouping, then for each tag this block has check use the value defined
            # for the tag in the shared_tags info coming in. If theres no info for the tag, it's kept empty
            # and filled out by the user next.

            # If tag_info and grouping, 

        else:

            raise ValueError("The block name '{self.block_name}' is not a legitimate block according to the block data fetched.")
        
    def parse(self):
        pass # Just parse block name and the tags. Ratio parsing is something that the replace class (ratio class?) adds on.
        

class replacer(block):

    def __init__(self, block_name, auto_ratio, shared_tags=False):

        super().__init__(input("Name of replacer block: "), shared_tags=shared_tags)

        if auto_ratio:

            self.ratio = False

        else:

            self.ratio = float(input("Put the ratio of how much this block should replace as part of a whole: "))


if __name__ == "__main__":

    blok = block("stosne")