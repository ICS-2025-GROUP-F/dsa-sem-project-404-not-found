import pytest
from src.Linkedlist_module.linked_list import LinkedList, Passenger

@pytest.fixture
def sample_list():
    return LinkedList()

def test_insert_adds_passenger(sample_list):
    p1 = Passenger("Alice", "A123")
    sample_list.insert(p1)
    assert len(sample_list.get_all()) == 1

def test_delete_removes_correct(sample_list):
    p1 = Passenger("Bob", "B456")
    sample_list.insert(p1)
    deleted = sample_list.delete_by_ticket("B456")
    assert deleted.name == "Bob"
    assert sample_list.is_empty()

def test_delete_nonexistent_raises(sample_list):
    with pytest.raises(ValueError):
        sample_list.delete_by_ticket("X000")

def test_search_finds_correct(sample_list):
    p1 = Passenger("Carl", "C789")
    sample_list.insert(p1)
    found = sample_list.search("C789")
    assert found.name == "Carl"

def test_search_returns_none_if_not_found(sample_list):
    assert sample_list.search("Y111") is None

def test_get_all_returns_all(sample_list):
    p1 = Passenger("Diana", "D321")
    p2 = Passenger("Eve", "E555")
    sample_list.insert(p1)
    sample_list.insert(p2)
    all_passengers = sample_list.get_all()
    assert len(all_passengers) == 2
    assert all_passengers[0].name == "Diana"