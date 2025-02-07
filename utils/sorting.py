def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  return merge(merge_sort(left), merge_sort(right))

def merge(left_arr, right_arr):
  merged = []
  i, j = 0, 0

  while i < len(left_arr) and j < len(right_arr):
    if  left_arr[i] <= right_arr[j]:
      merged.append(left_arr[i])
      i += 1
    else:
      merged.append(right_arr[j])
      j += 1

  if i < len(left_arr):
    merged.extend(left_arr[i:])
  if j < len(right_arr):
    merged.extend(right_arr[j:])

  return merged

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

  return arr  

def timsort(arr):
  return sorted(arr)