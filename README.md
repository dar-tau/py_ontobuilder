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

## Song
"
Ontobuilder. 

Qu'est-ce que c'est

Pa-Pa-Pa-Pa Python - far better!

Plu-, Plu-, Plug, Plug, Plug and Play! 
"
