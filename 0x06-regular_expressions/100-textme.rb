#!/usr/bin/env ruby
ars1 = ARGV[0].match(/\[from:(.*?)\]/).captures
ars2 = ARGV[0].match(/\[to:(.*?)\]/).captures
ars3 = ARGV[0].match(/\[flags:(.*?)\]/).captures

puts [ars1, ars2, ars3].reject(&:empty?).join(' ')
