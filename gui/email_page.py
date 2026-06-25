import customtkinter as ctk
from tkinter import filedialog

from modules.email_extractor import extract_emails


class EmailPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Email Extractor",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(
            pady=20
        )

        # Input file
        self.input_button = ctk.CTkButton(
            self,
            text="Select Input File",
            command=self.select_input_file
        )

        self.input_button.pack(
            pady=10
        )

        self.input_label = ctk.CTkLabel(
            self,
            text="No file selected"
        )

        self.input_label.pack()

        # Output file
        self.output_button = ctk.CTkButton(
            self,
            text="Select Output File",
            command=self.select_output_file
        )

        self.output_button.pack(
            pady=10
        )

        self.output_label = ctk.CTkLabel(
            self,
            text="No output selected"
        )

        self.output_label.pack()

        # Extract button
        self.extract_button = ctk.CTkButton(
            self,
            text="Extract Emails",
            command=self.extract
        )

        self.extract_button.pack(
            pady=20
        )

        # Result area
        self.result_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.result_label.pack(
            pady=20
        )

        self.input_file = ""

        self.output_file = ""

    def select_input_file(self):

        self.input_file = filedialog.askopenfilename()

        self.input_label.configure(
            text=self.input_file
        )

    def select_output_file(self):

        self.output_file = filedialog.asksaveasfilename(
            defaultextension=".txt"
        )

        self.output_label.configure(
            text=self.output_file
        )

    def extract(self):

        if not self.input_file or not self.output_file:

            self.result_label.configure(
                text="Please select both files."
            )

            return

        result = extract_emails(
            self.input_file,
            self.output_file
        )

        if result["success"]:

            self.result_label.configure(
                text=
                f"Total Emails: {result['total_found']}\n"
                f"Unique Emails: {result['unique_found']}\n"
                f"Duplicates Removed: {result['duplicates_removed']}"
            )

        else:

            self.result_label.configure(
                text=result["message"]
            )