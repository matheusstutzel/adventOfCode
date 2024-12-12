defmodule P11 do
  def calc(_, 0) do
    1
  end

  def calc(0, limit) do
    calc(1, limit - 1)
  end

  def calc(x, limit) do
    case :ets.lookup(:mem, [x, limit]) do
      [{_, v} | _] ->
        # IO.inspect("hit #{x} #{limit} -> #{v}")
        v

      [] ->
        result = do_calc(x, limit)
        # IO.inspect("miss #{x} #{limit} -> #{result}")
        :ets.insert(:mem, {[x, limit], result})
        result
    end
  end

  def do_calc(x, limit) do
    size = round(:math.floor(:math.log10(x)) + 1)

    if rem(size, 2) == 0 do
      mid = div(size, 2)
      calc(div(x, 10 ** mid), limit - 1) + calc(rem(x, 10 ** mid), limit - 1)
    else
      calc(x * 2024, limit - 1)
    end
  end
end

limit = 75
:ets.new(:mem, [:named_table, :public])

IO.read(:stdio, :eof)
|> String.split("\n", trim: true)
|> IO.inspect()
|> Enum.flat_map(fn x -> String.split(x, " ", trim: true) end)
|> Enum.map(&String.to_integer/1)
|> IO.inspect()
|> Enum.map(fn x -> P11.calc(x, limit) end)
|> IO.inspect()
|> Enum.sum()
|> IO.inspect()
