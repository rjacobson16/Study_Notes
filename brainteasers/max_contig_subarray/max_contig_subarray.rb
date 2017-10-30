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

puts max_sub_array2([-2,1,-3,4,-1,2,1,-5,4])
