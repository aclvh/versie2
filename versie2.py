#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# In[ ]:


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


# In[ ]:


def data_analyse():
    import streamlit as st
    import pandas as pd
    from IPython import get_ipython
    
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
        # data inladen via API
        !kaggle datasets download -d whenamancodes/alcohol-effects-on-study
        !unzip alcohol-effects-on-study.zip

        # Data inladen m.b.v. csv
        Maths = pd.read_csv('Maths.csv')
        Portugese = pd.read_csv('Portuguese.csv')"""
    st.code(code_API, language = 'python')
    
#     !kaggle datasets download -d whenamancodes/alcohol-effects-on-study
#     !unzip alcohol-effects-on-study.zip
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
    
    
    # Datasets samenvoegen
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


# In[1]:


def grafieken():
    import streamlit as st
    import pandas as pd
    import plotly.express as px
    #from IPython import get_ipython
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write("""
        Op deze pagina zijn grafieken te vinden van situaties die team 10 graag wilde onderzoeken.
        Heeft de hoeveelheid dagelijkse alcoholgebruik invloed op het uiteindelijke cijfer? Halen leerlingen minder hoge
        cijfers ze een langere reistijd hebben naar school? Dit zijn enkele vragen die beantwoord worden op deze pagina.
        Eerst zullen twee grafieken worden getoond met informatie over beide vakken.
        Vervolgens kan voor verschillende grafieken informatie gekregen worden over een specifiek vak
        **👈 Hiervoor kan een keuze worden gemaakt in de balk hiernaast**""")
    
    ###################################################################################################################
    # Datasets inladen en aanpassen
    ###################################################################################################################
    
#     !kaggle datasets download -d whenamancodes/alcohol-effects-on-study
#     !unzip alcohol-effects-on-study.zip
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
    
    ###################################################################################################################
    # Keuezevak voor vak: Wiskunde of Portugees
    InvoerVak = st.sidebar.selectbox('Selecteer het vak', ('Wiskunde','Portugees'))
    df = df_sameng[df_sameng['subject']==InvoerVak]
    
    ###################################################################################################################
    # Kleurenpallet voor plotjes
    kleuren_cijfer = {'A':'rgb(0,223,45)',
                      'B':'rgb(0,223,45)',
                      'C':'rgb(0,223,45)',
                      'D':'rgb(0,223,45)',
                      'E':'rgb(255,178,102)',
                      'F': 'rgb(255,65,65)'}
    
    kleuren_alcoholgebruik = {"1) erg laag" : "rgb(255,0,0)",
                             "2) laag" : "rgb(255,65,65)",
                             "3) gemiddeld" : "rgb(255,178,102)",
                             "4) hoog" : "rgb(0,233,45)",
                             "5) erg hoog" : "rgb(0,255,0)"}
    
    ###################################################################################################################
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
    # Plot health and Dalc
    st.write("""
        ## Invloed van alcoholgebruik op de gezondheid
        Hier kun je het alcoholgebruik doordeweeks selecteren. Er zal dan een pie chart getoond worden waarin de gezondheidstatus 
        verdeling wordt weergegeven van de studenten met het geselecteerde alcohol gebruik. """)
    
    piedf = df_sameng.value_counts(["Dalc", "health"]).reset_index()
    piedf.rename(columns = {0: "aantal"}, inplace = True)
    piedf = piedf.sort_values(by=["Dalc"])
    
    piedf['Dalc'].replace([1,2,3,4,5],
                       ['1) erg laag','2) laag','3) gemiddeld', '4) hoog', '5) erg hoog'],
                       inplace=True)

    piedf['health'].replace([1,2,3,4,5],
                            ['1) uitstekende gezondheid', '2) goede gezondheid', '3) redelijke gezondheid',
                             '4) matige gezondheid', '5) slechte gezondheid'], inplace=True)
    
    st.write("Hoeveelheid alcoholgebruik doordeweeks")
    
    check_dalc1 = st.checkbox('1) erg laag')
    check_dalc2 = st.checkbox('2) laag')
    check_dalc3 = st.checkbox('3) gemiddeld')
    check_dalc4 = st.checkbox('4) hoog')
    check_dalc5 = st.checkbox('5) erg hoog')
    
    if check_dalc1:
        piedf = piedf[piedf['Dalc'] == '1) erg laag']
        fig_dalc1 = px.pie(data_frame = piedf,
                           values = "aantal",
                           names = "health")
        fig_dalc1.update_layout(title = "Gezondheid van de studenten",
                                legend_title = 'Gezondheidsstatus van de studenten')
        st.plotly_chart(fig_dalc1)
    
    if check_dalc2:
        piedf = piedf[piedf['Dalc'] == '2) laag']
        fig_dalc2 = px.pie(data_frame = piedf,
                           values = "aantal",
                           names = "health")
        fig_dalc2.update_layout(title = "Gezondheid van de studenten",
                                legend_title = 'Gezondheidsstatus van de studenten')
        st.plotly_chart(fig_dalc2)
    
    if check_dalc3:
        piedf = piedf[piedf['Dalc'] == '3) gemiddeld']
        fig_dalc3 = px.pie(data_frame = piedf,
                           values = "aantal",
                           names = "health")
        fig_dalc3.update_layout(title = "Gezondheid van de studenten",
                                legend_title = 'Gezondheidsstatus van de studenten')
        st.plotly_chart(fig_dalc3)
    
    if check_dalc4:
        piedf = piedf[piedf['Dalc'] == '4) hoog']
        fig_dalc4 = px.pie(data_frame = piedf,
                           values = "aantal",
                           names = "health")
        fig_dalc4.update_layout(title = "Gezondheid van de studenten",
                                legend_title = 'Gezondheidsstatus van de studenten')
        st.plotly_chart(fig_dalc4)
    
    if check_dalc5:
        piedf = piedf[piedf['Dalc'] == '5) erg hoog']
        fig_dalc5 = px.pie(data_frame = piedf,
                           values = "aantal",
                           names = "health")
        fig_dalc5.update_layout(title = "Gezondheid van de studenten",
                                legend_title = 'Gezondheidsstatus van de studenten')
        st.plotly_chart(fig_dalc5)
    
    st.write("""
        Uit deze grafieken blijkt dat er niet een direct verband is tussen het alcohol gebruik door de weeks en de
        gezondheidsstatus van de studenten. Dit kan komen doordat ziektes niet gerelateerd zijn het alcoholgebruik """)
    
    
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
    selectie['percentages'] = round(selectie['aantal']/selectie['tot_per_groep']*100,2)
    selectie['traveltime'].replace([1,2,3,4],['1) < 15 min','2) 15 tot 30 min','3) 30 tot 60 min', '4) > 60 min'], inplace=True)
    
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
    selectie1['percentages'] = round(selectie1['aantal']/selectie1['tot_per_groep']*100,2)
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
        Uit deze grafiek is goed te zien dat wanneer er meer tijd in de studie gaat het percentage dat een "E" of een "F" haalt
        lager wordt
        """)
    
    ###################################################################################################################
    # Plot Dalc and G3
    st.write("""
        ## Invloed van de hoeveelheid door de weeks alcoholgebruik op studieresultaten
        In onderstaande grafiek worden de verdelingen van de resultaten van een vak per niveau alcoholgebruik getoond
        voor het gekozen vak.""")
    df['Dalc'].replace([1,2,3,4,5],
                       ['1) erg laag','2) laag','3) gemiddeld', '4) hoog', '5) erg hoog'],
                       inplace=True)
    fig = px.box(df,
                 x = "Dalc",
                 y = "G3",
                # color = "G3",
                # color_discrete_map = kleuren_alcoholgebruik)

    fig.update_layout(title = 'Relatie tussen alcoholgebruik (door de weeks) en de hoogte van de cijfers',
                      xaxis_title = 'Door de weeks alcoholgebruik',
                      yaxis_title = 'Eindcijfer')
    
    st.plotly_chart(fig)
    
    st.write("""
        Uit deze grafiek blijkt dat het alcohol gebruik niet direct een invloed heeft op het behaalde cijfer. Namelijk als het
        alcoholgebruik "erg hoog" is, halen deze student doorgaans een hoger cijfer dan de anderen. Wel is goed te zien dat 
        Mensen die geen of weinig alcohol drinken door de weeks hogere cijfers kunnen halen
        """)
    
    ###################################################################################################################
    # Plot age en G3 met dropdown!
    st.write("""
    ## Invloed van de leeftijd van een student op het behaalde resultaat
    In de onderstaande grafiek wordt de relatie weergegeven tussen de leeftijd van een student en het resultaat dat de
    student had behaald voor het vak.""")
    
    
    InvoerSchool = st.selectbox("# Selecteer een school:", ("Gabriel Pereira", "Mousinho da Silveira"))
    
    df_tijdelijk= df
    df_tijdelijk["school"].replace(["GP","MS"],
                     ["Gabriel Pereira", "Mousinho da Silveira"],
                    inplace = True)
    
    df_school = df_tijdelijk[df_tijdelijk["school"] == InvoerSchool]
    
    fig_school = px.box(data_frame=df_school,
          x = "age",
          y = "G3")

    st.plotly_chart(fig_school)
    
    st.write("""
        Uit deze grafiek blijkt dat er op Gabriel Pereira oudere studenten zitten. De oudere studenten halen lagere cijfers
        dan de studenten die tussen 15 en 20 zijn. Verder zijn de cijfers van de studenten in deze leeftijdscategorie aardig 
        geljk
        """)
    
    ######################################################################################################################
    #Plot 
    
    st.write("""
    ## Invloed van het opleidingsniveau van de ouders op het wel of niet halen van het vak
    In de onderstaande grafiek wordt de relatie weergegeven tussen het opleidingsniveau van de ouders, en of de student
    wel of niet het vak heeft gehaald.""")
    
    df["hoogste_opleidingsniveau"] = np.where(df["Medu"] >= df["Fedu"], df["Medu"], df["Fedu"])
    df['behaald'] = df['G3'].apply(lambda x: 'behaald' if x >=10  else 'niet behaald')
    df['hoogste_opleidingsniveau'].nunique()
    selectie2 = df[['hoogste_opleidingsniveau','behaald']].groupby(['hoogste_opleidingsniveau','behaald']).value_counts()
    selectie2 = pd.DataFrame(selectie2, columns=['aantal'])
    selectie2 = selectie2.reset_index()
    selectie2['tot_deelname'] = selectie2.groupby('hoogste_opleidingsniveau')['aantal'].transform('sum')
    selectie2['percentage_behaald'] = round(selectie2['aantal']/selectie2['tot_deelname']*100,2)
    selectie2['hoogste_opleidingsniveau'].replace([0,1,2,3,4],['geen opleiding','basis onderwijs',
                                                               '3de klas middelbareschool', 'voortgezet onderwijs afgerond', 
                                                               'hoger onderwijs'],
                       inplace=True)

    
    fig_opleidingouders = px.line(selectie2,x='hoogste_opleidingsniveau', y='percentage_behaald',color='behaald')
    fig_opleidingouders.update_layout(title="verband behaalde examens en opleidingsniveau ouders",
                 xaxis_title= "opleidingsniveau ouders",
                 yaxis_title="percentage behaald")

    st.plotly_chart(fig_opleidingouders)
    
    st.write("""
        Uit deze grafiek blijkt dus ...................
        """)

    
    
    ######################################################################################################################
page_names_to_funcs = {
    "Opdrachtomschrijving": intro,
    "Data analyse": data_analyse,
    "Grafieken": grafieken,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

