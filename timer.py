import time 

def timer():
    try:
         user_mins = int(input("Enter timer duration in minutes: "))
         user_interval = int(input("Enter your interval: "))
         if user_mins <= 0:
             print("Enter a positve number of minutes")
             return
    except ValueError:
             print("Invalid input")
             return
         
    total_seconds = user_mins * 60
    elapsed_time = 0 
    interval = user_interval * 60 
    
    print("timer started for {} minutes." .format(user_mins))
    
    while elapsed_time < total_seconds:
        time.sleep(1)
        elapsed_time += 1 
        
        if elapsed_time % interval == 0:
            minutes_passed = elapsed_time // 60
            print(f"{minutes_passed * 1} minutes has passed")
            
    print("Time's UP!!")
         

timer()
    
        