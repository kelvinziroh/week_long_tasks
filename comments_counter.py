import re
import sys

# Define regular expression patterns for comments
COMMENT_PATTERNS = {
    "LINE_COMMENT": r"//.*",
    "BLOCK_COMMENT": r"/\(.|\n)?\*/",
}


# Function to count comments in the input code
def count_comments(code):
    count = 0
    for comment_type, pattern in COMMENT_PATTERNS.items():
        count += len(re.findall(pattern, code))
    return count


if len(sys.argv) != 2:
    print("Usage: python count_comments.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    # Read the code from the file
    with open(file_path, "r") as file:
        code = file.read()

    # Count the comments in the code
    comment_count = count_comments(code)

    print(f"Total number of comments in the file: {comment_count}")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
