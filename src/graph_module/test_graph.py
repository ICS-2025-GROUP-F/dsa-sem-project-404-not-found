import pytest
from src.graph_module.graph import Graph, Passenger

@pytest.fixture
def sample_graph():
    return Graph()



def test_add_passenger(sample_graph):
    p1 = Passenger("Alice", "A123")
    sample_graph.add_passenger(p1)
    assert sample_graph.has_passenger("A123")

def test_add_duplicate_passenger_raises(sample_graph):
    p1 = Passenger("Bob", "B456")
    sample_graph.add_passenger(p1)
    with pytest.raises(ValueError):
        sample_graph.add_passenger(p1)  # Should raise ValueError

def test_add_connection(sample_graph):
    p1 = Passenger("C", "C789")
    p2 = Passenger("D", "D101")
    sample_graph.add_passenger(p1)
    sample_graph.add_passenger(p2)
    sample_graph.add_connection("C789", "D101")
    assert "D101" in sample_graph.get_connections("C789")

def test_remove_passenger(sample_graph):
    p1 = Passenger("E", "E202")
    sample_graph.add_passenger(p1)
    sample_graph.remove_passenger("E202")
    assert not sample_graph.has_passenger("E202")

def test_get_connections_returns_list(sample_graph):
    p1 = Passenger("F", "F303")
    p2 = Passenger("G", "G404")
    sample_graph.add_passenger(p1)
    sample_graph.add_passenger(p2)
    sample_graph.add_connection("F303", "G404")
    result = sample_graph.get_connections("F303")
    assert isinstance(result, list)
    assert "G404" in result

def test_has_passenger(sample_graph):
    p1 = Passenger("H", "H505")
    sample_graph.add_passenger(p1)
    assert sample_graph.has_passenger("H505")

def test_remove_nonexistent_passenger_raises(sample_graph):
    with pytest.raises(ValueError):
        sample_graph.remove_passenger("X999")
