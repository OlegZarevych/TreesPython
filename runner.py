from Tree import * 

if __name__ == '__main__':
    print('Hello from tree')
    node = Node(10)
    node.left = Node(5)
    node.right = Node(15)
    print(node.right.data)
    print('Let\'s check Tree')
    tree = Tree(Node(15))
    tree.root.left = Node(14)
    tree.root.right = Node(16)
    tree.root.left.left = Node(13)
    tree.root.right.right = Node(17)
    tree.root.right.right.right = Node(19)

    print('Pre')
    tree.traverse_pre_order()

    print('In')
    tree.traverse_in_order()

    print('Post')
    tree.traverse_post_order()
    
    print('Tree height is ', tree.get_height())

    tree.print()
    