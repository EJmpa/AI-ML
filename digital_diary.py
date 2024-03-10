#!/usr/bin/env python3
from typing import List, Tuple

class DigitalDiary:
    def __init__(self) -> None:
        """Initialize DigitalDiary with an empty list to store contacts."""
        self.contacts: List[Tuple[str, str]] = []

    def add_contact(self, name: str, phone_number: str) -> None:
        """
        Adds a new contact to the diary.

        Args:
            name (str): Name of the contact.
            phone_number (str): Phone number of the contact.
        """
        if name.strip() and phone_number.strip():
            self.contacts.append((name, phone_number))
            print("\nContact added successfully!")
        else:
            print("\nPlease provide both name and number.")

    def show_contacts(self) -> None:
        """Displays all contacts."""
        if self.contacts:
            print("\n--- Contacts ---")
            for idx, (name, phone_number) in enumerate(self.contacts, start=1):
                print(f"{idx}. {name}: {phone_number}")
        else:
            print("\nNo contacts found in the diary.")

