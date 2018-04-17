import cryptoutil as cu

class MerkelNode(object):
    def __init__(self, depth):
        self.hash = ""
        self.left = None
        self.right = None
        self.depth = depth
        if depth < 1:
            raise ValueError("Depth must be positive.")
        if depth > 1:
            self.left = MerkelNode(depth - 1)
            self.right = MerkelNode(depth - 1)


    def update_tree(self):
        if self.depth > 1:
            self.left.update_tree()
            self.right.update_tree()
            self.hash = cu.hash_hex_val((self.left.hash + self.right.hash).encode('utf-8'))


    def get_child(self, num):
        reversed = 0
        while num > 0:
            bit = num&1
            num = num >> 1
            reversed = reversed << 1
            reversed = reversed | bit
        return self.__get_child__(reversed)

    def __get_child__(self, num):
        if num > (2**self.depth) - 1:
            raise ValueError("Nth child is not in tree, tree is not deep enough.")
        if self.depth > 1:
            if num&1 == 1:
                return self.right.get_child(num >> 1)
            else:
                return self.left.get_child(num >> 1)
        return self
