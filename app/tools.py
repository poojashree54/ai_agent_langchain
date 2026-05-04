@tool
def calculator(expression: str) -> str:
    try:
        cleaned = re.sub(r"[^0-9+\-*/().]", "", expression)

        if cleaned == "":
            return "Invalid expression"

        result = eval(cleaned)

        return f"Final Answer: {result}"   # ✅ IMPORTANT

    except Exception as e:
        return f"Error: {str(e)}"