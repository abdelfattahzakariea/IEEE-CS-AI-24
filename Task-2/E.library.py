library_catalogue = {}
details = {"authar":"",
           "publication_year":""}

flag=True

while flag:
    title = input("\nWhat is book title ? ")
    authar = input("authar name ? ") 
    publication_year = input("publication year ? ")
# Store the response in the dictionary:
    details["authar"]=authar
    details["publication_year"]=publication_year
    library_catalogue[title] = details
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to enter another book ? (yes/ no) ")
    if repeat == 'no':
        flag = False
#print(library_catalogue.items())

# Polling is complete. Show the results.
print("\n--- liprary books ---")
for title , detail in library_catalogue.items():
    print(f" book => {title} " + " authar => " + detail["authar"] + "   publication year =>"+detail["publication_year"] )