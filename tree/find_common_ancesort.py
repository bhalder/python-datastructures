# Author : Barun Halder
# Date : January, 2016

from bst import Node, BST

def find_ancestor( root, val1, val2 ):
    if root.item:
        if root.item > val1 and root.item < val2:
            return root.item
        elif root.item < val1 and root.item > val2:
            return root.item
        elif val1 < root.item:
            return find_ancestor( root.left, val1, val2 )
        elif val1 > root.item:
            return find_ancestor( root.right, val1, val2 )
    else :
        return None

if __name__ == "__main__":
    bst = BST()

    l = [ 10, 9, 6, 1, 8 , 11, 15, 12, 5 ]
    for i in l :
        bst._add( i )

    print ( find_ancestor( bst.root, 1, 8) )
