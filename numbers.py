import json
valid_operations = ["+", "-", "*", "/"]


def save_task(reluts):
    if save == "y":
        data = {"a" : number, "operation": operation, "b": number_2, "result": reluts }
        with open("text.txt","a") as f :
            json.dump(data ,f)
            f.write("\n")
            print("saved :)")
                    
    else: 
        print("didnt save")       
    return
        
def show_task():
    if show == "y":
        with open ("text.txt", "r", encoding='utf-8') as f :
            for line in f:
                line = line.strip()
                if line:
                    view = json.loads(line)
                    print(f"{view['a']} {view['operation']} {view['b']} = {view['result']}")
            return   
            
while True:
    
    operation = input("whats the operation? ")
    
    if operation == "q":
            print ("bye")
            break
    
    if operation not in valid_operations:
        print("wrong operation")
        continue
        
    
    number = int (input("whats the first number? "))
    number_2 =  int(input("whats the second number? "))
    

    try:
        if operation == "+":
            reluts = number + number_2

        elif operation == "-" :
            reluts = number - number_2

        elif operation == "*":
            reluts = number * number_2 
            
        elif operation == "/":
            reluts = number / number_2
            
        else:
            print("wrong opration")

        print(reluts)
    
    except ZeroDivisionError:
        print("diffrent number ")

            
           
    save = input(f"do you want to save the {reluts} y/n ") 
    if save == "y":
        save_task(reluts)
    show = input("do you want see the resluts ? y/n ")
    if show == "y":
        show_task()
    

