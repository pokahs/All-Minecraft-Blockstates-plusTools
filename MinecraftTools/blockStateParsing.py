import json

def optimizing_load(json_input=None, json_output=None):

    try:

        with open(json_input, 'r') as json_file:
            json_data = json.load(json_file)


        new_data = {}


        for block_name, block_data in json_data.items():

            new_data[block_name] = {}

            if "variants" in block_data:

                variants_data = block_data["variants"]
                first_variation = next(iter(variants_data), None)

                if first_variation:

                    states_split = first_variation.split(',')
                    block_states = [part.split("=")[0] for part in states_split]

                    for state in block_states:

                        new_data[block_name][state] = []

                for states, useless_shit in variants_data.items():

                    if not states:
                        continue

                    states_split = states.split(',')

                    block_state_values = [part.split("=")[1] for part in states_split]

                    i = 0

                    for state in block_states:

                        if not block_state_values[i] in new_data[block_name][state]:

                            new_data[block_name][state].append(block_state_values[i])

                        i += 1

        with open(json_output, 'w') as json_file:
            json.dump(new_data, json_file, indent=4)


    except FileNotFoundError:
        print(f"File not found: {json_input}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_input}")




def grouping_load(json_input=None, json_output=None):


    try:

        with open(json_input, 'r') as json_file:
            json_data = json.load(json_file)


        new_data = {}

        group_num = 1

        #EX --> { "group_1": {"cases": ["stone, planks"], "tags": {"tag1": ["val1", "val2"], "tag2": ["val1", "val2", "val3"] } } }

        for block_name, block_tags in json_data.items():


            # Goes thorugh all attrs for each group. If it does match with a group, it adds to that group and breaks. 
            # If it never breaks, meaning it found no match, it does the else for the for loop and creates a new group.

            for group_name, group_data in new_data.items():

                group_tags = group_data["tags"]

                if group_tags != block_tags:

                    continue

                    
                # If it reached here, it means the current block matches the current group
                new_data[group_name]["cases"].append(block_name)
                break

            else:
                new_data["group_" + str(group_num)] = {"cases": [block_name], "tags": block_tags}
                group_num += 1
                # This will occur if the past for loop never breaked, meaning it never found a match. So, here we create a new group.

        try:
            with open(json_output, 'w') as json_file:
                json.dump(new_data, json_file, indent=4)

        except FileNotFoundError:
            print(f"File not found: {json_output}")


    except FileNotFoundError:
        print(f"File not found: {json_input}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_input}")
