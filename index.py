#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:14:24 2021

@author: thejeswarreddynarravala
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app


from apps import simulations, lockdown, policies



# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Projections", href="/Projections"),
        dbc.DropdownMenuItem("Lockdown Release Projections", href="/lockdown"),
        dbc.DropdownMenuItem("Policies", href="/policies"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A([
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        #dbc.Col(html.Img(src="/assets/virus.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Indian COVID-19 Projections",style={'font-size': '40px'})),
                      
                         
                    ],
                    #align="right",
                    no_gutters=True,
                ),dbc.Row([ 
                    html.P(dcc.Link('Computational Decision Science Laboratory', 
                                         href='https://sites.google.com/iit.edu/cdsl',target="_blank",
                                         style = {"color": "#ff1127",}),style = {'font-size': '20px','margin-left':"20px"}  ,id='submit-val'),]),
                dbc.Row([ 
                    html.P(dcc.Link( 'Illinois Institute of Technology', 
                                         href='https://www.iit.edu/',target="_blank",
                                         style = {"color": "#ff1127",}),style = {'font-size': '20px','margin-left':"20px"}  ,id='iit'),])
                    ],href="/home",
                
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return policies.layout
    elif pathname == '/lockdown':
        return lockdown.layout
    elif pathname == '/policies':
        return policies.layout
    else:
        return simulations.layout



if __name__ == '__main__':
    app.run_server(debug=True)
