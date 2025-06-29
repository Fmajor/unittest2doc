from pathlib import Path
import unittest2doc
from unittest2doc import Unittest2Doc
from unittest2doc.utils.exec_tool import filter_after_comment_by, load_module, collect_module_attr, load_main

""" Note
This is a special way to run test cases in the ``if __name__ == "__main__"`` block of a test file (src/unittest2doc/utils/exec_tool.py),
Using the helper functions from that file.
"""

if __name__ == "__main__":
    test_module = "unittest2doc.utils.exec_tool"
    module = load_module(test_module)
    module_globals = collect_module_attr(module, all=True)

    main = load_main(
             module,
             code_filter=filter_after_comment_by("Run unittests"),
             globals=module_globals,
             add_code_object=True,
           )

    t = unittest2doc.Unittest2Doc(
        testcase=main['TestExecTool'](),
        name='unittest2doc.utils.exec_tool',
        ref=':mod:`unittest2doc.utils.exec_tool`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
        open_input=False,
    )
    t.generate_docs()