# Author : Barun Amalkumar Halder
# Date : January, 2016

# Function to check if the tree is balanced or not

from bst import BST, Node

def left_tree_weight ( node ) :
    if not node :
        return 0
    else :
        return left_tree_weight( node.left ) + 1
    
def right_tree_weight ( node ) :
    if not node :
        return 0
    else :
        return right_tree_weight( node.right ) + 1

def check_balance ( node ) :
    left_weight = left_tree_weight( node )
    right_weight = right_tree_weight( node )

    if left_weight > right_weight:
        if left_weight - right_weight > 2 :
            return False
    else:
        if right_weight - left_weight > 2 : 
            return False
    if (not node.left) and (not node.right):
        return True

    if node.left and node.right : 
        return check_balance( node.left ) and check_balance( node.right )
    elif node.left and (not node.right) :
        return check_balance( node.left )
    else :
        return check_balance( node.right )


if __name__=="__main__":
    bst = BST()
    for i in range( 11,12):
        bst._add(i)

    if check_balance( bst.root):
        print "Tree is balanced"
    else : 
        print "Tree is not balanced"
