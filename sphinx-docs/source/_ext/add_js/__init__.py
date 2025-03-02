from os import makedirs, path
import shutil
__version__ = "0.0.1"

import sphinx
_ROOT_DIR = path.abspath(path.dirname(__file__))
_FILES = [
  ('jquery.js', 'sha384-....'),
  ('_sphinx_javascript_frameworks_compat.js', 'sha384-....'),
  ('underscore.js', 'sha384-....'),
  ('underscore_rename.js', "sha384-..."),
]
def add_js_files(app, config):
    jquery_installed = getattr(app, "_addjs_installed", False)

    if sphinx.version_info[:2] >= (6, 0) and not jquery_installed:
        makedirs(path.join(app.outdir, '_static'), exist_ok=True)
        for (filename, integrity) in _FILES:
            # The default is not to enable subresource integrity checks, as it
            # does not trigger the hash check but instead blocks the request
            # when viewing documentation locally through the ``file://`` URIs.
            if config.jquery_use_sri:
                app.add_js_file(filename, priority=100, integrity=integrity)
            else:
                app.add_js_file(filename, priority=100)
            shutil.copyfile(
                path.join(_ROOT_DIR, filename),
                path.join(app.outdir, '_static', filename)
            )
        app._addjs_installed = True

def setup(app):
    # Configuration value for enabling `subresource integrity`__ (SRI) checks
    # __ https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
    app.add_config_value("jquery_use_sri", default=False, rebuild="html", types=(bool,))
    app.connect('config-inited', add_js_files)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }