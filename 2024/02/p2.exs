defmodule P02 do
  def parse(s) do
    s
    |> String.split(" ", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def diff(y) do
	#IO.inspect(y)
    y
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.map(fn [x, y] -> x - y end)
    |> Enum.into(MapSet.new)
  end

  def valid(y) do
  	x= diff(y)
#  	|> IO.inspect
  	safe(x, MapSet.new([1,2,3])) or safe(x, MapSet.new([-1,-2,-3]))
  end

  def safe(x,y) do
  	MapSet.size(MapSet.difference(x,y)) ==0
  end
  def validWithSkip(y, -1) do
  	valid(y) or validWithSkip(y, 0)
  end

  def validWithSkip(y, n) do
  	if n>=length(y) do
  		false
  	else
  		valid(Enum.concat(Enum.slice(y,0, n),Enum.slice(y, (n+1)..length(y)))) or validWithSkip(y, n+1)
  	end
  end

  def calc(y) do
  	validWithSkip(y, -1)  	
  end
end

x = IO.read(:stdio, :eof)
|> String.split("\n", trim: true)
#|> IO.inspect()
|> Enum.map(&P02.parse/1)
|> Enum.map(&P02.calc/1)
#|> IO.inspect()


IO.inspect(Enum.count(x, & &1))
