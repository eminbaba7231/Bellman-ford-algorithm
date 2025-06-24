import unittest
from algorithm import bellman_ford

class TestBellmanFord(unittest.TestCase):

    def test_valid(self):
        nodes = ["A", "B", "C"]
        edges = [
            {"from_node": "A", "to_node": "B", "weight": 4},
            {"from_node": "A", "to_node": "C", "weight": 5},
            {"from_node": "B", "to_node": "C", "weight": -2}
        ]
        result = bellman_ford(nodes, edges, "A")
        self.assertEqual(result["final"]["C"], 2)

    def test_negative_cycle(self):
        nodes = ["A", "B", "C"]
        edges = [
            {"from_node": "A", "to_node": "B", "weight": 1},
            {"from_node": "B", "to_node": "C", "weight": -2},
            {"from_node": "C", "to_node": "A", "weight": -2}
        ]
        result = bellman_ford(nodes, edges, "A")
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
