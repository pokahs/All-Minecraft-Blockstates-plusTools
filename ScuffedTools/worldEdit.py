# IN THE MAKING, NOT DONE :O




from typing import Any
import pyperclip # pyperclip.copy(final_command)


# block of comments here is old
#  |
#  |
# \ /

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

group_data_json = "BlockstateStuff/group_data.json"
grouped_block_data_json = "BlockstateStuff/grouped_block_data.json"

grouped_block_data, group_data = None, None

try:
    
    with open(grouped_block_data_json, 'r') as json_file:
            grouped_block_data = json.load(json_file)

except FileNotFoundError:
    print(f"BIG WARNING! Data file not found: {grouped_block_data_json}")

except json.JSONDecodeError:
    print(f"BIG WARNING! Data in json file formatted wrong: {grouped_block_data_json}")


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

    def __init__(self, auto_ratio=True, shared_tags=True):


        self.shared_tags = shared_tags if type(shared_tags) is dict else {} # Will happen unless user inputted a dictionary with tags values already
        
        self.target = block(name=input("Block to replace: ").lower())

        self.shared_tags.update(self.target.tag_info)


        self.replacers = []

        while True:

            self.replacers.append(replacer(input("Replacer block: "), auto_ratio=auto_ratio, shared_tags=shared_tags))

            self.shared_tags.update(self.replacers[-1].tag_info)

            if not len(input("Add another replacer? ")):
                break

    @classmethod
    def newSet(cls, auto_ratios=True, shared_tags=True):

        pass

    def parseCommand(self):

        # If any attributes of the 
        pass




class block:

    def __init__(self, name, checkvalidity=True, shared_tags=False) -> None:
        
        self.name = name # Add check in json for the name if checkvalidity is True

        self.tag_info = {}

        self.newDefiner = False

        self.group = grouped_block_data[self.name]["group"]


        if (checkvalidity and self.name in grouped_block_data) or (not checkvalidity):

            
            # We have now verified the block to be a valid block. (or it isnt but checkvalidity was off)

            # The next step depends on if there is merging tag info, and if it group based or not.

            if shared_tags:

                if self.group in shared_tags:
                    for tag in shared_tags[self.group]:

                        self.tag_info[tag] = shared_tags[self.group][tag]

                else: # The group's tags hasnt been defined, so now we ask user for each.

                    self.newDefiner = True


                    print(f"{self.name} is not in a defined tag group! Please define all the tags for this group :P")

                    group_tags = group_data[self.group]["tags"]
                    
                    for base_tag in group_tags:

                        # Here we get new tag value from user input, making sure it is either None/nothing (undefined/skipped), "all", or one of the approipiate tags.

                        new_tag_value = None

                        while True:

                            new_tag_value = input(f"Value for {base_tag} tag (Possible values: {group_tags[base_tag]}, type: {type(group_tags[base_tag][0])}): ").lower()

                            if new_tag_value == '':

                                new_tag_value = None

                                break

                            elif new_tag_value == 'all':

                                break

                            for possible_val in group_tags[base_tag]:

                                print(str(possible_val))

                                if str(possible_val) == new_tag_value:

                                    new_tag_value = type(group_tags[base_tag][0])(new_tag_value)

                                    break

                            print(f"{new_tag_value} is not a valid value. Redoing...")


                        self.tag_info[base_tag] = new_tag_value

        else:

            raise ValueError("The block name '{self.name}' is not a legitimate block according to the block data fetched.")
        
    def parse(self, all_tags_filled=None):

        # ALL Procedure:
        # There are 2 types of all defined tags:

        # An indepdent all tag: It is either any target block, or it is a replacer block where the target block does not the same tag defined as all.
        # Indepdent is prob more common

        # A dependent all tag: Only a replacer blocks tag that mimics the target blocks exact same tag.

        # Flow:

        # Add block name. simple lol

        # Now add each tag and its value.
        # This is easy for most tags;
        # Normal tags you just add name = value
        # None defined tags you just dont do anything
        # But then the all tags come in those bithces

        # There will be a global looped nested for loop in the command parser thing
        # It goes:
        # For each different all tag (differentiating same tags but dif groups), cycle the tag's values and parse a command with that
        # E.g if you have a command prompt thats 3 all tags with values 2, 3, 4, thats gonna end up as 24 commands pretty sure.

        # Not sure how ratios gonna interpret all this shit. cuz say like no all tags in target and just indepdent all tags in replacers.
        # Then you might one block replaced equally  by 3 dif blocks, but one block has one state, one has 2 states, and one has 5. 
        # Thats gonna become 7 commands, with the ratios being like 1/3, 1/6 * 2, 1/15 * 5. you smell me?

        # Not sure how subclass functions can access like data here, but the replacer subclass like function of this is gonna need to access
        # some saved data here like "total ratios" or something, which you know inital ratio combined with now how many types of the block there
        # are if an all tag influenced. Howveer, this wouldnt be needed i think in parts where it is a dependent all tag you know? cuz then theres 
        # dif versions of the target that just kinda like cycle flow for the replacer matched with it. GYATTDAM THIS IS A LOT AAAAAAAAAAAAA

        # gonna fard
        pass # Just parse block name and the tags. Ratio parsing is something that the replace class (ratio class?) adds on.
        
        

class replacer(block):

    def __init__(self, name, checkvalidity=True, shared_tags=False, auto_ratio=True):

        super().__init__(name, checkvalidity=checkvalidity, shared_tags=shared_tags)

        if auto_ratio:

            self.ratio = False

        else:

            self.ratio = float(input("Put the ratio of how much this block should replace as part of a whole: "))

    
    def parse(self):

        super().parse(self)


# Example of shared tag dict: 
dic = { "axis": { "axis": "x"}}

if __name__ == "__main__":

    blok = block("campfire", shared_tags=dic)
    print(blok.tag_info)