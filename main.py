#from MinecraftTools import worldEdit

#worldEdit.replaceCommand.newSet()


#from MinecraftTools import blockStateParsing


#blockStateParsing.optimizing_load(json_input="themotherload.json", json_output="block_data.json")

#blockStateParsing.grouping_load(json_input="block_data.json", json_output="group_data.json")

#blockStateParsing.addgroupatr_load(json_input="group_data.json", json_output="block_data.json")
import json

def sort_data(input_file, output_file):
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

# Usage
input_file = 'group_data.json'
output_file = 'organized_group_data.json'
sort_data(input_file, output_file)


