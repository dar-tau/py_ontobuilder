# Ontobuilder

This is a Python port to [Ontobuilder](https://github.com/shraga89/ontobuilderDev).

This can actually be modified to work with basically any Java package in JAR format by replacing the contents of `src/ontobuilder/jars` and adapting `src/ontobuilder/__init__.py` accordingly. 


## Installation
### Conda
1. (**Optional**) Create new environment (might be useful if package conflicts with other packages arise in step 2):
```
conda create -n ontobuilder
conda activate ontobuilder
```

2. Run
```
conda install -c conda-forge -y openjdk>=11.0.9 maven jpype1
```

3. Then simply run:
```
pip install -e git+https://github.com/dar-tau/py_ontobuilder.git@main#egg=ontobuilder
```

## Package Structure
the main three submodules are: **ontobuilder.core**, **ontobuilder.matching**, **ontobuilder.io**. However, in Python, unlike Java, we prefer less hierarchical submodule paths. 
Consequently, we decided to flatten out the module structure by extracting important submodules to the second layer of the hierarchy (namely, directly under ontobuilder):
* **ontobuilder.core**
* **ontobuilder.matching**
* **ontobuilder.io**
* **ontobuilder.ontology** (ontobuilder.core.ontology)
* **ontobuilder.imports** (ontobuilder.io.imports)
* **ontobuilder.exports** (ontobuilder.io.exports)
* **ontobuilder.algorithms** (ontobuilder.matching.algorithms)
* **ontobuilder.wrapper** (ontobuilder.matching.wrapper)

## Examples
```python
from ontobuilder.ontology import Ontology, Term
from ontobuilder.wrapper import OntobuilderWrapper

obw = OntobuilderWrapper(True)
o1 = Ontology("Test1", "Title Test 1")
o2 = Ontology("Test2", "Title Test 2")
o1.setLight(True)
o2.setLight(True)

o1.addTerm(Term("airplane", "Skipper"))
o2.addTerm(Term( "aircraft", "B-52"))

res1 = obw.matchOntologies(o1, o2, "Term Match")
res2 = obw.matchOntologies(o1, o2, "WordNet Match")
```

## Song
"  
Ontobuilder.  
Qu'est-ce que c'est?  
Pa-Pa-Pa-Pa Python - far better!  
Run, run, run, plug and play!  
"
