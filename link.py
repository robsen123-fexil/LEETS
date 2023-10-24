class node:
    def __init__(self, data):
        self.data=data
        self.ref= None
class solution:
    def __init__(self,data):
        self.head= None
     
    def print_lk(self,list1,list2):
        combined_list=solution()
        i=list1.head
        j=list2.head
        while  i and j is not None:
            combined_list.append(i+j)
            i=i.next
            j=j.next
        return combined_list    


    


