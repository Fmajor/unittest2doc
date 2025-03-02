import unittest
import sys
import os
import json
from pathlib import Path
from unittest2doc import Unittest2Doc, FLog
from unittest2doc.formatter.json_formatter import pformat_json

class TestJsonFormatter(Unittest2Doc):
    """ Test cases for json_formatter module's pformat_json function
    """

    def setUp(self):
        """ here we also test the FLog class, it is a helper class to print function inputs and outputs """
        self.flog = FLog(do_print=True, output_suffix='\n', input_suffix=' # ===>')
        self.frun = self.flog.frun
    
    def test_basic_format(self):
        """ {"output_highlight": "python"}
        """
        # Test basic dictionary formatting
        data = {"name": "John", "age": 30, "city": "New York"}
        # call pformat_json(data) and print the result
        self.frun(pformat_json, data)
        
        # Test basic list formatting
        data = [1, 2, 3, "four", 5.0]
        # call pformat_json(data) and print the result
        self.frun(pformat_json, data)
        
        # Test simple value
        data = "simple string"
        # call pformat_json(data) and print the result
        self.frun(pformat_json, data)
    
    def test_nested_structures(self):
        """ {"output_highlight": "python"}
        """
        # Test nested dictionary and list
        data = {
            "person": {
                "name": "Alice",
                "details": {
                    "age": 28,
                    "occupation": "Engineer"
                }
            },
            "hobbies": ["reading", "hiking", {"sport": "tennis"}]
        }
        self.frun(pformat_json, data)
    
    def test_dict_title_comment(self):
        """ {"output_highlight": "python"}
        """
        # Test using string comment for dict title
        data = {"key1": "value1", "key2": "value2"}
        self.frun(pformat_json, data, comments="Dictionary Title")
        
        # Test using __dtitle__ special key
        data = {"key1": "value1", "key2": "value2"}
        comments = {"__dtitle__": "Dictionary Title With Special Key"}
        self.frun(pformat_json, data, comments=comments)
        
        # Test multi-line dict title
        comments = {"__dtitle__": "First Line\nSecond Line\nThird Line"}
        self.frun(pformat_json, data, comments=comments)
    
    def test_list_title_comment(self):
        """ {"output_highlight": "python"}
        """
        # Test using string comment for list title
        data = ["item1", "item2", "item3"]
        self.frun(pformat_json, data, comments="List Title")
        
        # Test using __ltitle__ special key
        comments = {"__ltitle__": "List Title With Special Key"}
        self.frun(pformat_json, data, comments=comments)
        
        # Test list prefix and suffix comments
        comments = {
            "__ltitle__": "List With Prefix and Suffix",
            "__lprefix__": ["Prefix Line 1", "Prefix Line 2"],
            "__lsuffix__": ["Suffix Line 1", "Suffix Line 2"]
        }
        self.frun(pformat_json, data, comments=comments)
    
    def test_specific_element_comments(self):
        """ {"output_highlight": "python"}
        """
        # Test comments for specific dict keys
        data = {"name": "Bob", "age": 45, "city": "Boston"}
        comments = {
            "name": "Person's name",
            "age": "Person's age in years",
            "city": "City of residence"
        }
        self.frun(pformat_json, data, comments=comments)
        
        # Test comments for specific list indices
        data = ["Python", "Java", "JavaScript", "C++"]
        comments = {
            0: "My favorite language",
            2: "Web development language"
        }
        self.frun(pformat_json, data, comments=comments)
    
    def test_callable_comments(self):
        """ {"output_highlight": "python"}
        """
        # Test callable comments for dict
        data = {"price": 129.99, "quantity": 5, "discount": 0.15}
        
        def calc_total(key, value):
            if key == "price":
                return f"Base price: ${value}"
            elif key == "quantity":
                return f"Order quantity of {value} units"
            elif key == "discount":
                return f"Discount rate of {int(value*100)}%"
            return ""
        
        comments = {
            "price": calc_total,
            "quantity": calc_total,
            "discount": calc_total
        }
        self.frun(pformat_json, data, comments=comments)
    
    def test_compact_mode(self):
        """ {"output_highlight": "python"}
        """
        # Test compact mode for dict
        data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
        comments = {
            "__lcompact__": 30,
            "a": "First item",
            "c": "Third item",
            "e": "Fifth item"
        }
        self.frun(pformat_json, data, comments=comments)
        
        comments['__lcompact__'] = 25
        self.frun(pformat_json, data, comments=comments)

        comments['__lcompact__'] = 20
        self.frun(pformat_json, data, comments=comments)

        comments['__lcompact__'] = 15
        self.frun(pformat_json, data, comments=comments)

        comments.pop('__lcompact__')
        self.frun(pformat_json, data, comments=comments)

        self.frun(pformat_json, data, comments=comments, compact=15)

        self.frun(pformat_json, data, comments=comments, compact=20)

        self.frun(pformat_json, data, comments=comments, compact=30)

    
    def test_recursive_comments(self):
        """ {"output_highlight": "python"}
        """
        # Test __lsub__ for all dict elements
        data = {
            "user": {
                "id": 12345,
                "name": "Alice Smith",
                "email": "alice@example.com"
            },
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        }
        comments = {
            "__dtitle__": "User Profile",
            "__lsub__": {
                "id": "Unique identifier",
                "name": "Full name",
                "theme": "UI theme preference"
            }
        }
        self.frun(pformat_json, data, comments=comments)
        
        # Test __llist__ and __ldict__ for typed elements
        data = [
            {"type": "book", "title": "Python Programming"},
            [1, 2, 3],
            {"type": "video", "title": "Advanced Python"}
        ]
        comments = {
            "__llist__": {
                "__lcompact__": 40
            },
            "__ldict__": {
                "type": "Content type",
                "title": "Content title"
            }
        }
        self.frun(pformat_json, data, comments=comments)
    
    def test_custom_indentation(self):
        """ {"output_highlight": "python"}
        """
        # Test custom indentation
        data = {
            "outer": {
                "middle": {
                    "inner": "value"
                }
            }
        }
        # Test with different indent values
        self.frun(pformat_json, data, indent=2)
        self.frun(pformat_json, data, indent=4)
    
    
    def test_custom_comment_prefix(self):
        """ {"output_highlight": "python"}
        """
        # Test custom comment prefix
        data = {"name": "John", "age": 30}
        comments = {
            "__dtitle__": "Person Info",
            "name": "Person's name",
            "age": "Age in years"
        }
        self.frun(pformat_json, data, comments=comments, comment_prefix="// ")
        
    def test_different_compact_values(self):
        """ {"output_highlight": "python"}
        """
        # Same data with different __lcompact__ values
        data = {"item1": 100, "item2": 200, "item3": 300, "item4": 400, "item5": 500}
        comments = {
            "item1": "First item comment",
            "item3": "Third item comment",
            "item5": "Fifth item comment"
        }
        
        # No compact mode
        print("\nNo compact mode:")
        self.frun(pformat_json, data, comments=comments)
        
        # Very wide compact mode (essentially same as no compact)
        print("\nCompact mode (width=100):")
        comments_wide = comments.copy()
        comments_wide["__lcompact__"] = 100
        self.frun(pformat_json, data, comments=comments_wide)
        
        # Medium compact mode
        print("\nCompact mode (width=50):")
        comments_medium = comments.copy()
        comments_medium["__lcompact__"] = 50
        self.frun(pformat_json, data, comments=comments_medium)
        
        # Narrow compact mode
        print("\nCompact mode (width=25):")
        comments_narrow = comments.copy()
        comments_narrow["__lcompact__"] = 25
        self.frun(pformat_json, data, comments=comments_narrow)
    
    def test_deeply_nested_structure(self):
        """ {"output_highlight": "python"}
        """
        # Create a deeply nested structure to test indentation handling
        data = {
            "level1": {
                "level2": {
                    "level3": {
                        "level4": {
                            "level5": {
                                "value": "deeply nested value"
                            },
                            "array": [1, 2, [3, 4, [5, 6]]]
                        }
                    }
                }
            }
        }
        
        comments = {
            "__dtitle__": "Deep Nesting Test",
            "__lsub__": {
                "level1": "First level",
                "level2": "Second level",
                "level3": "Third level",
                "level4": "Fourth level",
                "level5": "Fifth level",
                "value": "The final value",
                "array": "Array of values"
            }
        }
        
        self.frun(pformat_json, data, comments=comments, debug=True)
    
    def test_comprehensive_example(self):
        """ {"output_highlight": "python"}
        """
        # Test case combining multiple features
        data = {
            "metadata": {
                "title": "Comprehensive Example",
                "version": 1.5,
                "tags": ["test", "example", "comprehensive"]
            },
            "configuration": {
                "enabled": True,
                "options": {
                    "debug": False,
                    "verbose": True,
                    "timeout": 30
                }
            },
            "data_points": [
                {"id": 1, "value": 10.5, "label": "Point A"},
                {"id": 2, "value": 20.7, "label": "Point B"},
                {"id": 3, "value": 15.3, "label": "Point C"}
            ],
            "statistics": {
                "count": 3,
                "average": 15.5,
                "max": 20.7,
                "min": 10.5
            }
        }
        
        # Define comprehensive comments
        def format_stat(key, value):
            if key == "average":
                return f"Average value: {value:.1f}"
            elif key == "max":
                return f"Maximum value: {value:.1f}"
            elif key == "min":
                return f"Minimum value: {value:.1f}"
            return str(value)
        
        comments = {
            "__dtitle__": "Complete Feature Demonstration",
            "__lcompact__": 60,
            "metadata": {
                "__dtitle__": "Document Metadata",
                "title": "The title of this example",
                "tags": "Keywords for categorization"
            },
            "configuration": {
                "__dtitle__": "System Configuration",
                "__lcompact__": 40,
                "options": {
                    "__dtitle__": "Available Options",
                    "debug": "Enable debug mode",
                    "verbose": "Show detailed output",
                    "timeout": "Operation timeout in seconds"
                }
            },
            "data_points": {
                "__ltitle__": "Measurement Data",
                "__lprefix__": ["Array of data point objects", "Each with id, value and label"],
                "__ldict__": {
                    "id": "Unique identifier",
                    "value": "Measurement value",
                    "label": "Display name"
                }
            },
            "statistics": {
                "__dtitle__": "Statistical Analysis",
                "count": "Number of data points",
                "average": format_stat,
                "max": format_stat,
                "min": format_stat
            }
        }
        
        result = pformat_json(data, comments=comments)
        print(result)

if __name__ == "__main__":
    t = TestJsonFormatter(
        name='unittest2doc.formatter.pformat_json',
        ref=':func:`unittest2doc.formatter.pformat_json`',
        doc_root=Path(__file__).absolute().parent.parent / 'sphinx-docs/source/unittests',
    )
    t.generate_docs()