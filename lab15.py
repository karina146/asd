def parse_tree(s):
    s = s.replace(" ", "")
    idx = 0

    def parse_node():
        nonlocal idx

        num = ""
        while idx < len(s) and s[idx].isdigit():
            num += s[idx]
            idx += 1

        if not num:
            return None

        node = [int(num), None, None]


        if idx >= len(s) or s[idx] != "(":
            return node

        idx += 1 

        
        if s[idx] != ",":
            node[1] = parse_node()

        
        if idx < len(s) and s[idx] == ",":
            idx += 1

        
        if s[idx] != ")":
            node[2] = parse_node()

        idx += 1 
        return node

    return parse_node()



def preorder(node):   # NLR
    if node is None:
        return []
    return [node[0]] + preorder(node[1]) + preorder(node[2])


def inorder(node):    # LNR
    if node is None:
        return []
    return inorder(node[1]) + [node[0]] + inorder(node[2])


def postorder(node):  # LRN
    if node is None:
        return []
    return postorder(node[1]) + postorder(node[2]) + [node[0]]


tree = parse_tree("8(3(1,6(4,7)),10(,14(13,)))")

print("Прямой     :", preorder(tree))
print("Центральный:", inorder(tree))
print("Концевой   :", postorder(tree))

