import json
from anytree import Node, RenderTree
from anytree.search import find

class TaxonomyParser:

    """
    This class is a wrapper on a Tree class from the anytree library to hold
    different data hierarchies read from a JSON representation
    """

    def __init__(self, level_prefix = "L"):
        self.prefix = level_prefix
        self.nodes = {}
        self.root_key = None

    def find_by_name(self, name) -> Node:
        """
        Retrieve a node by its unique identifier name
        """
        root = self.nodes[self.root_key]
        node = find(root, lambda node: node.name == name)
        return node
   
    def read_from_json(self, fname):
        """
        Read the taxonomy from a JSON file given as input
        """
        
        self.nodes = {}
        try:
            with open(fname, "r") as f:
                data = json.load(f)
                n_levels = len(list(data.keys()))

                # read the root node
                root = data[f"{self.prefix}0"][0]
                name = root["name"]
                _ = root.pop("name")
                
                self.nodes[name] = Node(name, **root)
                self.root_key = name

                # populate the tree
                for k in range(1, n_levels):
                    
                    key = f"{self.prefix}{k}"
                    nodes = data[key]

                    for n in nodes:
                        try:
                            assert "name" in n
                            name = n["name"]
                            _ = n.pop("name")
                            parent = n["parent"]
                            _ = n.pop("parent")
                            
                            self.nodes[name] = Node(
                                name,
                                parent=self.nodes[parent],
                                **n
                            )
                        except AssertionError:
                            print(f"Malformed node representation: {n}")
                        except KeyError:
                            print(f"Detected a dangling node: {n['name']}")

        except (FileNotFoundError, KeyError):
            raise Exception("Not existent or malformed input JSON file")