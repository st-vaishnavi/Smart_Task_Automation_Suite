from modules.email_extractor import extract_emails
from modules.file_organizer import organize_files
from modules.web_scraper import scrape_title
from modules.batch_scraper import batch_scrape

while True:

    print("\n===== SMART TASK AUTOMATION SUITE =====")
    print("1. Email Extractor")
    print("2. File Organizer")
    print("3. Single Website Scraper")
    print("4. Batch Website Scraper")
    print("5. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":

        result = extract_emails(
            "input/sample.txt",
            "output/emails.txt"
        )

        if result["success"]:

            print("\nEmail extraction completed successfully.")

            print(
                "Total emails found:",
                result["total_found"]
            )

            print(
                "Unique emails found:",
                result["unique_found"]
            )

            print(
                "Duplicates removed:",
                result["duplicates_removed"]
            )

        else:

            print(
                "Error:",
                result["message"]
            )

    elif choice == "2":

        result = organize_files(
            "input/Downloads"
        )

        if result["success"]:

            print(
                "\nFile organization completed successfully."
            )

            print(
                "Files moved:",
                result["moved_files"]
            )

            print(
                "Files skipped:",
                result["skipped_files"]
            )

            print(
                "Total size processed:",
                result["total_size_bytes"],
                "bytes"
            )

        else:

            print(
                "Error:",
                result["message"]
            )

    elif choice == "3":

        url = input("Enter the website URL: ")

        result = scrape_title(url)
        print(result)

        if result["success"]:

            print(
                "\nWebsite title scraping completed successfully."
            )

            print(
                "Title:",
                result["title"]
            )

            print(
                "Status Code:",
                result["status_code"]
            )

            print(
                "Response Time:",
                result["response_time"],
                "seconds"
            )
        else:

            print(
                "Error:",
                result["message"]
            )

    elif choice == "4":
        result = batch_scrape(
            "input/urls.txt"
        )

        if result["success"]:

            print(
                "\nBatch scraping completed successfully."
            )

            print(
                "Total URLs:",
                result["total_urls"]
            )

            print(
                "Successful:",
                result["successful"]
            )

            print(
                "Failed:",
                result["failed"]
            )

            print(
    "Average Response Time:",
    result["average_response_time"],
    "seconds"
)

            print(
    "Success Rate:",
    result["success_rate"],
    "%"
)

            print(
    "Fastest Website:",
    result["fastest_domain"]
)

            print(
    "Slowest Website:",
    result["slowest_domain"]
)

        else:

            print(
                "Error:",
                result["message"]
            )
    elif choice == "5":

        print("\nExiting...")
        break

    else:

        print(
            "\nInvalid choice!"
        )