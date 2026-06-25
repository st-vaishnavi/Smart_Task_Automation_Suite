import customtkinter as ctk
from tkinter import filedialog

from modules.file_organizer import organize_files
from modules.undo_manager import undo_last_operation


class OrganizerPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.folder_path = ""

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="File Organizer",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(
            pady=(20, 10)
        )

        # Select folder button
        self.select_button = ctk.CTkButton(
            self,
            text="Select Folder",
            command=self.select_folder
        )

        self.select_button.pack(
            pady=10
        )

        # Folder label
        self.folder_label = ctk.CTkLabel(
            self,
            text="No folder selected"
        )

        self.folder_label.pack()

        # Organize button
        self.organize_button = ctk.CTkButton(
            self,
            text="Organize Files",
            command=self.organize
        )

        self.organize_button.pack(
            pady=10
        )

        # Undo button
        self.undo_button = ctk.CTkButton(
            self,
            text="Undo Last Operation",
            command=self.undo_operation
        )

        self.undo_button.pack(
            pady=10
        )

        # Result label
        self.result_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.result_label.pack(
            pady=10
        )

        # Scrollable textbox
        self.result_box = ctk.CTkTextbox(
            self,
            width=700,
            height=300
        )

        self.result_box.pack(
            pady=20
        )

    def select_folder(self):

        self.folder_path = filedialog.askdirectory()

        self.folder_label.configure(
            text=self.folder_path
        )

    def organize(self):

        if not self.folder_path:

            self.result_label.configure(
                text="Please select a folder.",
                text_color="red"
            )

            return

        result = organize_files(
            self.folder_path
        )

        if result["success"]:

            self.result_label.configure(
                text="File organization completed successfully.",
                text_color="green"
            )

            self.result_box.delete(
                "1.0",
                "end"
            )

            text = ""

            text += (
                f"Files Moved: "
                f"{result['moved_files']}\n"
            )

            text += (
                f"Files Skipped: "
                f"{result['skipped_files']}\n"
            )

            text += (
                f"Total Size: "
                f"{result['total_size_bytes']} bytes\n\n"
            )

            text += "Category Statistics\n"
            text += "-" * 25 + "\n"

            for category, count in result[
                "category_stats"
            ].items():

                text += (
                    f"{category}: {count}\n"
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

    def undo_operation(self):

        result = undo_last_operation()

        if result["success"]:

            self.result_label.configure(
                text=
                f"{result['restored_files']} files restored successfully.",
                text_color="green"
            )

        else:

            self.result_label.configure(
                text=result["message"],
                text_color="red"
            )