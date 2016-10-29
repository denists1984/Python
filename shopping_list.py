shopping_list = []

# print instructions
def help_func():
    print("Start add to the list")
    print("Enter 'DONE' to quit")
    print("Enter 'HELP' to get usage")
    print("Enter 'SHOW' to get the list")

# print out the list
def compl_list():
    print ("Here is your list:")
    for i in shopping_list:
        print(i)
    print("Now you have to buy {} items.".format(len(shopping_list)))

# add items
def add_new_item(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

#def main():
    #ask for help
help_func()

# ask for new items
while True:
    new_item = raw_input("--> ")

    # quit statement
    if new_item.lower() == 'done':
        compl_list()
        break
    elif new_item.lower() == 'help':
        help_func()
        continue
    elif new_item.lower() == 'show':
        compl_list()
        continue
    else:
        add_new_item(new_item)
