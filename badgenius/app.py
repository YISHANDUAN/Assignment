import random
def S40_to_20(S):
    ans = ''
    for i in range(0, len(S), 2):
        ans += mapping[S[i:i+2]]

    return ans


def S20_to_40(S):
    ans = ''
    for i in range(0, len(S)):
        ans += demapping[S[i]]

    return ans

mapping = {
    'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
    'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
    'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
    'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
}


demapping = {
    'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad',
    'E': 'ba', 'F': 'bb', 'G': 'bc', 'H': 'bd',
    'I': 'ca', 'J': 'cb', 'K': 'cc', 'L': 'cd',
    'M': 'da', 'N': 'db', 'O': 'dc', 'P': 'dd'
}
res = ''.join(random.choice('abcd') for _ in range(40))

code_res = S40_to_20(res)
print("Before encoding:  ", res)
print("length: ", len(res))

print("after encoding:  ", code_res)
print("length: ", len(code_res))

code_res = S20_to_40(code_res)
print("after decoding:  ", code_res)
print("length: ", len(code_res))