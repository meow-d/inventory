import os


def extract_functions(file_path):
    # Read the content of the Python file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the content into lines
    lines = content.split("\n")

    functions = []
    current_function = []
    inside_function = False

    # Iterate over each line in the file
    for line in lines:
        # Check if the line starts with 'def ' to identify function definition
        if line.startswith("def "):
            # If already inside a function, save the previous one
            if inside_function:
                functions.append("\n".join(current_function))
                current_function = []

            inside_function = True

        if inside_function:
            current_function.append(line)

    # Save the last function encountered
    if current_function:
        functions.append("\n".join(current_function))

    return functions


# Provide the path to the Python file you want to separate into functions
output_file_path = "flowchart/main2.py"

# Extract functions from the file
function_list = extract_functions(output_file_path)

# Create a directory to store the individual function files
python_output_directory = "flowchart/functions/"
os.makedirs(python_output_directory, exist_ok=True)

# Save each function into separate files
for index, function in enumerate(function_list):
    function_name = f"function_{index}.py"
    function_file_path = os.path.join(python_output_directory, function_name)
    with open(function_file_path, "w") as function_file:
        function_file.write(function)


flowchart_output_directory = "flowchart/flowchart/"
svg_output_directory = "flowchart/flowchart_svg/"

# convert py to flowchart
os.makedirs(flowchart_output_directory, exist_ok=True)
for filename in os.listdir(python_output_directory):
    input_file_path = os.path.join(python_output_directory, filename)
    output_file_path = os.path.join(flowchart_output_directory, filename)
    os.system(f"python3 -m pyflowchart {input_file_path} > {output_file_path}.txt")

# convert flowchart to svg
