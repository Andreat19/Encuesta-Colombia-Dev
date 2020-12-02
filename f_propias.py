#!/usr/bin/env python
# coding: utf-8



import pandas as pd

def table(df,x_column,y_column):
    est ={}
    Máx = []
    Median = []
    Min = [] 
    leng = []
    name = x_column
    for i in df[x_column].unique():
        data = df[df[x_column] == i]
        leng.append(i)
        Máx.append(round(data[y_column].max(),1))
        Median.append(round(data[y_column].median(),1))
        Min.append(round(data[y_column].min(),1))
    est[name] = leng
    est['Max'] = Máx
    est['Median'] = Median
    est['Min'] = Min
    out = pd.DataFrame(est).sort_values('Max', ascending= False)
    return out.head(10)

def ingles2(x):
    if x ==  0:
        return 'Ninguno'
    elif x ==  1:
        return 'Básico'
        
    elif x == 2:
        return 'Intermedio'
    elif x == 3: 
        return 'Avanzado'
        
    elif x == 4:
        return 'Nativo'



def salario_vs_ingles(df,leng,exp,money):
    nivel = []
    Máx = []
    Median = []
    Min = []
    outcome = {}
    for i in range(0,5):
        data =  df[(df['Lenguaje más usado'] == leng) & (df['Experiencia en desarrollo de software'] == exp) & (df['Nivel de Ingles'] == i)]
        nivel.append(ingles2(i))
        Máx.append(round(data[money].max(),1))
        Median.append(round(data[money].median(),1))
        Min.append(round(data[money].min(),1))
    outcome['Nivel de Ingles'] = nivel
    outcome['Máx'] = Máx
    outcome['Median'] = Median
    outcome['Min'] = Min
    return pd.DataFrame(outcome)


def salario_vs_genero(df,money):
    Experiencia = []
    Máx_m = []
    Median_m = []
    Min_m = []
    Máx_w = []
    Median_w = []
    Min_w = []
    outcome = {}
    exp = ['menos de 1 año','1+ año','2+ años','3 - 5 años', '5 - 10 años','10 - 15 años','más de 15 años']
    for i in exp:
        data1 =  df[(df['Genero'] == 'él') & (df['Experiencia en desarrollo de software'] == i)].sort_values('Order by Exp')
        data2 =  df[(df['Genero'] == 'ella') & (df['Experiencia en desarrollo de software']== i)].sort_values('Order by Exp')
        Experiencia.append(i)
        
        Máx_m.append(round(data1[money].max(),1))
        Median_m.append(round(data1[money].median(),1))
        Min_m.append(round(data1[money].min(),1))
        
        Máx_w.append(round(data2[money].max(),1))
        Median_w.append(round(data2[money].median(),1))
        Min_w.append(round(data2[money].min(),1))
        
    outcome['Experiencia'] = Experiencia
    outcome['Máx - Hombres'] = Máx_m
    outcome['Máx - Mujeres'] = Máx_w
    outcome['Median - Hombres'] = Median_m
    outcome['Median - Mujeres'] = Median_w
    outcome['Min - Hombres'] = Min_m
    outcome['Min - Mujeres'] = Min_w
    return pd.DataFrame(outcome)


def table_exp(df):
    out = df.groupby(['Rol principal', 'Genero']).count()['Mercado']
    out = pd.DataFrame(out).reset_index().rename(columns={"Genero": "Genero","Mercado":"Cantidad"})
    return out

def filtro_exp_leng(df,leng,exp):
    data =  df[(df['Lenguaje más usado'] == leng) & (df['Experiencia en desarrollo de software'] == exp)]
    return data
    

def table_j(df, x_column,y_column):
    mediana = []
    maximo =[]
    counts = []
    column_in_x =[]
    k = {}
    for i in df[x_column].unique():
        column_in_x.append(i)
        m = round(df[df[x_column] == i][y_column].median(),2)
        m2 = round(df[df[x_column] == i][y_column].max(),2)
        c = round(df[df[x_column] == i][y_column].count(),2)
        maximo.append(m2)
        mediana.append(m)
        counts.append(c)
    k[x_column] = column_in_x
    k['Mediana de Ingresos'] = mediana
    k['Ingreso Máximo'] = maximo
    k['Encuestados'] = counts
    return pd.DataFrame(k).sort_values('Encuestados', ascending = False)[:20]


# In[18]:


def values_X(df,x_variable,y_variable):
    xp_values = []
    for i in df[x_variable].unique():
        x_values = []
        for j in df[y_variable].unique():
            s = df[(df[x_variable] == i)&(df[y_variable]== j)]['Rol'].count()
            x_values.append(s)
        div = sum(x_values)
        xp_values.append((x_values/div)*100)
    return xp_values






