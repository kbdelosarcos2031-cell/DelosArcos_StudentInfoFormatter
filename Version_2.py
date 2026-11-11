#In lines 2 to 5 it asks the user for their name, section and favorite subject.
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

#In lines 8 to 13 it reviews and modifies the inputs and structure them correctly
full_name = first_name + " " + last_name
name_title = full_name.title()
name_upper = full_name.upper()
sec_upper = section.upper()
sub_title = favorite_subject.title()
char_count = len(full_name)

#in the final lines 16 to 21 it prints out a recipt about the inputs and its correct structure.
print("Formatted Output:")
print("Name:", name_title)
print("Name Code:", name_upper)
print("Section:", section_upper)
print("Favorite Subject:", subject_title)
print("Character Count:", char_count)
