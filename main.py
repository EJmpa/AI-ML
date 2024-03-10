#!/usr/bin/env python3
import time
from digital_diary import DigitalDiary

def main() -> None:
    """
    Main function to run the digital diary program.
    """
    diary = DigitalDiary()

    while True:
        print("\n1. Add Contact")
        print("2. Show Contacts")
        print("3. Exit")

        choice: str = input("Enter your choice: ")

        if choice == '1':
            name: str = input("Enter your full name: ")
            phone_number: str = input("Enter phone number: ")
            diary.add_contact(name, phone_number)
        elif choice == '2':
            diary.show_contacts()
        elif choice == '3':
            print("Exiting...")
            time.sleep(2)
            print("Successfully Exited")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
