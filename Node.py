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

  def find_min(self):
    if self.left:
      return self.left.find_min()
    return self.data
  
  def is_balanced(self):
    left_height = self.left.height()+1 if self.left else 0
    right_height = self.right.height()+1 if self.right else 0
    return abs(left_height, right_height) < 2
  
  def get_left_right_height_diff(self):
    left_height = self.left.height()+1 if self.left else 0
    right_height = self.right.height()+1 if self.right else 0
    return left_height - right_height

  def fix_imbalance_if_exist(self):
    if self.get_left_right_height_diff() > 1:
      # left imbalance
      if self.left.get_left_right_height_diff() > 0:
        # left left imbalance
        return rotate_right(self)
      else:
        # left right imbalance
        self.left = rotate_left(self.left)
        return rotate_right(self)
    elif self.get_left_right_height_diff() < -1:
      # right imbalance
      if self.right.get_left_right_height_diff() < 0:
        # right right imbalance
        return rotate_left(self)
      else:
        self.right = rotate_right(self.right)
        return rotate_left(self)
 

  def rebalance(self):
    if self.left:
      self.left.rebalance()
      self.left = self.left.fix_imbalance_if_exist()
    if self.right:
      self.right.rebalance()
      self.right = self.right.fix_imbalance_if_exist()


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

  def delete(self, data):
    if self.data == data:
      if self.left and self.right:
        minValue = self.right.findMin()
        self.data = minValue
        self.right = self.right.delete(minValue)
        return self
      else:
        return self.left or self.right 

    if self.right and data > self.data:
      self.right = self.right.delete(data)
    if self.left and data < self.data:
      self.left = self.left.delete(data)
    return self

def rotate_right(root):
  pivot = root.left
  reattached_node = pivot.right
  root.left = reattached_node
  pivot.right = root
  return pivot

def rotate_left(root):
  pivot = root.right
  reattached_node = pivot.left
  root.right = reattached_node
  pivot.left = root
  return pivot