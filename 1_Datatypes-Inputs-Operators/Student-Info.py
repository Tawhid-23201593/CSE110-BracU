"""
Take the first name, last name, age and CGPA of a student.
Change the last name to "Rahman". Subtract 2 from the age
and add 0.25 with the CGPA. Finally print the information
in the way shown in the output.
Sample Input:
First Name: Labiba
Last Name: Arif
Age: 23
CGPA: 3.7
Sample Output:
Name: Labiba Rahman
Age: 21
CGPA: 3.95

"""
name1 = input("First Name: ")
name2 = input("Second name: ")
age = int(input("Age: "))
cgpa = float(input("CGPA: "))
print("Name:",name1,"Rahman")
print("Age:",age-2)
print("CGPA:",cgpa+0.25)