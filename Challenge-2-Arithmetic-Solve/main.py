
import ast
import operator
import re


# Supported mathematical operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def evaluate(node):

    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            return node.value
        raise ValueError("Invalid number")

    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise ValueError("Unsupported operator")

        left = evaluate(node.left)
        right = evaluate(node.right)

        return OPERATORS[op_type](left, right)

    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise ValueError("Unsupported operator")

        return OPERATORS[op_type](evaluate(node.operand))

    else:
        raise ValueError("Invalid expression")


def solve_expression(expression):

    # Convert alternative minus signs to standard minus
    expression = expression.replace("–", "-").replace("−", "-")

    # Convert exponentiation into Python syntax
    expression = expression.replace("^", "**")

    # Convert square and curly brackets into parentheses
    expression = expression.replace("[", "(").replace("]", ")")
    expression = expression.replace("{", "(").replace("}", ")")

    # Remove spaces
    expression = expression.replace(" ", "")

    # Add implicit multiplication:
    # Example: (2+3)(4+5) -> (2+3)*(4+5)
    expression = re.sub(r"(\))(\()", r"\1*\2", expression)
    expression = re.sub(r"(\d)(\()", r"\1*\2", expression)
    expression = re.sub(r"(\))(\d)", r"\1*\2", expression)

    # Parse expression safely
    tree = ast.parse(expression, mode="eval")

    result = evaluate(tree.body)

    return result


def format_result(result):

    if isinstance(result, float) and result.is_integer():
        return str(int(result))

    return str(result)


def process_file(input_file, output_file):

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        output_lines = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            try:
                # Remove existing equals sign
                expression = line.split("=")[0].strip()

                answer = solve_expression(expression)

                output_lines.append(
                    f"{expression} = {format_result(answer)}"
                )

            except Exception as error:
                output_lines.append(
                    f"{line} ERROR: {error}"
                )

        # Generate output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(output_lines))

        print("Calculation completed successfully!")
        print(f"Output saved to: {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found!")


if __name__ == "__main__":

    input_file = "input.txt"
    output_file = "output.txt"

    process_file(input_file, output_file)
