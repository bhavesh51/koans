#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)
        expected_sets = {'MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod'}
        self.assertEqual(expected_sets, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        expected_sets = {1,2,3}
        self.assertEqual(expected_sets, {1, 2, 3})
        self.assertEqual(set(), set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(dict, {}.__class__)

    def test_creating_sets_using_strings(self):
        self.assertEqual(set({'12345'}), {'12345'})
        self.assertEqual({'1','2','3','4','5'}, set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        expected_sets = ['1','2','3','4','5']
        self.assertEqual(expected_sets, sorted(set('12345')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        expected_output1 = {'Willie'}
        expected_output2 = {'Leonidas', 'MacLeod', 'Wallace', 'Willie'}
        expected_output3 = {'MacLeod', 'Wallace'}
        expected_output4 = {'Leonidas', 'Willie'}
        self.assertEqual(expected_output1, scotsmen - warriors)
        self.assertEqual(expected_output2, scotsmen | warriors)
        self.assertEqual(expected_output3, scotsmen & warriors)
        self.assertEqual(expected_output4, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )

        self.assertEqual(False, set('cake') > set('pie'))
