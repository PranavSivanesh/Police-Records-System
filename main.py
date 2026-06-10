import csv
import os
import matplotlib.pyplot as plt

print("**************Crime Records System ****************")

while(True):
    print("Choose one of the options")
    print()
    print("1. View Criminal Records")
    print("2. Search Criminal Records")
    print("3. Add Criminal Record")
    print("4. Delete a Criminal Record")
    print("5. Update a Criminal Record")
    print()
    print("6. View Police Records")
    print("7. Search Police Records")
    print("8. Add a new officer")
    print("9. Delete an officer record")
    print("10. Update an Officer record")
    print()
    print("GRAPHS")
    print("11. Most Common Crime Types")
    print("12. Crime rate Over the years")
    print("13. Crimes by Emirates")
    print("14. Crimes against Women")
    print("15. Crimes against Senior Citizens")
    print("16. Age distribution of Criminals")
    print("17. Exit")



    choice = int(input("Option Number: "))
    print()

    if choice == 1:
        with open("Criminal.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0]
            if not rows:
                print("Empty File")
            print("Convict Details!")
            print()
            for row in rows:
                print("Id: " + row[0])
                print("Name: " + row[1])
                print("Age: " + row[2])
                print('Gender: ' + row[3])
                print()
        input("\nPress Enter to continue...")

    elif choice == 2:
        search = input('Enter name of the Criminal: ')
        with open("Criminal.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 0:
                    continue
                if row[1] == search:
                    print()
                    print("Convict Details!")
                    print("Id: " + row[0])
                    print("Name: " + row[1])
                    print("Age: " + row[2])
                    print('Gender: ' + row[3])
        input("\nPress Enter to continue...")

    elif choice == 3:
        id = 0
        if os.path.exists("Criminal.csv"):
            with open("Criminal.csv", "r") as file:
                reader = csv.reader(file)
                rows = [row for row in reader if len(row) > 0]
                if rows:
                    id = max(int(row[0]) for row in rows)

        name = input("Enter Name: ")
        print()
        age = int(input("Enter age of Convict: "))
        print()
        gender = input("Enter convict's gender: ")
        id += 1

        with open("Criminal.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([id,name,age,gender])
        print()
        print("Criminal " + name + " of age " + str(age) + " added!")
        input("\nPress Enter to continue...")

    elif choice == 4:
        name = input("Enter the Criminal Name to be deleted: ")
        with open("Criminal.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0 and row[0] != name]         
                                                                                    #same as rows = []
        with open("Criminal.csv", "w") as file:                                              #for row in reader:
            writer = csv.writer(file)                                                            #if row[0] != name:
            writer.writerows(rows)                                                                     #rows.append(row)
        input("\nPress Enter to continue...")     

    elif choice == 5:
        id = int(input("Enter the ID of the criminal to be updated: "))
        print()
        edit = int(input("Enter the number of changes to make: "))
        print()
        
        with open("Criminal.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0]
        
        for row in rows:
            if int(row[0]) == id:
                for i in range(edit):
                    change = input("Enter the field you want to make changes (Name, Age, Gender): ")
                    new_value = input("Enter new Value: ")
                    if change.lower() == "name":
                        row[1] = new_value
                        print("Name Edited")
                    elif change.lower() == "age":
                        row[2] = new_value
                        print("Age edited")
                    elif change.lower() == "gender":
                        row[3] = new_value
                        print("Gender edited")
                    else:
                        print("Enter Valid field name!")
        
        with open("Criminal.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        input("\nPress Enter to continue...")  

    elif choice == 6:
        with open("Officer.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0]
            
            if not rows:
                print("Empty File")
            print("Officer Details!")
            print()
            
            for row in rows:
                print("Id: " + row[0])
                print("Name: " + row[1])
                print("Age: " + row[2])
                print('Gender: ' + row[3])
                print()
        input("\nPress Enter to continue...")  

    elif choice == 7:
        search = input('Enter name of the Officer: ')
        with open("Officer.csv", "r") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) == 0:
                    continue
                if row[1] == search:
                    print()
                    print("Officer Details!")
                    print("Id: " + row[0])
                    print("Name: " + row[1])
                    print("Age: " + row[2])
                    print('Gender: ' + row[3])
        input("\nPress Enter to continue...")  

    elif choice == 8:
        id = 0
        if os.path.exists("Officer.csv"):
            with open("Officer.csv", "r") as file:
                reader = csv.reader(file)
                rows = [row for row in reader if len(row) > 0]
                if rows:
                    id = max(int(row[0]) for row in rows)

        name = input("Enter Name: ")
        print()
        age = int(input("Enter age of Officer: "))
        print()
        gender = input("Enter officer's gender: ")
        id += 1

        with open("Officer.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([id,name,age,gender])
        print()
        print("Officer " + name + " of age " + str(age) + " added!")
        input("\nPress Enter to continue...")  

    elif choice == 9:
        name = input("Enter the Officer Name to be deleted: ")
        with open("Officer.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0 and row[0] != name]        
        
        with open("Officer.csv", "w") as file:                                     
            writer = csv.writer(file)                                            
            writer.writerows(rows)      
        input("\nPress Enter to continue...")  

    elif choice == 10:
        id = int(input("Enter the ID of the Officer to be updated: "))
        print()
        edit = int(input("Enter the number of changes to make: "))
        print()
        
        with open("Officer.csv", "r") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if len(row) > 0]
        
        for row in rows:
            if int(row[0]) == id:
                for i in range(edit):
                    change = input("Enter the field you want to make changes (Name, Age, Gender): ")
                    new_value = input("Enter new Value: ")
                    if change.lower() == "name":
                        row[1] = new_value
                        print("Name Edited")
                    elif change.lower() == "age":
                        row[2] = new_value
                        print("Age edited")
                    elif change.lower() == "gender":
                        row[3] = new_value
                        print("Gender edited")
                    else:
                        print("Enter Valid field name!")
        
        with open("Officer.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        input("\nPress Enter to continue...")  

    elif choice == 11:
        labels = ["Theft", "Assault", "Fraud", "Harassment", "Trafficking"]
        sizes = [35, 25, 20, 12, 8]

        plt.pie(sizes, labels = labels, autopct='%1.1f%%')
        plt.title("Most Common Crime Types in UAE")
        plt.show()
        input("\nPress Enter to continue...")
    
    elif choice == 12:
        years = [2018, 2019, 2020, 2021, 2022, 2023]
        crime_rate = [4500, 4800, 3900, 4100, 4600, 4300]

        plt.plot(years, crime_rate, marker='o')
        plt.title("Crime Rate Over Years")
        plt.xlabel("Year")
        plt.ylabel("Number of Crimes")
        plt.show()
        input("\nPress Enter to continue...")

    elif choice == 13:
        emirates = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "RAK", "Fujairah", "UAQ"]
        crimes = [1200, 980, 650, 320, 280, 190, 150]

        plt.bar(emirates, crimes, color='blue')
        plt.title("Crimes by Emirate")
        plt.xlabel("Emirate")
        plt.ylabel("Number of Crimes")
        plt.show()
        input("\nPress Enter to continue...")
    
    elif choice == 14:
        categories = ["Harassment", "Domestic Violence", "Assault", "Trafficking"]
        cases = [320, 210, 180, 90]

        plt.bar(categories, cases, color='red')
        plt.title("Crimes Against Women")
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Cases")
        plt.show()
        input("\nPress Enter to continue...")
    
    elif choice == 15:
        crimes = ["Fraud", "Theft", "Assault", "Neglect"]
        cases = [150, 200, 80, 120]
        
        plt.bar(crimes, cases, color='orange')
        plt.title("Crimes Against Senior Citizens")
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Cases")
        plt.show()
        input("\nPress Enter to continue...")

    elif choice == 16:
        ages = []
        with open("Criminal.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    ages.append(int(row[2]))  # age is at index 2

        plt.hist(ages, bins=5)
        plt.title("Age Distribution of Criminals")
        plt.xlabel("Age")
        plt.ylabel("Number of Criminals")
        plt.show()
        input("\nPress Enter to continue...")

    elif choice == 17:
        print("Goodbye")
        break
    else:
        print("Enter Valid Input. Goodbye")
        input("\nPress Enter to continue...")  