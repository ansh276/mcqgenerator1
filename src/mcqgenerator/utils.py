import os
import json
import traceback
from PyPDF2 import PdfReader


def read_file(file):
    try:
        # ---------- PDF ----------
        if file.name.endswith(".pdf"):
            reader = PdfReader(file)
            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            return text.strip()

        # ---------- TXT ----------
        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8")

        # ---------- Unsupported ----------
        else:
            raise Exception("Unsupported file format. Only PDF and TXT are supported.")

    except Exception as e:
        print("PDF/Text read error:", e)
        raise Exception("error reading the PDF file")


def get_table_data(quiz_str):
    try:
        # convert quiz string → dictionary
        quiz_dict = json.loads(quiz_str)

        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]

            options = " || ".join(
                f"{option} -> {option_value}"
                for option, option_value in value["options"].items()
            )

            correct = value["correct"]

            quiz_table_data.append(
                {
                    "MCQ": mcq,
                    "Choices": options,
                    "Correct": correct
                }
            )

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
