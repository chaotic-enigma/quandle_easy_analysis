import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import quandl
import plotly.graph_objs as go
import auth

def easy_analysis(quandl_dataset):
	api_key = auth.key

	df = quandl.get(quandl_dataset,authtoken=api_key)
	df = df.reset_index()

	app = dash.Dash(__name__)

	app.layout = html.Div([
			html.H3(quandl_dataset),
			dcc.Dropdown(
					id='data_columns',
					options=[{'label' : s,'value' : s} for s in df.columns[1:]],
					value=['Open'],
					multi=True
				),
			dcc.Graph(id='column_graph')
		])

	@app.callback(
			Output('column_graph','figure'),
			[Input('data_columns','value')]
		)

	def draw_graph(data_columns):
		graphs = []

		for column in data_columns:
			graphs.append(go.Scatter(
					x=list(df.Date),
					y=list(df[column]),
					name=str(column),
					mode='lines'
				))

		return {'data' : graphs}

	app.run_server(debug=True)
