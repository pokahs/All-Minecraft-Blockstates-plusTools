#from MinecraftTools import worldEdit

#worldEdit.replaceCommand.newSet()

'''class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

obj = MyClass(1, 2, 3)

# Using vars()
print(vars(obj).items())

for attribute, value in vars(obj).items():
    print(f"Attribute: {attribute}, Value: {value}")

# Using __dict__
for attribute, value in obj.__dict__.items():
    print(f"Attribute: {attribute}, Value: {value}")'''

from MinecraftTools import blockStateParsing


#blockStateParsing.optimizing_load(json_input="themotherload.json", json_output="optimized_data.json")

blockStateParsing.grouping_load(json_input="optimized_data.json", json_output="grouped_data.json")