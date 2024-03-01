# Domain Specific Language for the Abstraction and Reasoning Corpus (ARC-DSL)

The DSL was created with the aim of being expressive enough to allow programs solving arbitrary ARC tasks, and generic, i.e. consisting of only few primitives, each useful for many tasks (see [`dsl.py`](dsl.py)). As a proof of concept, solver programs for the training tasks were written (see [`solvers.py`](solvers.py)). See [`arc_dsl_writeup.pdf`](arc_dsl_writeup.pdf) for a more detailed description of the work.


## Example solver program for task 00d62c1b written in the DSL

![Task 00d62c1b](00d62c1b.png)

```python
def solve_00d62c1b(I):
    objs = objects(grid=I, univalued=T, diagonal=F, without_bg=F)
    black_objs = colorfilter(objs=objs, value=ZERO)
    borders = rbind(function=bordering, fixed=I)
    does_not_border = compose(outer=flip, inner=borders)
    enclosed = mfilter(container=black_objs, function=does_not_border)
    O = fill(grid=I, value=FOUR, patch=enclosed)
    return O
```

The function `solve_00d62c1b` takes an input grid `I` and returns the correct output grid `O`. An explanation of what the variables store and how their values were computed:

- `objs`: the set of objects extracted from the input grid `I` that are single-color only, where individual objects may only have cells that are connected directly, and cells may be of the background color (black); the result of calling the `objects` primitive on `I` with `univalued=True`, `diagonal=False` and `without_background=True`
- `black_objs`: the subset of the objects `objs` which are black; the result of filtering objects by their color, i.e. calling `colorfilter` with `objects=objs` and `color=ZERO` (black)
- `borders`: a function taking an object and returning `True` iff that object is at the border of the grid; the result of fixing the right argument of the `bordering` primitive to `I` by calling the function `rbind` on `function=bordering` and `fixed=I`
- `does_not_border`: a function that returns the inverse of the previous function, i.e. a function that returns `True` iff an object does not touch the grid border; the result of composing the `flip` primitive (which simply negates a boolean) and `borders`
- `enclosed`: a single object defined as the union of objects `black_objs` for which function `does_not_border` returns `True`, i.e. the black objects which do not touch the grid border (corresponding to the "holes" in the green objects); the result of calling `mfilter` (which combines `merge` and `filter`) with `container=black_objs` and `condition=does_not_border`
- `O`: the output grid, created by coloring all pixels of the object `enclosed` yellow; the result of calling the `fill` primitive on `I` with `color=FOUR` (yellow) and `patch=enclosed`


## Another solver example: 5521c0d9

![Task 5521c0d9](5521c0d9.png)

```python
def solve_5521c0d9(I):
    objs = objects(grid=I, univalued=T, diagonal=F, without_bgT)
    foreground = merge(containers=objs)
    empty_grid = cover(grid=I, patch=foreground)
    offset_getter = chain(h=toivec, g=invert, f=height)
    shifter = fork(outer=shift, a=identity, b=offset_getter)
    shifted = mapply(function=shifter, container=objs)
    O = paint(grid=empty_grid, obj=shifted)
    return O
```

- `objs`: the set of objects extracted from the input grid `I` that are single-color only, ignoring the background color; the result of calling the `objects` primitive on `I` with `univalued=True`, `diagonal=False` and `without_background=True`
- `foreground`: all the objects treated as a single object, the result of calling the `merge` primitive on the objects `objs`
- `empty_grid`: a new grid, where `foreground` is removed (covered), i.e. replaced with the background color (black); the result of calling the `cover` primitive with `grid=I` and `patch=foreground`
- `offset_getter`: a function that takes an object and returns a vector pointing up by as much as that object is high; the result of composing the three functions `toivec`, `invert` and `height`; the result of calling the `chain` primitive with `h=toivec`, `g=invert` and `f=height`
- `shifter`: a function that takes an object and shifts it as much upwards as it is high; the result of calling the `fork` primitive with `outer=shift`, `a=identity` and `b=offset_getter`
- `shifted`: all the objects shifted up by their heights, as a single object, obtained by appling the constructed function on the set of objects and merging the results; the result of calling the `mapply` primitive on `function=shifter` and `container=objs`
- `O` the desired output grid, obtained by painting the resulting object onto the grid `empty_grid` where the original objects were removed from; the result of calling the `paint` primitive on `grid=empty_grid` and `obj=shifted`
