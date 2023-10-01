class hierarchy_node:
    def __init__(self, id, childrens) -> None:
        self.id = id
        self.childrens = childrens

class hierarchy_Tree:
    def __init__(self, hierarchy) -> None:
        self.hierarchy = hierarchy[0]
        self.nodes_count = len(self.hierarchy)
        self.nodes = {}
        for node in range(self.nodes_count):
            self.nodes[node] = hierarchy_node(node, [])
        self.build_tree()
    
    def build_tree(self):
        id = 0
        for _, _, child_id, parent_id in self.hierarchy:
            # get the hierarchy node of the current working node and it's first child
            node = self.nodes[id]
            if child_id != -1:
                child_node = self.nodes[child_id]
                # add the child node to the childrens of current node
                if child_node not in node.childrens:
                    node.childrens.append(child_node)
            # add the current node to the childrens of its parent node 
            # if not done previously
            if parent_id != -1:
                parent_node = self.nodes[parent_id]
                if node not in parent_node.childrens:
                    parent_node.childrens.append(node)
            id += 1
    
    def retrieve_root(self):
        id = 0
        for _, _, _, parent in self.hierarchy:
            if parent == -1:
                return self.nodes[id]
            id += 1


