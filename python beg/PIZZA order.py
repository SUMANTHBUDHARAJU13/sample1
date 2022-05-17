size=input("What size of Pizza do you want? S, M ,L ")
add_pepperoni=input("Do you want to add pepperoni? Yes or No ")
extr_cheese=input("Do you want extra cheese? Yes or No ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
if add_pepperoni=="Yes":
    if size =="S":
        bill+=2
    else:
        bill+=3
if extr_cheese=="Yes":
    bill+=1
print(f"your final bill is ${bill}")


