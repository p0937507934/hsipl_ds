# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:53:06 2021

@author: M10817021
"""

class Node:
    def __init__(self,val=0,next=None):
        '''create a node with value and function to point next node'''
        self.val=val
        self.next=next

class Linkedlist:
    def __init__(self,head=None):
        self.head=head
    
    def isempty(self):
        '''to confirm that if linkedlist is empty or not'''
        return self.head == None
    def add(self,val):
        '''add value to head'''
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def append(self,val):
        '''add value to end'''
        if self.head==None:
            self.head = Node(val)
        else:
            node = Node(val)
            cur = self.head
            while cur.next !=None:
                cur = cur.next
            cur.next=node
    
    def show(self):
        '''show all values in current linkedlist'''
        cur=self.head
        while cur!=None:
            print (cur.val)
            cur = cur.next
    def delete_val(self,val):
        '''delete the value in linkedlist if it existed'''
        cur = self.head
        if self.head.val == val:
            self.head = self.head.next
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur=cur.next
        
    def delete_index(self,index):
        '''delete the index in linkedlist'''
        flag=0
        if index == 0:
            self.head = self.head.next
        cur = self.head
        while(cur.next!=None):
            if flag+1 == index:
                cur.next = cur.next.next
                break
            else:
                flag+=1
                cur = cur.next
    def insert(self,pos,val):
        '''insert new node of val in linkedlist'''
        flag = 0
        cur = self.head
        node = Node(val)
        while cur.next != None:
            if flag+1 == pos:
                node.next = cur.next
                cur.next = node
                break
            else:
                flag += 1
                cur=cur.next
    def length(self):
        '''show the length of linkedlist'''
        i=0
        cur = self.head
        while(cur!=None):
            i=i+1
            cur=cur.next
        return i
    def search_val(self,val):
        '''search the value in linkedlist where it existed'''
        ans,n = [],0
        cur = self.head
        while cur != None:
            if  cur.val == val:
                ans.append(n)
            n+=1
            cur = cur.next
        return ans
    def search_index(self,index):
        '''show the value of target index in linkedlist'''
        n=0
        cur = self.head
        while cur != None:
            if n == index:
                return cur.val
            n+=1
            cur =cur.next
    def replace(self, pos, val):
        '''replace the value of target postion(index)'''
        self.insert(pos,val)
        self.delete_index(pos-1)
s=Linkedlist()
for i in range(10):
    s.append(i)
