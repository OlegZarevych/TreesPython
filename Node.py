class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
  
  def search(self, target):
    if self.data == target:
        print('Found target {target}')
        return self

    if self.left and self.data > target:
      return self.left.search(target)

    if self.right and self.data < target:
        return self.right.search(target)

    print('Value is not in tree')

  def traverse_pre_order(self):
    print(self.data)
    if self.left:
      self.left.traverse_pre_order()
    
    if self.right:
      self.right.traverse_pre_order()

  def traverse_in_order(self):
    if self.left:
      self.left.traverse_pre_order()
    print(self.data)    
    if self.right:
      self.right.traverse_pre_order()

  def traverse_post_order(self):
    if self.left:
      self.left.traverse_pre_order()

    if self.right:
      self.right.traverse_pre_order()
    print(self.data)    

  def height(self, h = 0):
    left_height = self.left.height(h + 1) if self.left else h
    right_height = self.right.height(h + 1) if self.right else h
    return max(left_height, right_height)

  def get_nodes_at_depth(self, depth, nodes = []):
    if depth == 0:
      nodes.append(self.data)
      return nodes
    
    if self.left:
      self.left.get_nodes_at_depth(depth - 1, nodes)
    else:
      nodes.extend([None]*2**(depth-1))
    if self.right:
      self.right.get_nodes_at_depth(depth - 1, nodes)
    else:
      nodes.extend([None]*2**(depth-1))
    return nodes

  def add(self, data):
    if self.data == data:
        return

    if self.left and self.data > data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.add(data)

    if self.right and self.data < data:
       if self.right is None:
         self.right = Node(data)
       else:
         self.right.add(data)

    print('Value is not in tree')