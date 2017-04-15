
from ex02_counting_characters import char_count

s = input("Enter a string, please: ")

print("By len(), string '{s}' is {len} characters".format(s=s, len=char_count.by_len(s)))
print("By counting, string '{s}' is {len} characters".format(s=s, len=char_count.by_counting(s)))
print("By reducing, string '{s}' is {len} characters".format(s=s, len=char_count.by_reduce(s)))
