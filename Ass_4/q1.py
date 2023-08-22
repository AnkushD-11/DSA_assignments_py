#Write a program to calculate difference between Start time & End time of an event. Time is
#expressed as hr-min-sec. Final result to be produced in seconds.

def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def time_difference(start_hr, start_min, start_sec, end_hr, end_min, end_sec):
    start_time = time_to_seconds(start_hr, start_min, start_sec)
    end_time = time_to_seconds(end_hr, end_min, end_sec)
    time_diff = end_time - start_time
    return time_diff

# Example start time:
start_hour = int(input("Enter starting hour: "))
start_minute = int(input("Enter starting minute: "))
start_second = int(input("Enter the second: "))

# Example end time: 
end_hour = int(input("Enter end_hour:"))
end_minute = int(input("Enter end_minute: "))
end_second = int(input("Enter end_second: "))

difference_seconds = time_difference(start_hour, start_minute, start_second, end_hour, end_minute, end_second)
print("Time difference in seconds:", difference_seconds)
