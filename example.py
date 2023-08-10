#!/usr/bin/python
import sys
import random

def git_opeation():
 print("I am adding example.py file to the remote repository.")
 data = sys.argv[1]
 print(data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
   
    def __init__(self):
        self.head = None

    def addNodes(self):

        self.head = Node(random.randint(1, 10))
        linkedList = self.head

        for i in range(2, 11): 
            linkedList.next = Node(random.randint(1, 10))
            linkedList = linkedList.next
    
    def print(self):

        while self.head != None:
            print(self.head.data, end = '_')
            self.head = self.head.next

ll = LinkedList()
ll.addNodes()
ll.print()
