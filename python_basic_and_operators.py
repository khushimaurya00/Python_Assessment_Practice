# member details
name=input("Enter member name:- ")
age=int(input("Enter age:- "))
classes=int(input("Enter classes booked this week:- "))
monthly_fees=float(input("Enter montly fees:- "))
membership = input("Is membership active? (yes/no): ") == "yes"

# book new classes
new_class=input("Do you want to book new class?(yes/no): ").lower()
if new_class == "yes":
    classes +=1

has_e='e' in name
eligible = (membership is True) and (age >15) and (classes <4)

# display summary
print("\n-:Gym Member Summary:- ")
print("member Name:-",name)
print("Age:-",age)
print("classes Booked:-",classes)
print("Monthly Fees:-",monthly_fees)
print("Active Membership:-",membership)
print("Contains letter 'e':-", has_e)
print("Eligible:-", "Eligible" if eligible else "Not Eligible")