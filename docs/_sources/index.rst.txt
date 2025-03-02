Welcome to documentation of Unittest2doc
====================================================

Unittest2doc 是一个将 Python 单元测试代码转换为文档的工具。本文档中的单元测试部分就是是使用 Unittest2doc 生成的。

百闻不如一见，我们直接通过本文档的例子来学习 Unittest2doc 的用法。

项目地址为: https://github.com/Fmajor/unittest2doc

项目的文件结构为:

.. code-block::

   unittest2doc/            # 项目根目录
     src/                   # 源代码目录
       unittest2doc/        # 源代码的包目录
         __init__.py
         unittest2doc.py
         ...
     sphinx-docs/           # 文档目录
       source/              # 文档源文件目录
         conf.py            # 配置文件, 在这里导入要测试的包
         index.rst
         unittests/         # Unittest2doc 会在这里生成rst文件
         src/               # sphinx通过autosummary功能生成的API文档
         ...
       build/               # 文档构建目录, 运行make html 后会在这里生成本文档
     tests/                 # 测试目录, 我们使用Unittest2doc的地方
       test_unittest2doc.py # 测试文件, 其中包括了一个Unittest2doc类, 和其运行示例
       test_pformat_json.py # 我们这里测试了一个结构化输出json的函数
                            #   对于一个结构化输出函数，最好的测试方法是展示出其结果并保存为文档
     pyproject.toml
     README.rst

* 在项目根目录使用 ``make unittest``

  * 实际执行 ``python -m unittest discover -s tests -p '*.py' -b``
  * 这就是一般的单元测试，我们只关心测试结果，不关心测试过程

* 在项目根目录使用 ``make generate-unittest-docs``

  * 实际执行 ``unittest2doc -s tests -p '*.py'``, 他会直接运行所有满足条件的测试文件
  * 我们每一个测试文件都可以单独执行, 其中的运行参数使得他们可以在运行的时候生成RST格式的sphinx文档,
    并且保存到 ``/sphinx-docs/source/unittests/`` 目录下, 最终展现在我们的文档中

这里我们直接展示测试文件

``tests/test_unittest2doc.py``
------------------------------

其生成的文档为: :doc:`/unittests/unittest2doc/unittest2doc/Unittest2Doc/index`

.. literalinclude:: ../../tests/test_unittest2doc.py
   :language: python
   :linenos:

``tests/test_pformat_json.py``
------------------------------

其生成的文档为: :doc:`/unittests/unittest2doc/formatter/index`

.. literalinclude:: ../../tests/test_pformat_json.py
   :language: python
   :linenos:

最后，我们来看一下生成的文档

* API 文档来源于我们的项目源代码, 是sphinx中的autosummary功能生成的, 不是本文的重点
* 而单元测试文档来源于我们的测试代码, 请自行探索其结果并与测试代码对比

API Documentation and Unittests
-------------------------------

.. toctree::
   :maxdepth: 1

   catalogue