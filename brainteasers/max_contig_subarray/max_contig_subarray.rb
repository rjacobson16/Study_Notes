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
