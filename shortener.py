import pyshorteners  # Importing package by which links can be shortened

print("\nThis program is developed by Akshat Dodhiya\t:)")

while 1:
    print("\nEnter 'Q' to Quit the program")

    link = input("Enter the Link to shorten:\n").lower()  # Inputs and stores url in lowercase

    if link == "q" or link == "quit":
        break

    shortener = pyshorteners.Shortener()  # Function to shorten the url

    shortened_link = shortener.tinyurl.short(link)  # using tinyurl.com for shortening the link

    print(shortened_link)  # Printing the shortened link
