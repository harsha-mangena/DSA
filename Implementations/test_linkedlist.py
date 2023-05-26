import pytest
from linkedlist import LinkedList
def test_for_insertion():
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert(15)
    ll.insert_at_beginning(5)
    
    assert ll.get_to_list() == [5,10,15]
    
def test_for_deletion():
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert(15)
    ll.insert_at_beginning(5)
    ll.delete(5)
    
    assert ll.get_to_list() == [10,15]
    
def test_to_clear():
    ll = LinkedList()
    ll.insert(1)
    
    assert ll.get_to_list() == [1]
    
    ll.clear()
    
    assert ll.get_to_list() == []
    
    