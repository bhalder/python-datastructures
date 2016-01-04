from bst import BST, Node

def get_maximum( root ):
    if not root:
        return False
    else :
        cur = root
        
        while cur.right:
            cur = cur.right

        return cur.item

if __name__=="__main__":
    bst = BST()

    l = [ 6, 2, 9, 8, 7, 3, 1 ]

    for i in l:
        bst._add( i )

    print "Maximum is : %d" % ( get_maximum(bst.root) )  
