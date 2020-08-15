import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

array = random.sample(range(0,20),10)

"""
Swap utility function
"""
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return

"""
Selection Sort 
Time complexity: Best Case and Worst Case O(n^2)
"""
def selection_sort(array):
    for i in range(0,len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
            yield array
        swap(array, i, min)
        yield array
 

"""
Bubble Sort
Time complexity: Worst Case O(n^2) Best Case O(n)
"""
def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)-i-1):
            if array[j+1] < array[j]:
                swap(array,j+1,j)

            yield array

"""
Insertion Sort
Time complexity: Worst Case O(n^2) Best Case O(n)
"""
def insertion_sort(array):
    for i in range(0,len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array,j,j-1)
            j = j-1
            yield array
  

"""
Merge Sort
Time complexity: Worst Case and Best Case O(nlogn)
"""
def merge_sort(a):
  if len(a) == 1:
    return a
  elif len(a) == 2:
    if a[0] > a[1]:
      return [a[1], a[0]]
    else:
      return a

  p = len(a)//2
  m1 = merge_sort(a[:p])
  m2 = merge_sort(a[p:])

  ret = []
  while 1:
    if len(m1) > 0 and len(m2) > 0:
      if m1[0] <= m2[0]:
        ret.append(m1[0])
        m1 = m1[1:]
      else:
        ret.append(m2[0])
        m2 = m2[1:]
    elif len(m1) > 0:
      ret += m1
      m1 = []
    elif len(m2) > 0:
      ret += m2
      m2 = []
    else:
      break
  return ret
"""
Quick Sort
Time complexity: Worst Case O(n^2) Best Case O(nlogn)
"""
def quick_sort(array,l, h):
    
    if l<h:
        j = partition(array,l,h)
        quick_sort(array,l,j-1)
        quick_sort(array,j+1,h)

    return
"""
Lomuto Partition

Every element on left of pivot is <
Every element on right of pivot is >
"""
def partition(array, l, h):
    pivot = array[h]
    i = l
    j = h

    while i <j:
        while array[i] <= pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i<j:
            swap(array, i, j)
    swap(array, l, j)

    return j + 1


#To do: Add matplotlib animation
#To do: heap sort, radix sort, bogo sort
if __name__ == "__main__":
   
    fig, ax = plt.subplots()
    generator = selection_sort(array) #the sorting visualization algo

    bar_rects = ax.bar(range(len(array)), array)
    
 
    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(len(array)) * 2)

    

   
    iteration = [0]
    def update(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
       

    final = animation.FuncAnimation(fig, func=update,fargs=(bar_rects, iteration), frames=generator, interval=10)


    plt.show()