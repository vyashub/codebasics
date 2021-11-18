class Node:
    def __init__(self, data=None,next_addr=None):
        self.data = data
        self.next_addr = next_addr
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node  
        else:
            itr = self.head
            while itr.next_addr is not None:
                itr = itr.next_addr
                  
            itr.next_addr = Node(data)
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            print(itr.data,itr.next_addr)
            itr = itr.next_addr
        print(llstr)
            
            
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(11)
    ll.insert_at_begin(199)
    ll.insert_at_end(888)
    ll.print()