from langchain.tools import tool
import re

@tool
def calculator(expression: str) -> str:
    """
    Use ONLY for math expressions like:
    2+2, 5*10, (10+5)*2
    """

    try:
        cleaned = re.sub(r"[^0-9+\-*/().]", "", expression)

        if cleaned == "":
            return "Invalid expression"

        result = eval(cleaned)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"