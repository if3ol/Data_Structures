# linked list class for storing keys at array index and for chaining collision
# initiliaze key, val so Node() can be called in HashMap class.
class Node:
    def __init__(self, key = None, val = None, next = None):
        self.val = val
        self.key = key
        self.next = next

class HashMap:
    def __init__(self, length=100):
        self.map = [Node() for _ in range(length)]
        self.length = length

    # function to insert inside the hash map
    def put(self, key, val):
        index = hash(key) % self.length #hash the key
        curr = self.map[index] # get the index 

        # traverse array while curr.next is not None
        while curr.next:
            if curr.next.key == key: # if inserted key already exists, update it and return
                curr.next.val = val
                return
            curr = curr.next # move to next node for traversal continuation
        curr.next = Node(key,val) # if key not found (new key), create new node and insert
        

    def get(self, key):
        index = hash(key) % self.length #hash the key
        curr = self.map[index] # get the index 
        # traverse the list and check if we can get the key, then return the corresponding value if key found
        # if not found return None
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return None

    def delete(self,key):
        index = hash(key) % self.length #hash the key
        curr = self.map[index] # get index
        #traverse and delete the node with the key
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False



dict1 = HashMap()
dict1.put("Name", "Alice")
dict1.put(10, 2)
dict1.put((2,3,1), "hello")

print(dict1.get("Name"))
print(dict1.get(10))
print(dict1.get((2,3,1)))

dict1.delete("Name")
print(dict1.get("Name"))
print(dict1.get(10))
print(dict1.get((2,3,1)))
        
