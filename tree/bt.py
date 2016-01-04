# Author : Barun Halder
# Date : January, 2016

# Simple BT in Python

class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

    def add(self, value):
        new_node = Node(value)
        if not self.right:
            self.right = new_node
        elif not self.left:
            self.left = new_node
        else:
            self.left = self.left.add( value)
        return self

    def search( self, value ) :
        if self.item == value :
            print "FOUND"
            return True
        else :
            if self.left:
                if self.left.search( value ):
                    print "FOUND"
                    return True
                else:
                    return False
            if self.right:
                if self.right.search( value ):
                    print "FOUND"
                    return True
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

if __name__ == "__main__":
    bst = BST()

    for i in range(10,20):
        bst._add(i)

    print
    bst._search(19)
    
    bst._print_preorder()
