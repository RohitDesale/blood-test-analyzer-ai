## Importing libraries and environment variables
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PDFLoader

# ========================= #
#       Search Tool         #
# ========================= #

# Optional: Useful if agents use web search
search_tool = SerperDevTool()


# ========================= #
#   Blood Report Reader     #
# ========================= #

class BloodTestReportTool:
    """
    A custom CrewAI tool to read blood test PDFs and return cleaned text.
    """

    def __init__(self, path='data/sample.pdf'):
        self.path = path

    def _run(self, **kwargs) -> str:
        path = kwargs.get("path", self.path)

        if not os.path.exists(path):
            return f"[ERROR] File not found: {path}"

        try:
            docs = PDFLoader(file_path=path).load()
            full_report = ""

            for data in docs:
                content = data.page_content.strip()
                content = content.replace("\n\n", "\n").replace("  ", " ")
                full_report += content + "\n"

            return full_report.strip()

        except Exception as e:
            return f"[ERROR] Failed to load PDF: {str(e)}"


# ========================= #
#     Nutrition Tool        #
# ========================= #

class NutritionTool:
    """
    Placeholder for analyzing nutrition from blood report data.
    """

    def _run(self, **kwargs) -> str:
        blood_report_data = kwargs.get("blood_report_data", "")
        cleaned = " ".join(blood_report_data.split())

        return (
            "[Nutrition Analysis]\n"
            f"Processed snippet: {cleaned[:200]}...\n"
            "Nutrition recommendations feature coming soon."
        )


# ========================= #
#     Exercise Tool         #
# ========================= #

class ExerciseTool:
    """
    Placeholder for generating workout plans based on blood report.
    """

    def _run(self, **kwargs) -> str:
        blood_report_data = kwargs.get("blood_report_data", "")
        cleaned = " ".join(blood_report_data.split())

        return (
            "[Exercise Plan]\n"
            f"Processed snippet: {cleaned[:200]}...\n"
            "Workout generation logic to be implemented."
        )
