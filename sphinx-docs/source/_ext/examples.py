# https://www.sphinx-doc.org/en/master/development/tutorials/todo.html
from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

__doc__ = """
put this in your doc str:
  .. example:: :doc:`/unittests/lib/dbs/Sqlite`
"""

class Example(nodes.Admonition, nodes.Element):
  pass
class ExampleDirective(SphinxDirective):
  # this enables content in the directive
  has_content = True
  def run(self):
    targetid = 'example-%d' % self.env.new_serialno('example')
    targetnode = nodes.target('', '', ids=[targetid])


    example_node = Example()
    example_node += nodes.title(_('Examples'), _('Examples'))

    self.state.nested_parse(self.content, self.content_offset, example_node)

    return [targetnode, example_node]

def visit_example_node(self, node):
  self.visit_admonition(node)
def depart_example_node(self, node):
  self.depart_admonition(node)

def process_example_nodes(app, doctree, fromdocname):
  env = app.builder.env

  for node in doctree.findall(Example):
    node.attributes['classes'].append('example-paragraph')

def setup(app):
  app.add_node(Example,
               html= (visit_example_node, depart_example_node),
               latex=(visit_example_node, depart_example_node),
               text= (visit_example_node, depart_example_node))

  app.add_directive('example', ExampleDirective)
  app.connect('doctree-resolved', process_example_nodes)

  return {
    'version': '0.1',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
