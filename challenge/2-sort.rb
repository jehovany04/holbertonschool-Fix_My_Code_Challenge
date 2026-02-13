#!/usr/bin/env ruby
# sorts a list of integers given as arguments

nums = ARGV.map(&:to_i)
puts nums.sort.join(' ')
