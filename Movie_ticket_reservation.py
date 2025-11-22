from datetime import datetime, timedelta
#movie names
M = ["Wicked", "Gladiator II", "Titanic", "Twilight", "Wolf Of Wall Street"] 

#timings
T = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
#seat types
P = { 
    1: {"n": "Reg", "p": 200}, 
    2: {"n": "Prem", "p": 350},
    3: {"n": "VIP", "p": 500}
}

# Booking
B = []

# rows and columns
R = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
C = list(range(1, 11))

def show_seats(m, d, t):
    """Show seat layout"""
    print("\n---------SEATS--------- ")
    print("---------SCREEN---------")
    print("\n    ", end="")
    for col in C:
        print(f"{col:3}", end="")
    print()
    
    for row in R:
        print(f"{row}  ", end="")
        for col in C:
            s = f"{row}{col}"
            # Check if booked
            if is_booked(m, d, t, s):
                print(" X ", end="")
            else:
                print(" O ", end="")
        print()
    print("O=Open | X=Taken")

def is_booked(m, d, t, s):
    #Check if seat is booked
    for b in B:
        if (b['movie'] == m and 
            b['date'] == d and 
            b['time'] == t and 
            s in b['seats']):
            return True
    return False

def get_seats(m, d, t, num): 
    #Get selected seats
    Seat_chosen = []
      
    for i in range(num):
        s = input(f"Enter seat {i+1} (e.g., A5): ").upper()
        
        # checking for invalid inputs
        if s[0] not in R or int(s[1:]) not in C:
            print("ERROR: Invalid seat, skipping.")
            continue
        #checking if the seat is already taken
        if is_booked(m, d, t, s):
            print("ERROR: Seat taken, skipping.")
            continue
            
        if s in Seat_chosen:
            print("ERROR: Already picked, skipping.")
            continue
            
        Seat_chosen.append(s)
        print(f"-> {s} selected")
    
    return Seat_chosen

print("CINEMA BOOKING ")

# Movie selection
print("\nMovies:")
for i, m in enumerate(M, 1):
    print(f"{i}. {m}")
movie_sel = int(input("\nSelect movie (1-5): "))
sel_m = M[movie_sel - 1]

# Date selection
print("\nDates (7 days):")
for i in range(7):
    day = datetime.now() + timedelta(days=i)
    print(f"{i+1}. {day.strftime('%Y-%m-%d')}")
d_sel = int(input("\nSelect date (1-7): "))
sel_d = (datetime.now() + timedelta(days=d_sel-1)).strftime('%Y-%m-%d (%A)')

# Time selection
print("\nTimes:")
for i, t in enumerate(T, 1):
    print(f"{i}. {t}")
t_sel = int(input("\nSelect time (1-5): "))
sel_t = T[t_sel - 1]

# Seat Type selection
print("\nPrices:")
for k, cat in P.items():
    print(f"{k}. {cat['n']} - {cat['p']}")
cat_sel = int(input("\nSelect price category (1-3): "))
sel_cat = P[cat_sel]

# Number of tickets
num_tickets = int(input("\nNumber of tickets: "))

# Display seats and get selection
show_seats(sel_m, sel_d, sel_t)
sel_seats = get_seats(sel_m, sel_d, sel_t, num_tickets)

# Customer details
name = input("\nName: ")
phone = input("Phone: ")

# Calculate total
final_price = sel_cat['p'] * num_tickets

# Summary
print("\n SUMMARY ")
print(f"Movie: {sel_m}")
print(f"Seats: {', '.join(sel_seats)}")
print(f"Total: {final_price}")

# Confirmation
ok = input("\nConfirm (yes/no): ").lower()

if ok == "yes":
    # Save booking
    B.append({
        'movie': sel_m,
        'date': sel_d,
        'time': sel_t,

        'seats': sel_seats,
        'name': name,
        'phone': phone
    })
    print("\nConfirmed!")
else:
    print("\nCancelled.")
