def permute(s)
  out = []

  if s.length == 1
    out = [s]
  end

  s.each_char.with_index do |ch, i|
    permute(s[0...i] + s[i+1..-1]).each do |perm|
      puts "perm is #{perm}"

      out.push(ch + perm)
    end
  end

  out
end

print permute('abc')
