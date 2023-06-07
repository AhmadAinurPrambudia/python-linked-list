class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def add_To_Front(self, data):
    New_Node = Node(data)
    New_Node.next = self.head
    self.head = New_Node
  
  def add_To_End(self, data):
    New_Node = Node(data)
    if self.head is None:
      self.head = New_Node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = New_Node

  def remove_Front(self):
    if self.head is None:
      return
    self.head = self.head.next

  def remove_End(self):
    if self.head is None:
      return
    if self.head.next is None:
      self.head = None
      return
    
    current = self.head
    while current.next.next:
      current = current.next
    current.next = None

  def print_Linked_List(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next
    print()

linked_list = LinkedList()

linked_list.add_To_Front(3)
linked_list.add_To_Front(2)
linked_list.add_To_Front(1)

linked_list.add_To_End(4)
linked_list.add_To_End(5)
linked_list.add_To_End(6)

print("Linked List Awal : ")
linked_list.print_Linked_List()

linked_list.remove_Front()
linked_list.remove_End()

print("Linked List Setelah penghapusan : ")
linked_list.print_Linked_List()
