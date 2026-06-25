import re
import csv
from pathlib import Path

from modules.logger import write_log
from modules.report_generator import generate_report


def extract_emails(
        input_file: str,
        output_file: str
) -> dict:

    try:
        input_path = Path(input_file)
        output_path = Path(output_file)

        # Create output directory automatically
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Read input file
        text = input_path.read_text(
            encoding="utf-8"
        )

        # Email regex pattern
        email_pattern = (
            r"[a-zA-Z0-9._%+-]+"
            r"@[a-zA-Z0-9.-]+"
            r"\.[a-zA-Z]{2,}"
        )

        emails = re.findall(
            email_pattern,
            text
        )

        # Remove duplicates
        unique_emails = sorted(
            set(emails)
        )

        # Save emails.txt
        with open(
                output_path,
                "w",
                encoding="utf-8"
        ) as file:

            for email in unique_emails:
                file.write(
                    email + "\n"
                )

        # Save emails.csv
        with open(
                "output/emails.csv",
                "w",
                newline="",
                encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(
                csv_file
            )

            writer.writerow(
                ["Email Address"]
            )

            for email in unique_emails:
                writer.writerow(
                    [email]
                )

        total_found = len(
            emails
        )

        unique_found = len(
            unique_emails
        )

        duplicates_removed = (
                total_found -
                unique_found
        )

        # Generate report
        generate_report(
            total_found,
            unique_found
        )

        # Write log
        write_log(
            "Email extraction completed successfully."
        )

        return {
            "success": True,
            "total_found": total_found,
            "unique_found": unique_found,
            "duplicates_removed": duplicates_removed
        }

    except FileNotFoundError:

        write_log(
            "Input file not found."
        )

        return {
            "success": False,
            "message": "Input file not found."
        }

    except Exception as e:

        write_log(
            f"Error occurred: {e}"
        )

        return {
            "success": False,
            "message": str(e)
        }