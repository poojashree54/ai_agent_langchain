from langchain.tools import tool
import re

@tool
def calculator(expression: str) -> str:
    """
    Use ONLY for math expressions like:
    2+2, 5*10, (10+5)*2

    DO NOT use words.
    Input must be a pure mathematical expression.
    """
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=3,
        early_stopping_method="generate",
        handle_parsing_errors=True
    )
    except Exception as e:
        return f"Calculation error: {str(e)}"