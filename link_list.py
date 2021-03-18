# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:51:40 2021

@author: HSIPL
"""

class node :
    def __init__ (self,val):
        self.next = None
        self.val = val
    
class Linklist:    
    def __init__ (self):
        self.head = None
        #self.tail = None
        
    def add(self,val):
        n = node(val)
        n.next = self.head
        self.head = n

    def append(self,val):
        if self.is_empty():
            self.add(val)
        else:
            n = node(val)
            temp = self.head
        
            while(temp.next != None):
                temp = temp.next
            temp.next = n

    def is_empty(self):
        return self.head == None
    
    def search(self,val):
        if self.is_empty():
            return -1
        else:
            temp = self.head
            count = 0
            while(temp.val != None):
                if temp.val == val:
                    return count
                elif temp.next != None:
                    temp = temp.next
                    count +=1
                else :
                    return -1

    def insert(self,pos,val):
        if pos == 0:
            self.add(val)
        elif  self.length() < pos  or pos < 0:
            return -1
        else:            
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            n = node(val)
            n.next = temp.next
            temp.next = n
    
    def length(self):
        if self.is_empty():
            return 0
        else:
            temp = self.head
            count = 1
            while(temp.next != None):
                temp = temp.next
                count +=1
            return count
    def print(self):
        #print('head = ' , self.head.val)
        temp = self.head
        for i in range(self.length()):
         #   print('head = ' , self.head.val)
            print(temp.val)
            temp = temp.next
            
            
a = node(1)
linklist = Linklist()  
linklist.head = a
#linklist.append(3)    