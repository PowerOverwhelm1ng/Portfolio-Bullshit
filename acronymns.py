user_input = str(input("Enter your phrase!: "))
text = user_input.split()
acronym = " "
for i in text:
    acronym = acronym + str(i[0]).upper()
print(acronym)