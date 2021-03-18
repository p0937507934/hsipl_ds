# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:17:20 2021

@author: HSIPL39
"""


class Node:
    
    
    def __init__(self,val):
        self.val = val
        self.next = None
    

class SingleLinkedList:
    
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head == None
    
    def append(self,val):
        node = Node(val)
        
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def travel(self):
        cur = self.head
        while cur:
            print(cur.val,end=" ")
            cur =  cur.next
        print("")
    
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count = count + 1
            cur = cur.next
        
        return count 
    
    def insert(self,pos,val):
        if pos <= 0:
            self.add(val)
        elif pos >= self.length():
            self.append(val)
        else:
            node = Node(val)
            cur = self.head
            while pos != 1:
                cur = cur.next
                pos = pos - 1
            node.next = cur.next
            cur.next = node
    def add(self,val):    
        node = Node(val)
        node.next = self.head
        self.head = node
    def search(self,val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False
    
    def delete(self,val):
        cur = self.head
        if cur.val == val:
            self.head = cur.next
        else:
            while cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                    return True
                else:
                    cur = cur.next
            return False


            
            
        
if __name__ == "__main__":

    s = SingleLinkedList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(5)
    s.travel()

    s.add(8)
    s.add(9)
    s.insert(2,7)
    s.insert(9,7)
    s.travel()
    print(s.search(10))
    s.delete(2)
    s.delete(9)
    s.delete(7)
    s.delete(7)
    s.travel()
            
            
            
            
            
        
    