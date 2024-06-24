#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees > 100 else "Conference room"
print(venue)

#Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees > 100 else "Conference room"
audio_system = "Large speaker" if attendees > 100 else "Small speaker"
projector = "Large projector" if attendees > 100 else "Small projector"

print("We'll need a" , venue, ",", audio_system, ", and a", projector)

#Task 3: Catering Choices

response = input("Would you like Vegetarian Food?")

if response == "yes":
    print("I recommend Veggie Delight Caterers")
else:
    print("In that case I recommend Gourmet Meals Caterers")