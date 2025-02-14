#title: average rainfall
#author: michael stoll
#date: 2/5/25
years = int(input('How many years?:'))
rainfall_list1 = []
for count1 in range(1, years + 1):
    for count2 in range(0,12):
        rainfall_list1 += [int(input('Enter inches of rain:'))]
average_rain = (sum(rainfall_list1))/(12*years)
print("Average amount of rain in",years, "year(s):",average_rain)