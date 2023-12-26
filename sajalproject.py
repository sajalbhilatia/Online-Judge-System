import subprocess
import os

# Define the supported programming languages and their corresponding file extensions
SUPPORTED_LANGUAGES = {
    'python': 'py',
    'java': 'java',
    'cpp': 'cpp'
}

# Function to compile and run code
def run_code(code, language):
    file_extension = SUPPORTED_LANGUAGES.get(language)
    
    if not file_extension:
        return "Unsupported language"

    # Write code to a temporary file
    with open(f'temp_code.{file_extension}', 'w') as file:
        file.write(code)

    # Compile and run the code
    if language == 'python':
        result = subprocess.run(['python', f'temp_code.{file_extension}'], capture_output=True)
    elif language == 'java':
        result = subprocess.run(['javac', f'temp_code.{file_extension}'], capture_output=True)
        if result.returncode == 0:
            result = subprocess.run(['java', f'temp_code'], capture_output=True)
    elif language == 'cpp':
        result = subprocess.run(['g++', f'temp_code.{file_extension}', '-o', 'temp_code'], capture_output=True)
        if result.returncode == 0:
            result = subprocess.run(['./temp_code'], capture_output=True)
    
    # Clean up temporary files
    os.remove(f'temp_code.{file_extension}')
    if language == 'cpp' or language == 'java':
        os.remove('temp_code')

    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

# Function to evaluate code correctness
def evaluate_code(user_code, expected_output):
    return "Correct" if user_code.strip() == expected_output.strip() else "Incorrect"

# Example usage
if _name_ == "_main_":
    # User-submitted code
    user_code = """
    # Python code example
    print("Hello, World!")
    """

    # Expected output
    expected_output = "Hello, World!"

    # Programming language
    language = 'python'

    # Run and evaluate the code
    output, error = run_code(user_code, language)
    correctness = evaluate_code(output, expected_output)

    # Display results
    print(f"Output:\n{output}")
    print(f"Error:\n{error}")
    print(f"Correctness: {correctness}")