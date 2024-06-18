"""tree module"""

import graphviz as gv

from typing import Any, Union

from .node import Node

class BaseTree:
    """
        `Tree` parent object class
    """

    def __init__(self):
        self._root = Node(None)
        self.__current = self._root
    
    def reset(self):
        """
            Reset the `BaseTree` variables (essentially nodes)
        """

        self.__init__()

    def __next(self, node: Node):
        """
            Add a children node if not exist,
            then change the current node to the new node
        """

        # create new node with the current node as parent
        node.parent = self.__current

        value = node.value

        # set it as a children of the current node
        if not value in self.__current.childrens:
            self.__current.childrens[value] = node

        # replace the current
        self.__current = node

    def next(self, *args, **kwargs):
        """
            Same as `self._next` but with function arguments
        """

        self.__next(Node(None, *args, **kwargs))

    @property
    def is_at_root(self) -> bool:
        """
            Return if the current node is the root node
        """

        return self.__current == self._root
        
    def back(self) -> bool:
        """
            Update the current node with its parent if it exists
        """

        if self.__current.parent == None:
            return False

        self.__current = self.__current.parent

        return True

    def _debug(self):
        """
            BFS used to display line by line
        """

        line = [self._root]

        while line:        
            size = len(line)

            display = []

            for i in range(size):
                childrens = line[i].childrens

                for _, children in childrens.items():
                    display.append(children)
                    line.append(children)

            line = line[size:]

            if display:
                print(", ".join(map(str, display)))

class Tree(gv.Graph, BaseTree):
    """
        Graphviz controller inheriting `BaseTree`
    """

    def __init__(self, format="png"):
        super().__init__(format=format)

    def process(self):
        """
            Link every node with Graphviz
        """

        def dfs(node: Node):
            """
                Link every node with Graphviz
            """

            if node.childrens == {}:
                return

            if node.parent == None:
                for children in node.childrens.values():
                    dfs(children)

                return
            
            self.node(node.name, node.label)

            for children in node.childrens.values():
                self.node(children.name, children.label)
                self.edge(node.name, children.name)
                
                dfs(children)

        dfs(self._root)