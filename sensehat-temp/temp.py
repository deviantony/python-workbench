import os
import sched
import time
# from sense_hat import SenseHat

# sense = SenseHat()

# Look for the environment variable named DATA_REFRESH
data_refresh = os.environ.get('DATA_REFRESH')

# If the environment variable is not found, use a default value of 10 seconds
if not data_refresh:
    data_refresh = 10

# Convert the value to an integer
data_refresh = int(data_refresh)

# Create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

# Define a function to print the message and schedule the next call
def print_message():
    print('26.234')
    #sense.show_message("Hello world")
    #sense.clear()
    #temp = sense.get_temperature()
    # print(temp)
    scheduler.enter(data_refresh, 1, print_message)

#sense.clear()
#temp = sense.get_temperature()
print('26.234')

# Schedule the first call to the function
scheduler.enter(data_refresh, 1, print_message)

# Start the scheduler
scheduler.run()
