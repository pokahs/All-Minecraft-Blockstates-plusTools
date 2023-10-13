import json

def sort_group_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            # Step 2: Parse the JSON data
            original_data = json.load(file)

            # Step 3: Extract and sort the keys
            sorted_keys = sorted(original_data.keys())

            # Step 4: Create a new dictionary with sorted keys
            sorted_data = {}
            for key in sorted_keys:
                current_dict = original_data[key]

                # Sort the "cases" key
                if "cases" in current_dict:
                    current_dict["cases"] = sorted(current_dict["cases"])

                # Sort the keys within the "tags" key
                if "tags" in current_dict and isinstance(current_dict["tags"], dict):
                    for tag_key, tag_value in current_dict["tags"].items():
                        if all(isinstance(val, bool) for val in tag_value):
                            # Sort boolean values, [false, true]
                            tag_value.sort()
                        elif all(isinstance(val, (int, float)) for val in tag_value):
                            # Sort numeric values, [0, 1, 2, 3]
                            tag_value.sort()
                        elif all(isinstance(val, str) for val in tag_value):
                            # Sort string values alphabetically
                            tag_value.sort()
                        # Update the value in the "tags" dictionary
                        current_dict["tags"][tag_key] = tag_value

                sorted_data[key] = current_dict

            # Print sorted keys
            print("Alphabetically sorted key names:")
            for key in sorted_keys:
                print(key)

            # Step 5: Convert the new dictionary back to JSON
            sorted_json = json.dumps(sorted_data, indent=2)

            # Step 6: Write the JSON data to a new file
            with open(output_file, 'w') as output_file:
                output_file.write(sorted_json)
            print(f'Sorted JSON data written to {output_file}')

    except FileNotFoundError:
        print(f'Error: The input file "{input_file}" does not exist.')

    except json.JSONDecodeError as e:
        print(f'Error parsing JSON data: {e}')

    except Exception as e:
        print(f'An error occurred: {e}')




def create_grouped_block_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            # Step 2: Parse the JSON data
            original_data = json.load(file)

            # Create a dictionary to store the new data
            new_data = {}

            for key, value in original_data.items():
                if "cases" in value:
                    for case in value["cases"]:
                        # Create a new key based on the case string
                        new_key = case

                        # Create the "group" and "tags" subkeys
                        new_data[new_key] = {
                            "group": key,  # Original key name
                            "tags": value.get("tags", {})
                        }

            # Step 5: Convert the new dictionary back to JSON
            sorted_new_json = json.dumps(
                new_data, indent=2, sort_keys=True
            )  # Sort keys alphabetically

            # Step 6: Write the new JSON data to a new file
            with open(output_file, 'w') as output_file:
                output_file.write(sorted_new_json)
            print(f'New JSON data written to {output_file}')

    except FileNotFoundError:
        print(f'Error: The input file "{input_file}" does not exist.')

    except json.JSONDecodeError as e:
        print(f'Error parsing JSON data: {e}')

    except Exception as e:
        print(f'An error occurred: {e}')



def create_nongrouped_block_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            # Step 2: Parse the JSON data
            original_data = json.load(file)

            # Create a dictionary to store the new data
            new_data = {}

            for key, value in original_data.items():
                if isinstance(value, dict):
                    # Remove the "group" key if it exists
                    value.pop("group", None)

                new_data[key] = value

            # Step 5: Convert the new dictionary back to JSON
            new_json = json.dumps(new_data, indent=2, sort_keys=True)

            # Step 6: Write the new JSON data to a new file
            with open(output_file, 'w') as output_file:
                output_file.write(new_json)
            print(f'New JSON data written to {output_file}')

    except FileNotFoundError:
        print(f'Error: The input file "{input_file}" does not exist.')

    except json.JSONDecodeError as e:
        print(f'Error parsing JSON data: {e}')

    except Exception as e:
        print(f'An error occurred: {e}')




if __name__ == "__main__":

    # Converts and organizes all data based off the group_data.json, so if thats not where you want new data coming from you gotta change this.

    sort_group_data('BlockstateData/group_data.json', 'BlockstateData/group_data.json')
    
    create_grouped_block_data('BlockstateData/group_data.json', 'BlockstateData/grouped_block_data.json')

    create_nongrouped_block_data('BlockstateData/grouped_block_data.json', 'BlockstateData/block_data.json')

    # and yes this code was blatantly 90% chatgptd



