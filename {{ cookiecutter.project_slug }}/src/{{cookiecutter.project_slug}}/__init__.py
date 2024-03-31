"""{{ cookiecutter.project_name }}"""
__version__ = '{{ cookiecutter.version }}'


import os

src_path = os.path.dirname( os.path.abspath(__file__))
root_absolute_path = os.path.abspath(os.path.join(src_path, os.pardir))
