# Michael's DSL for ARC (Abstraction and Reasoning Corpus)

<table>
<tr>
<th>Code</th>
<th>Task</th>
</tr>
<tr>
<td><img src="documents/arc-561rdbcf-code.jpg"></td>
<td><img src="documents/arc-561rdbcf-show.jpg"></td>
</tr>
<tr>
<td><img src="documents/arc-46442a0e-code.jpg"></td>
<td><img src="documents/arc-46442a0e-show.jpg"></td>
</tr>
<tr>
<td><img src="documents/arc-67a423a3-code.jpg"></td>
<td><img src="documents/arc-67a423a3-show.jpg"></td>
</tr>
</table>

Handcrafted solutions for ARC tasks.
You may be wondering what is going on in a particular task, and you can see its implementation.
The [`solvers.py`](solvers.py) has the shortest solutions at the top, and the longest at the bottom.

---

The DSL was created with the aim of being expressive enough to allow programs solving arbitrary ARC tasks, and generic, i.e. consisting of only few primitives, each useful for many tasks (see ```dsl.py```). As a proof of concept, solver programs for the training tasks were written (see ```solvers.py```).

## Repo structure

These are the important files:
* [`arc_types.py`](arc_types.py) - description.
* [`constants.py`](constants.py) - Often used constants.
* [`dsl.py`](dsl.py) - The code for expressing a solution.
* [`main.py`](main.py) - description.
* [`solvers.py`](solvers.py) - description.
* [`test.py`](tests.py) - Testing the DSL is behaving correctly.

## License

MIT.
