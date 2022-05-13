import matplotlib.pyplot as plt
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=[("Text files", "*.txt"), ("All Files", "*.*")]) # show an "Open" dialog box and return the path to the selected file
print(filename)

# Read syllabus file
with open(filename) as in_file:
    file_text = in_file.read()

keys_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
syll_dict = {key: 0 for key in keys_list} # Initialize dictionary keys to 0

# Count number of times each letter (not differentiating between uppercase and lowercase) and number appear
for char in file_text:
    if char.lower() in syll_dict:
        syll_dict[char.lower()] = syll_dict.get(char.lower()) + 1

# Plot values on graph
plt.bar(keys_list, list(syll_dict.values())) # plt.bar(x data, y data) displays graph as bars
plt.title("Number of Occurrences vs. Letters and Numbers in Syllabus")
plt.xlabel('Letters and Numbers')
plt.ylabel('Number of Occurrences')
plt.show()