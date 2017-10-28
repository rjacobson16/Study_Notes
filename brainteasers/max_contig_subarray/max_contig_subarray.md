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
