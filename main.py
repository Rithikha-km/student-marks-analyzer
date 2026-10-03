name=input('Enter name: ')
python=int(input("Enter Python mark: "))
maths=int(input("Enter Maths mark: "))
physics=int(input("Enter Physics mark: "))
chemistry=int(input("Enter Chemistry mark: "))
english=int(input("Enter English mark: "))
total = python + maths + physics + chemistry + english
percentage = total/5
if percentage >= 90:
    grade="A+"
elif percentage >= 80:
    grade="A"
elif percentage >= 70:
    grade="B"
elif percentage >= 60:
    grade="C"
else:
    grade="D"
highest=max(python, maths, physics, chemistry, english)
lowest=min(python, maths, physics, chemistry, english)
print("\n----- RESULT -----")
print("Name:", name)
print("Total:", total, "/500")
print("Percentage:", percentage)
print("Grade:", grade)
print("Highest mark:", highest)
print("Lowest mark:", lowest)