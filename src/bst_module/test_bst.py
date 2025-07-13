import pytest
from bst_module.binarysearchtree import BinarySearchTree, Passenger

@pytest.fixture
def bst():
    return BinarySearchTree()

def test_insert_and_search(bst):
    p1 = Passenger("Alice", "A123")
    bst.insert(p1)
    found = bst.search("A123")
    assert found is not None
    assert found.name == "Alice"

def test_insert_duplicate_raises(bst):
    p1 = Passenger("Bob", "B123")
    bst.insert(p1)
    with pytest.raises(ValueError):
        bst.insert(Passenger("Bob2", "B123"))

def test_delete_existing(bst):
    p1 = Passenger("Carol", "C123")
    bst.insert(p1)
    bst.delete("C123")
    assert bst.search("C123") is None

def test_delete_non_existing(bst):
    bst.delete("D123")  # Should not raise error

def test_inorder_traversal(bst):
    p1 = Passenger("Eve", "E001")
    p2 = Passenger("Dan", "D001")
    p3 = Passenger("Frank", "F001")
    bst.insert(p1)
    bst.insert(p2)
    bst.insert(p3)
    result = bst.inorder()
    assert result == sorted(result, key=lambda p: p.ticket_number)
