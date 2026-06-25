import json
import shutil
from pathlib import Path

from modules.logger import write_log
from modules.report_generator import (
    generate_organization_report
)


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


def organize_files(source_folder: str) -> dict:

    source_path = Path(source_folder)

    moved_count = 0
    skipped_count = 0
    total_size = 0

    category_stats = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0,
        "Archives": 0,
        "Others": 0
    }

    try:

        ignore_folders = set(category_stats.keys())
        history = []

        for item in source_path.rglob("*"):

            if item.is_file():

                # Skip files already inside category folders
                if len(item.parts) > len(source_path.parts):

                    parent_folder = item.parent.name

                    if parent_folder in ignore_folders:
                        continue

                category = "Others"

                for folder_name, extensions in FILE_TYPES.items():

                    if item.suffix.lower() in extensions:

                        category = folder_name
                        break

                destination_folder = source_path / category

                destination_folder.mkdir(
                    parents=True,
                    exist_ok=True
                )

                destination_file = (
                    destination_folder / item.name
                )

                if destination_file.exists():

                    skipped_count += 1

                    write_log(
                        f"Skipped duplicate file: {item.name}"
                    )

                    continue

                file_size = item.stat().st_size

                shutil.move(
                    str(item),
                    str(destination_file)
                )

                # Add to history
                history.append({
                    "original_path": str(destination_file),
                    "current_path": str(item)
                })

                moved_count += 1

                total_size += file_size

                category_stats[category] += 1

        write_log(
            f"{moved_count} files organized successfully."
        )
        generate_organization_report(
         moved_count,
         skipped_count,
         total_size,
         category_stats
       )  
        with open(
            "output/history.json",
            "w",
            encoding="utf-8"
       ) as file:

           json.dump(
            history,
            file,
            indent=4
       )
        return {
            "success": True,
            "moved_files": moved_count,
            "skipped_files": skipped_count,
            "total_size_bytes": total_size,
            "category_stats": category_stats
        }

    except Exception as e:

        write_log(
            f"File organization error: {e}"
        )

        return {
            "success": False,
            "message": str(e)
        }