#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

class MailMerge:
    def __init__(self, letter_template, names_list) -> None:
        with open(letter_template, "r") as txt:
            self.letter_template = txt.read()
        
        with open(names_list, "r") as txt:
            self.names_list = [line.rstrip('\n') for line in txt]

    def print_letter(self):
        return self.letter_template

    def print_names(self):
        return self.names_list

    def mail_merge(self):
        if "[name]" in self.letter_template:
            for name in self.names_list:
                output = self.letter_template.replace("[name]", name) 
                with open(f"Output\ReadyToSend\letter_to_{name}", "w") as txt:
                    txt.write(output)
    
if __name__ == "__main__":
    obj = MailMerge("Input/Letters/starting_letter.txt", "Input/Names/invited_names.txt")
    print(obj.print_letter())
    print(obj.print_names())
    # obj.mail_merge()




# with open("..\..\..\..\OneDrive\Desktop\dat.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()


#C:\Users\HP\OneDrive\Desktop
# C:\Users\HP\Documents\code_projects\100DaysOfCode\day24\main.py

# #Read only
# with open("my_file.txt", mode="r") as file:
#     file.write("New text.")

# #Overwrite
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# #Append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nThis is another line.")

# # Write to new file
# with open("my_new_file.txt", mode="w") as file:
#     file.write("New file's text.")