class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, items=None):
        """Initialize this doubly linked list and append the given items, if any."""
        self.head = None  # First node
        self.current = None
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this doubly linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this doubly linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())

    def __iter__(self):
        """Identifies DoublyLinkedList as an iterable type"""
        self.current = self.head
        return self
    
    def __next__(self):
        """Identifies DoublyLinkedList as an iterable type"""
        current = self.current
        if self.current is None:
            raise StopIteration
        self.current = self.current.next
        return current

    def items(self):
        """Return a list (dynamic array) of all items in this doubly linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in doubly linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this doubly linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this doubly linked list by traversing its nodes.
        Running time: O(1) since simply calling a variable"""
        # current_node = self.head
        # count = 0
        # while current_node != None:
        #     count += 1
        #     current_node = current_node.next
        # return count
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this doubly linked list.
        Running time: O(1) since does same execution every time"""
        self.size += 1
        new_node = Node(item)
        if self.head is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this doubly linked list.
        Running time: O(1) since does same execution every time"""
        self.size += 1
        new_node = Node(item)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this doubly linked list satisfying the given quality.
        Best case running time: O(1) if first item
        Worst case running time: O(n) if last item because must traverse whole list"""
        current_node = self.head
        while current_node != None:
            if quality(current_node.data):
                return current_node
        return None

    def delete(self, item):
        """Delete the given item from this doubly linked list, or raise ValueError.
        Best case running time: O(1) if list empty, if item is first node
        Worst case running time: O(n) if last item or not in list because it 
            must traverse the whole list"""
        handled = False
        if self.size == 0:
            raise ValueError('Item not found: {}'.format(item))
        if item == self.head.data:
            if self.head.next is not None:
                self.head.next.prev = None  
            self.head = self.head.next
            self.size -= 1
            handled = True
        if item == self.tail.data:   
            if self.tail.prev is not None:
                self.tail.prev.next = None     
            self.tail = self.tail.prev
            if not handled:
                self.size -= 1
                handled = True
        if handled:
            return
        current_node = self.head
        while current_node != None:
            if item == current_node.data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                self.size -= 1
                return
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, replacement):
        """Replaces the given item from this doubly linked list with replacement, or raise ValueError.
        Best case running time: O(1) if list empty, if item is first node
        Worst case running time: O(n) if last item or not in list because it 
            must traverse the whole list"""
        if item == self.head.data:
            self.head.data = replacement
            return
        current_node = self.head
        while current_node != None:
            if item == current_node.data:
                self.head.data = replacement
                return
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    dll = DoublyLinkedList()
    print('list: {}'.format(dll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        dll.append(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    for item in ['B', 'C', 'A']:
        print('delete({!r})'.format(item))
        dll.delete(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    print('\nTesting prepend:')
    for item in ['A', 'B', 'C']:
        print('prepend({!r})'.format(item))
        dll.prepend(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    print('\nTesting delete:')
    for item in ['B', 'C', 'A']:
        print('delete({!r})'.format(item))
        dll.delete(item)
        print('list: {}'.format(dll))

    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('length: {}'.format(dll.length()))

    print('\nTesting iter:')
    for item in ['A', 'B', 'C', 'D']:
        dll.append(item)
    for index, node in enumerate(dll):
        print(index, node.data)

if __name__ == '__main__':
    test_linked_list()
