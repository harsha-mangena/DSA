from doublylinkedlist import DoublyLinkedList
import pytest

def test_operations():
    ll = DoublyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert(15)
    ll.insert_at_beginning(5)
    
    assert ll.get_to_list() == [5,10,15]
    
    ll.clear()
    
    assert ll.get_to_list() == []