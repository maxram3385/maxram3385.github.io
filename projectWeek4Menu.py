from datetime import datetime

studentID = "maxram3385"

menuOptions = (
    "Input Data",
    "View Current Data",
    "Generate Report"
)


# Converts a weight from pounds to kilograms.
def convertData(data):
    convertedValue = data / 2.205
    return convertedValue


# Appends comma-separated data to a CSV file or creates the file if it does not exist.
def insertData(path, data):
    try:
        with open(path, "a") as file:
            file.write(data + "\n")
        return True
    except OSError as error:
        print("Error writing to the file:", error)
        return False


# Displays the path and contents of a CSV file.
def viewData(path):
    try:
        with open(path, "r") as file:
            print("The file", path)
            print(file.read())
    except OSError as error:
        print("Error reading the file:", error)


# Gets the user's data, converts the weight, and saves each entry to the CSV file.
def getInput():
    try:
        entries = int(input("How many entries are you inputting?\n"))

        for entry in range(entries):
            date = input("Enter a date:\n")
            value = float(input("Enter the weight in pounds for the inputted date:\n"))

            convertedValue = convertData(value)
            data = str(date) + "," + str(value) + "," + str(convertedValue)

            if insertData("ZooData.csv", data):
                print("The following data was saved at", datetime.now(), ":", data)
    except (ValueError, OSError) as error:
        print("Error entering or saving the data:", error)


print(studentID + "'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

for number, option in enumerate(menuOptions, start=1):
    print(number, option)

choice = input()

if choice == "1":
    print("You selected 1 at", datetime.now())
    getInput()
elif choice == "2":
    print("You selected 2 at", datetime.now())
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")