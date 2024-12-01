defmodule P do
  def x(s) do
    s |> Enum.map(&String.to_integer/1)
  end

  def y([h | t]) do
    [a, b] = h
    [tA, tB] = y(t)
    [[a | tA], [b | tB]]
  end

  def y([]) do
    [[], []]
  end

  def calc([[], []]) do
    0
  end

  def calc([[a | ta], [b | tb]]) do
    abs(a - b) + calc([ta, tb])
  end
end

IO.read(:stdio, :eof)
|> String.split("\n")
|> Enum.map(fn x -> String.split(x, "   ") end)
|> Enum.reject(fn x -> x == [""] end)
|> Enum.map(&P.x/1)
|> P.y()
|> Enum.map(&Enum.sort/1)
# |> IO.inspect
|> P.calc()
|> IO.inspect()
