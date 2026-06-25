from datetime import datetime


def generate_report(
        total_found: int,
        unique_found: int
) -> None:

    duplicates_removed = (
        total_found -
        unique_found
    )

    with open(
            "output/report.txt",
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            f"Total Emails Found      : {total_found}\n"
        )

        file.write(
            f"Unique Emails Found     : {unique_found}\n"
        )

        file.write(
            f"Duplicate Emails Removed: {duplicates_removed}\n"
        )


def generate_organization_report(
        moved_files: int,
        skipped_files: int,
        total_size: int,
        category_stats: dict
) -> None:

    with open(
            "output/organization_report.txt",
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            "SMART FILE ORGANIZER REPORT\n"
        )

        file.write(
            "=" * 35 + "\n\n"
        )

        file.write(
            f"Generated On : {datetime.now()}\n\n"
        )

        file.write(
            f"Files Moved : {moved_files}\n"
        )

        file.write(
            f"Files Skipped : {skipped_files}\n"
        )

        file.write(
            f"Total Size Processed : "
            f"{total_size} bytes\n\n"
        )

        file.write(
            "CATEGORY STATISTICS\n"
        )

        file.write(
            "-" * 25 + "\n"
        )

        for category, count in category_stats.items():

            file.write(
                f"{category}: {count}\n"
            )