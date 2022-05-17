print("Welcome to love calculator🧡🧡")
name1=input("Enter Name1:\n")
name2=input("Enter Name2:\n")
combined_name=name1+name2
lower_case_of_name=combined_name.lower()
t=lower_case_of_name.count("t")
r=lower_case_of_name.count("r")
u=lower_case_of_name.count("u")
e=lower_case_of_name.count("e")
Total1=t+r+u+e
l=lower_case_of_name.count("l")
o=lower_case_of_name.count("o")
v=lower_case_of_name.count("v")
e=lower_case_of_name.count("e")
Total2=l+o+v+e
print("Your Love Score is",Total1+Total2)