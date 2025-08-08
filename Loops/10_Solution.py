import time

wait_time = 1
max_retrise = 5
attempts = 0

while attempts < max_retrise:
    print("Attempt", attempts + 1, "-Wait_time", wait_time)
    time.sleep(wait_time)
    # wait_time *= 1  
    wait_time = wait_time * 2
    # attempts += 1
    attempts = attempts + 1