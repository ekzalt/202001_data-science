# Readme

Install libs with pip

```bash
pip install numpy scipy matplotlib ipython jupyter pandas sympy nose seaborn statsmodels scikit-learn

# for maps
# pip install folium
```

[Python](https://www.python.org)

[Jupyter Notebook](https://jupyter.org) - Interactive development environment

[NumPy](https://numpy.org/) - Linear Algebra in Python (written with C)

[Pandas](https://pandas.pydata.org/) - Data Analysis and Manipulation tool

[Scikit Learn](https://scikit-learn.org/stable/user_guide.html) - Machine Learning in Python

[TensorFlow](https://www.tensorflow.org/) - End-to-End Machine Learning platform

[StatsModels](https://www.statsmodels.org/dev/install.html) - Statistics, Timelines

```bash
# install jupyter notebook
pip install jupyterlab
pip install notebook

# run jupyter notebook
jupyter notebook
```

Resolve Win Jupyter Notebook [issue](https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror)

```py
# editing the file: tornado/platform/asyncio.py
import sys

if sys.platform == 'win32':
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
