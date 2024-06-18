n = int(input())
s = input()

max_common_chars = 0

# 各切断位置で共通の文字の種類数を計算
for i in range(n):
    left_part = s[:i]
    right_part = s[i:]
    
    left_set = set(left_part)
    right_set = set(right_part)
    #intersectionはleft_setとright_setの共通部分をはじき出す関数
    #入力例
    """
    set1 = {'a', 'b', 'c'}
    set2 = {'b', 'c', 'd'}
    set1.itersection(set2)
    """
    #出力例
    """
    出力: {'b', 'c'}
    """
    common_chars = left_set.intersection(right_set)
    max_common_chars = max(max_common_chars, len(common_chars))

print(max_common_chars)
