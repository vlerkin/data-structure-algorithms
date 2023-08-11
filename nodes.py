
# defining class Node that gives access to values but keeps it immutable
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

# defining nodes without links
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# linking nodes
dot.set_link_node(wacko)
yacko.set_link_node(dot)

# accessing data of a node through a linked node
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)