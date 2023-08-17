validation = ['()', '(())', '([', '(({{}}))', ')', '(}', ']', '(()', '', '(({{[[]]}}))']

def balanceParens(str: str):
    mapping = {"open": ('([{'),
               "closed": (')]}')}
    stack = []
    for i in str:
        if i in mapping['open']:
            stack.append(i)
        if i in mapping['closed'] and not stack:
            return False
        if i in mapping['closed'] and mapping['open'][mapping['closed'].index(i)] == stack[-1]:
            stack.pop()
    return True if not stack else False

for s in validation:
    print(balanceParens(s))
