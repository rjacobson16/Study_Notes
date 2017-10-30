## Instructions:

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,
the contiguous subarray `[4,-1,2,1]` has the largest sum = 6.

## Solutions & Explanation

### Naive Solution

```
def max_sub_array(nums)
 subarrays = { }
 nums.each_index do |i|
   j = i+1
   while j < nums.length
     subarr = nums[i..j]
     subarrays[subarr] = subarr.inject(&:+)
     j+=1
   end
 end
    result = subarrays.max_by {|k,v| v}

    "The largest continuous subarray is #{result[0]}, which sums to #{result[1]}"
end

puts max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
# => "The largest continuous subarray is [4, -1, 2, 1], which sums to 6"
```

Here, we find all of the contiguous subarrays and then picking out the one that results in the largest sum.

The nested loop means that we iterate through the entire array `array.length` times for each element in the array, which takes O(n^2) time.

### Dynamic Programming Solution (Kadane's Algorithm)

```
def max_sub_array2(nums)
  max_so_far = nums[0]
  max_ending_here = 0
  start_idx, end_idx, current_idx = 0, 0, 0

  nums.each_with_index do |n, i|
    max_ending_here += n
    if max_ending_here < 0
      max_ending_here = 0
      current_idx = i+1
    end

    if max_so_far < max_ending_here
      max_so_far = max_ending_here
      start_idx = current_idx
      end_idx = i
    end
  end

  "The largest continuous subarray is #{nums[start_idx..end_idx]}, which sums to #{max_so_far}"
end
```

Here, we loop through the array only once, resulting in O(n) time complexity.

Kadane's algorithm works by looping through the array and keeping track of the maximum sum, as well as the start and ending indices of the sub-array yielding that sum. At each step, we check to see if the current sum (`max_ending_here`) is greater than the maximum sum (`max_so_far`), and if so, we re-assign the maximum sum to the current sum. If the current sum (`max_ending_here`) is < 0, we know that the current sum will never contribute to our maximum sum, and we reset the current sum to 0. 
