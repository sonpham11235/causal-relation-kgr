import subprocess

def run(input_file_path: str, output_file_path: str):
    result = subprocess.run(
        ["./search", input_file_path, 2, -1, output_file_path],
        capture_output=True,
        text=True
    )

    if (result.stderr):
        print("Error:", result.stderr)
    else:
        print("Search completed successfully. ", result.stdout.strip())