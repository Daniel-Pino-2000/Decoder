"""
This function reads an encoded message from a .txt file and returns its decoded version as a string. The argument of the
function is the path of the .txx file. After processing all the lines of the file separating the information in different 
variables it calls the "create_staircase" function to be able to access the last integer of each list of the staircase. Then
it creates and returns a string with each word using a dictionary.
"""

def decode(file_path):
    
    organized_pair = {}
    numbers = []
    staircase_list = []
    key_numbers = []
    decoded_message = ''
    
    def create_staircase(nums):
        '''
        Attempts to form the input array into a staircase. Each iteration of the while loop fills one step 
        of the staircase by appending the current step to the subsets list. If the nums list has less elements 
        than the necessary step amount for a given iteration, then the array isn't a staircase and the function
        returns False, otherwise it returns the staircase.
        '''
        step = 1
        subsets = []
        while len(nums) != 0:
            
            if len(nums) >= step:
                subsets.append(nums[0:step])
                nums = nums[step:]
                step += 1
                
            else:
                return False
            
        return subsets
    
    
    with open(file_path ,'r') as file: # Opens and reads through each line of the .txt file processing the information.
        for line in file:
            line = line.strip()
            line = line.split()
            organized_pair[int(line[0])] = line[1]
            numbers.append(line[0])
            
            
    numbers = list(map(int, numbers)) # Converts to "int" all the numbers in the string.
    numbers = sorted(numbers)
    staircase_list = create_staircase(numbers) 
    
    for inner_list in staircase_list: # Adds all the final values of the staircase list to use them as keys of the dictionary to acces the correct words. 
        key_numbers.append(inner_list[-1])
        
    for key in key_numbers: # Creates the string using the words paired to the correct integers of the staircase.
        decoded_message += organized_pair[key]
        
        if key != key_numbers[-1]: # Adds a space after each word except the last one.
            decoded_message += ' '
    
    return decoded_message


path = 'D:\Interview\coding_qual_input.txt'
print(decode(path))


    