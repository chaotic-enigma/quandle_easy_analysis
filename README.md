# quandle_easy_analysis
Qundle easy analysis with Python and Dash. All it needs is __Quandle API key__ and a python library __quandle__. These two things are very important along with other requirements such as

```
dash
dash_renderer
dash_core_components
dash_html_components
plotly
```
and of course

```
quandl
```
As usual __pip install <the_package_name>__ makes the installation work easy. If you have the above mentioned packages, you are good to go and analaze the [Quandle data](https://www.quandl.com/). Search for the dataset that is suitable for your objective (specifically NSE stock data), copy and paste the __python library code__, __qundle.get('NSE/KOTAKNIFTY')__ (just an examlpe) and  

```
from one_last_chance import easy_analysis

easy_analysis('specify_the_python_library_code')
```
and in your terminal
```
python3 file_name.py
```
you would see the graphs and plots on your default browser which is very graceful.
