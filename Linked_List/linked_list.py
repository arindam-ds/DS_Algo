class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linked_List:
    def __init__(self, head=None):
        self.head = head
    
    def insert_at_end(self, node):
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = node
            
    def insert_at_start(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def print_linked_list(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end='')
            if tmp.next:
                tmp = tmp.next
                print(' -> ', end='')
            else:
                break
        print('\n')
        
    def get_length(self):
        length = 0
        tmp = self.head
        while tmp:
            length+=1
            if tmp.next:
                tmp = tmp.next
            else:
                break
        return length
    
    def reverse_linked_list(self):
        prev_ptr = None
        curr_ptr = self.head
        next_ptr = None
        while curr_ptr:
            next_ptr = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
        self.head = prev_ptr    

ll = Linked_List()
ll.insert_at_end(Node(12))
ll.insert_at_end(Node(5))
ll.insert_at_end(Node(20))
ll.insert_at_end(Node(10))
ll.insert_at_end(Node(25))
ll.insert_at_start(Node(50))
ll.print_linked_list()
ll.reverse_linked_list()
ll.print_linked_list()