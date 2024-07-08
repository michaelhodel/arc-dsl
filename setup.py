from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'ARC-DSL'
LONG_DESCRIPTION = 'Domain Specific Language for the Abstraction and Reasoning Corpus'

setup(
        name="arcdsl",
        version=VERSION,
        author="Michael Hodel",
        author_email="<mihodel@ethz.ch>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['arc', 'arc-dsl'],
)
