import json
import shutil
from pathlib import Path

from modules.logger import write_log


def undo_last_operation():

    try:

        history_file = Path(
            "output/history.json"
        )

        if not history_file.exists():

            return {
                "success": False,
                "message": "No history found."
            }

        with open(
                history_file,
                "r",
                encoding="utf-8"
        ) as file:

            history = json.load(
                file
            )

        restored_count = 0

        for item in history:

            source = Path(
                item["current_path"]
            )

            destination = Path(
                item["original_path"]
            )

            if source.exists():

                destination.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                shutil.move(
                    str(source),
                    str(destination)
                )

                restored_count += 1

        write_log(
            f"{restored_count} files restored."
        )

        return {
            "success": True,
            "restored_files": restored_count
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }