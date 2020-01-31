from datetime import date, datetime

class Customer ():
    def __init__(self, name = None, num_people = None, rooms = None, location = None, budget = None, n_nights = None, s_date = None):
        self.name = name
        self.num_people = num_people
        self.rooms = rooms
        self.location = location
        self.budget = budget
        self.n_nights = n_nights
        self.s_date = s_date

class Room ():
    def __init__(self, number = None, price = None, booking_start = None, booking_end = None, location = None, type = None):
        self.number = number
        self.price = price
        self.booking_start = booking_start
        self.booking_end = booking_end
        self.location = location
        self.type = type

def match_customer_to_room (customer, rooms):
    booked_rooms = []
    i = 0
    #while the customer still has rooms to book
    while i < customer.rooms:
        for room in rooms:
            #if the room is available when the customer wants to book and the room is within price range
            if room.booking_end <= customer.s_date and room.price + 100 <= customer.budget:
                #if the customer did not specify a location or the current room is at the customers location
                if not customer.location or room.location == customer.location:
                    #save room
                    booked_rooms.append(room)
                    room.booking_start = customer.s_date
                    room.booking_end =  customer.s_date + customer.n_nights
                    i+=1
        break

pelagos_suites = []
aqua_blu_boutique = []
albergo_gelsomino = []

def create_hotel (n_rooms, price, location, type):
    #store all the rooms
    hotel = []
    #create a new room for every number of rooms specified
    for i in range (n_rooms):
        #create a room object and assign it its attributes based on the functions inputs
        room = Room()
        room.price = price
        room.location = location
        room.type = type
        hotel.append(room)
    return hotel

def quizAI (HumanInput):
    print('Processing')
    print('done')

    if (HumanInput[2] == '400 or more'):
        return 'Aqua Blue Boutique'

    if (HumanInput[1] == 'A La Carte'):
        return 'Albergo Gelsomino'

    if (HumanInput[0] == 'Family Resort'):
        return 'Pelagos Suites'

    return 'Pelagos Suites'

#example: This creates 10 rooms for the pelagos_suites hotel. Each room costs $500 a night, is at Lambi_beach, and is a studio_suite
pelagos_suites_1 = create_hotel (10, 500, "Lambi_beach", "studio_suite")
#example: This creates 10 rooms for the pelagos_suites hotel. Each room costs $1000 a night, is at Lambi_beach, and is a junior_suite
pelagos_suites_2 = create_hotel (10, 1000, "Lambi_beach", "junior_suite")
#add these rooms to the pelagos_suites array
pelagos_suites.extend(pelagos_suites_1)
pelagos_suites.extend(pelagos_suites_2)

#creates a customer object and assings it the propper attributes
customer = Customer()
customer.name = "Teddy"
customer.num_people = 3
customer.rooms = 2
customer.budget = 10000
customer.n_nights = 5
#booking start date in year/month/day
customer.s_date = datetime(2019,5,9)

Inp = ['Family Resort', 'A La Carte', '400 or more', 'Other']
print(quizAI(Inp))