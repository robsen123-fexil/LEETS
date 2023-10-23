class node:
    def __init__(self, data):
        self.data=data
        self.ref= None
class solution:
    def __init__(self):
        self.head= None
    def appendd(self, list1,list2):
        new_node= Node(data)
        if not self.head is not None:
            self.head=new_  node  
    def print_lk(self,list1,list2):
        combined_list=node()
        i=list1.head
        j=list2.head
        while not i and j is not None:
            combined_list.append(i+j)
            i=i.next
            j=j.next
        return combined_list    
obj=solution()
result=obj.print_lk()
print(result)    

    


