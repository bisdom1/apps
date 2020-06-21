# Python web app comparison
Comparison of different python packages for generating web-based applications, using a basic example of data visualization with limited user interaction. 

## General requirements
Python 3.x set-up with `pandas` and `plotly` packages. The dataset used in the apps is found in assets/. 

## Streamlit
[Streamlit](https://www.streamlit.io/) is an app framework optimized for data science and machine learning, with powerful caching. Adding interactive user elements typically only takes 1 line of code per element.

1. Install the `streamlit` package via `pip install streamlit` or `conda install streamlit` commands.
2. Download the `streamlit.py` example app from this repository.
3. To run the app in streamlit, open a python console (e.g. Anaconda prompt) and run the command `streamlit run streamlit.py`.
4. Open the app in your browser (Edge or Chrome) via http://localhost:8051.

## Plotly Dash
Compared to streamlit, [Plotly Dash](https://plotly.com/dash/) allows for building more complex user interfaces with more flexible and advanced customization for visualization, including for example interactive graphics with crosslinking between different plots. The downside is that building apps requires more coding, but by using pre-built elements from [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) the amount of code required can be quickly reduced.

1. Install the following 2 packages via `pip install` or `conda install`:
    1. `dash`
    2. `dash-bootstrap-components` (library of prebuilt dash components)
2. Download the `plotlydash.py` example app from this repository.
3. Launch the app by running the python file in your python environment (`python plotlydash.py`).
4. Open the app in your browser via http://localhost:8050.

## Jupyter Voila
Using [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/), interactive user widgets can be added to jupyter notebooks. In combination with [Juypter Voila](https://github.com/voila-dashboards/voila), these notebooks can be converted to web applications with a completely customizable user interface. Voila is particularly useful for converting existing notebooks into apps, but coding is less intuitive compared to streamlit and dash.

1. Install `voila` and its dependencies using `pip install voila` or `conda install voila`. Note that it is also recommended to install a JupyterLab preview extension for Voila, see this [Github page](https://github.com/voila-dashboards/voila) for more detailed set-up instructions.
2. Download the `jupytervoila.ipynb` notebook example from this repository.
3. To run the app, there are 2 options:
    1. If you have the Jupyter voila extension, open the notebook in Jupyter. You can edit the notebook as a basic notebook. To run the notebook in voila, click on the __Voila__ button located in the top menu.
    2. Alternatively, launch the app via the command line interface: Open a python console (e.g. Anaconda prompt) and run the command `voila jupytervoila.ipynb`.
3. Open the app in your browser via http://localhost:8866/.