from queue_ import Queue
import pytest

def test_operations():
    queue = Queue()
    
    assert queue.is_empty() == True
    
    queue.enqueue(10)
    queue.enqueue(20)
    
    queue.dequeue()
    
    assert queue.peek() == 20
    
    assert queue.is_full() == False
    assert queue.is_empty() == False