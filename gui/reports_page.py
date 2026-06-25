import os
import subprocess
from pathlib import Path
import customtkinter as ctk
import customtkinter as ctk
from pathlib import Path


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)
        self.current_file = None

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Reports",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(
            pady=(20, 20)
        )

        # Buttons
        self.email_button = ctk.CTkButton(
            self,
            text="Email Report",
            command=lambda: self.load_report(
                "output/emails.txt"
            )
        )

        self.email_button.pack(
            pady=5
        )

        self.web_button = ctk.CTkButton(
            self,
            text="Web Scraper Report",
            command=lambda: self.load_report(
                "output/web_report.txt"
            )
        )

        self.web_button.pack(
            pady=5
        )

        self.organizer_button = ctk.CTkButton(
            self,
            text="Organization Report",
            command=lambda: self.load_report(
                "output/organization_report.txt"
            )
        )

        self.organizer_button.pack(
            pady=5
        )

        self.log_button = ctk.CTkButton(
            self,
            text="Logs",
            command=lambda: self.load_report(
                "output/logs.txt"
            )
        )

        self.log_button.pack(
            pady=5
        )

        # Status label
        self.status_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.status_label.pack(
            pady=10
        )
        self.refresh_button = ctk.CTkButton(
         self,
         text="Refresh",
         command=self.refresh_report
        )
        self.refresh_button.pack(pady=5)

        self.open_button = ctk.CTkButton(
            self,
            text="Open Report",
            command=self.open_report
        )
        self.open_button.pack(pady=5)

        self.clear_button = ctk.CTkButton(
        self,
        text="Clear Report",
        command=self.clear_report
     )
        self.clear_button.pack(pady=5)   

        # Textbox
        self.report_box = ctk.CTkTextbox(
            self,
            width=750,
            height=350
        )

        self.report_box.pack(
            pady=20
        )


    def load_report(self, file_path):
        self.current_file = file_path
        self.report_box.delete(
            "1.0",
            "end"
        )

        path = Path(file_path)

        if path.exists():

            content = path.read_text(
                encoding="utf-8"
            )

            self.report_box.insert(
                "1.0",
                content
            )

            self.status_label.configure(
                text="Report loaded successfully.",
                text_color="green"
            )

        else:

            self.status_label.configure(
                text="File not found.",
                text_color="red"
            )
    def refresh_report(self):
        if self.current_file:
            self.load_report(
                self.current_file
            )

    def open_report(self):
        if not self.current_file:
            return

        path = Path(
            self.current_file
        )

        if path.exists():
            os.startfile(
                path
            )

    def clear_report(self):
        if not self.current_file:
            return

        path = Path(
            self.current_file
        )

        if path.exists():
            path.write_text(
                "",
                encoding="utf-8"
            )

            self.report_box.delete(
                "1.0",
                "end"
            )

            self.status_label.configure(
                text="Report cleared successfully.",
                text_color="green"
            )