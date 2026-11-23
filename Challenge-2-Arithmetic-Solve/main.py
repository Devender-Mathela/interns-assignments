
import re

def calculate(exp):
    exp = exp.replace("^", "**").replace("–", "-").replace("−", "-")
    exp = exp.replace("[", "(").replace("]", ")")
    exp = exp.replace("{", "(").replace("}", ")")

    exp = re.sub(r'(\))\s*(\()', r'\1*\2', exp)
    exp = re.sub(r'(\d)\s*(\()', r'\1*\2', exp)
    exp = re.sub(r'(\))\s*(\d)', r'\1*\2', exp)

    return eval(exp, {"__builtins__": {}}, {})


with open("input.txt", "r") as file:
    lines = file.readlines()

results = []

for line in lines:
    exp = line.strip().split("=")[0].strip()

    if not exp:
        continue

    try:
        answer = calculate(exp)
        results.append(f"{exp} = {answer}")
    except Exception:
        results.append(f"{line.strip()} = Invalid Expression")

with open("output.txt", "w") as file:
    file.write("\n".join(results))

print("Calculation completed!")
print("Check output.txt")
