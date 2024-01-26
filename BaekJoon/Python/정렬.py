# 버블 정렬
def bubblesort(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1], A[j]

# 퀵정렬
def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] =A[right], A[left]
                
                left +=1
                #print(pivot,'',left)
                print(A)
        A[left], A[hi] = A[hi], A[left]
        #print(A)
        return left
    #print(lo,'',hi)
    if lo < hi:
        pivot = partition(lo,hi)
        quicksort(A,lo,pivot - 1)
        
        quicksort(A,pivot + 1, hi)
    return A
quicksort([2,8,7,1,3,5,6,4],0,7)