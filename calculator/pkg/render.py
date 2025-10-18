import json


def format_json_output(expression: str, result: float | int, indent: int = 2) -> str:
    """
    Formats the given expression and its result into a JSON string.

    If the result is a float and represents a whole number (e.g., 5.0),
    it is converted to an integer for cleaner JSON output.

    Args:
        expression (str): The mathematical expression string.
        result (float | int): The numerical result of the expression.
        indent (int): The indentation level for the JSON output, defaults to 2.

    Returns:
        str: A JSON string containing the expression and its result.
    """
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)
