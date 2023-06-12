import os.path
import re

"""
INSTRUCTIONS
1. Create a file with the following code
2. Put the file you want to convert into the same folder as it, and rename it to "py_file.py"
3. Add a "#F" comment to any lines in the code which have a function call that doesn't assign anything (so no =),
as the program cannot handle these convincingly
4. Run the converter file
"""

python_file = "./main.py"

basic_conversion_rules = {
    "for": "FOR",
    "if": "IF",
    "while": "WHILE",
    "until": "UNTIL",
    "import": "IMPORT",
    "class": "CLASS",
    "def": "FUNCTION",
    "else:": "ELSE:",
    "elif": "ELIF",
    "except:": "EXCEPT:",
    "try:": "TRY:",
    "pass": "PASS",
    "in": "IN",
}
prefix_conversion_rules = {}
advanced_conversion_rules = {"print": "PRINT", "return": "RETURN", "input": "INPUT"}


def l2pseudo(to_pseudo):
    for line in to_pseudo:
        line_index = to_pseudo.index(line)
        line = str(line)
        line = re.split(r"(\s+)", line)
        for key, value in basic_conversion_rules.items():
            for word in line:
                if key == str(word):
                    line[line.index(word)] = value
        for key, value in advanced_conversion_rules.items():
            for word in line:
                line[line.index(word)] = word.replace(key, value)
        to_pseudo[line_index] = "".join(line)
    return to_pseudo


def p2file(to_file):
    py_file = os.path.splitext(os.path.basename(python_file))[0]
    with open(py_file + "_pseudocode.txt", "w") as writer:
        writer.write("".join(to_file))


def main():
    with open(python_file, "r+") as py_file_reader:
        file_lines = py_file_reader.readlines()
        work_file = l2pseudo(file_lines)
        p2file(work_file)


if __name__ == "__main__":
    main()
