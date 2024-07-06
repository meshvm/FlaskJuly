# # [1,2,3,[4,5,[6,7],[8,9,[10,11]]]]
# 
# 
# res_list =[]
# def demo_fun():
#     demo_list = [1, 2, 3, [4, 5, [6, 7], [8, 9, [10, 11]]]]
#     while type(demo_list)==list:
#         for ele in demo_list:
#             if type(ele) != list:
#                 print(ele)
#             elif type(ele) == list:
#                 n=ele
#                 return
#
# demo_fun()
# 
# 
# # # print(out)
# def parse_nested_list(nested_list):
#     tree = {}
#     def add_nodes(lst, parent=None):
#         for item in lst:
#             if isinstance(item, list):
#                 add_nodes(item, current)
#             else:
#                 current = item
#                 tree[current] = parent
#     add_nodes(nested_list)
#     return tree
#
# nested_list = [1, 2, 3, [4, 5, [6, 7], [8, 9, [10, 11]]]]
# tree = parse_nested_list(nested_list)
# for node, parent in tree.items():
#     print(f"Node: {node}, Parent: {parent}")


def demo_fun():
    demo_list = [1, 2, 3, [4, 5, [6, 7], [8, 9, [10, 11]]]]
    stack = [demo_list]  # Initialize stack with the outermost list

    while stack:
        current_list = stack.pop()
        for ele in current_list:
            if isinstance(ele, list):
                stack.append(ele)  # Push nested lists onto the stack
            else:
                print(ele)

demo_fun()