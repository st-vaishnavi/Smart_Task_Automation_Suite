from datetime import datetime


def write_log(message: str) -> None:
    """
    Write messages to logs.txt with timestamp.
    """

    with open("output/logs.txt", "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(
            f"[{current_time}] {message}\n"
        )