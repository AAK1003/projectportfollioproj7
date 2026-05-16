from email.headerregistry import Address

task_list = []
loop_keep_going = True

def check_actions(prompt):
    while True:
        action = input(prompt).lower()
        if action in ['add', 'remove', 'view', 'exit']:
            return action
        print('Invalid response, please try again.')

def doing_action(action):
    if action == 'add':
        addition = input('What do you want to add to the list? ')
        task_list.append(addition)
        loop_keep_going = True
        return loop_keep_going
    elif action == 'exit':
        print('Goodbye!')
        loop_keep_going = False
        return loop_keep_going
    elif action == 'view':
        print('Your list has:')
        for task in task_list:
            print(task)
        loop_keep_going = True
        return loop_keep_going
    elif action == 'remove':
        if not task_list:
            print('The list is empty, please add something if you want to remove.')
            loop_keep_going = True
            return loop_keep_going
        else:
            print('Your current tasks:')
            for index, task in enumerate(task_list):
                print(f'{index}: {task}')
            choice = input('Enter the number of the task you want to remove: ')
            if choice.isnumeric():
                idx = int(choice)
                if 0 <= idx <= len(task_list):
                    removed = task_list.pop(idx)
                    print(f'Removed: {removed}')
                    loop_keep_going = True
                    return loop_keep_going
                else:
                    print('Please enter a number that is on the list.')
                    loop_keep_going = True
                    return loop_keep_going
            else:
                print('PLease enter a valid number.')
                loop_keep_going = True
                return loop_keep_going




while loop_keep_going == True:
    what_to_do = check_actions('What would you like to do? Add(add to list), Remove(remove from list), View(view current list), or Exit(exit the app)? ')
    loop_keep_going = doing_action(what_to_do)
