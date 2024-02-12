class TupleOperations:

    def __init__(self):
        self.my_tuple=(1,2,6,8,9,6)
        print(self.my_tuple)

    def create_mixed_tuple(self):
        self.mixed_tuple=(1,2,"hello",9,45)
        print(self.mixed_tuple)
    
    def unpack_tuple(self):
        self.unpacked_tuple=(1,2,3)
        a,b,c=self.unpacked_tuple
        print("a=",a)
        print("b=",b)
        print("c=",c)

    def create_colon_tuple(self):
        self.colon_tuple=(self.my_tuple)*3
        print(self.colon_tuple)
    
    def find_repeat_items(self):
        repeated_items=[]
        unique_items=set()
        
        for item in self.my_tuple:
            if item in unique_items:
                repeated_items.append(item)
            else:
                unique_items.add(item)
        
        print(repeated_items)
            

    def check_existence(self,num):
        if num in self.my_tuple:
            print(f"{num} is present in tuple")
        else:
            print("not present")

    def convert_list_to_tuple(self):
        self.mylist=[1,3,5,5,67,89]
        self.my_tuple=tuple(self.mylist)
        print(self.my_tuple)

    def remove_item(self,item):
        ttl=list(self.my_tuple)
       
        ttl.remove(item)
        self.my_tuple=tuple(ttl)
        print(self.my_tuple)

    def sliced_tuple(self):
         print(self.my_tuple[1:3])

    def reversed_tuple(self):
        reversed_tuple = tuple(reversed(self.my_tuple))

        print(reversed_tuple)

obj=TupleOperations()

obj.create_mixed_tuple()
obj.unpack_tuple()
obj.create_colon_tuple()
obj.find_repeat_items()
obj.check_existence(6)
obj.convert_list_to_tuple()
obj.remove_item(67)
obj.sliced_tuple()
obj.reversed_tuple()



        