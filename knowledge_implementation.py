#using the knowlege that i have gained till now and implementing on creating something.
#building a to do list system 

print ("let's make your day productive!")
print("for adding the task tap 1")
print("for removing the task tap 2")
print("for printing the whole task tap 3")
tasks = []
while True:
    
    tap = int(input("enter your need "))

    match tap:
    
        case 1:
        
            while True:
                task = input("enter your task")
                tasks.append(task)
                print("do you want to add more task? if yess type yes,if you don't want to add type any key")
                result = input("enter").lower().strip()
                if result != "yes":
                    break
                        
    
                
                
        case 2:
            print("type \"all\" if you want to remove all list ")
            print("type \"one\" if you want to remove selected task only.")
            choose = input("enter your choice").lower().strip()
            if choose == "all":
                tasks.clear()
                print("all data from the list has been deleted")
            elif choose == "one":
                delete = int(input("enter the position of the item that you want to delete"))
                del tasks[delete - 1]
                print("that data has been deleted")
            else:
                print("enter a valid input please")
        case 3:
            print(f"your works to be completed are here{tasks}")
            if len(tasks) == 0:
                print("your list is empty,can you please write something in it")

        case _:
            print("do you want to exit?")
            decision = input("enter yes or no")
            if decision == "yes":
                print("byee")
                break
            
