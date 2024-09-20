import time

def print_minutes_passed():
    user_interval = int(input("Enter the interval in minutes: "))
    user_minutes = int(input("Enter the total minutes: "))
    
    current_time = 0
    while current_time < user_minutes:
        print(f"{current_time} minutes passed")
        time.sleep(user_interval * 60)  # Wait for the interval in seconds
        current_time += user_interval
    print(f"{user_minutes} minutes finished")

# Example usage
print_minutes_passed()
