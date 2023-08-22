# Domain Specific Language for the Abstraction and Reasoning Corpus (ARC-DSL)

The DSL was created with the aim of being expressive enough to allow programs solving arbitrary ARC tasks, and generic, i.e. consisting of only few primitives, each useful for many tasks (see [`dsl.py`](dsl.py)). As a proof of concept, solver programs for the training tasks were written (see [`solvers.py`](solvers.py)). See [`arc_dsl_writeup.pdf`](arc_dsl_writeup.pdf) for a more detailed description of the work.


## Example solver program for task 00d62c1b written in the DSL

![Tux, the Linux mascot](00d62c1b.png)

```python
def solve_00d62c1b(I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = mfilter(x2, x4)
    O  = fill(I, FOUR, x5)
    return O
```

The function `solve_00d62c1b` takes an input grid `I` and returns the correct output grid `O`. An explanation of what the variables store and how their values were computed:

- `x1`: the set of objects extracted from the input grid `I` that are single-colored only, where individual objects may only have cells that are connected directly, and cells may be of the background color (black); the result of calling the `objects` primitive on `I` with `univalued=True`, `diagonal=False` and `without_background=True`
- `x2`: the subset of the objects `x1` which are black; the result of filtering objects by their color, i.e. calling `colorfilter` with `objects=x1` and `color=ZERO` (black)
- `x3`: a function with signature $f: object \rightarrow bool$ that returns `True` iff an object is at the border of the grid; the result of fixing the right argument of the `bordering` primitive to `I` by calling the function `rbind` on `function=bordering` and `fixed=I`
- `x4`: a function that returns the inverse of the previous function, i.e. a function that returns `True` iff an object does not border the grid border; the result of composing the `flip` primitive (which simply negates flips a boolean) and `x3`
- `x5`: a single object defined as the union of objects `x2` for which function `x4` returns `True`, i.e. the black objects which do not border the grid border (corresponding to the "holes" in the green objects); the result of calling `mfilter` (which combines `merge` and `filter`) with `container=x2` and `condition=x4`
- `O`: the output grid, created by coloring all pixels of the object `x5` yellow; the result of calling the `fill` primitive on `I` with `color=FOUR` (yellow) and `patch=x5`
