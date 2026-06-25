import csv
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from modules.logger import write_log


def scrape_title(url: str) -> dict:

    try:

        start_time = time.time()

        response = requests.get(
            url,
            timeout=10
        )

        response_time = round(
            time.time() - start_time,
            3
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string.strip()

        status_code = response.status_code

        timestamp = datetime.now()

        with open(
                "output/web_titles.txt",
                "a",
                encoding="utf-8"
        ) as file:

            file.write(
                f"URL: {url}\n"
            )

            file.write(
                f"Title: {title}\n"
            )

            file.write(
                f"Status Code: {status_code}\n"
            )

            file.write(
                f"Response Time: {response_time} sec\n"
            )

            file.write(
                f"Timestamp: {timestamp}\n\n"
            )

        with open(
                "output/web_titles.csv",
                "a",
                newline="",
                encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(
                csv_file
            )

            writer.writerow(
                [
                    url,
                    title,
                    status_code,
                    response_time,
                    timestamp
                ]
            )

        write_log(
            f"Title extracted from {url}"
        )

        return {
            "success": True,
            "title": title,
            "status_code": status_code,
            "response_time": response_time
        }

    except Exception as e:

        write_log(
            f"Web scraping error: {e}"
        )

        return {
            "success": False,
            "message": str(e)
        }