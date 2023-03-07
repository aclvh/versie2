#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    Hieronder zal de opdrachtomschrijving van het project worden uitgelegd.
    Om vervolgens meer informatie over het project te lezen **👈 Selecteer dan een keuze uit de balk hiernaast**.
    
    ## Opdrachtomschrijving
    Voor deze opdracht moet een tech report (blogpost) worden geschreven over een dataset naar keuze.
    Voor deze opdracht is zijn de datasets Maths.csv en Portugese.csv gekozen. Deze gaan over de 'alcohol-effects-on-study'
    en zijn te vinden op kaggle met behulp van onderstaande link:

    https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study
    
    * De data moet ingeladen worden via een openbare API.
        * Geprobeerd moet worden om meerdere datasets te combineren. (In dit geval worden de datasets over wiskunde en
        Portugees dus gecombineerd.)
        * De data moet grondig verkend worden.

    * De data moet grondig geanalyseerd en bewerkt worden. Vervolgens worden de interessante inzichten worden gedeelt.
        * Nieuwe variabelen verkregen door data manipulatie
        * Beschrijvende analyses
        * Statistiek moet gebruikt worden
        * Voorspellende modellen

    * Je ondersteunt je verhaal met interactieve visualisaties middels streamlit

    * Je levert een gepubliceerde streamlit app op""")

def data_analyse():
    import streamlit as st
    import pandas as pd
    
    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')    
    
    # Informatie over wat er te lezen is op deze pagina
    st.write("""
        Op deze pagina is informatie te lezen over de volgende twee datasets van kaggele:
        * Maths.csv
        * Portugese.csv

        Deze datasets bevatten informatie over de cijfers van leerlingen die natuurkunde en wiskunde volgen op 2 scholen
        in Portugal en de informatie over hun alcoholgebruik etc.
        
        De datasets zijn ingeladen met behulp van een API. Door een aantal dingen juist te installeren op een laptop kan een API command
        van de datasets worden gekopieerd vanaf Kaggle. Met behulp van deze link kunnen de datasets worden ingeladen op de computer,
        maar kunnen deze ook geünzipt worden. Hierna zullen ze met behulp van pd.read_csv worden ingelezen.
        Met behulp van welke code dit gedaan wordt is hieronder te zien:
        """)
    
    
    # API en data inladen
    code_API ="""
        # Data inladen m.b.v API
        !kaggle datasets download -d whenamancodes/alcohol-effects-on-study
        !unzip mxmh-survey-results.zip

        # Data inladen m.b.v. csv
        Maths = pd.read_csv('Maths.csv')
        Portugese = pd.read_csv('Portuguese.csv')"""
    st.code(code_API, language = 'python')
    
    Maths = pd.read_csv('Maths.csv')
    Portugese = pd.read_csv('Portuguese.csv')
    
    
    # Kolommen datasets en extra informatie
    st.write("""
        De datasets bevatten beide de volgende kolommen met bijbehorende omschrijving en informatie:""")
    
    variabelen = pd.read_excel("variables.xlsx", index_col = 0)
    st.table(variabelen)

    code_formaat = """
        # Aantal rijen en kolommen dataframe printen
        print('Wiskunde dataframe bestaat uit ', Maths.shape[0], ' rijen en ', Maths.shape[1], ' kolommen.')
        print('Portugees dataframe bestaat uit ', Portugese.shape[0], ' rijen en ', Portugese.shape[1], ' kolommen.')
        print()

        # https://datatofish.com/count-nan-pandas-dataframe/
        print('Aantal missing values in wiskunde dataframe: ', Maths.isna().sum().sum())
        print('Aantal missing values in portugees dataframe: ', Portugese.isna().sum().sum())

        totaal_rijen_samengevoegd_straks = Maths.shape[0] + Portugese.shape[0]
        print('Wanneer de dataframes samen worden gevoegd bestaat deze uit ', totaal_rijen_samengevoegd_straks, 'aantal rijen')"""
    st.code(code_formaat, language = 'python')
    
    st.write("""
        * Wiskunde dataframe bestaat uit  395  rijen en  33  kolommen en heeft geen missing values.
        * Portugees dataframe bestaat uit  649  rijen en  33  kolommen en heeft geen missing values.""")
    
    code_desc_math = """Maths.describe()"""
    st.code(code_desc_math, language = 'python')
    math_desc = Maths.describe()
    st.write(math_desc)
    
    code_desc_port = """Portugese.describe()"""
    st.code(code_desc_port, language = 'python')
    port_desc = Portugese.describe()
    st.write(port_desc)
    
    
    # Datasets samenvoeegen
    st.write("""
        Aangezien beide tabellen exact dezelfde kolommen bevatten (ze zijn ook hetzelfde geschreven) en geen opvallende waarden
        bevatten kunnen de datasets worden gejoind met behulp van 'concat'. Echter is dan niet meer zichtbaar welke rij over
        welk vak gaat. Vandaar dat eerst een extra kolom wordt toegevoegd aan beide dataset waarin te zien is over welk vak
        die rij gaat. Hieronder wordt het stuk code laten zien waarmee dat wordt gedaan en wordt ook laten zien hoe vervolgens
        de datasets samengevoegd zijn.""")
    
    code_samenvoegen = """
        # Voor het samenvoegen van de dataframes wil je straks nog wel weten welke rij bij welk vak hoorde
        Maths['subject'] = 'Wiskunde'
        Portugese['subject'] = 'Portugees'
        
        # Dataframes Maths en Portugese samenvoegen
        df = pd.concat([Maths, Portugese])
        """
    st.code(code_samenvoegen, language = 'python')
    
    Maths['subject'] = 'Wiskunde'
    Portugese['subject'] = 'Portugees'
    df = pd.concat([Maths, Portugese])
    
    aantal_rijen = df.shape[0]
    aantal_kolommen = df.shape[1]
    
    st.write("De dataset ziet er nu als volgt uit:", df, "De dataset bestaat nu uit ", aantal_rijen, " rijen en ",
        aantal_kolommen, " aantal_kolommen. Verder bevat de dataset dus 0 missing values.")
    

def grafieken():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write("""
        Op deze pagina zijn grafieken te vinden van situaties die team 10 graag wilde onderzoeken.
        Heeft de hoeveelheid dagelijkse alcoholgebruik invloed op het uiteindelijke cijfer? Halen leerlingen minder hoge
        cijfers ze een langere reistijd hebben naar school? Dit zijn enkele vragen die beantwoord worden op deze pagina.
        Eerst zullen twee grafieken worden getoond met informatie over beide vakken.
        Vervolgens kan voor verschillende grafieken informatie gekregen worden over een specifiek vak
        **👈 Hiervoor kan een keuze worden gemaakt in de balk hiernaast**""")
    
    ## Data inladen m.b.v. csv
    Maths = pd.read_csv('Maths.csv')
    Portugese = pd.read_csv('Portuguese.csv')

    # Voor het samenvoegen van de dataframes wil je straks nog wel weten welke rij bij welk vak hoorde
    Maths['subject'] = 'Wiskunde'
    Portugese['subject'] = 'Portugees'

    # Dataframes math en port samenvoegen
    # https://datacarpentry.org/python-socialsci/11-joins/index.html#:~:text=We%20can%20join%20columns%20from,want%20using%20the%20how%20parameter.
    df_sameng = pd.concat([Maths, Portugese])

    cat_G3 = []
    for G3 in df_sameng["G3"]:
        if G3 < 10 : cat_G3.append("F")
        elif G3 < 12: cat_G3.append("E")
        elif G3 < 14: cat_G3.append("D")
        elif G3 < 16: cat_G3.append("C")
        elif G3 < 18: cat_G3.append("B")    
        elif G3 <= 20: cat_G3.append("A")
    # Lijst als kolom toevoegen aan dataset
    df_sameng["Cat_G3"] = cat_G3
    
    # Keuezevak voor vak: Wiskunde of Portugees
    InvoerVak = st.sidebar.selectbox('Selecteer het vak', ('Wiskunde','Portugees'))
    df = df_sameng[df_sameng['subject']==InvoerVak]
    
    ##################################################
    kleuren_cijfer = {'A':'rgb(0,223,45)',
                      'B':'rgb(0,223,45)',
                      'C':'rgb(0,223,45)',
                      'D':'rgb(0,223,45)',
                      'E':'rgb(255,178,102)',
                      'F': 'rgb(255,65,65)'}
    
    #############################################################################################################
    # Grafiek over verdeling van de eindcijfers per vak en geslacht
    st.write("""
        ## Verdeling van de eindcijfers per vak en geslacht
        In onderstaande grafiek worden de resultaten van een vak vergeleken voor elk geslacht.""")
    
    fig = px.box(df_sameng,
             x = "sex",
             y = "G3",
             title = "Verdeling eindcijfers per vak en geslacht",
             color = 'sex',
             facet_col  = 'subject',
             labels = {'G3': 'Eindcijfer',
                       'sex': 'Geslacht'})

    newnames = {"F":"Vrouw", "M": "Man"}

    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))

    fig.update_xaxes(ticktext=["Man", "Vrouw"],
                     tickvals=["M", "F"])

    st.plotly_chart(fig)
    
    st.write("""
        Uit deze grafiek blijkt dat vrouwen over het algemeen iets hogere cijfers halen bij Portugees dan mannen.
        Ook blijkt dat mannen over het algemeen iets hogere cijfers halen bij wiskunde van vrouwen.""")
    
    ###################################################################################################################
    # Plot traveltime and G3
    st.write("""
        ## Invloed van reistijd op studieresultaten
        In onderstaande grafiek worden de resultaten van een vak onderverdeeld in de categorieën A t/m F. Vervolgens is
        af te lezen hoeveel procent van de leerlingen dat eindcijfer hebben behaald.""")
    
    # Dataframe plot traveltime and G3
    selectie = df[['traveltime','Cat_G3']].groupby(['traveltime','Cat_G3']).value_counts()
    selectie = pd.DataFrame(selectie, columns = ['aantal'])
    selectie = selectie.reset_index()
    selectie['tot_per_groep'] = selectie.groupby('traveltime')['aantal'].transform('sum')
    selectie['percentages'] = selectie['aantal']/selectie['tot_per_groep']*100
    selectie['traveltime'].replace([1,2,3,4],['1) < 2 uur','2) 2 tot 5 uur','3) ', '4) > 60 min'], inplace=True)
    
    # Plot traveltime and G3
    hoogte_plot = (selectie['percentages'].max() + 10)
    
    fig = px.histogram(selectie,
                       y = 'percentages',
                       x = 'Cat_G3',
                       color = 'Cat_G3',
                       color_discrete_map = kleuren_cijfer,
                       animation_frame = 'traveltime',
                       animation_group = 'Cat_G3')

    fig.update_layout(title = 'Relatie tussen reistijd en de hoogte van de cijfers',
                      xaxis_title = 'Cijfergroep',
                      yaxis_title = 'Percentage',
                      legend_title = 'Cijfergroep')
    fig.update_yaxes(range = [0,hoogte_plot])
    
    fig['layout'].pop('updatemenus')
    
    st.plotly_chart(fig)
    
    st.write("""
        Uit deze grafiek blijkt dus dat mensen minder hoge cijfers halen wanneer zij een langere reistijd naar school hebben.
        """)
    
    ###################################################################################################################
    # Plot studytime and G3
    st.write("""
        ## Invloed van de hoeveelheid studietijd op studieresultaten
        In onderstaande grafiek worden de resultaten van een vak onderverdeeld in de categorieën A t/m F. Vervolgens is
        af te lezen hoeveel procent van de leerlingen dat eindcijfer hebben behaald bij een bepaalde categorie studietijd.""")
    selectie1 = df[['studytime','Cat_G3']].groupby(['studytime','Cat_G3']).value_counts()
    selectie1 = pd.DataFrame(selectie1, columns = ['aantal'])
    selectie1 = selectie1.reset_index()
    selectie1['tot_per_groep'] = selectie1.groupby('studytime')['aantal'].transform('sum')
    selectie1['percentages'] = selectie1['aantal']/selectie1['tot_per_groep']*100
    selectie1['studytime'].replace([1,2,3,4],['1) < 2 uur','2) 2 tot 5 uur','3) 5 tot 10 uur', '4) > 10 uur'], inplace=True)

    # Plot traveltime and G3
    hoogte_plot = (selectie1['percentages'].max() + 10)

    fig = px.histogram(selectie1,
                        y = 'percentages',
                        x = 'Cat_G3',
                        color = 'Cat_G3',
                        color_discrete_map = kleuren_cijfer,
                        animation_frame = 'studytime',
                        animation_group = 'Cat_G3')

    fig.update_layout(title = 'Relatie tussen studietijd en de hoogte van de cijfers',
                      xaxis_title = 'Cijfergroep',
                      yaxis_title = 'Percentage',
                      legend_title = 'Cijfergroep')

    fig.update_yaxes(range = [0,hoogte_plot])
    
    st.plotly_chart(fig)
    
    st.write("""
        Uit deze grafiek blijkt dus dat mensen minder hoge cijfers halen wanneer zij een langere reistijd naar school hebben.
        """)
    
    ###################################################################################################################
    # Plot Dalc and G3
    st.write("""
        ## Invloed van dagelijks alcoholgebruik op studieresultaten""")
    
    fig = px.box(df,
                 x = "Dalc",
                 y = "G3")
    st.plotly_chart(fig)
    


page_names_to_funcs = {
    "Opdrachtomschrijving": intro,
    "Data analyse": data_analyse,
    "Grafieken": grafieken,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

