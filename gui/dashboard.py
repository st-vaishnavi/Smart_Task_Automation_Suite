import customtkinter as ctk
from pathlib import Path


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        # Title
        title = ctk.CTkLabel(
            self,
            text="Smart Task Automation Suite",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(30, 20))

        # Cards frame
        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(pady=20)

        # Create cards
        self.email_card = self.create_card(
            cards_frame,
            "📧 Email Extractor",
            self.get_email_count()
        )

        self.organizer_card = self.create_card(
            cards_frame,
            "📁 File Organizer",
            self.get_file_count()
        )

        self.scraper_card = self.create_card(
            cards_frame,
            "🌐 Web Scraper",
            self.get_web_count()
        )

        self.report_card = self.create_card(
            cards_frame,
            "📄 Reports",
            self.get_report_count()
        )

        # Grid
        self.email_card.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )

        self.organizer_card.grid(
            row=0,
            column=1,
            padx=20,
            pady=20
        )

        self.scraper_card.grid(
            row=1,
            column=0,
            padx=20,
            pady=20
        )

        self.report_card.grid(
            row=1,
            column=1,
            padx=20,
            pady=20
        )

        # Status
        status = ctk.CTkLabel(
            self,
            text="System Ready ✅",
            font=("Arial", 18)
        )
        status.pack(pady=20)

    def create_card(
            self,
            parent,
            title,
            value
    ):

        card = ctk.CTkFrame(
            parent,
            width=250,
            height=130
        )

        card.pack_propagate(False)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=(20, 10))

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 20)
        )
        value_label.pack()

        return card

    def get_email_count(self):

        path = Path(
            "output/emails.txt"
        )

        if path.exists():

            with open(
                    path,
                    "r",
                    encoding="utf-8"
            ) as file:

                return str(
                    len(file.readlines())
                )

        return "0"

    def get_file_count(self):

        path = Path(
            "output/history.json"
        )

        if path.exists():

            return "Available"

        return "0"

    def get_web_count(self):

        path = Path(
            "output/web_titles.txt"
        )

        if path.exists():

            with open(
                    path,
                    "r",
                    encoding="utf-8"
            ) as file:

                lines = file.readlines()

            return str(
                len(
                    [
                        line
                        for line in lines
                        if line.startswith(
                            "URL:"
                        )
                    ]
                )
            )

        return "0"

    def get_report_count(self):

        output = Path(
            "output"
        )

        if output.exists():

            return str(
                len(
                    list(
                        output.glob("*")
                    )
                )
            )

        return "0"