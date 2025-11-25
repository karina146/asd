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

def preorder_iter(root):
    if root is None:
        return ""

    stack = [root]
    result = []

    while stack:
        node = stack.pop()

        result.append(str(node[0]))

        if node[2] is not None:
            stack.append(node[2])
        if node[1] is not None:
            stack.append(node[1])

    return " ".join(result)


tree = parse_tree("8(3(1,6(4,7)),10(,14(13,)))")


print("Нерекурсивный прямой обход:", preorder_iter(tree))


