import sys
from pathlib import Path


sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)
import customtkinter as ctk

from dashboard import DashboardPage
from email_page import EmailPage
from organizer_page import OrganizerPage
from scraper_page import ScraperPage
from reports_page import ReportsPage
from settings_page import SettingsPage
from about_page import AboutPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SmartTaskApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Smart Task Automation Suite")
        self.geometry("1200x700")

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Main frame
        self.main_frame = ctk.CTkFrame(
            self
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Title
        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="Smart Task\nAutomation",
            font=(
                "Arial",
                18,
                "bold"
            )
        )

        self.title_label.pack(
            pady=(30, 40),
            padx=20
        )

        # Buttons
        self.dashboard_button = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            command=self.show_dashboard
        )

        self.dashboard_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.email_button = ctk.CTkButton(
            self.sidebar,
            text="Email Extractor",
            command=self.show_email
        )

        self.email_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.organizer_button = ctk.CTkButton(
            self.sidebar,
            text="File Organizer",
            command=self.show_organizer
        )

        self.organizer_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.scraper_button = ctk.CTkButton(
            self.sidebar,
            text="Web Scraper",
            command=self.show_scraper
        )

        self.scraper_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.report_button = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            command=self.show_reports
        )

        self.report_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.settings_button = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            command=self.show_settings
        )

        self.settings_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.about_button = ctk.CTkButton(
            self.sidebar,
            text="About",
            command=self.show_about
        )

        self.about_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # Start page
        self.current_page = None

        self.show_dashboard()

    def clear_page(self):

        if self.current_page is not None:
            self.current_page.destroy()

    def show_dashboard(self):

        self.clear_page()

        self.current_page = DashboardPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_email(self):

        self.clear_page()

        self.current_page = EmailPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_organizer(self):

        self.clear_page()

        self.current_page = OrganizerPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_scraper(self):

        self.clear_page()

        self.current_page = ScraperPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_reports(self):

        self.clear_page()

        self.current_page = ReportsPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_settings(self):

        self.clear_page()

        self.current_page = SettingsPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_about(self):

        self.clear_page()

        self.current_page = AboutPage(
            self.main_frame
        )

        self.current_page.pack(
            fill="both",
            expand=True
        )

app = SmartTaskApp()

app.mainloop()