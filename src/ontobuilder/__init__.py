import os
import sys
import jpype
from jpype import JPackage
from importlib.machinery import ModuleSpec as _ModuleSpec


dir_path = os.path.dirname(os.path.realpath(__file__))
jpype.startJVM(classpath=[f"{dir_path}/jars/*/*", f"{dir_path}/jars/*/target/dependency/*"])


_base_package = JPackage("ac").technion.iem.ontobuilder
_core = _base_package.core
_matching = _base_package.matching
_io = _base_package.io

_base_pkg_name = 'ontobuilder'
_pkgs = {'core': _core, 'matching': _matching, 'io': _io, 'ontology': _core.ontology,
         'imports': _io.imports, 'exports': _io.exports, 'algorithms': _matching.algorithms,
         'wrapper': _matching.wrapper
         }


# importer trick
class _JavaImportProxy:
    """ (internal) Finder hook for importlib. """

    def find_spec(self, name, path, target=None):
        parts = name.rpartition('.')

        # if top level module - it is not relevant (since the TLD is ontobuilder)
        if not parts[1]:
            return None

        # if of the form ontobuilder.{core, matching, io}        
        if (parts[0] == _base_pkg_name) and (parts[2] in _pkgs.keys()):
            ms = _ModuleSpec(name, self)
            ms._jname = parts[2]
            return ms

        base = sys.modules.get(parts[0], None)
        if not base or not isinstance(base, JPackage):
            return None

        if not hasattr(base, parts[2]):
            raise ImportError("Failed to import '%s'" % name)

        return _ModuleSpec(name, self)

    """ (internal) Loader hook for importlib. """
    def create_module(self, spec):
        if spec.parent == _base_pkg_name:
            return _pkgs[spec._jname]
        parts = spec.name.rsplit('.', 1)
        rc = getattr(sys.modules[spec.parent], parts[1])

        return rc

    def exec_module(self, fullname):
        pass


# Install hooks into python importlib
sys.meta_path.append(_JavaImportProxy())
