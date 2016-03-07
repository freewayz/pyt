import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
from ast import parse

from pyt.vars_visitor import VarsVisitor


class LabelVisitorTestCase(unittest.TestCase):
    '''Baseclass for LabelVisitor tests'''

    def perform_vars_on_expression(self, expr):
        obj = parse(expr)
        vars = VarsVisitor()
        vars.visit(obj)

        return vars

class LabelVisitorTest(LabelVisitorTestCase):
    def test_assign_var_and_num(self):
        vars = self.perform_vars_on_expression('a = 1')
        self.assertEqual(vars.result,['a'])

    def test_assign_var_and_var(self):
        vars = self.perform_vars_on_expression('a = x')
        self.assertEqual(vars.result,['a','x'])

    def test_call(self):
        vars = self.perform_vars_on_expression('print(x)')
        self.assertEqual(vars.result,['x'])

    def test_keyword_vararg(self):
        vars = self.perform_vars_on_expression('print(arg = x)')
        self.assertEqual(vars.result,['x'])

    def test_keyword_numarg(self):
        vars = self.perform_vars_on_expression('print(arg = 1)')
        self.assertEqual(vars.result,[])