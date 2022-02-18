import os
import jpype
from jpype import JPackage

dir_path = os.path.dirname(os.path.realpath(__file__))
jpype.startJVM(classpath=[f"{dir_path}/jars/*/*", f"{dir_path}/jars/*/target/dependency/*"])
_base_package = JPackage("ac").technion.iem.ontobuilder
core = _base_package.core
matching = _base_package.matching
io = _base_package.io
Ontology = core.ontology.Ontology
Term = core.ontology.Term
