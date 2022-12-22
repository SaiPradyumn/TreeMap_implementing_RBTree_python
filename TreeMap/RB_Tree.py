from TreeMap.Color import Color
from TreeMap.Node import Node
import warnings
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class rb_tree:
    root: object

    # Temporary constructor
    def __init__(self, root=None) -> None:
        self.root = root

    def rotate_left(self, node):
        R_child = node.right
        node.right = R_child.left
        if R_child.left is not None:
            R_child.left.parent = node
        R_child.parent = node.parent
        if node.parent is None:
            self.root = R_child
        elif node is node.parent.left:
            node.parent.left = R_child
        else:
            node.parent.right = R_child
        R_child.left = node
        node.parent = R_child

    def rotate_right(self, node):
        L_child = node.left
        node.left = L_child.right
        if L_child.right is not None:
            L_child.right.parent = node
        L_child.parent = node.parent
        if node.parent is None:
            self.root = L_child
        elif node is node.parent.right:
            node.parent.right = L_child
        else:
            node.parent.left = L_child
        L_child.right = node
        node.parent = L_child

    def insert(self, key, val)->Node:
        # Create a red node with two black leaves
        node = Node(key, val, Color.RED, None, None, None)
        node.left = Node(None, None, Color.BLACK, node, None, None)
        node.right = Node(None, None, Color.BLACK, node, None, None)
        # Insert the node at a leaf position
        if self.root is None:
            position_node = node
            self.root = position_node
        else:
            position_node = self.search_tree(self.root, key)
            # Since we don't know if the node we got is the left or right child, we compare
            if position_node.key == node.key:
                position_node.value = val
                warning_message = "Duplicate Key: {key} found. Value updated".format(
                    key=node.key)
                warnings.warn(warning_message, category=SyntaxWarning)
                return
            elif position_node.parent.left is position_node:
                position_node.parent.left = node
            else:
                position_node.parent.right = node
            node.parent = position_node.parent
        # Case 1
        if node.parent is None:
            node.color = Color.BLACK
            return

        # Case 2
        if node.grand_parent() is None:
            return

        # Balancing the tree after insert operation
        self.fix(node)

        return self.root

    # Reccursive function to insert a node like a binary search tree

    def search_tree(self, node, search_key) -> Node:
        # Since in rb trees we also insert None nodes after each node, we need to
        # check if key of the node is none or if a duplicate key is present
        if node.key is None or node.key == search_key:
            return node

        if node.key < search_key:
            return self.search_tree(node.right, search_key)

        return self.search_tree(node.left, search_key)

    def fix(self, node):
        # Case 2 condition
        while node.parent.color == Color.RED:
            if node.parent is node.grand_parent().right:
                uncle = node.uncle()
                # Case 3
                if uncle.color == Color.RED:
                    uncle.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.grand_parent().color = Color.RED
                    node = node.grand_parent()
                else:
                    # Case 4 pt 2
                    if node is node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    # Case 5 pt 2
                    else:
                        node.parent.color = Color.BLACK
                        node.grand_parent().color = Color.RED
                        self.rotate_left(node.grand_parent())
            else:
                uncle = node.uncle()
                # Case 3
                if uncle.color == Color.RED:
                    uncle.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.grand_parent().color = Color.RED
                    node = node.grand_parent()
                else:
                    # Case 4 pt 1
                    if node is node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    # Case 5 pt 1
                    else:
                        node.parent.color = Color.BLACK
                        node.grand_parent().color = Color.RED
                        self.rotate_right(node.grand_parent())
            if node == self.root:
                break
        self.root.color = Color.BLACK

    def maximum(self, node):
        while(node.right.key is not None):
            node = node.right
        return node

    def fix_delete(self, node):
        while node is not self.root and node.color == Color.BLACK:
            # If node is the left child
            if node is node.parent.left:
                # s - sibling of node
                s = node.parent.right
                if s.color == Color.RED:
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_left(node.parent)
                    s = node.parent.right
                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.right.color == Color.BLACK:
                        s.left.color = Color.BLACK
                        s.color = Color.RED
                        self.rotate_right(s)
                        s = node.parent.right

                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.right.color = Color.BLACK
                    self.rotate_left(node.parent)
                    node = self.root
            # If node is the right child
            else:
                s = node.parent.left
                if s.color == Color.RED:
                    s.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_right(node.parent)
                    s = node.parent.left
                if s.left.color == Color.BLACK and s.right.color == Color.BLACK:
                    s.color = Color.RED
                    node = node.parent
                else:
                    if s.left.color == Color.BLACK:
                        s.right.color = Color.BLACK
                        s.color = Color.RED
                        self.rotate_left(s)
                        s = node.parent.left

                    s.color = node.parent.color
                    node.parent.color = Color.BLACK
                    s.left.color = Color.BLACK
                    self.rotate_right(node.parent)
                    node = self.root

        node.color = Color.BLACK

    def replace(self, node, child):
        if node.parent is None:
            self.root = child
        elif node is node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.parent = node.parent

    def delete_node(self, node):
        max_node = node
        max_color = node.color

        if node.left.key is None:
            child = node.right
            self.replace(node, node.right)
        elif node.right.key is None:
            child = node.left
            self.replace(node, node.left)
        else:
            # Finding Maximum of left sub tree
            max_node = self.maximum(node.left)
            max_color = max_node.color
            child = max_node.left
            if(max_node.parent is node):
                child.parent = max_node
            else:
                self.replace(max_node, max_node.left)
                max_node.left = node.left
                max_node.left.parent = max_node
            self.replace(node, max_node)
            max_node.right = node.right
            max_node.right.parent = max_node
            max_node.color = node.color
        if max_color == Color.BLACK:
            self.fix_delete(child)

    def delete(self, key):
        node = self.search_tree(self.root, key)
        if node.key is None:
            raise KeyError('Invalid Key')
        else:
            self.delete_node(node)


    def tree_traversal(self):
        order_list = []
        def inorder_traversal(node):
            if node is None or node.key is None:
                return
            inorder_traversal(node.left)
            order_list.append(node)
            inorder_traversal(node.right)
        
        inorder_traversal(self.root)
        return order_list

    def first_ele(self):
        node = self.root
        if node is not None:
            if node.left is not None:
                while node.left.key is not None:
                    node = node.left
        return node
    
    def last_ele(self):
        node = self.root
        if node is not None:
            if node.right is not None:
                while node.right.key is not None:
                    node = node.right
        return node

    def clear_tree(self):
        obj_list = self.tree_traversal()
        for i in obj_list:
            del i
        self.root = None
    
    def poll_first(self):
        node = self.first_ele()
        self.delete_node(node)
    
    def poll_last(self):
        node = self.last_ele()
        self.delete_node(node)
    

    def display_graph(self):
        def create_graph(node,g,colors):
            if(node.left.key != None):
                g.add_edge(node.key,node.left.key)
                colors.append(str(node.left.color)[6:])
                create_graph(node.left,g,colors)
            if(node.right.key != None):
                g.add_edge(node.key,node.right.key)
                colors.append(str(node.right.color)[6:])
                create_graph(node.right,g,colors)

        root = self.root
        if root is not None:
            if root.key is not None:
                g = nx.Graph()
                colors = []
                colors.append(str(root.color)[6:])
                create_graph(root,g,colors)
                g.add_node(root.key)
                pos = graphviz_layout(g, prog="dot")
                nx.draw(g, pos,with_labels=True, node_color=colors, font_color="white")
                plt.show()
            else:
                print("Blank Graph")
        else:
            print("Empty Tree")