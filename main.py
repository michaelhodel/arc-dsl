import os
import json
import inspect
import tqdm

import arc_types
import constants
import dsl
import tests
import solvers



def get_data(train=True):
    path = f'../data/{"training" if train else "evaluation"}'
    data = {}
    for fn in os.listdir(path):
        with open(f'{path}/{fn}') as f:
            data[fn.rstrip('.json')] = json.load(f)
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_functions(path):
    """ returns a list of available functions """
    with open(path, 'r') as f:
        code = f.read()
    functions = []
    for row in code.split('\n'):
        if row.startswith('def '):
            function = row.split('def ')[1].split('(')[0]
            functions.append(function)
    return functions


def run_dsl_tests(dsl_module, test_module):
    """ test DSL primitives """
    dsl_functions = get_functions(dsl_module.__file__)
    test_functions = get_functions(test_module.__file__)
    expected = set([f'test_{f}' for f in dsl_functions])
    assert set(test_functions) == expected
    for fun in test_functions:
        getattr(test_module, fun)()


def test_solvers_formatting(solvers_module, dsl_module):
    """ tests the implementd solvers for formatting """
    with open('constants.py', 'r') as f:
        constants = [c.split(' = ')[0] for c in f.readlines() if ' = ' in c]
    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in get_functions(solvers_module.__file__)
    }
    dsl_interface = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)
    for key, definition in definitions.items():
        try:
            lines = definition.split('\n')
            assert lines[0] == f'def {key}(I):'
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for line in lines[1:-2]:
                variable, call = line.lstrip().split(' = ')
                function, args = call.split('(')
                assert variable not in dsl_interface
                assert variable not in variables
                assert call not in calls
                variables.add(variable)
                calls.add(call)
                assert function in dsl_interface or function in variables
                assert args[-1] == ')'
                args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
                for arg in args:
                    assert any([
                        arg in variables, arg in dsl_interface,
                        arg in constants, arg == 'I'
                    ])
            for v in variables:
                assert sum([
                    definition.count(vs) for vs in [
                        f'({v})', f'({v}, ', f', {v})',
                        f', {v}, ', f' {v} = ', f' {v}('
                    ]
                ]) > 1 or v == 'O'
            n_correct += 1
        except:
            pass
    print(f'{n_correct} out of {n} solvers formatted correctly.')


def test_solvers_correctness(data, solvers_module):
    """ tests the implemented solvers for correctness """
    n_correct = 0
    n = len(data["train"])
    for key in tqdm.tqdm(data['train'].keys(), total=n):
        task = data['train'][key] + data['test'][key]
        try:
            solver = getattr(solvers_module, f'solve_{key}')
            for ex in task:
                assert solver(ex['input']) == ex['output']
            n_correct += 1
        except:
            pass
    print(f'{n_correct} out of {n} tasks solved correctly.')


def main():
    data = get_data(train=True)
    run_dsl_tests(dsl, tests)
    test_solvers_formatting(solvers, dsl)
    test_solvers_correctness(data, solvers)


if __name__ == '__main__':
    main()
