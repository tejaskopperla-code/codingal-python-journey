class stringReverse:

    def __init__(self,text : str):
        self.text = text 


    def reverse_words(self):
        words = self.text.split()
        reversed_list = words[::-1]
        return "".join(reversed_list)
    
processer =stringReverse(" CODDINGAL IS THE BEST ")
result = processer.reverse_words()

print(" Orignal word : CONDINGAL IS THE BEST")
print("Reversed Version : ", result)