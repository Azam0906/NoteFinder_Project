import tkinter as tk
from tkinter import filedialog, messagebox
import re


class NoteFinder:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Finder")
        self.root.iconbitmap("NoteFinder.ico") 
        self.root.geometry("500x400")
        
        self.file_paths = []
        self.search_word = ""
        
        # Listbox to Show Selected Files
        self.file_listbox = tk.Listbox(root, width=70, height=5)
        self.file_listbox.pack(pady=5)
        
        # Frame for Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
         
        # File Selection Button
        self.file_button = tk.Button(button_frame, text="Add File(s)", command=self.add_file)
        self.file_button.pack(side=tk.LEFT, padx=5)
        
        # Clear File List Button
        self.clear_button = tk.Button(button_frame, text="Clear Files", command=self.clear_files)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Entry for Search Word
        self.word_entry = tk.Entry(root, width=40)
        self.word_entry.pack(pady=10)
        self.word_entry.insert(0, "Enter search word")
         
        # Search Button
        self.search_button = tk.Button(root, text="Search", command=self.search_word_in_files)
        self.search_button.pack(pady=10)
        
        # Textbox to Display Results
        self.result_text = tk.Text(root, height=10, width=60)
        self.result_text.pack(pady=10)

    def add_file(self):
        files = filedialog.askopenfilenames(filetypes = [("Text Files","*.txt")])
        for file in files:
            # if not file.endswith(".txt"):
            #     messagebox.showwarning("Invalid File", "Only .txt files are allowed!")
            #     continue
            if file not in self.file_paths:
                self.file_paths.append(file)
                self.file_listbox.insert(tk.END, file)
    
    def clear_files(self):
        self.file_listbox.delete(0, tk.END)
        self.file_paths = []
    
    def search_word_in_files(self):
        self.result_text.delete(1.0, tk.END)
        self.search_word = self.word_entry.get().strip()
        
        if not self.file_paths or not self.search_word:
            messagebox.showerror("Error", "Please select files and enter a search word.")
            return
        
        word_found = False
        for file_path in self.file_paths:
            try:
                with open(file_path, mode='r', encoding='utf-8', errors='ignore') as file:
                    lines = file.readlines()
                    for line_no, line in enumerate(lines, start=1):
                        if re.search(self.search_word, line, re.IGNORECASE):
                            word_found = True
                            self.result_text.insert(tk.END, f"'{self.search_word}' found in '{file_path}' on line {line_no}.\n")
            except FileNotFoundError:
                self.result_text.insert(tk.END, f"File not found: {file_path}\n")
        
        if not word_found:
            self.result_text.insert(tk.END, f"'{self.search_word}' not found in any file.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = NoteFinder(root)
    root.mainloop()