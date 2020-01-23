# Name: Gabriel Barney


class Queue:
   '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''


   def __init__(self, capacity):
       '''Creates an empty Queue with a capacity'''
       self.capacity=capacity
       self.length=0
       self.front=0
       self.rear=0
       self.items=[None]*self.capacity


   def is_empty(self):
       '''Returns True if the Queue is empty, and False otherwise'''
       return self.length==0


   def is_full(self):
       '''Returns True if the Queue is full, and False otherwise'''
       return self.length==self.capacity


   def enqueue(self, item):
       '''If Queue is not full, enqueues (adds) item to Queue
         If Queue is full when enqueue is attempted, raises IndexError'''
       if self.length==self.capacity:
           raise IndexError('Queue is full')
       self.items[self.rear]=item
       self.rear+=1
       self.rear%=self.capacity
       self.length+=1


   def dequeue(self):
       '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
         #If Queue is empty when dequeue is attempted, raises IndexError'''
       if self.length == 0:
           raise IndexError('Queue is empty')
       temp = self.items[self.front]
       self.front+=1
       self.front%=self.capacity
       self.length-=1
       return temp


   def size(self):
       '''Returns the number of elements currently in the Queue, not the capacity'''
       return self.length
