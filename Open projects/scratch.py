def depth(tree):
    count = 0
    node_list = []
    while tree:
        for node in tree:
            if node[1] == None:
                pass
            node_list.append(node)
            print(node_list)
            count +=1

            tree.pop(node)
            depth(node_list)
    return count



# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[: mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1:])

    return tree_node


# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1))
print(depth(tree_level_2))
print(depth(tree_level_4))
