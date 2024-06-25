import re

loc_list = []

print("Enter file paths (type 'done' when finished):")

while True:
    path = input()
    if path.lower() == 'done':
        break
    loc_list.append(path)

word = input('enter word: ')
for j in loc_list:
    match_chk = 0
    with open (j, mode = 'r') as efile:
        efi = efile.read().split('\n')
    ##    print(efi)
        for i in efi:      
            
            match = re.findall(word, i)
            if match != []:
                x = j.split(".")
                match_chk+=1
                
                print(f'{word} is in line {efi.index(i)+1} and it is present in file {x[0]}')
else:
    if match_chk == 0:
        print(f"{word} is not present in any file")