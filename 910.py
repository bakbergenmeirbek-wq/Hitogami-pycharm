# def analyze_text(text):
#     vowels = "aeiouy"
#     text = text.lower()
#
#     cleaned = ""
#     for ch in text:
#         if ch.isalpha() or ch == " ":
#             cleaned += ch
#
#     unique_vowels = ""
#     words = []
#     current = ""
#
#     for ch in cleaned:
#         if ch in vowels and ch not in unique_vowels:
#             unique_vowels += ch
#
#         if ch != " ":
#             current += ch
#         else:
#             if current:
#                 words.append(current)
#                 current = ""
#
#     if current:
#         words.append(current)
#
#     result = []
#     for w in words:
#         if len(w) >= 5 and w[0] == w[-1] and w not in result:
#             result.append(w)
#
#     return len(unique_vowels), " ".join(result)



#2
# process_text = lambda text: " ".join(
#     filter(
#         lambda w: len(w) % 2 == 0,
#         map(
#             lambda w: w[::-1],
#             filter(
#                 lambda w: not any(ch.isdigit() for ch in w),
#                 text.split()
#             )
#         )
#     )
# )

#3
# def top_k_words(text, k):
#     text = text.lower()
#
#     cleaned = ""
#     for ch in text:
#         if ch.isalpha() or ch == " ":
#             cleaned += ch
#
#     words = []
#     current = ""
#     for ch in cleaned:
#         if ch != " ":
#             current += ch
#         elif current:
#             words.append(current)
#             current = ""
#     if current:
#         words.append(current)
#
#     counts = {}
#     for w in words:
#         counts[w] = counts.get(w, 0) + 1
#
#     items = list(counts.items())
#     items.sort(key=lambda x: (-x[1], x[0]))
#
#     result = []
#     for i in range(min(k, len(items))):
#         result.append(items[i][0])
#
#     return result

#4
# process_words = lambda text: " ".join(
#     map(
#         lambda w: w.lower(),
#         filter(
#             lambda w: sum(1 for c in w if c.isupper()) == 1
#             and not w[0].isupper()
#             and not w[-1].isupper(),
#             text.split()
#         )
#     )
# )

#5
# def compress_text(text):
#     if not text:
#         return ""
#
#     result = ""
#     count = 1
#
#     for i in range(1, len(text)):
#         if text[i].lower() == text[i - 1].lower():
#             count += 1
#         else:
#             if count > 1:
#                 result += text[i - 1] + str(count)
#             else:
#                 result += text[i - 1]
#             count = 1
#
#     if count > 1:
#         result += text[-1] + str(count)
#     else:
#         result += text[-1]
#
#     return result

#6
# filter_words = lambda text: list(
#     filter(
#         lambda w: len(w) >= 4 and w.isalpha() and len(set(w)) == len(w),
#         text.split()
#     )
# )

#7
# def palindrome_words(text):
#     cleaned = ""
#     for ch in text:
#         if ch.isalpha() or ch == " ":
#             cleaned += ch.lower()
#     words, current = [], ""
#     for ch in cleaned:
#         if ch != " ":
#             current += ch
#         elif current:
#             words.append(current)
#             current = ""
#     if current:
#         words.append(current)
#     palindromes = []
#     for w in words:
#         if len(w) >= 3 and w == w[::-1] and w not in palindromes:
#             palindromes.append(w)
#     for i in range(len(palindromes)):
#         for j in range(i + 1, len(palindromes)):
#             if len(palindromes[i]) < len(palindromes[j]) or \
#                (len(palindromes[i]) == len(palindromes[j]) and palindromes[i] > palindromes[j]):
#                 palindromes[i], palindromes[j] = palindromes[j], palindromes[i]
#     return palindromes
#idu make with gpt(


#8
# process_vowels = lambda text: " ".join(
#     map(
#         lambda w: w if any(ch.isdigit() for ch in w) else ("VOWEL" if w[0].lower() in "aeiouy" else "CONSONANT"),
#         text.split()
#     )
# )

#9
# def alternate_case_blocks(text, n):
#     result = ""
#     i = 0
#     block_num = 0
#     while i < len(text):
#         block = text[i:i+n]
#         if block_num % 2 == 0:
#             result += block.upper()
#         else:
#             result += block.lower()
#         i += n
#         block_num += 1
#     return result

#10
# count_words = lambda text: sum(1 for w in text.split() if any(c.isdigit() for c in w) and not w[0].isdigit() and len(w) >= 5)

#11
# def common_unique_chars(s1, s2):
#     s2_chars = set(s2)
#     result = ""
#     for ch in s1:
#         if ch in s2_chars and ch.isalpha() and ch not in result:
#             result += ch
#     return result

#12
# filter_words = lambda text: list(
#     filter(
#         lambda w: len(w) > 3 and w[0].lower() == w[-1].lower() and w.lower() != w[::-1].lower(),
#         text.split()
#     )
# )

#13
# def replace_every_nth(text, n, char):
#     result = ""
#     i = 0
#     while i < len(text):
#         # определяем границы слова
#         if text[i].isalpha():
#             start = i
#             while i < len(text) and text[i].isalpha():
#                 i += 1
#             word_len = i - start
#             for j in range(start, start + word_len):
#                 if word_len >= 3 and (j - start + 1) % n == 0:
#                     result += char
#                 else:
#                     result += text[j]
#         else:
#             # для пробелов, цифр и других символов просто добавляем
#             result += text[i]
#             i += 1
#     return result
# helped gpt

#14
# process_words = lambda text: ",".join(
#     w for w in text.split()
#     if len(set(w.lower())) > 3 and all(w.lower().count(v) <= 1 for v in "aeiouy")
# )

#16
# def transform_list(nums):
#     result = []
#     for n in nums:
#         if n < 0:
#             continue
#         if n % 2 == 0:
#             result.append(n**2)
#         elif n > 10:
#             result.append(sum(int(d) for d in str(n)))
#         else:
#             result.append(n)
#     return result

#17
# process_numbers = lambda nums: list(
#     map(
#         lambda x: x**2,
#         filter(
#             lambda x: (x % 3 == 0 or x % 5 == 0) and x % 15 != 0 and len(str(abs(x))) % 2 == 1,
#             nums
#         )
#     )
# )

#19
# common_even = lambda lst1, lst2: [x for x, y in zip(lst1, lst2) if x == y and x % 2 == 0]

#20
# def max_subarray_sum(nums, k):
#     max_sum = None
#     for i in range(len(nums) - k + 1):
#         sub = nums[i:i+k]
#         if all(x > 0 for x in sub):
#             s = sum(sub)
#             if max_sum is None or s > max_sum:
#                 max_sum = s
#     return max_sum
#by gpt

#21
# filter_strings = lambda lst: [s.upper() for s in lst if s.isalpha() and len(s) > 4 and len(set(s.lower())) == len(s)]

#22
# def group_by_parity_and_sort(nums):
#     even = []
#     odd = []
#     for n in nums:
#         if n % 2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)
#     even.sort()
#     odd.sort()
#     return even + odd

#23
# is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
# select_odd_prime_index = lambda lst: [x for i, x in enumerate(lst) if is_prime(i) and x % 2 == 1 and x > sum(lst)/len(lst)]


#24
# def longest_increasing_sublist(nums):
#     if not nums:
#         return []
#     max_sub = current_sub = [nums[0]]
#     for i in range(1, len(nums)):
#         if nums[i] > nums[i-1]:
#             current_sub.append(nums[i])
#         else:
#             if len(current_sub) > len(max_sub):
#                 max_sub = current_sub
#             current_sub = [nums[i]]
#     if len(current_sub) > len(max_sub):
#         max_sub = current_sub
#     return max_sub

#25
# avg_of_sublists = lambda lst: [sum(sub)/len(sub) for sub in lst if len(sub) >= 3 and sum(sub) % 2 == 0]

# 26
# def remove_duplicates_keep_last(nums):
#     seen = set()
#     result = []
#     for n in reversed(nums):
#         if n not in seen:
#             seen.add(n)
#             result.append(n)
#     return list(reversed(result))
#
# 27
# sort_strings = lambda lst: sorted(lst, key=lambda s: (-len(s), s))[:5]
#
# 28
# def moving_average(nums, k):
#     result = []
#     for i in range(len(nums)-k+1):
#         window = nums[i:i+k]
#         if all(x >= 0 for x in window):
#             result.append(sum(window)/k)
#     return result
#
# 29
# filter_list = lambda a, b: [x for x in a if x not in b and x > sum(a)/len(a)]
#
# 30
# def analyze_strings_list(words):
#     seen = set()
#     result = []
#     for w in words:
#         if any(c.isdigit() for c in w):
#             continue
#         if len(w) % 2 == 0:
#             w_new = w[::-1]
#         else:
#             w_new = w.upper()
#         if w_new not in seen:
#             seen.add(w_new)
#             result.append(w_new)
#     return result