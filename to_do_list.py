def task():
    tasks=[]
    print("------Welcome To The Personalized Task Manager-------")

    total_tasks=int(input("enter the number of task you want to add: "))

    for i in range(1,total_tasks+1):
        task_name=input(f"Enter Name Of The {i} Task: ")
        tasks.append(task_name)
    print("-------------------------------")
    print(f"Todays tasks are \n {tasks}")
    print("-------------------------------")
    
    while True:
        operations=int(input("Enter 1-Add\n2-Update\n3-delete\n4-View\n5-Exit/stop"))
        
        if operations==1:
            add=input("Enter The Task You Want To Add : ")
            tasks.append(add)
            print(f"task {add} has successfully been added.....")
        
        elif operations==2:
            update_val=input("Enter the task you want to update ")
            if update_val in tasks:
                up=input("Enter the new task: ")
                lnd=tasks.index(update_val)
                tasks[lnd]=up
                print(f"Updated task {up}")
        
        elif operations==3:
            del_val=input("Enter the value you want to remove=")
            if del_val in tasks:
                ind= tasks.index(del_val)
                del tasks[ind]
                print(f"The task {del_val} has been pushed out")
        elif operations==4:
            print(f"Total tasks are = {tasks}")
        
        elif operations==5:
            print("Closing the program.....")
            break 
        
        else:
            print("Please select the valid <Operations>")


task()




