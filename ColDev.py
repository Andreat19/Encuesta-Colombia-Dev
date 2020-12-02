#!/usr/bin/env python
# coding: utf-8

# Importando Librerias Necesarias

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px 
import dash_table
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import f_propias
from f_propias import table, ingles2,salario_vs_ingles
import pandas as pd

# Importando Datos.

df = pd.read_csv('data_limpia.csv')
data = pd.read_csv('Comparativa_por_gen.csv')
available_lenguajes = df['Lenguaje más usado'].unique()
available_experiencia = df['Experiencia en desarrollo de software'].unique()
tabla_1 = pd.read_csv('tabla_1.csv')
tabla_1 = tabla_1.drop('Unnamed: 0', axis = 1).sort_values('Total', ascending = False)




# Página 1, Distribución de la muestra

layout_tabla1 =  go.Layout(
    title = "¿Ciudad de residencia?",
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )',
    )

layout_tabla2 =  go.Layout(
    title = "¿País de Origen?",
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )',
    )




# Figura 1 tabla de distribución 

data_geo1 = pd.DataFrame(df['Ciudad Residencia'].value_counts()).reset_index()
cities = data_geo1['index'][:10]
count = data_geo1['Ciudad Residencia'][:10]

t_ciudades = go.Table(
    header=dict(values=['Ciudad','Total'],
              fill_color='rgb(96,102,110)',
              font=dict(color='white', size=15),
              align='left'),
    cells=dict(
        values= [cities,count],
        fill_color='rgb(255, 255, 255 )',
        line_color='darkslategray',
        height=30,
        align='left'))

Ciudades = go.Figure(t_ciudades, layout_tabla1)

# Figura 2 tabla de distribución 

data_geo2 = pd.DataFrame(df['Origen'].value_counts()).reset_index()
country = data_geo2['index'][:10]
count_country = data_geo2['Origen'][:10]


t_paises = go.Table(
    header=dict(values=['País','Total'],
              fill_color='rgb(96,102,110)',
              font=dict(color='white', size=15),
              align='left'),
    cells=dict(
        values= [country,count_country],
        fill_color='rgb(255, 255, 255 )',
        line_color='darkslategray',
        height=30,
        align='left'))

Paises = go.Figure(t_paises, layout_tabla2)


#Selectores página 1

ys=['Rol principal', 'Nacionalidad','Genero']
xs= ['Nivel de ingles', 'Experiencia en desarrollo de software','Tipo de titulo','Moneda de Pago']

selec_p11 = dbc.Card([
    dbc.FormGroup([
        dbc.Label('Contratación por:'),
        dcc.Dropdown(id="drop_p11",
                     options=[{"label": i, "value": i} for i in ys
                    ],
                    value="Rol principal")]), 
])

selec_p12 = dbc.Card([
    dbc.FormGroup([
        dbc.Label('Distribución base'),
        dcc.Dropdown(id="drop_p12",
                     options=[{"label": i, "value": i} for i in ys
                    ],
                    value="Rol principal")]), 
    
    dbc.FormGroup([
        dbc.Label('Distribución secundaria'),
        dcc.Dropdown(id="drop_p13",
                     options=[{"label": j, "value": j} for j in xs
                    ],
                    value="Experiencia en desarrollo de software")])
])





page_1 = html.Div(
                     children = [
                         html.H1('Distribución de la muestra'),
                         
                         dbc.Row([
                             dbc.Col(dcc.Graph(id = 't-city', figure = Ciudades),
                                     width=12, lg = 6),
                             dbc.Col(dcc.Graph(id = 'c-country', figure = Paises),
                                     width=12, lg = 6)
                         ]),
                         
                        html.Hr(), 
                        html.H2("Contratación por tipo de empresa"),
                        dbc.Row([
                            dbc.Col(selec_p11,width=12, lg = 4),
                            dbc.Col(dcc.Graph(id = "Contratación"), width=12,lg = 8)
                        ], justify = 'center'),
                         
                        html.Hr(),
                        html.H2('Distribución Cruzada'),
                        dbc.Row([
                            dbc.Col(selec_p12,width=12, lg = 4),
                            dbc.Col(dcc.Graph(id = "Distribución-cliente"), width=12,lg = 8)
                        ], justify = 'center')
                         
])
                                                      


# Página 2

layout_tabla =  go.Layout(
    title = "¿Como prefiere que le llamemos?",
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    yaxis2 = {'anchor': 'x2', 'title': 'Cantidad'},
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )',
    width = 90)

layout_fig2 =  go.Layout(
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    yaxis2 = {'anchor': 'x2', 'title': 'Cantidad'},
    plot_bgcolor='rgb(226, 230, 230 )',
    paper_bgcolor='rgb(226, 230, 230 )')

layout_fig3 =  go.Layout(
    title = "Dispersón Experiencia Vs Salarios",
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    yaxis2 = {'anchor': 'x2', 'title': 'Cantidad'},
    plot_bgcolor='rgb(226, 230, 230 )',
    paper_bgcolor='rgb(226, 230, 230 )')

layout_fig4 =  go.Layout(
    title = "Mediana Salarial Vs Experiencia",
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    yaxis2 = {'anchor': 'x2', 'title': 'Cantidad'},
    plot_bgcolor='rgb(226, 230, 230 )',
    paper_bgcolor='rgb(226, 230, 230 )')



# Figura 1 tabla de distribución por generos

t1 = go.Table(header=dict(values=list(tabla_1.columns),
              fill_color='rgb(96,102,110)',
              font=dict(color='white', size=15),
              align='left'),
    cells=dict(
        values=[tabla_1['Genero'],tabla_1['Desarrollo'],tabla_1['Gerencia de Ingenieria'],tabla_1['Gestión de Proyectos'],tabla_1['Liderazgo Técnico'],tabla_1['Sin Clasificar'],tabla_1['Total']],
        fill_color='rgb(255, 255, 255 )',
        line_color='darkslategray',
        height=30,
        align='left'))


tabla = go.Figure(t1, layout_tabla)


        

#Figura 2 selectores de rol


selector = dbc.Card([
    dbc.FormGroup([
        dbc.Label('Distribución de Generos por Rol'),
        dcc.Dropdown(id="rol-value",
                     options=[{"label": col, "value": col} for col in tabla_1.columns[1:]
                    ],
                    value="Desarrollo")])
])

colors = ['rgb(9, 241, 225 )','rgb(233, 90, 140 )','rgb(28, 169, 228 )','rgb(195, 28, 228)','rgba(93, 88, 88 )']


# Definición de variables figura 3

df = df.sort_values('Order by Exp')

x1 = df[df['Genero'] == 'él']['Ingreso en dólares']
x2 = df[df['Genero'] == 'ella']['Ingreso en dólares']
x3 = df[df['Genero'] == 'AH-64 Apache']['Ingreso en dólares']
x4 = df[df['Genero'] == 'Ing']['Ingreso en dólares']
x5 = df[df['Genero'] == '[redactado]']['Ingreso en dólares']

y1 = df[df['Genero'] == 'él']['Experiencia en desarrollo de software']
y2 = df[df['Genero'] == 'ella']['Experiencia en desarrollo de software']
y3 = df[df['Genero'] == 'AH-64 Apache']['Experiencia en desarrollo de software']
y4 = df[df['Genero'] == 'Ing']['Experiencia en desarrollo de software']
y5 =  df[df['Genero'] == '[redactado]']['Experiencia en desarrollo de software']

fig_3 = go.Figure()

fig3_t0 = go.Scatter(
    x=x1, y=y1,
    name='Ellos',
    mode='markers',
    marker_color='rgb(9, 241, 225 )'
)

fig3_t1 = go.Scatter(
    x=x2, y=y2,
    name='Ellas',
    mode='markers',
    marker_color='rgb(233, 90, 140 )'
)

fig3_t2 = go.Scatter(
    x=x3, y=y3,
    name='AH-64 APACHE',
    mode='markers',
    marker_color='rgb(28, 169, 228 )'
)

fig3_t3 = go.Scatter(
    x=x4, y=y4,
    name='Ing',
    mode='markers',
    marker_color='rgb(195, 28, 228)'
)

fig3_t4 = go.Scatter(
    x=x5, y=y5,
    name='[redactado]',
    mode='markers',
    marker_color='rgba(93, 88, 88 )'
)


fig_3 = go.Figure([fig3_t0,fig3_t1,fig3_t2,fig3_t3,fig3_t4], layout=layout_fig3)



#Barras mediana salarial por experiencia


Experiencias = f_propias.salario_vs_genero(df,'Ingreso en dólares')['Experiencia']
men = f_propias.salario_vs_genero(df,'Ingreso en dólares')['Median - Hombres']
women = f_propias.salario_vs_genero(df,'Ingreso en dólares')['Median - Mujeres']

barras_1 = go.Bar( x=Experiencias,
    y=men,
    name='Hombres',
    marker_color='rgb(9, 241, 225 )'
)
barras_2 = go.Bar(x = Experiencias,
    y=women,
    name='Mujeres',
    marker_color='rgb(233, 90, 140 )'
)

bar = go.Figure([barras_1,barras_2],layout=layout_fig4)


tabs_p2 = dbc.FormGroup([
              dbc.Tabs(id="tabs-p2", active_tab = "barras", children = 
                  [dbc.Tab(label="Gráfico de dispersión", tab_id="scatter_1"),
                   dbc.Tab(label="Comparación salarial por genero", tab_id="barras"),
                    ],
                 ),
              html.Div(id = 'tab-content-p2')
])


# Estructura de la hoja 2

page_2  = html.Div(
                     children = [
                         html.H1('Exploración de Diversidad'),
                        dbc.Row([
                            dbc.Col(dcc.Graph(id = 'Tabla_1', figure = tabla),width=12, lg = 8),
                            dbc.Col([
                                 selector,
                                 dcc.Graph(id = 'Genero Rol')
                                 ],width=12, lg = 4, align = 'start')
                             ],justify = 'center',align="end"
                        ),

                        html.Hr(),
                        dbc.Row([
                        dbc.Col(tabs_p2)
                        ], justify = 'center')
                         
                     ],
)


# Página 3

selec_p31 = dbc.Card([
       dbc.FormGroup(
            [dbc.Label('Clasificar por: '),
            dcc.Dropdown(id='drop_p31',
                options=[{'label':'Rol', 'value': 'Rol principal'},
                        {'label':'Lenjuages más usado','value':'Lenguaje más usado'}],
                value='Rol principal')
            ]),
    dbc.FormGroup([
        dbc.Label('Ingreso en: '),
        dcc.RadioItems( id='drop_p32',
            options=[{'label': 'Dólares $', 'value': 'Ingreso en dólares'},
                    {'label':'Pesos COP', 'value': 'Ingreso en pesos'}],
            value='Ingreso en dólares')
            ])
])


taps_g1 = dbc.FormGroup([
              dbc.Tabs(id="tabs", active_tab ="scatter", children = 
                  [dbc.Tab(label="Gráfico de dispersión", tab_id="scatter"),
                   dbc.Tab(label="Tabla de estadísticas", tab_id="table"),
                    ],
                 ),
              html.Div(id = 'tab-content')
])

    
selec_p32 = dbc.Card([
    dbc.FormGroup([
        dbc.Label('Lenguaje que más usas'),
            dcc.Dropdown(id='drop_p33',
                options= [{'label': i, 'value': i} for i in available_lenguajes],
                value='Python')
    ]),
    
    dbc.FormGroup([
        dbc.Label('Experiencia en desarrollo'),
        dcc.Dropdown(id='drop_p34',
            options= [{'label': i, 'value': i} for i in available_experiencia],
            value= '3 - 5 años')
    ]),
    
    dbc.FormGroup([
        dbc.Label('Ingreso en: '),
        dcc.RadioItems(id='radio_p31',
            options=[{'label': 'Dólares $', 'value': 'Ingreso en dólares'},
                    {'label':'Pesos COP', 'value': 'Ingreso en pesos'}],
            value='Ingreso en dólares',
            labelStyle={'display': 'inline-block'}
            )        
    ])
])


taps_g2 = dbc.FormGroup([
              dbc.Tabs(id="tabs_2", active_tab ="line", children = [
                  dbc.Tab(label="Salario vs Nivel de Ingles", tab_id="line"),
                  dbc.Tab(label="Tabla de estadísticas", tab_id="table_2")]),
             html.Div(id = 'tab-content2')
    
])


page_3 = html.Div(
    [
        html.H1('Exploración de Ingresos'),
        html.Hr(),
        dbc.Row([
            dbc.Col(selec_p31,
                     width=12, lg =4 ),
            dbc.Col (taps_g1, width=12, lg = 8)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(selec_p32,width=12, lg =4 ),
            dbc.Col (taps_g2, width=12, lg = 8)
        ]),
])
        
        
        

# LLamados

PLOTLY_LOGO = "https://pbs.twimg.com/profile_images/639524779414843392/PINX5Chk_400x400.jpg"

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
server = app.server
app.config.suppress_callback_exceptions = True
nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

#Elementos de menú

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Distribución",
                            id = 'page_1'),
        dbc.DropdownMenuItem("Diversidad",
                            id="page_2"),
        dbc.DropdownMenuItem("Gráficas Salariales",
                            id="page_3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
    id="dropdownmenu",
)

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px"), 
                               ),
                        dbc.Col(dbc.NavbarBrand("Encuesta Colombia Dev 2020", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                    
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)


app.layout =html.Div(
   
    [logo,
    dbc.Container([
        html.Div(id = "view_port", className = 'mf_12')],fluid = True
        )],
)


# LLamados navegador 

@app.callback(
    Output("dropdownmenu", "label"),
    [Input("page_1", "n_clicks"), Input("page_2", "n_clicks"), Input("page_3", "n_clicks")],
)


#Identificar la página abierta
def update_label(n1, n2, n3):
    id_lookup = {"page_1": "Distribución", "page_2": "Diversidad", "page_3":"Gráficas salariales"}
    ctx = dash.callback_context

    if (n1 is None and n2 is None) or not ctx.triggered:
        return "Menu"
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    return id_lookup[button_id]

#Cambiar página
@app.callback(
    Output("view_port", "children"),
    [Input("page_1", "n_clicks"), Input("page_2", "n_clicks"), Input("page_3", "n_clicks")],
)

def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'page_1' in changed_id:
        return page_1
    elif 'page_2' in changed_id:
        return page_2
    elif 'page_3':
        return page_3
    

# LLamados Página 1

@app.callback(
    Output("Distribución-cliente", "figure"),
    [Input("drop_p12", "value"),
    Input("drop_p13", "value")]
)

def graph_sunburst (x_variable,y_variable):
    
    fig = px.sunburst(df, path= [x_variable,y_variable], color = x_variable)
    return fig.update_layout(
    margin = dict(t=0, l=0, r=0, b=0),
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )')

 
@app.callback(
    Output("Contratación", "figure"),
    [Input("drop_p11", "value")]
)

def graph_bar(x_variable):
    
    fig = px.bar(df, x= 'Tipo de Empresa', y= 'count', color = x_variable,
             barmode='group',
             )
    return fig.update_layout(
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )')


    
# Llamados página 2

@app.callback(
    Output("Genero Rol", "figure"),
    [Input("rol-value", "value")],
)

def pie_grah(x_variable):
    label = tabla_1[tabla_1[x_variable] != 0]['Genero']
    value = tabla_1[tabla_1[x_variable] != 0][x_variable]
    data = go.Pie(labels=label, values= value)
    fig= go.Figure(data, layout=layout_fig2)
    fig.update_traces(hoverinfo='label+percent',
                  marker=dict(colors=colors, line=dict(color='#000000', width=1)))
    return fig.update_layout(
    margin = dict(t=0, l=0, r=0, b=0),
    font = dict(
      size = 15,
      color = 'rgb(51, 54, 54 )'
    ),
    plot_bgcolor='rgb(255, 255, 255 )',
    paper_bgcolor='rgb(255, 255, 255 )')
    


@app.callback(Output('tab-content-p2', 'children'),
              [Input('tabs-p2', 'active_tab')]
             )


def graph_gen(t1):
    if t1 == 'scatter_1': 
        return dcc.Graph(id = 'Dispersión', figure = fig_3)
    elif t1 == 'barras':
        return dcc.Graph(id = 'Barras', figure = bar)


# Llamados página ingresos

@app.callback(Output('tab-content', 'children'),
              [Input('tabs', 'active_tab'),
               Input('drop_p31', 'value'),
               Input('drop_p32', 'value')]
             )

def render_content(tab,x_column,y_column):
    if tab == 'scatter':
        data_grah = f_propias.table_j(df,x_column, y_column)
        fig = px.scatter(data_grah, x="Encuestados", y="Mediana de Ingresos", color=x_column,size = 'Ingreso Máximo')
        
        fig.update_layout(title_text="Distribución de Ingresos",
            plot_bgcolor='rgb(226, 230, 230 )',
            paper_bgcolor='rgb(226, 230, 230 )',
            font_color= 'rgb(51, 54, 54 )')
        
        return html.Div([
            dcc.Graph(
            id='Salarios',figure = fig) 
        ])
    
    
    elif tab == 'table':
        data_table = f_propias.table(df,x_column,y_column)
        colorscale = [[ 0 , 'rgb(52,58,64)' ], [ 0.5 , 'rgb(226, 230, 230 )'], [ 1 ,'rgb(226, 230, 230 )']]
        table1 = ff.create_table(data_table,height_constant = 60 , colorscale = colorscale)
        return html.Div(
            dcc.Graph(id = 'Estadísticas por Nivel de Ingles', figure = table1)
           
                                )
    
# Llamado pagina Salarios
    
@app.callback(Output('tab-content2', 'children'),
              [Input('tabs_2','active_tab'),
               Input('drop_p33', 'value'),
               Input('drop_p34', 'value'),
               Input('radio_p31', 'value')]
             )  
    
def outcome_nivel(tab2,leng,exp,money):
    if tab2 == 'line':
        
        # Defino datos y variables
        data_grah =  f_propias.filtro_exp_leng(df,leng,exp)
        y1 = data_grah[data_grah['Nivel de Ingles'] == 1][money]
        y2 = data_grah[data_grah['Nivel de Ingles'] == 2][money]
        y3 =data_grah[data_grah['Nivel de Ingles'] == 3][money]
        y4 = data_grah[data_grah['Nivel de Ingles'] == 4][money]
        
        #Defino los boxs
        fig = go.Figure()

        fig.add_trace(go.Box(
            y=y1,
            name="Basico",
            boxpoints='outliers', # only outliers
            marker_color='rgb(233, 90, 140 )',
            line_color='rgb(233, 90, 140)'
        ))

        fig.add_trace(go.Box(
            y=y2,
            name="Intermedio",
            boxpoints='outliers', # only outliers
            marker_color='rgb(195, 28, 228)',
            line_color='rgb(195, 28, 228 )'
        ))

        fig.add_trace(go.Box(
           y=y3,
           name="Avanzado",
           boxpoints='outliers', # only outliers
           marker_color='rgb(28, 169, 228 )',
           line_color='rgb(28, 169, 228 )'
        ))
        fig.add_trace(go.Box(
           y=y4,
           name="Nativo",
           boxpoints='outliers', # only outliers
           marker_color='rgb(9, 241, 225)',
           line_color='rgb(9, 241, 225 )'
        ))
 
        fig.update_layout(title_text="Box Salarios por Nivel de Ingles",
            plot_bgcolor='rgb(226, 230, 230 )',
            paper_bgcolor='rgb(226, 230, 230 )',
            font_color= 'rgb(51, 54, 54 )')

        
        return html.Div([
                dcc.Graph(id='Salarios y Nivel de Ingles',figure = fig )
        ])

   
    elif tab2 == 'table_2':
        
        data_table =  f_propias.salario_vs_ingles(df,leng,exp,money)
        colorscale = [[ 0 , 'rgb(52,58,64)' ], [ 0.5 , 'rgb(226, 230, 230 )'], [ 1 ,'rgb(226, 230, 230 )']]
        table2 = ff.create_table(data_table,height_constant = 60 , colorscale = colorscale)
        return html.Div(
            dcc.Graph(id = 'Estadísticas por Nivel de Ingles', figure = table2))



if __name__ == "__main__":
    app.run_server()







