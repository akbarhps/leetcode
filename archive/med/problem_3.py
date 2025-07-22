s = "bbbbb"

counter = 0
max_count = 0
cache = {}
for char in s:
   if char in cache:
       max_count = max(max_count, counter)
       cache = {char: True}
       counter = 1
       continue
       
   counter += 1
   cache[char] = True

print(max_count)
