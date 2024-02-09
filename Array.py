class integer_array:

    def __init__(self):
        self.array=[0]* 5

    def input_array(self):
        print("enter 5 elements")
        for i in range(5):
            
            self.array[i]=int(input())

    def display(self):
        
        print(self.array)

    def reverse_array(self):
        self.array.reverse()
        print(self.array)
    
    def occurence(self,num):
        count=0
        for i in range(5):
            if self.array[i]==num:
                count=count+1
        return count
    
    def remove_element(self,num_remove):
        self.array.remove(num_remove)
        print(f"the updated array: {self.array}")

obj=integer_array()
obj.input_array()
obj.display()
obj.reverse_array()

num=int(input(f"enter the number to finds in occurence:"))
print(obj.occurence(num))

num_remove=int(input(f"enter the elemnet to be removed:"))
obj.remove_element(num_remove)