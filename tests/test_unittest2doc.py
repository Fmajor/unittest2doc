import unittest
import unittest2doc
from unittest2doc import Unittest2Doc, docpprint
import time
import json
import yaml
import textwrap
from pathlib import Path

if 'test Unittest2Doc' and 1:
    class Test(unittest.TestCase):
        ''' docstring of class, new title
            -----------------------------

            * Sphinx have already use "=" as title marker
            * to form a subtitle, we should use ``-`` as the title marker

        '''
        def test(s):
            a = 1
            b = 2
            print("# this is a normal unittest.TestCase")
            print("# we can use all its assertion methods")
            s.assertEqual(a, 1)
            s.assertNotEqual(a, b)
            s.assertIs(a, 1)
            s.assertIsNot(a, b)
            s.assertIsNone(None)
            s.assertIsNotNone(a)
            s.assertTrue(True)
            s.assertFalse(False)
            
        def rst_test_doc(s):
            ''' group of tests
                --------------

                function startswith rst will only provide its docstring to generate docs

                we set the ``title_marker`` config to '^', and following tests will be grouped under this title

                because rst title markers have these priorities:

                * ``=`` (already used by upper Sphinx structure)
                * ``-``
                * ``^``

            '''
            unittest2doc.update_config(s, title_marker='^')

        #@unittest2doc.stop_after
        #@unittest2doc.only
        #@unittest2doc.stop
        def test_show_variable(s):
            """ the title marker is `^` (set in previous function rst_test_doc)

                here we test the ``Unittest2Doc.v`` method, to display variables
            """
            a = 1
            b = '2'
            c = {
                'normal': 'some data',
                'secret': 'should be masked',
                'subsecret': {
                    'good': 1,
                    'bad': 0,
                    'sub': {
                        'good': 1,
                        'bad': 0,
                    }
                }
            }
            d = [1,2,3]
            unittest2doc.v(['a', 'b', 'c', 'd'], locals(), globals(), mask=[
                'c.secret',
                'c.subsecret.bad',
                'c.subsecret.sub.bad',
            ])
        def test_add_more_doc_0(s):
            """ {"open_input":false}

                here we close the input block by json setting at first line of docstring

                the title marker is still `^` (set in previous function rst_test_doc)

            """
            pass
        def test_add_more_doc_1(s):
            """ {"open_output": false}

                here we close the output block by json setting at first line of docstring

                the title marker is still `^` (set in previous function rst_test_doc)
            """
            print('here we close the output ')
        def test_add_more_doc_2(s):
            """ after this, set title level to '-', and the current group is finished
            """
            unittest2doc.update_config(s, title_marker='-') # set title level to '-' after this test
        def test_add_more_doc_3(s):
            """ this test back to top level (because title_marker is set to '-' at last function)
            """
            pass
        def test_title_marker_for_single_test(s):
            """ {"title_marker": "^"}

                title marker set by above json is only effective in this function

            """
            print("# the title_marker ^ is only used in this function, and will not affect other tests")
            print("# after this test, the title_marker is back to previous '-'")
        def test_output_as_json(s):
            """ {"output_highlight": "json"}

                the output is highlighted as ``json``

                the title marker here and below are all the default ``-``
            """
            print(json.dumps({"1":1, "2":"2", "3": 3.0, "4":4, "a":[{"1":1, "2":2}, {"3":3, "4":4}]}, indent=2))
        def test_output_as_yaml(s):
            """ {"output_highlight": "yaml"}

                the output is highlighted as ``yaml``
            """
            # pprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]}, expand_all=True, indent_guides=False)
            docpprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]})
        def test_output_as_python(s):
            """ {"output_highlight": "python"}
            """
            # print(pformat_json({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]}))
            docpprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]})
            from datetime import datetime
            from collections import OrderedDict
            d = [
                  {
                    'system_tags': [
                      OrderedDict([('a', 1), ('b', 2), ('c', 3)]),
                    ],
                    'date': datetime.now(),
                  }
                ]
            docpprint(d)
        @unittest2doc.skip
        def test_skipped(s):
            raise Exception('this function should be skipped and we should not get this Exception')

        @unittest2doc.expected_failure
        def test_with_exception(s):
            """ {"output_processors": ["no_home_folder"]}

                test with exception, the output string will be processed by ``no_home_folder`` processor defined below
            """
            raise Exception('expected exception')
          
        def test_add_foldable_output(s):
          """ add extra foldable text at end of the doc page
          """
          print("# add some output")
          unittest2doc.add_foldable_output(
            s, # must pass self into add_foldable_output
            name='some python code',
            highlight='python',
            output=textwrap.dedent('''
                  # some code ...
                  def func(*args, **kwargs):
                    pass
                '''
            )
          )

          # some nested data
          data = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': {
              'a': 1,
              'b': 2,
              'c': 3,
            }
          }
          print("# add some output")

          unittest2doc.add_foldable_output(
            s, # must pass self into add_foldable_output
            name='some yaml data',
            highlight='yaml',
            output=yaml.dump(data, indent=2)
          )
          print("# add some output")
        
        def test_last(s):
          """ we use decorator above, make sure that this test is the last one """
          pass

    class Test2(unittest.TestCase):
        ''' docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.only``

        '''
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        @unittest2doc.only
        def test_only_1(s):
          """ when you use ``Unittest2Doc.generate_docs()``, this test will be executed

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed
              
              Thus the `only` decorator should only be used during your development and testing,
              e.g., you just want to test one function and want to skip others for speed

          """
          pass

        def test_other(s):
          """ when you use ``Unittest2Doc.generate_docs()``, this test will be skipped because of not @unittest2doc.only decorator

              it will be executed anyway if you use ``python -m unittest ...`` framework

          """
          pass

        @unittest2doc.only
        def test_only_2(s):
          """ when you use ``Unittest2Doc.generate_docs()``, this test will be executed
          """
          pass
    
    class Test3(unittest.TestCase):
        """ docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.stop``

        """
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        def test_3(s):
          """ this should be the only test when you use ``Unittest2Doc.generate_docs()``

              we have a @unittest2doc.stop decorator at next test

          """
          pass

        @unittest2doc.stop
        def test_2(s):
          """ stop before this test when you use ``Unittest2Doc.generate_docs()``

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed

              Thus the `stop` decorator should only be used during your development and testing,
              e.g., you just want to test above function and want to skip others for speed
          
          """
          pass
        
        def test_1(s):
          pass

    class Test4(unittest.TestCase):
        """ docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.stop_after``

        """
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        def test_3(s):
          """ this should be the executed when you use ``Unittest2Doc.generate_docs()`` """
          pass

        @unittest2doc.stop_after
        def test_2(s):
          """ stop after this test when you use ``Unittest2Doc.generate_docs()``

          """
          pass

        def test_1(s):
          """ this should be skipped when you use ``Unittest2Doc.generate_docs()``

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed

              Thus the `stop_after` decorator should only be used during your development and testing,
              e.g., you just want to test above function and want to skip others for speed

          """
          pass
    
    class Test5(unittest.TestCase):
        """ docstring of class
            ------------------

            in this class, we test the unittest decorator (not unittest2doc decorator)

        """
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")
        
        @unittest.skip
        def test_skipped(s):
          raise Exception('this function should be skipped and we should not get this Exception') 

        @unittest.expectedFailure
        def test_with_exception(s):
          raise Exception('expected exception')


if __name__ == "__main__":
    def no_home_folder(output):
        # filter out `${HOME}/*/unittest2doc` to `${PROJECT_ROOT}/unittest2doc`
        import os
        home = os.environ.get('HOME')
        import re
        pattern = r"{home}/(?:[^/]+/)*?unittest2doc/".format(home=home)
        replacement = r"${PROJECT_ROOT}/unittest2doc/"
        output = re.sub(pattern, replacement, output)
        return output
    t = Unittest2Doc(
        testcase=Test(),
        name='unittest2doc.unittest2doc.Unittest2Doc.basic',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
        output_processors=dict(
          no_home_folder=no_home_folder,
        )
    )
    t.generate_docs()

    t2 = Unittest2Doc(
        testcase=Test2(),
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_only',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t2.generate_docs()

    t3 = Unittest2Doc(
        testcase=Test3(),
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_stop',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t3.generate_docs()

    t4 = Unittest2Doc(
        testcase=Test4(),
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_stop_after',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t4.generate_docs()

    t5 = Unittest2Doc(
        testcase=Test5(),
        name='unittest2doc.unittest2doc.Unittest2Doc.test_unittest_decorator',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t5.generate_docs()
