import customtkinter as ctk

from modules.web_scraper import scrape_title
from modules.batch_scraper import batch_scrape


class ScraperPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        # Title
        title = ctk.CTkLabel(
            self,
            text="Web Scraper",
            font=("Arial", 30, "bold")
        )

        title.pack(
            pady=(20, 20)
        )

        # URL Entry
        self.url_entry = ctk.CTkEntry(
            self,
            width=500,
            placeholder_text="Enter Website URL"
        )

        self.url_entry.pack(
            pady=10
        )

        # Single Scrape Button
        self.scrape_button = ctk.CTkButton(
            self,
            text="Scrape Website",
            command=self.scrape_single
        )

        self.scrape_button.pack(
            pady=10
        )

        # Batch Scrape Button
        self.batch_button = ctk.CTkButton(
            self,
            text="Run Batch Scraper",
            command=self.run_batch
        )

        self.batch_button.pack(
            pady=10
        )

        # Status Label
        self.result_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.result_label.pack(
            pady=10
        )

        # Output Box
        self.result_box = ctk.CTkTextbox(
            self,
            width=700,
            height=300
        )

        self.result_box.pack(
            pady=20
        )

    def scrape_single(self):

        url = self.url_entry.get()

        result = scrape_title(
            url
        )

        self.result_box.delete(
            "1.0",
            "end"
        )

        if result["success"]:

            self.result_label.configure(
                text="Website title extracted successfully.",
                text_color="green"
            )

            text = ""

            text += (
                f"Title: "
                f"{result['title']}\n\n"
            )

            text += (
                f"Status Code: "
                f"{result['status_code']}\n\n"
            )

            text += (
                f"Response Time: "
                f"{result['response_time']} sec"
            )

            self.result_box.insert(
                "1.0",
                text
            )

        else:

            self.result_label.configure(
                text=result["message"],
                text_color="red"
            )

    def run_batch(self):

        result = batch_scrape(
            "input/urls.txt"
        )

        self.result_box.delete(
            "1.0",
            "end"
        )

        if result["success"]:

            self.result_label.configure(
                text="Batch scraping completed successfully.",
                text_color="green"
            )

            text = ""

            text += (
                f"Total URLs: "
                f"{result['total_urls']}\n\n"
            )

            text += (
                f"Successful: "
                f"{result['successful']}\n\n"
            )

            text += (
                f"Failed: "
                f"{result['failed']}\n\n"
            )

            text += (
                f"Success Rate: "
                f"{result['success_rate']}%\n\n"
            )

            text += (
                f"Average Response Time: "
                f"{result['average_response_time']} sec\n\n"
            )

            text += (
                f"Fastest Website: "
                f"{result['fastest_domain']}\n\n"
            )

            text += (
                f"Slowest Website: "
                f"{result['slowest_domain']}"
            )

            self.result_box.insert(
                "1.0",
                text
            )

        else:

            self.result_label.configure(
                text=result["message"],
                text_color="red"
            )