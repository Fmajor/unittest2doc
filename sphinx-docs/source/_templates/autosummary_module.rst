{{ fullname | escape | underline}}

.. automodule:: {{ fullname }}

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: autosummary_module.rst
   :recursive:
{% for item in modules %}
{%-if ".tests_" not in item and not item.endswith(".tests") %}
   {{ item }}
{%- endif %}
{%- endfor %}

{% endif %}
{% endblock %}
