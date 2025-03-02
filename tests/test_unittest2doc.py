from unittest2doc import *
import time
import json
import yaml
import textwrap
from pathlib import Path

if 'test Unittest2Doc' and 1:
    class Test(Unittest2Doc):
        ''' docstring of class, new title
            -----------------------------

            * this docstring is added to top of the document page

              * we should use ``-`` as the title marker
        '''
        def test(s):
            a = 1
            b = 2
            print("# Unittest2Doc is a subclass of unittest.TestCase")
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

                we set self.title_marker to '^', and following tests will be grouped under this title

                because rst title markers have these priorities:

                * `-`
                * `^`

            '''
            s.title_marker = '^'

        #@Unittest2Doc.stop_after
        #@Unittest2Doc.only
        #@Unittest2Doc.stop
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
            s.v(['a', 'b', 'c', 'd'], locals(), globals(), mask=[
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
            s.title_marker = '-'
        def test_add_more_doc_3(s):
            """ this test back to top level
            """
            pass
        def test_doc_string(s):
            """ {"title_marker": "^"}

                title marker set by above json is only effective in this function

                * test list

                  * test list indent

            """
            s.title_marker = '-' # resume title level
        def test_output_as_json(s):
            """ {"output_highlight": "json"}

                the output is highlighted as `json`
                the title marker here and below are all the default `-`
            """
            print(json.dumps({"1":1, "2":"2", "3": 3.0, "4":4, "a":[{"1":1, "2":2}, {"3":3, "4":4}]}, indent=2))
        def test_output_as_yaml(s):
            """ {"output_highlight": "yaml"}

                the output is highlighted as `yaml`
            """
            # pprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]}, expand_all=True, indent_guides=False)
            docpprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]})
        def test_output_as_python(s):
            """ {"output_highlight": "python"}
            """
            # print(pformat_json({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]}))
            docpprint({1:1, '2':'2', '3': 3.0, '4':4, 'a':[{1:1, 2:2}, {3:3, 4:4}]})
            d = [
                  {
                    'user_id': '9876543210987654321',
                    'system_tags': [
                      {
                        'category': {
                          'id': 'ed',
                          'name': 'EdTech',
                        },
                        'item': {
                          'id': '998877665544332211',
                          'name': 'EduTech Platform',
                        },
                      },
                      {
                        'category': {
                          'id': 'ac',
                          'name': 'Academia',
                        },
                        'item': {
                          'id': '112233445566778899',
                          'name': 'CS101 Course',
                        },
                      },
                    ],
                    'thread_id': '1626426375145156611',
                    'created_at': '2023-02-17T03:40:40.000Z',
                    'edit_history': [
                      '1626426375145156611',
                    ],
                    'metadata': {
                      'labels': [
                        {
                          'start': 64,
                          'end': 67,
                        },
                      ],
                      'hashtags': [
                        {
                          'start': 86,
                          'end': 91,
                        },
                      ],
                    },
                    'geo': {
                    },
                    'id': '1626426375145156611',
                    'lang': 'en',
                    'stats': {
                      'shares': 331,
                      'replies': 0,
                    },
                    'references': [
                      {
                        'type': 'repost',
                        'id': '1626173352330002434',
                      },
                    ],
                    'text': "RT @edu_tech: New online learning platform launched! 🚀 Check out our AI-powered courses #EdTech",
                    '__tablename__': 'social.posts',
                  },
                  {
                    'created_at': '2021-02-08T18:21:13.000Z',
                    'bio': '',
                    'verified': False,
                    'stats': {
                      'followers': 272,
                      'following': 253,
                      'posts': 6543,
                      'listed': 4,
                    },
                    'username': 'AcademiaNews',
                    '__tablename__': 'social.users',
                  },
                ]
            # print(pformat_json(d, indent=4))
            docpprint(d)
        @Unittest2Doc.skip
        def test_another_skipped(s):
            raise Exception('this function should be skipped and we should not get this Exception')

        @Unittest2Doc.expected_failure
        def test_with_exception(s):
            """ test with exception """
            raise Exception('expected exception')
          
        def test_add_foldable_output(s):
          """ add extra foldable text at end of the doc page
          """
          print("# add some output")
          s.add_foldable_output(
            {
              'name': 'some python code',
              'highlight': 'python',
              'output':textwrap.dedent('''
                  # some code ...
                  def func(*args, **kwargs):
                    pass
                ''')
            } 
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

          s.add_foldable_output(
            {
              'name': 'some yaml data',
              'highlight': 'yaml',
              'output': yaml.dump(data, indent=2)
            } 
          )
          print("# add some output")
        
        def test_last(s):
          """ we use decorator above, make sure that this test is the last one """
          pass

    class Test2(Unittest2Doc):
        ''' docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.only``

        '''
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        @Unittest2Doc.only
        def test_only(s):
          """ this should be the only test use you use ``Unittest2Doc.generate_docs()``

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed
              
              Thus the `only` decorator should only be used during your development and testing,
              e.g., you just want to test one function and want to skip others for speed

          """
          pass

        def test_other(s):
          """ this should be skipped when you use ``Unittest2Doc.generate_docs()``

              it will be executed anyway if you use ``python -m unittest ...`` framework

          """
          pass
    
    class Test3(Unittest2Doc):
        """ docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.stop``

        """
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        def test_1(s):
          """ this should be the only test when you use ``Unittest2Doc.generate_docs()`` """
          pass

        @Unittest2Doc.stop
        def test_2(s):
          """ stop before this test when you use ``Unittest2Doc.generate_docs()``

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed

              Thus the `stop` decorator should only be used during your development and testing,
              e.g., you just want to test above function and want to skip others for speed
          
          """
          pass

    class Test4(Unittest2Doc):
        """ docstring of class
            ------------------

            in this class, we test the decorator ``@Unittest2Doc.stop_after``

        """
        def setUp(s):
          print("# this setup function is always called at beginning")
        def tearDown(s):
          print("# this tearDown function is always called at end")

        def test_1(s):
          """ this should be the executed when you use ``Unittest2Doc.generate_docs()`` """
          pass

        @Unittest2Doc.stop_after
        def test_2(s):
          """ stop after this test when you use ``Unittest2Doc.generate_docs()``

          """
          pass

        def test_3(s):
          """ this should be skipped when you use ``Unittest2Doc.generate_docs()``

              Note that if you use ``python -m unittest ...`` framework, all tests will be executed

              Thus the `stop_after` decorator should only be used during your development and testing,
              e.g., you just want to test above function and want to skip others for speed

          """
          pass


if __name__ == "__main__":
    t = Test(
        name='unittest2doc.unittest2doc.Unittest2Doc.basic',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t.generate_docs()


    t2 = Test2(
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_only',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t2.generate_docs()

    t3 = Test3(
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_stop',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t3.generate_docs()

    t4 = Test4(
        name='unittest2doc.unittest2doc.Unittest2Doc.test_decorator_stop_after',
        ref=':class:`unittest2doc.unittest2doc.Unittest2Doc`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t4.generate_docs()