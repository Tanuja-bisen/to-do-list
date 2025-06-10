def task():
    task = []  # empty list 
    print("--------welcome to the task management app------")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {1} = ")
        task.append(task_name)

    print(f"Today's tasks  are\n{task}")    

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            task.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task you want to add = ") 
            if updated_val in task:
                up = input("Enter new task = ")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"updated task{up}")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in task:
                ind = task.index(del_val)
                del task[ind]
                print(f"Task {del_val} has been deleted...")

        elif operation == 4:
            print(f" Total task = {task}")
        
        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("invalid input")


task()





      