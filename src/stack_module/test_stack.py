import pytest
from src.stack_module.stack import Stack, Passenger

@pytest.fixture
def sample_stack():
    return Stack()

def test_push_increases_size(sample_stack):
    p1 = Passenger("Alice", "A123")
    sample_stack.push(p1)
    assert sample_stack.size() == 1

def test_pop_returns_last_passenger(sample_stack):
    p1 = Passenger("Bob", "B456")
    sample_stack.push(p1)
    popped = sample_stack.pop()
    assert popped.name == "Bob"

def test_pop_empty_raises_error(sample_stack):
    with pytest.raises(IndexError):
        sample_stack.pop()

def test_peek_returns_top(sample_stack):
    p1 = Passenger("Carl", "C789")
    sample_stack.push(p1)
    assert sample_stack.peek().name == "Carl"

def test_is_empty(sample_stack):
    assert sample_stack.is_empty()
    sample_stack.push(Passenger("D", "D101"))
    assert not sample_stack.is_empty()

def test_get_all_returns_copy(sample_stack):
    p1 = Passenger("E", "E202")
    p2 = Passenger("F", "F303")
    sample_stack.push(p1)
    sample_stack.push(p2)
    all_items = sample_stack.get_all()
    assert len(all_items) == 2
    assert all_items[0].name == "E"
    assert all_items[1].name == "F"
