import unittest
from dependencies import DependencyInspector, CircularDependencyException


class DependencyInspectorTestCase(unittest.TestCase):
    def setUp(self):
        self.target = DependencyInspector()

    def test_add_direct(self):
        self.target.add_direct('A', 'B C')

        self.assertListEqual(self.target.dependencies_for('A'), ['B', 'C'])

    def test_add_direct_raises_value_error_if_dependencies_previously_added(self):
        self.target.add_direct('A', 'B C')

        with self.assertRaises(ValueError):
            self.target.add_direct('A', 'D E')

    def test_dependencies_for_basic(self):
        self.target.add_direct('A', 'B C')
        self.target.add_direct('B', 'D E')

        self.assertListEqual(self.target.dependencies_for('A'),
                             ['B', 'C', 'D', 'E'])

    def test_dependencies_for_non_existent_member_returns_empty_list(self):
        self.target.add_direct('A', 'B C')

        self.assertListEqual(self.target.dependencies_for('B'), [])

    def test_dependencies_for_raises_exception_when_circular_dependency_exists(self):
        self.target.add_direct('A', 'B')
        self.target.add_direct('B', 'C')
        self.target.add_direct('C', 'A')

        with self.assertRaises(CircularDependencyException):
            self.target.dependencies_for('A')
