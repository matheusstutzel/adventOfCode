defmodule P03 do
	def calc(input)do
		Regex.scan(~r/mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don\'t\(\)/, input, [])
		|> Enum.reduce([0,:true], fn x, [sum, enabled]->case [x, enabled] do
		[["don't()"],_] -> [sum,:false]
		[["do()"],_] -> [sum, :true]
		[_,:false] -> [sum,enabled]
		[[_, a,b],:true] -> [sum+ (String.to_integer(a)*String.to_integer(b)), enabled]		
		end end)
		|> hd
		
	end
end

IO.read(:stdio, :eof)
|> P03.calc
|> IO.inspect
