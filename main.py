def convert_to_am_pm(time_24):
    # Split the input time into hours and minutes
    hours, minutes = map(int, time_24.split(':'))

    # Determine if it's AM or PM
    period = "AM" if hours < 12 else "PM"

    # Convert hours from 24-hour to 12-hour format
    hours = hours % 12
    if hours == 0:
        hours = 12

    # Format and return the time in 12-hour format with AM/PM
    return f"{hours}:{minutes:02d} {period}"

def convert_to_24_hour(time_am_pm):
    # Split the time into time part and period (AM/PM)
    time_part, period = time_am_pm.split()

    # Split the time part into hours and minutes
    hours, minutes = map(int, time_part.split(':'))

    # Convert to 24-hour format based on AM or PM
    if period.upper() == "PM" and hours != 12:
        hours += 12
    elif period.upper() == "AM" and hours == 12:
        hours = 0

    # Format and return the time in 24-hour format
    return f"{hours:02d}:{minutes:02d}"

# Example usage:



time_24 = input("convert_to_am_pm : ")
converted_time = convert_to_am_pm(time_24)
print(converted_time)  

time_24 = input("convert_to_24_hour : ")
converted_time = convert_to_24_hour(time_24)
print(converted_time)  

