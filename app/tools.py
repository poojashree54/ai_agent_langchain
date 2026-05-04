from langchain.tools import tool
import re

@tool
def calculator(expression: str) -> str:
    """
    Use this for math calculations like 2+2 or (5*10).
    Only valid math expressions.
    """
    try:
        # Clean the input (VERY IMPORTANT)
        cleaned = re.sub(r"[^0-9+\-*/().]", "", expression)

        if cleaned == "":
            return "Invalid expression"

        result = eval(cleaned)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"