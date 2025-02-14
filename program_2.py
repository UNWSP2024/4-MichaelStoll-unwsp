#title: movie tickets
#author: michael stoll
#date: 2/11/25
movies = int(input('How many movies?:'))
ticket_list1 = []
for count in range(1, movies + 1):
    movie = str(input("Enter movie name:"))
    ticket_list1 += [int(input('Enter number of tickets:'))]
total_tickets = sum(ticket_list1)
print(ticket_list1)
print("Total amount of tickets:",total_tickets)