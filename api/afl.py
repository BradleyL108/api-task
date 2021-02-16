nonvicteams = ["Brisbane Lions", "Gold Coast Suns", "Sydney Swans", "Greater Western Sydney Giants", "Adelaide Crows", "Port Adelaide Power", "West Coast Eagles", "Fremantle Dockers"]
start = "yes"
def starting():
    start = (input("Would you like to try another function? "))
    print("""
          """)
    if start == "yes" or start == "y":
        AFLlist()
    elif start == "no" or start == "n":
        print("Thank you!")
    elif start != "1" or start != "2" or start != "3":
        starting()
def printteams():
    nonvicteams = ["Brisbane Lions", "Gold Coast Suns", "Sydney Swans", "Greater Western Sydney Giants", "Adelaide Crows", "Port Adelaide Power", "West Coast Eagles", "Fremantle Dockers"]
    for d in nonvicteams:
        print("*", d)
    starting()
def teamsearch():
    nonvicteams = ["Brisbane Lions", "Gold Coast Suns", "Sydney Swans", "Greater Western Sydney Giants", "Adelaide Crows", "Port Adelaide Power", "West Coast Eagles", "Fremantle Dockers"]
    answer = input("What team would you like to search for in the non-Victorian AFL team list? ")
    if answer in nonvicteams:
        print("Yes", answer, ", Is in Non-Victorian Teams")
        team = input("Would you like to search for another team? ")
    else:
        print("No", answer, ", is not in Non-Victorian Teams")
        team = input("Would you like to search for another team? ")
    if team == "y" or team == "yes":
        teamsearch()
    elif team == "no" or team == "n":
        starting()
def teamcount():
    nonvicteams = ["Brisbane Lions", "Gold Coast Suns", "Sydney Swans", "Greater Western Sydney Giants", "Adelaide Crows", "Port Adelaide Power", "West Coast Eagles", "Fremantle Dockers"]
    print(len(nonvicteams))
    starting()
def AFLlist():
    section = input("""1 = Print all non Victorian Teams
2 = Search for a team in Non Victorian teams
3 = Print the amount of Non Victorian Teams

Which function would you like to use? """)
    if section == "1":
        printteams()
    elif section == "2":
        teamsearch()
    elif section == "3":
        teamcount()
    elif section != "1" or section != "2" or section != "3":
        AFLlist()
if start == "yes" or start == "y":
    AFLlist()