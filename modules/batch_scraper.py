from datetime import datetime
from urllib.parse import urlparse

from modules.web_scraper import scrape_title


def batch_scrape(
        input_file: str
) -> dict:

    try:

        with open(
                input_file,
                "r",
                encoding="utf-8"
        ) as file:

            urls = [
                line.strip()
                for line in file
                if line.strip()
            ]

        total_urls = len(urls)

        successful = 0

        failed = 0

        total_response_time = 0

        fastest_domain = ""

        slowest_domain = ""

        fastest_time = float("inf")

        slowest_time = 0

        for url in urls:

            if not (
                    url.startswith("http://")
                    or
                    url.startswith("https://")
            ):

                failed += 1

                continue

            result = scrape_title(
                url
            )

            if result["success"]:

                successful += 1

                response_time = (
                    result["response_time"]
                )

                total_response_time += (
                    response_time
                )

                domain = urlparse(
                    url
                ).netloc

                if response_time < fastest_time:

                    fastest_time = response_time

                    fastest_domain = domain

                if response_time > slowest_time:

                    slowest_time = response_time

                    slowest_domain = domain

            else:

                failed += 1

        average_response_time = 0

        if successful > 0:

            average_response_time = round(
                total_response_time /
                successful,
                3
            )

        success_rate = 0

        if total_urls > 0:

            success_rate = round(
                (
                        successful /
                        total_urls
                ) * 100,
                2
            )

        with open(
                "output/web_report.txt",
                "w",
                encoding="utf-8"
        ) as file:

            file.write(
                "WEB SCRAPER REPORT\n"
            )

            file.write(
                "=" * 35 + "\n\n"
            )

            file.write(
                f"Generated On: "
                f"{datetime.now()}\n\n"
            )

            file.write(
                f"Total URLs: {total_urls}\n"
            )

            file.write(
                f"Successful: {successful}\n"
            )

            file.write(
                f"Failed: {failed}\n"
            )

            file.write(
                f"Success Rate: "
                f"{success_rate}%\n"
            )

            file.write(
                f"Average Response Time: "
                f"{average_response_time} sec\n"
            )

            file.write(
                f"Fastest Website: "
                f"{fastest_domain}\n"
            )

            file.write(
                f"Slowest Website: "
                f"{slowest_domain}\n"
            )

        return {

            "success": True,

            "total_urls": total_urls,

            "successful": successful,

            "failed": failed,

            "success_rate": success_rate,

            "average_response_time":
                average_response_time,

            "fastest_domain":
                fastest_domain,

            "slowest_domain":
                slowest_domain
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }