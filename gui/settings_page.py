import customtkinter as ctk
from pathlib import Path


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Settings",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=30)

        # Theme label
        mode_label = ctk.CTkLabel(
            self,
            text="Appearance Mode"
        )
        mode_label.pack(pady=(20, 5))

        # Theme dropdown
        self.mode_menu = ctk.CTkOptionMenu(
            self,
            values=["Dark", "Light", "System"],
            command=self.change_mode
        )
        self.mode_menu.pack(pady=10)

        # Clear Logs button
        self.logs_button = ctk.CTkButton(
            self,
            text="Clear Logs",
            command=self.clear_logs
        )
        self.logs_button.pack(
            pady=20
        )

        # Clear Reports button
        self.report_button = ctk.CTkButton(
            self,
            text="Clear Reports",
            command=self.clear_reports
        )
        self.report_button.pack(
            pady=10
        )

        # Version info
        version = ctk.CTkLabel(
            self,
            text="Version: 1.0\nDeveloper: Vaishnavi Bagal"
        )
        version.pack(
            pady=40
        )

    # Change theme
    def change_mode(self, mode):

        ctk.set_appearance_mode(
            mode
        )

    # Clear logs
    def clear_logs(self):

        try:
            Path(
                "output/logs.txt"
            ).write_text("")

        except:
            pass

    # Clear reports
    def clear_reports(self):

        files = [
            "output/report.txt",
            "output/organization_report.txt",
            "output/web_report.txt"
        ]

        for file in files:

            try:
                Path(
                    file
                ).write_text("")

            except:
                pass