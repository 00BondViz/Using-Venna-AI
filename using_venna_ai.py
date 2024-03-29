# -*- coding: utf-8 -*-
"""Using_Venna_AI

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yc-hwkd9NKIlqFxoON1pIC_B9pyXNUyk
"""

!pip install vanna

#This part of the code speaks to the dependencies needed
import vanna
from vanna.remote import VannaDefault

# Venna requires use of api key, of which one can use instead of email everytime they would want to use it
api_key = vanna.get_api_key('00BondViz@gmail.com')

# For this demo we are going to use a public database known as Chinook Database
# https://www.sqlitetutorial.net/sqlite-sample-database/
vanna_model_name = 'chinook' # This is the name of the RAG model. This is typically associated with a specific dataset.
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

# This part of the code speaks to the connection to the desired database
# You can connect to any SQL database, for the sake of the demo we are using SQLlite
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

# With the use of the vn.ask we can ask questions and it will generate SQL queries and show tables and generate a chart
vn.ask("What are the top 5 artists by sales?")

vn.ask("What are the top 5 playlists with the most tracks?")

vn.ask("What are the top 5 media types that are most frequently purchased?")

# using flask with Venna
from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run()