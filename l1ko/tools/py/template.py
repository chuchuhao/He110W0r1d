# -*- coding: utf-8 -*-
# !/usr/bin/env python3

"""
{title}

{question}

{example}

Source : {Source}
Date : {Date}
"""

import unittest
from collections import namedtuple

TestCase = namedtyple('TestCase', ['in', 'out'])

class Solution:
	def solution(self):
		pass

class SolutionTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_solution_function(self):
		s = Solution()

		testCases = [TestCase([1,2,3], 2)]
		for testCase in testCases:
			self.assertEqual(s.solution(testCase.x), testCase.y)
		
if __name__ == '__main__':
	unittest.main()

