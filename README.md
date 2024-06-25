
# Note Finder

The Note Finder Tool is a Python script designed to search for occurrences of a specified word within one or more text files. Users can input file paths interactively, allowing flexibility in selecting files for analysis. The script utilizes Python's re module for efficient regular expression-based searching, enabling users to find exact matches or patterns within the text file/files.




## Features
File Selection: Users can input multiple file paths or directories to search through, providing flexibility in analyzing various text sources.

Interactive Input: The tool prompts users to enter file paths until they indicate they have finished ('done'), making it easy to customize the scope of the search.

Regex-based Search: Supports advanced searching using regular expressions, allowing for complex pattern matching beyond simple word searches.

Detailed Output: When a match is found, the tool displays the specific line number and file name where each occurrence of the word is located, aiding in precise analysis.

Error Handling: Basic error handling ensures smooth execution, notifying users if a specified file cannot be found.
## Usage
*  Python 3.x
* 're' module(standard library)

## Setup
* Clone the repository : git clone https://github.com/your-username/your-repository.git

* Navigate to the directory : cd your-repository

## Execution
### Input
* Execute the script in your terminal.
* Enter the word you want to search.

### Output
* The script will display the line number and file name where the word was found.
* If the word is not found in the file, it will indicate that.