def sort_by_size(item):
	return item[1]

def count_letters(txt_path):
	with open(txt_path) as f:
		file_contents = f.read()
		words = file_contents.split()
		letters = {}
		
		for word in words:
			for letter in word.lower():
				
				if letter in letters:
					letters[letter] += 1
				else:
					letters[letter] = 1
				
				
		print(f"--- Begin report of {txt_path} ---")
		print(f"{len(words)} words found in the document\n")
			
					
		for letter in sorted(letters.items(), key=lambda x: x[1], reverse=True): 
			if letter[0].isalpha():
				print(f"The '{letter[0]}' character was found {letter[1]} times")
		print(f"--- End report ---")		
		
count_letters("books/frankenstein.txt")
