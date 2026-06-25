import customtkinter as ctk
import webbrowser


class AboutPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="About",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(30, 20))

        info = """
Smart Task Automation Suite

Version: 1.0

Developer:
Vaishnavi Bagal

Technologies:
• Python
• CustomTkinter
• Requests
• BeautifulSoup
• JSON
• CSV

A desktop automation suite that
includes:

✓ Email Extractor
✓ File Organizer
✓ Web Scraper
✓ Reports Manager
        """

        label = ctk.CTkLabel(
            self,
            text=info,
            justify="left",
            font=("Arial", 16)
        )
        label.pack(pady=20)

        github_button = ctk.CTkButton(
            self,
            text="Open GitHub Repository",
            command=self.open_github
        )
        github_button.pack(pady=10)

    def open_github(self):

        webbrowser.open(
            "https://github.com/YOUR_USERNAME/Smart_Task_Automation_Suite"
        )