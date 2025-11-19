def check_brackets(expr):
    stack = []
    pairs = {')': '('}
    for bkt in expr:
        if bkt == '(':
            stack.append(bkt)
        elif bkt == ')':
            if not stack or stack[-1] != pairs[bkt]:
                return False
            stack.pop()
    return not stack


def validate_expression(expr):
    allowed = "0123456789+-*/().="
    for ch in expr:
        if ch not in allowed:
            return "Ошибка: недопустимый символ"

    if expr.count('=') != 1 or not expr.endswith('='):
        return "Ошибка: выражение должно заканчиваться знаком '='"

    body = expr[:-1]
    if not body:
        return "Ошибка: выражение отсутствует"

    if not check_brackets(body):
        return "Ошибка: скобки расставлены неверно"

    for i in range(len(body) - 1):
        if body[i] in "+-*/" and body[i + 1] in "+-*/":
            return "Ошибка: два знака подряд"

    if "/0" in body.replace(" ", ""):
        return "Ошибка: деление на ноль"

    return None

def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

def apply_operator(ops, nums):
        op = ops.pop()
        b = nums.pop()
        a = nums.pop()
        if op == '+':
            nums.append(a + b)
        elif op == '-':
            nums.append(a - b)
        elif op == '*':
            nums.append(a * b)
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError
            nums.append(a / b)

def calculate_expression(expr):

    body = expr[:-1]
    nums = []
    ops = []
    i = 0

    while i < len(body):
        ch = body[i]

        if ch == ' ':
            i += 1
            continue

        if ch.isdigit() or ch == '.':
            num = ''
            while i < len(body) and (body[i].isdigit() or body[i] == '.'):
                num += body[i]
                i += 1
            nums.append(float(num))
            continue

        if ch == '(':
            ops.append(ch)
        elif ch == ')':
            while ops and ops[-1] != '(':
                apply_operator(ops, nums)
            ops.pop()
        elif ch in '+-*/':
            while ops and precedence(ops[-1]) >= precedence(ch):
                apply_operator(ops, nums)
            ops.append(ch)
        else:
            return "Ошибка: недопустимый символ"

        i += 1

    while ops:
        apply_operator(ops, nums)

    return nums[0]


def process_expression(expr):
    error = validate_expression(expr)
    if error:
        return error

    try:
        result = calculate_expression(expr)
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception:
        return "Ошибка: некорректное выражение"


expr = input("Введите математическое выражение: ")
print(process_expression(expr))
