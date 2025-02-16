
# Note Finder

The Note Finder Tool is a Python application with a GUI built using Tkinter. It allows users to search for occurrences of a specified word within one or more text files. Users can interactively select files, enter a search word, and view results in an easy-to-use interface.



## Features
- **Graphical File Selection**: Browse and select multiple text files using a file dialog.
- **File Management**: View selected files in a listbox and clear the list as needed.
- **Regex Support**: Utilize regular expressions for advanced pattern matching (case-insensitive by default).
- **Results Display**: View matches with file names, line numbers, and context within an integrated text box.
- **Error Handling**: Clear error messages for missing files or invalid inputs via dialog boxes.
- **Cross-Platform**: Works on Windows, macOS, and Linux (with proper Tkinter support).


## Requirements
*  Python 3.x
* 're' module(standard library)
* Tkinker

## Setup
* Clone the repository : ```git clone https://github.com/Azam0906/NoteFinder_Project.git```

* Navigate to the directory(Project)

## Execution
### Input
* Launch the Application : python Note_finder.py
  (The GUI window will open.)

* Enter the word you want to search.
### Using the Application
 Click **Add File(s)** to select text files for searching.
- Enter the word or phrase to search in the entry field.
* Click **Search** to begin the search.
* The results will be displayed in the text box below.
* Use **Clear Files** to remove all selected files and start fresh.

### Output
* The application displays matches in the format:
  'searched_word' found in 'filename.txt' on line X.

* If no matches are found:
  'searched_word' not found in any file.

* If a file cannot be opened:
  File not found: filename.txt