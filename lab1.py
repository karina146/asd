def checking_brackets(line):
    if not line:
        return "Строка не существует"

    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for bkt in line:
        if bkt in "([{":
            stack.append(bkt)
        elif bkt in ")]}":
            if not stack or stack[-1] != brackets[bkt]:
                return "Строка не существует"
            stack.pop()
        else:
            return "Недопустимые символы"

    if not stack:
        return "Строка существует"
    else:
        return "Строка не существует"


line = input(" ")
print(checking_brackets(line))
