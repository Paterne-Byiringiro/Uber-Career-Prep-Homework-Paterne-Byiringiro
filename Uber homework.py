# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:59:19 2021

@author: RF511
"""

##################################
#Question 1 a
##
def isStringPermutation(s1, s2):
    
    def make_dict(string):
        my_dict = {}
        for i in string:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        return my_dict
    
    dict_1 = make_dict(s1)
    dict_2 = make_dict(s2)
   
    return dict_1 == dict_2
print(isStringPermutation("asdf", "fsda"))
print(isStringPermutation("asdf", "fsa"))
print(isStringPermutation("asdf", "fsax"))

# Second way
def isStringPermutation(s1, s2):
    return sorted(s1) == sorted(s2)

print(isStringPermutation("asdf", "fsda"))
print(isStringPermutation("asdf", "fsa"))
print(isStringPermutation("asdf", "fsax"))        
    


##########################################################
#Question 1b
# Using iteration
##########
def pairsThatEqualSum(inputArray, targetSum):
    my_list = []
    
    for i in range(len(inputArray)):
        for x in inputArray[i+1:]:
            if inputArray[i] + x == targetSum:
                my_list.append((inputArray[i],x))
    return my_list

print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))        
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))        
    
#Question 1b
# Using Recursion. which generalized everything, may be we can be given to look for n elements which sum to a target sum
#I made a new argument, n_comb    

def combinations(inputArray, n_comb, target_sum):
    solutions = []
    if n_comb == 1:
        return [{i} for i in inputArray]
    for x in inputArray:
        solution = combinations([y for y in inputArray if y != x], n_comb-1, target_sum - x)
        for s in solution:
        
            s.add(x)
            if s not in solutions and sum(s) == target_sum:
                solutions.append(s)
    return solutions

print(combinations([1,2,3,4,5], 2, 5))

## Question 1b Third way
def pairsThatEqualSum(inputArray, targetSum):
    
    my_list = []
    for i in range(len(inputArray)):
        the_list = [{inputArray[i],inputArray[x]} for x in range(len(inputArray))
                    if x != i and inputArray[i] + inputArray[x] == targetSum]
        for x in the_list:
            if x not in my_list:
                my_list.append(x)
    final_list = []   
    for c in my_list:
        final_list.append(list(c))
    return final_list

print(pairsThatEqualSum([1,2,3,4,5,], 5))
        

##################################################################################
#############################################################################
################################################################################
## IMPLEMENTATION OF STACKS
class Node():
    def __init__(self,d,n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
        
class Stack():
    def __init__(self, r=None):
        self.root = r
        self.size = 0
        self.minimum = None

    def push(self, d):
        ## Like append in linked list
      if self.minimum == None:
          self.minimum = d
      elif d < self.minimum:
          self.minimum = d
          
      self.size += 1
      my_last_node = Node(d)
      
      if self.root == None:
          self.root = my_last_node
      else:
          
          this_node = self.root
          while this_node.get_next() != None:
              this_node = this_node.get_next()
          this_node.set_next(my_last_node)
    
          
    def top(self):
      
        this_node = self.root
        while this_node.get_next() != None:
           
            this_node = this_node.get_next()
        return this_node.get_data()
    
    def pop(self):
        self.size -= 1
        last_node = self.top()
        this_node = self.root.get_data()
        the_min = self.root.get_data()
        if this_node == last_node:
            self.root = None
            self.minimum = None
            return this_node
        else:
            while this_node.get_next() != last_node:
                this_node = this_node.get_next()
                if this_node.get_data() < the_min:
                    the_min = this_node.get_data()
         
            self.minimum = the_min
            this_node.set_next(None)
        
    def isEmpyty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def size_(self):
        ### When I call my function size, it doesn't give me the answer
        return self.size
        # this_node = self.root
        # tot = 0
        # while this_node.get_next() != None:
        #     tot += 1
        #     this_node = this_node.get_next()
        # return tot+1
    
    def min_(self):
        return self.minimum
        
    
myStack = Stack()
myStack.push(42)


print("Top of stack: ", myStack.top())

print("Size of stack: ", myStack.size_())
popped_value = myStack.pop()
print("Popped value: " , popped_value)
print("Size of stack: ", myStack.size_())
print(myStack.min_())


## Fo non inter values:
# I thought of making anew function for lesss than to compare the minimum 
# And I am asking my self a question how to implement a mimum function i case we have differenet types of inputs


#####################################################################
###################################################################33
# IMPLEMENTATION OF Queues

class Node():
    def __init__(self,d,n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
        
class Queue():
    def __init__(self, r=None):
        self.root = r
        self.size = 0
      
   
    def enqueue(self, d):
       
        self.size += 1
        my_last_node = Node(d)
          
        if self.root == None:
            self.root = my_last_node
        else:
            this_node = self.root
            while this_node.get_next() != None:
                this_node = this_node.get_next()
            this_node.set_next(my_last_node)
          
          
    def dequeue(self):
        self.size -= 1
        this_node = self.root
        if this_node.get_next() == None:
            self.root = None
            
        else:
            first = this_node.get_next()
            self.root = first
            return this_node.get_data()
            
        
          
    def rear(self):
        this_node = self.root
        while this_node.get_next() != None:
           
            this_node = this_node.get_next()
        return this_node.get_data()
    
    
    def front(self):
        return self.root.get_data()
    
    def size_(self):
        return self.size
    
   
    def isEmpyty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    
  
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("Size of queue: ", myQueue.size_())
print("Front of queue: ", myQueue.front())
print("Rear of queue: ", myQueue.rear())
dequeuedItem = myQueue.dequeue()
print("Dequeue item: ", dequeuedItem)

## This Queu does everything
             

###########################################################################
#########################################################################
################################################################################

## Question 4 and 5
# LINKED LISTS
class Node():
    def __init__(self,d,n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
        
        
class Linked_list():
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    
    def push(self, d):
        my_last_node = Node(d)
        
        if self.root == None:
            self.root = my_last_node
        else:
            
            this_node = self.root
            while this_node.get_next() != None:
                this_node = this_node.get_next()
            this_node.set_next(my_last_node)
    
    def pop(self):
        if self.root == None:
            return None
        if self.root.get_next() == None:
            self.size -= 1
            return self.root
       
        this_node = self.root
        while this_node.get_next() != None:
            prev_node = this_node
            this_node = this_node.get_next()
        self.size -= 1
        prev_node.set_next(None)
        return this_node.get_data()
    
    def insert(self,index, the_node):
        ##the_node = Node(d)
        if index >= self.size:
            return 
           
        elif index == 0:
            former_root = self.root
            self.root = the_node
            self.root.sset_next(former_root)
            
        else:
           
            this_node = self.root
            prev_node = this_node
            tot = 0
            while tot < self.size:
                if tot == index:
                    self.size += 1
                    prev_node.set_next(the_node)
                    the_node.set_next(this_node)
                else:
                    prev_node = this_node
                    this_node = this_node.get_next()
                    tot += 1
                    
    def remove(self, index):
          if index >= self.size:
              return 
         
          elif index == 0:
              self.root = self.root.get_next()
             
          else:
             
              this_node = self.root
              prev_node = this_node
              tot = 0
              while tot < self.size:
                 
                  if tot == index:
                      self.size -= 1
                      prev_node.set_next(this_node.get_next())
                  else:
                      prev_node = this_node
                      this_node = this_node.get_next()
                      tot += 1
            
    def elementAt(self,index):
        if index >= self.size:
              return 
         
        elif index == 0:
            self.root = self.root.get_next()
             
        else:
            this_node = self.root
            prev_node = this_node
            tot = 0
            while tot < self.size:
                 
                if tot == index:
                    return prev_node.get_data()
                else:
                    prev_node = this_node
                    this_node = this_node.get_next()
                    tot += 1
           
            
    def size_(self):
        return self.size
    
    
    def has_cycle(self):
        my_set = set()
        if self.size  <= 1:
            return False
        this_node = self.root
        my_set.add(this_node.get_data())
        while this_node.get_next() != None:
            if this_node.get_next().get_data not in my_set:
                my_set.add(this_node.get_next().get_data())
            else:
                return True
          
            this_node = this_node.get_next()
            
        return False
        
    
   
    def display(self):
        elements = []
        this_node = self.root
        while this_node.get_next() != None:
            elements.append(this_node.get_data())
            this_node = this_node.get_next()
            
        elements.append(this_node.get_data())
        return elements

    
    def palindrome(self):
        elements = self.display()
        def to_reverse_list(numbss):
            nums = numbss[:]
            left = 0
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums
        
        the_reverse = to_reverse_list(elements)
        
        return the_reverse == elements
        
       
        
    def reverse(self):
        this_node = self.root
        prev_node = None
        
        while this_node:
            c = this_node.get_next()
            this_node.set_next(prev_node) 
            prev_node = this_node
            this_node = c
        self.root = prev_node
    
    
            
  
        
          
    
          


        
        
    