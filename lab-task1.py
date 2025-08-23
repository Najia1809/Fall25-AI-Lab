tasks = []

while True:
    task = input("Enter task or type done to finish: ")
    if task == "done":  
        break
    tasks.append(task)

print("Your tasks:")
for t in tasks:
    print(t)
    
while True:
    operation = int(input("enter any number 1 to 4"))
    if operation == 1:
       add = input("enter task that you want to add: ")
       tasks.append(add)
       print(t)

    elif operation == 2:
        previous_task = input("Enter the task name you want to update: ")
        if previous_task in tasks:
            updated_task = input("Enter new task: ")
            task_index = tasks.index(previous_task)  
            tasks[task_index] = updated_task        
            print(t)
    elif operation == 3:
        task_to_remove = input("Enter the task name you want to remove: ")
        if task_to_remove in tasks:
            tasks.remove(task_to_remove)  
           
            print(t)
    elif operation == 4:
        print("list is closed")
        break
    else:
        print("invalid input")