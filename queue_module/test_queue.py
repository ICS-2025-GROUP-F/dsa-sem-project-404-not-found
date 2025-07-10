# src/queue_module/test_queue.py

import pytest
from queue_module.queue import Queue, Passenger

@pytest.fixture
def sample_queue():
    return Queue()

def test_enqueue_increases_size(sample_queue):
    p1 = Passenger("Alice", "A123")
    sample_queue.enqueue(p1)
    assert sample_queue.size() == 1

    p2 = Passenger("Bob", "B456")
    sample_queue.enqueue(p2)
    assert sample_queue.size() == 2

def test_dequeue_returns_correct_passenger(sample_queue):
    p1 = Passenger("Charlie", "C789")
    p2 = Passenger("Diana", "D321")
    sample_queue.enqueue(p1)
    sample_queue.enqueue(p2)

    dequeued = sample_queue.dequeue()
    assert dequeued.name == "Charlie"
    assert dequeued.ticket_number =="C789"
    assert sample_queue.size() == 1

def test_dequeue_empty_raises_error(sample_queue):
    with pytest.raises(IndexError) as excinfo:
        sample_queue.dequeue()
    assert "Queue is empty" in str(excinfo.value)

def test_peek_returns_first_passenger_without_removing(sample_queue):
    p1 = Passenger("Eve", "E555")
    p2 = Passenger("Frank", "F777")
    sample_queue.enqueue(p1)
    sample_queue.enqueue(p2)

    peeked = sample_queue.peek()
    assert peeked.name == "Eve"
    assert peeked.ticket_number == "E555"
    assert sample_queue.size() == 2  # Should not remove anything

def test_is_empty(sample_queue):
    assert sample_queue.is_empty() is True
    p = Passenger("Grace", "G999")
    sample_queue.enqueue(p)
    assert sample_queue.is_empty() is False

def test_get_all_returns_copy(sample_queue):
    p1 = Passenger("Hank", "H111")
    p2 = Passenger("Ivy", "I222")
    sample_queue.enqueue(p1)
    sample_queue.enqueue(p2)

    all_passengers = sample_queue.get_all()
    assert isinstance(all_passengers, list)
    assert len(all_passengers) == 2
    assert all_passengers[0].name == "Hank"
    assert all_passengers[1].ticket_number == "I222"
