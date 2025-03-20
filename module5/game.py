def payoff(ticket, draw):
    
    # Count how many numbers appear on both the ticket
    # and the winning 3-number draw
    count=0
    for x in ticket:
        if x in draw:
            count+=1
        
    # If 3 numbers match, return $210.  If 2 numbers match, return $70
    if count==3: return 210
    elif count==2: return 70
    else: return 0


def profit(alltickets, draw):
    
    # You pay 200 dollars at the start
    winnings = -200

    # For each ticket, add the payoff to the total winnings
    for ticket in alltickets:
        winnings += payoff(ticket, draw)
    return winnings


# Decide what the seven tickets are (you fill this out!)
# Can you pick seven tickets where you NEVER lose money?

T1=[1,2,3]
T2=[1,4,5]
T3=[1,6,7]
T4=[2,4,6]
T5=[2,5,7]
T6=[3,5,6]
T7=[3,4,7]
OurTickets = [T1,T2,T3,T4,T5,T6,T7]

# Randomly choose three different numbers from 1 to 7
import random
OurDraw = random.sample(range(1, 8), 3)


print(f"the triplet is {OurDraw}. Our profit was", profit(OurTickets, OurDraw), "dollars")