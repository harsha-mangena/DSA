import pytest
from linkedlist import LinkedList
def test_for_operations():
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert(15)
    ll.insert_at_beginning(5)
    
    assert ll.get_to_list() == [5,10,15]
    
    ll.delete(15)
    
    assert ll.get_to_list() == [5,10]
    
    ll.clear()
    
    assert ll.get_to_list() == []