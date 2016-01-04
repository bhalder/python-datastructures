# Author : Barun Halder
# Date : January, 2016

# Simple BST in Python

class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

    def add(self, value):
        new_node = Node(value)
        if value < self.item :
            if self.left :
                self.left.add(value)
            else :
                self.left = new_node
        else:
            if self.right :
                self.right.add(value)
            else :
                self.right = new_node
        return self

    def search( self, value ) :
        if self.item == value :
            print "FOUND"
            return True
        else :
            if self.left and value < self.item :
                self.left.search( value )
            elif self.right and value > self.item :
                self.right.search( value )
            else:
                return False

    def is_leaf( self ):
        if not self.left and not self.right :
            return True
        else :
            return False
                    
    def print_preorder( self ) :
        print self.item

        if self.left:
            self.left.print_preorder()

        if self.right:
            self.right.print_preorder()

    def array_preorder( self ) :
        nodes = []
        if self.item :
            nodes.append( self.item ) # adds only one value

        if self.left:
            nodes.extend( self.left.array_preorder() ) # adds value from iterable

        if self.right:
            nodes.extend( self.right.array_preorder() ) # adds value from iterable
        return nodes

class BST(object) :
    def __init__(self):
        self.root = None

    def _add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add(value)
    
    def _search(self, value):
        if self.root:
            self.root.search( value )

    def _print_preorder(self):
        if self.root:
            self.root.print_preorder()

    def _array_preorder( self ):
        if self.root:
            return self.root.array_preorder();

if __name__ == "__main__":
    bst = BST()

    for i in range(10,20):
        bst._add(i)

    print
    bst._search(19)
    
    bst._print_preorder()
