import sys

donation_data = {
'William Gates, III': [100000.00,553784.49],
'Mark Zuckerberg': [5000.00,5000.00,6396.10],
'Jeff Bezos': [877.33],
'Paul Allen': [100.00,100.00,508.42]
}

def menu():
    selection = input("""This program will hopefully help you send some meaningful messages
Type the corresponding number to select from the following list:

1: Send a Thank You
2: Create a Report
3: Send Thank You to Everyone
4: Quit
>""")

    switch_menu = {
        '1': send_thank_you,
        '2': create_report,
        '3': send_all,
        '4': quit
    }
    
    while selection not in switch_menu:
        print("Sorry, I didn't recognize that command")
        return

    switch_menu[selection]()

def quit():
    sys.exit()

def send_thank_you():
    name = input("Please enter a full name > ")
	
    while name == "list":
        list_of_donors = "{}, "*(len(donation_data)-1)+"{}"
        print(list_of_donors.format(*donation_data))
        name = input("Please enter a full name > ")

    if name.lower() == "quit":
        return
    
    donation = input("Donation Amount? > ")
    if donation.lower() == "quit":
        return

    donation_data.setdefault(name,[]).append(float(donation))
    print("Data added!")
    letter_dictionary = {'donor':name,'amount':round(float(donation),2)}
    letter(letter_dictionary)
    print(donation_data)

    return donation_data
	
def letter(letter_dictionary):		
    content = """
Dear {donor},

Thank you for your generous donation of ${amount:.2f}

Sincerely,
The Charity
""".format(**letter_dictionary)
    print(content)
    return(content)

	
def create_report():
    result = calculation()
    table(result)
    return

def table(result):
    print(" ")
    print("{:<24}{:<1}{:^13}{:<1}{:^13}{:<1}{:^17}".format('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift'))
    print("-"*67)
    for row in result:
        print("{:<25}{:<1}{:>12.2f}{:>14}{:>2}{:>13.2f}".format(*row))
    print(" ")

def use_total(amounts):
    return amounts[2]

def calculation():
    data = []

    for donor, donations in donation_data.items():
        total_given = round(sum(donations),2)
        num_gifts = len(donations)
        average = round(float(total_given)/float(num_gifts),2)
        data.append([donor, "$", total_given, num_gifts, "$", average])

    sorted_data = sorted(data,key=use_total,reverse=True)
    return sorted_data

def send_all():
    for person in donation_data:
        with open(person.replace(' ','_')+'.txt','w') as f:
            f.write(letter({'donor':person,'amount':donation_data[person][-1]}))
    print("Done!")

if __name__ == '__main__':
    while True:
        menu()