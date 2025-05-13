# def get_temperatures():
#     temperatures = []
#     print("Enter temperatures for 7 days:")
#     for i in range(7):
#         temp = float(input(f"Day {i+1} temperature (°C): "))
#         temperatures.append(temp)
#     return temperatures

# def calculate_average(temps):
#     return sum(temps) / len(temps)

# def calculate_max(temps):
#     return max(temps)

# def calculate_min(temps):
#     return min(temps)

# def display_results(temps):
#     avg = calculate_average(temps)
#     highest = calculate_max(temps)
#     lowest = calculate_min(temps)

#     print("\n--- Weekly Temperature Summary ---")
#     # for i, temp in enumerate(temps):
#     #     print(f"Day {i+1}: {temp}°C")
#     print(f"\nAverage Temperature: {avg:.2f}°C")
#     print(f"Highest Temperature: {highest}°C")
#     print(f"Lowest Temperature: {lowest}°C")
# temperatures = get_temperatures()
# display_results(temperatures)

def get_temperatures():
    temperatures=[]
    print("Enter temperatures for 7 days")
    for a in range(7):
        temp=int(input(f"Day {a+1} temperature (°C) : "))
        temperatures.append(temp)
    return temperatures
def calculate_average(temp):
    return sum(temp)/len(temp)
def calculate_max(temp):
    return max(temp)
def calculate_min(temp):
    return min(temp)

def display_results(temp):
    average=calculate_average(temp)
    highest=calculate_max(temp)
    lowest=calculate_min(temp)
    print("-------Weekly Temperature summary-------")
    print(f"Average Temperature : {average:.2f}°C")
    print(f"Highest Temperature : {highest}°C")
    print(f"lowest Temperature : {lowest}°C")
temperatures=get_temperatures()
display_results(temperatures)   