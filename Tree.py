from Node import *

class Tree:
  def __init__(self, root, name = ''):
    self.root = root
    self.name = name

  def search(self, target):
      return self.root.search(target)

  def traverse_pre_order(self):
      return self.root.traverse_pre_order()

  def traverse_in_order(self):
      return self.root.traverse_in_order()

  def traverse_post_order(self):
      return self.root.traverse_post_order()

  def get_height(self):
      return self.root.height()

  def get_nodes_at_depth(self, depth):
      return self.root.get_nodes_at_depth(depth)

  def _nodeToChar(self, n, spacing):
      if n is None:
          return '_' + (' '*spacing)
      spacing = spacing - len(str(n)) + 1
      return str(n)+(' '*spacing)
  
  def print(self):
      print ('Tree name:', self.name)
      height = self.get_height()
      # Calculate how much spaces we need for pretty output
      spacing = 3
      width = int((2**height-1) * (spacing+1) + 1)
      offset = int((width-1)/2)
      for depth in range(0, height+1):
          if depth > 0:
              print(' '*(offset+1) + (' '*(spacing*2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
          row = self.root.get_nodes_at_depth(depth, [])
          print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
          spacig = offset + 1
      print('')

  def add(self, data):
    self.root.add(data)

  def delete(self, data):
    self.root = self.root.delete(data)

  def rebalance(self):
    self.root.rebalance()
    self.root = self.root.fix_imbalance_if_exist()

