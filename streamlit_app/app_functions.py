# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:41:31 2022

@author: RPM6364
"""


import streamlit as st
import pandas as pd
import numpy as np
from plotnine import *
datos = pd.read_csv(r'C:/Users/belengarcia/Downloads/curso_alertas/application_train.csv')

def set_slider():
    st.header('¿Cómo se obtienen las alertas?')
    st.subheader('Variables continuas')
    # Obtener el valor mínimo y máximo de la columna AMT_INCOME_TOTAL
    min_income = datos['AMT_INCOME_TOTAL'].min()
    max_income = 4678038.92
    x = st.slider('INGRESOS DEL CLIENTE',
                  min_value=min_income,
                  max_value=max_income,
                  value=min_income,
                  step = 100000.0,
                  format="$%.2f")

    # Filtrar los registros por debajo y por encima de x
    below_x = datos[datos['AMT_INCOME_TOTAL'] < x]
    above_x = datos[datos['AMT_INCOME_TOTAL'] >= x]
    
    # Contar morosos y no morosos por debajo de x
    morosos_below_x = below_x[below_x['TARGET'] == 1].shape[0]
    no_morosos_below_x = below_x[below_x['TARGET'] == 0].shape[0]
    
    # Contar morosos y no morosos por encima de x
    morosos_above_x = above_x[above_x['TARGET'] == 1].shape[0]
    no_morosos_above_x = above_x[above_x['TARGET'] == 0].shape[0]

   # Crear una tabla 2x2 con los resultados
    table_data = {
        'Debajo de ' + str(x): [morosos_below_x, no_morosos_below_x],
        'Encima de ' + str(x): [morosos_above_x, no_morosos_above_x]
    }
    
    index_labels = ['Morosos', 'No morosos']
    result_table = pd.DataFrame(table_data, index=index_labels)
    
    # Aplicar estilos a la tabla (morosos en rojo, no morosos en verde)
    def color_rows(row):
        if row.name == 'Morosos':
            return ['background-color: red'] * len(row)
        elif row.name == 'No morosos':
            return ['background-color: green'] * len(row)
        return [''] * len(row)

    # Aplicar estilo y mostrar la tabla
    styled_table = result_table.style.apply(color_rows, axis=1)

    st.write(f"Clientes con ingresos inferiores a {x} y su comportamiento de pago:")
    st.dataframe(styled_table)

def set_gini():
    st.header('¿Cómo se obtienen las alertas?')
    st.subheader('Variables continuas')
    # Obtener el valor mínimo y máximo de la columna AMT_INCOME_TOTAL
    min_income = datos['AMT_INCOME_TOTAL'].min()
    max_income = 4678038.92
    x = st.slider('INGRESOS DEL CLIENTE',
                  min_value=min_income,
                  max_value=max_income,
                  value=min_income,
                  step = 100000.0,
                  format="$%.2f")

    # Filtrar los registros por debajo y por encima de x
    below_x = datos[datos['AMT_INCOME_TOTAL'] < x]
    above_x = datos[datos['AMT_INCOME_TOTAL'] >= x]
    
    # Contar morosos y no morosos por debajo de x
    morosos_below_x = below_x[below_x['TARGET'] == 1].shape[0]
    no_morosos_below_x = below_x[below_x['TARGET'] == 0].shape[0]
    
    # Contar morosos y no morosos por encima de x
    morosos_above_x = above_x[above_x['TARGET'] == 1].shape[0]
    no_morosos_above_x = above_x[above_x['TARGET'] == 0].shape[0]

   # Crear una tabla 2x2 con los resultados
    table_data = {
        'Debajo de ' + str(x): [morosos_below_x, no_morosos_below_x],
        'Encima de ' + str(x): [morosos_above_x, no_morosos_above_x]
    }
    
    index_labels = ['Morosos', 'No morosos']
    result_table = pd.DataFrame(table_data, index=index_labels)
    
    # Aplicar estilos a la tabla (morosos en rojo, no morosos en verde)
    def color_rows(row):
        if row.name == 'Morosos':
            return ['background-color: red'] * len(row)
        elif row.name == 'No morosos':
            return ['background-color: green'] * len(row)
        return [''] * len(row)

    # Aplicar estilo y mostrar la tabla
    styled_table = result_table.style.apply(color_rows, axis=1)

    st.write(f"Clientes con ingresos inferiores a {x} y su comportamiento de pago:")
    st.dataframe(styled_table)

    gini_izq = 1- (morosos_below_x/below_x.shape[0])**2 - (no_morosos_below_x/below_x.shape[0])
    gini_dcha = 1- (morosos_above_x/above_x.shape[0])**2 - (no_morosos_above_x/above_x.shape[0])
    
    st.write(gini_izq)
    st.write(gini_dcha)