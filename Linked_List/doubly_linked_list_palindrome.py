'''
You are given a doubly linked list. 
Determine if it is a palindrome.

'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def is_palindrome(node):
    head = node
    while True:
        if node == None:
            break
        tail = node
        node = node.next
        
    while head != tail or head != None:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.prev
    return True
        

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('c')
node.next.next.prev = node.next
node.next.next.next = Node('b')
node.next.next.next.prev = node.next.next
node.next.next.next.next = Node('a')
node.next.next.next.next.prev = node.next.next.next

print(is_palindrome(node))