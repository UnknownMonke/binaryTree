from random import random

class Coordinates:
    """
    Object to hold coordinates of the line created.

    v: value
    w: width
    h: height
    m: middle
    """
    def __init__(self, v, w: int, h: int, m: int):
        self.v = v
        self.w = w
        self.h = h
        self.m = m


class Node:
    """
    Tree element. Defines a tree.

    A tree consists of a root Node which contains its value and its children.
    Each children contains its own subtree.

    At the bottom of the tree, a Node without children is a leaf Node.

    ---

    In case of a binary tree, each Node can only have 2 children, left and right.
    """
    # Constructor
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    # Utility
    def is_leaf(self):
        return self.left is None and self.right is None


    def insert(self, val, rand: bool):
        """
        Inserts into a Node.

        If the current Node has a value, we add to children.
        If the current Node has no value, it cannot have children.

        ---

        If the rand argument is specified, the value is added either left or right randomly.

        Otherwise, the value is added right if greater than the current node value.

        ---

        The Node is always added at the bottom of the tree: the function is called recursively until we reach a Node with no children.
        """
        if self.value is not None: # Existing node, adds to children.

            if rand:
                dest = bool(round(random())) # 0 for left or 1 for right.
            else:
                dest = self.value > val
                
            if dest:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val, rand)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val, rand)
        else: # Adds to node value.
            self.value = val


    # ----------- Display -----------


    def display(self):
        lines = self.generate()
        for line in lines.v:
            print(line)


    def generate(self):
        """ 
        Parses the tree and recursively constructs an array of lines to print.

        ---

        Each levels returns an array of 2 lines, the value line and top links, ex:

            /  \
            0  1

        Right link is escaped to be printed, so '\\'.
        """
        # No child.
        if self.is_leaf():
            val = str(self.value)
            width = len(val) # in case of large number or string or expression, centers the value by setting the link in its middle.
            height = 1
            middle = width // 2 
            return Coordinates([val], width, height, middle)

        # Only left child.
        if self.right is None:
            child = self.left.generate()
            
            val = str(self.value)
            width = len(val)
            
            # fist line: value line, centered with the child as extremity. We draw an horizontal line from the middle of the child to the value.
            first_line = (child.m + 1) * ' ' + (child.w - child.m - 1) * '_' + val
            # second line: draws one vertical line from the middle of the child value.
            second_line = child.m * ' ' + '/' + (child.w - child.m - 1 + width) * ' '

            shifted_lines = [v + width * ' ' for v in child.v] # Shifts the value beneath to adjust for node value length.

            # Updates the array of lines to print with the 2 new lines generated, and the new coordinates width, height and middle updated.
            return Coordinates([first_line, second_line] + shifted_lines, child.w + width, child.h + 2, child.w + width // 2)

        # Only right child.
        elif self.left is None:
            child = self.right.generate()
            
            val = str(self.value)
            width = len(val)
            
            first_line = val + child.m * '_' + (child.w - child.m) * ' '
            second_line = (width + child.m) * ' ' + '\\' + (child.w - child.m - 1) * ' '

            shifted_lines = [width * ' ' + v for v in child.v]

            return Coordinates([first_line, second_line] + shifted_lines, child.w + width, child.h + 2, width // 2)

        # Two children.
        else:
            left = self.left.generate()
            right = self.right.generate()

            val = str(self.value)
            width = len(val)

            first_line = (left.m + 1) * ' ' + (left.w- left.m - 1) * '_' + val + right.m * '_' + (right.w - right.m) * ' '
            second_line = left.m * ' ' + '/' + (left.w - left.m - 1 + width + right.m) * ' ' + '\\' + (right.w - right.m - 1) * ' '
            
            if left.h < right.h:
                left.v += [left.w * ' '] * (right.h - left.h)
            elif right.h < left.h:
                right.v += [right.w * ' '] * (left.h - right.h)
            
            zipped_lines = zip(left.v, right.v)
            lines = [first_line, second_line] + [a + width * ' ' + b for a, b in zipped_lines]

            return Coordinates(lines, left.w + right.w + width, max(left.h, right.h) + 2, left.w + width // 2)


# ----------- Utility -----------
def str(val) -> str:
    "Converts a value to String safely."
    return '%s' % val # '%s' % value is analog to String.format() in Java. Concatenates string and automatically convert type.
