import time 

def timer():
    try:
         user_input = int(input("Enter timer duration in minutes: "))
         if user_input <= 0:
             print("Enter a positve number of minutes")
             return
    except ValueError:
             print("Invalid input")
             return
         
    total_seconds = user_input * 60
    elapsed_time = 0 
    interval = 1 * 60 
    
    print("timer started for {} minutes." .format(user_input))
    
    while elapsed_time < total_seconds:
        time.sleep(1)
        elapsed_time += 1 
        
        if elapsed_time % interval == 0:
            minutes_passed = elapsed_time // 60
            print(f"{minutes_passed * 1} minutes has passed")
            
    print("Time's UP!!")
         

timer()
    
        