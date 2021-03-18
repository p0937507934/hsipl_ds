# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:51:32 2021

@author: user
"""

class Node:
    def __init__(self, value):     
        
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add (self, value):  #value可以 Node試試看
        '''
        add to head
        '''
        n = Node(value)
        n.next = self.head
        self.head = n
        
        
    def append(self,value):
        '''
        add to end
        '''
        n = Node(value)
        if(self.head!=None):
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = n
        else:
             self.head = n
            
    def travel(self):
         cur =  self.head
         print(cur.value)
         while cur.next!=None:    
             print(cur.next.value)
             cur.next = cur.next.next
             
    # def insert(self, pos, value):
    # def search(self,value):     
    # def length(self):   
    # def delete(slef,value) :        
        
a = LinkedList()    
a.add(1)
a.add(2)
a.add(3)
a.append(4)
a.travel()
    