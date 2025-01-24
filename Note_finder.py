import re  #when, how, why

class WordSearcher:
    def __init__(self):
        self.file_paths = []
        self.search_word = ""

    def add_file_path(self, path):
        if path in self.file_paths:
            print(f"File path '{path}' is already added.")
        else:
            self.file_paths.append(path)

    def set_search_word(self, word):
        self.search_word = word

    def search_word_in_files(self):
        if not self.file_paths or not self.search_word:
            print("No files or search word provided.")
            return
        
        word_found = False
        
        for file_path in self.file_paths:
            try:
                with open(file_path, mode='r') as file:
                    lines = file.readlines()
                    for line_no, line in enumerate(lines, start=1):
                        if re.search(self.search_word, line):
                            word_found = True
                            print(f"'{self.search_word}' found in file '{file_path}' on line {line_no}.")
            except FileNotFoundError:
                print(f" Sorry, File not found: {file_path}")
        
        if not word_found:
            print(f"'{self.search_word}' not found in any file.")

# -----------Main program-----------------
def main():
    searcher = WordSearcher()
    
    print("Enter file paths (type 'done' when finished):")
    while True:
        path = input()
        if path.lower() == 'done':
            break
        if not path.strip():
            print("Invalid input, Please enter a valid file path.")
            continue
        searcher.add_file_path(path)
    
    word = input("Enter the word to search: ").strip()
    if not word:
        print("Invalid input, Please enter a non-empty search word.")
        return
    
    searcher.set_search_word(word)
    searcher.search_word_in_files()

if __name__ == "__main__":
    main()
