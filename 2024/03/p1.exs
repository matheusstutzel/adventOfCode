defmodule P03 do
  def calc(input) do
    Regex.scan(~r/mul\(([0-9]{1,3}),([0-9]{1,3})\)/, input, [])
    # |> IO.inspect
    |> Enum.map(fn [_, a, b] -> String.to_integer(a) * String.to_integer(b) end)
    # |> IO.inspect
    |> Enum.sum()
  end
end

IO.read(:stdio, :eof)
|> P03.calc()
|> IO.inspect()
