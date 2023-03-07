#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def intro():
    import streamlit as st

    st.write("# Case 2 – Tech report/Blog")
    st.sidebar.success("Select a demo above.")

    st.markdown(
    """
    Streamlit is een open-source app framework wat specifiek is gemaakt voor
    Machine Learning en Data Science projecten.
    In dit project is een data-analyse gedaan over 2 datasets van kaggle.
    Om hier meer informatie over te lezen **👈 Selecteer dan een kleuze uit de balk hiernaast**.
    
    ### Opdrachtomschrijving
    Voor deze opdracht moet een tech report (blogpost) worden geschreven over een dataset naar keuze.
    Voor deze opdracht is zijnn de datasets math.csv en portugese.csv gekozen. Deze gaan over de 'alcohol-effects-on-study' en zijn te vinden op kaggle met behulp van onderstaande link:

    https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study
    
    * De data moet ingeladen worden via een openbare API.
        * Geprobeerd moet worden om meerdere datasets te combineren. (In dit geval worden de datasets over wiskunde en portugees dus gecombineerd.)
        * De data moet grondig verkend worden.

    * De data moet grondig geanalyseerd en bewerkt worden. Vervolgens worden de interessante inzichten worden gedeelt.
        * Nieuwe variabelen verkregen door data manipulatie
        * Beschrijvende analyses
        * Statistiek moet gebruikt worden
        * Voorspellende modellen

    * Je ondersteunt je verhaal met interactieve visualisaties middels streamlit

    * Je levert een gepubliceerde streamlit app op
    """
    )

def data_analyse():
    import streamlit as st
    import pandas as pd
    
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    
    st.write("# Case 2 – Tech report/Blog")
    
    st.write(
        """
        Op deze pagina is informatie te lezen over de volgende twee datasets van kaggele:
        * Maths.csv
        * Portugese.csv

        Deze datasets bevatten informatie over de cijfers van leerlingen die natuurkunde en wiskunde volgen op 2 scholen
        in Portugal en de informatie over hun alcoholgebruik etc.
        De datasets bevatten beide de volgende kolommen met bijbehorende omschrijving en informatie:
        """
    )
    
    variabelen = pd.read_excel('variables.xlsx', index_col = 0)
    st.table(variabelen)

    st.write(
        """
        test deze regel
        """
    )    

def grafieken():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        Hier komen grafieken te staan.
""")
    
    ## Data inladen m.b.v. csv
    math = pd.read_csv('Maths.csv')
    port = pd.read_csv('Portuguese.csv')

    # Voor het samenvoegen van de dataframes wil je straks nog wel weten welke rij bij welk vak hoorde
    math['subject'] = 'Wiskunde'
    port['subject'] = 'Portugees'

    # Dataframes math en port samenvoegen
    # https://datacarpentry.org/python-socialsci/11-joins/index.html#:~:text=We%20can%20join%20columns%20from,want%20using%20the%20how%20parameter.
    df = pd.concat([math, port])

    cat_G3 = []
    for G3 in df["G3"]:
        if G3 < 10 : cat_G3.append("F")
        elif G3 < 12: cat_G3.append("E")
        elif G3 < 14: cat_G3.append("D")
        elif G3 < 16: cat_G3.append("C")
        elif G3 < 18: cat_G3.append("B")    
        elif G3 <= 20: cat_G3.append("A")


    # Lijst als kolom toevoegen aan dataset
    df["Cat_G3"] = cat_G3
    
#     keuze = 'Wiskunde'

#     perc = df[df['subject'] == keuze].value_counts('Cat_G3') / df[df['subject'] == keuze].shape[0] * 100

#     # https://stackoverflow.com/questions/26097916/convert-pandas-series-to-dataframe
#     perc = pd.DataFrame({'Cat_G3':perc.index, 'percentages':perc.values})
#     perc = perc.sort_values(by=['Cat_G3'])
    
#     # https://plotly.com/python/pie-charts/#pie-chart-with-plotly-express
#     my_scale = [('A', "green"), ('E', "orange"), ('F', "red")]

#     fig = px.pie(perc,
#              values='percentages',
#              names='Cat_G3',
#              title='Titel',
#              color = 'percentages',
#              color_discrete_map={'A':'lightcyan',
#                                  'B':'cyan',
#                                  'C':'royalblue',
#                                  'D': 'darkblue',
#                                  'E': 'pink',
#                                  'F': 'blue'}
#             )

#     fig.update_traces(textposition='inside', textinfo='percent+label')
    
#     st.plotly_chart(fig)
    selectie = df[['traveltime','Cat_G3']].groupby(['traveltime','Cat_G3']).value_counts()
    selectie = pd.DataFrame(selectie, columns = ['aantal'])
    selectie = selectie.reset_index()
    selectie['tot_per_groep'] = selectie.groupby('traveltime')['aantal'].transform('sum')
    selectie['percentages'] = selectie['aantal']/selectie['tot_per_groep']*100
    selectie['traveltime'].replace([1,2,3,4],['1) < 15 min','2) 15 tot 30 min','3) 30 tot 60 min', '4) > 60 min'], inplace=True)
    
    hoogte_plot = (selectie['percentages'].max() + 10)
    
    fig = px.histogram(selectie,
                       y = 'percentages',
                       x = 'Cat_G3',
                       color = 'Cat_G3',
                       color_discrete_map={'A':'rgb(0,223,45)',
                                           'B':'rgb(0,223,45)',
                                           'C':'rgb(0,223,45)',
                                           'D':'rgb(0,223,45)',
                                           'E':'rgb(255,178,102)',
                                           'F': 'rgb(255,65,65)'},
                       animation_frame = 'traveltime',
                       animation_group = 'Cat_G3')

    fig.update_layout(title = 'Relatie tussen reistijd en de hoogte van de cijfers',
                      xaxis_title = 'Cijfergroep',
                      yaxis_title = 'Percentage',
                      legend_title = 'Cijfergroep')
    fig.update_yaxes(range = [0,hoogte_plot])

    fig['layout'].pop('updatemenus')

    st.plotly_chart(fig)


page_names_to_funcs = {
    "—": intro,
    "Data analyse": data_analyse,
    "grafieken": grafieken,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

