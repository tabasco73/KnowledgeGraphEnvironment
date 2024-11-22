import unittest
from utility.graph_creation.generate_cat_edges import create_graph_from_classes
from domains.pydantic.parkit_imports import classes_list

class TestDataStructureFormat(unittest.TestCase):
    
    def setUp(self):
        self.categories, self.edges = create_graph_from_classes(classes_list, output_filename='pydantic_graph_test_dot.png', layout_prog='dot')
        print(f'{self.categories=}')

    def test_categories_format(self):
        self.assertIsInstance(self.categories, list)
        for category in self.categories:
            self.assertIsInstance(category, dict)
            self.assertIn('name', category)
            self.assertIn('color', category)
            self.assertIn('shape', category)
            self.assertIn('nodes', category)
            self.assertIsInstance(category['nodes'], list)
            for node in category['nodes']:
                self.assertIsInstance(node, dict)
                self.assertIn('id', node)
                self.assertIn('name', node)
                self.assertIsInstance(node['id'], int)
                self.assertIsInstance(node['name'], str)
            

    def test_edges_format(self):
        self.assertIsInstance(self.edges, list)
        for edge in self.edges:
            self.assertIsInstance(edge, dict)
            self.assertIn('color', edge)
            self.assertIn('connections', edge)
            self.assertIn('arrowhead', edge)
            self.assertIsInstance(edge['connections'], list)
            for connection in edge['connections']:
                self.assertIsInstance(connection, dict)
                self.assertIn('id_from', connection)
                self.assertIn('ids_to', connection)
                self.assertIsInstance(connection['id_from'], int)
                self.assertIsInstance(connection['ids_to'], list)
                for id_to in connection['ids_to']:
                    self.assertIsInstance(id_to, int)

if __name__ == '__main__':
    unittest.main()