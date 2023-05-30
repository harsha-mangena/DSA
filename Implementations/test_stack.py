import pytest
from stack import Stack

def test_operations():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    
    assert stack.peek() == 20
    
    stack.pop()
    
    assert stack.peek() == 10
    
    stack.clear()
    
    assert stack.is_empty() == True
    
    assert stack.peek() == -1
    
    
    