# Author : Barun Halder
# Date : January, 2016

# Binary Search


def bin_search( a ):
    i = 0

    while i < len(a):
        j = 0
        while j < len(a) - i - 1:
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
            j+=1
        i+=1

    return a

if __name__ == "__main__":
    a = [1, 3, 2 , 6, 9, 5, 4 ]

    print "Original Array", a
    print "Sorted Array", bin_search(a)
 
    
