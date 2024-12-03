defmodule P02 do
  def parse(s) do
    s
    |> String.split(" ", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def diff(y) do
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


  def calc(y) do
  	valid(y)
  end
end

x = IO.read(:stdio, :eof)
|> String.split("\n", trim: true)
#|> IO.inspect()
|> Enum.map(&P02.parse/1)
|> Enum.map(&P02.calc/1)
#|> IO.inspect()


IO.inspect(Enum.count(x, & &1))
