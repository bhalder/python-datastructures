# Author : Barun Halder
# Date : January, 2016

# Function for Breadth First Search

from collections import deque
from bst import BST, Node

def bfs( root ):
    q = deque()
    nodes = []
    q.append( root )

    while q :
        cur = q.popleft()
        nodes.append( cur.item )
        
        if cur.left:
            q.append( cur.left )
        
        if cur.right:
            q.append( cur.right )

    return nodes

if __name__ == "__main__":
    bst = BST()
    l = [10, 6, 5, 7, 15, 12, 17, 19, 21 ]
    for i in l :
        bst._add( i )

    print "Input is - "
    print l
    print "The BFS traversal is - "
    print bfs( bst.root ) 
