# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word
        

    def match(self, entered_list):
        
        self.entered_list = entered_list
        a_list = []
        self.word_string_to_list = [letter for letter in self.word]
        
        for item in entered_list:
            item_string_to_list = [letter for letter in item]
            
            if sorted(self.word_string_to_list) == sorted(item_string_to_list) : 
             
                a_list.append(item)
        return a_list


# import ipdb

# class Anagram:

#     def __init__(self,word):
#         self.word = word
        

#     def match(self, entered_list):
#         print("hi there how are you", entered_list)
#         print("I'm the second parenth", self.word)
#         self.entered_list = entered_list
#         a_list = []
#         self.word = [letter for letter in self.word]
#         print(self.word)
#         for item in entered_list:
#             item = [letter for letter in item]
#             print(item)
#             if sorted(self.word) == sorted(item): 
#                 item_recombined = ""
#                 item_recombined = item_recombined.join(item) # join is is nondestructive so hast to be set equal to something.
#                 # ipdb.set_trace()
#                 a_list.append(item_recombined)
#         return a_list
            

# first = Anagram(work)    
# Step 1: We want to turn a work into a list
# Step 2: Sort that new list
# Step 3: Iterate through through the entered list
# - Do something for each list
# Step 4: Create an if statement to see if they are equal
# Step 5: if equal - return the ___ in the __
# Return the item in the entered list                          