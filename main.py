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
