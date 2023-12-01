import pandas as pd
import streamlit as st
import pickle
from urllib.request import urlopen
import json

# load our best model
# PATH = "C:\Users\DELL\Formation OC\API_P7\Datas\"

#Load Dataframe


# X_test=pd.read_csv(PATH+'X_test.csv')
# y_test=pd.read_csv(PATH+'y_test.csv')
dataframe=pd.read_csv('./Datas/dFreduced.csv')

# Main sections
header = st.container()
dataset= st.container()
features = st.container()
model_training = st.container()

model = pickle.load(open('./Datas/model.pkl','rb'))
with header:
    st.title("Make sure a client is a sure client!") 
    

    
with dataset:
    st.header("The train dataset is made of a selection of relevant features chosen after EDA")
    credit_data = dataframe
    st.write (credit_data.head())

with model_training:
   
       
    model_selection_column, display_column = st.columns(2)
    test_clients = pd.read_csv('./Datas/dFreduced.csv')
    liste_id = test_clients['SK_ID_CURR'].tolist()

     # Choose a client

    # chosen_client = str(model_selection_column.selectbox("Please chose your client ID", test_clients['SK_ID_CURR']))
    chosen_client = st.text_input('Veuillez saisir l\'identifiant d\'un client:', )

    st.success("client chosen")
    
    if chosen_client == '':

        st.write('Veuillez recommencer')
        
    elif (int(chosen_client) in liste_id) :
        
        with st.spinner('Attente du score du client choisi ...'):   
            
            ID = int(chosen_client)   
        
            # récupération des données clients
            X = dataframe[dataframe['SK_ID_CURR'] == ID]
            X = X.drop(['TARGET', 'SK_ID_CURR'], axis=1)
            
            prediction = model.predict(X)
            
            y_probabiliste = model.predict_proba(X)
            
            dict_final = {
                'prediction' : int(prediction),
                'proba' : float(y_probabiliste[0][0])
                }
            if dict_final["prediction"] == 1:
                resultat = "client dangereux"
            else:
                resultat = "client sûr"
            
            
            print('Nouvelle Prédiction : \n', dict_final) 


                
            chaine = 'Prédiction : **' + resultat +  '** avec **' + str(round((1-dict_final['proba'])*100)) + '%** de risque d''erreur '
            st.markdown(chaine)

            fig = go.Figure(go.Indicator(
                    mode = 'gauge+number+delta',
                    
                    value = dict_final['proba'])*100,

                    domain = {'x': [0, 1], 'y': [0, 1]},

                    title = {'text': 'Crédit score du client', 'font': {'size': 24}},

                    # Score des 10 voisins test set
                    # df_dashboard['SCORE_10_VOISINS_MEAN_TEST']

                    delta = {'reference': 76,
                            'increasing': {'color': 'Crimson'},
                            'decreasing': {'color': 'Green'}},

                    gauge = {'axis': {'range': [None, 100],
                                    'tickwidth': 3,
                                    'tickcolor': 'darkblue'},
                            'bar': {'color': 'white', 'thickness' : 0.25},
                            'bgcolor': 'white',
                            'borderwidth': 2,
                            'bordercolor': 'gray',
                            'steps': [{'range': [0, 25], 'color': 'Green'},
                                    {'range': [25, 49.49], 'color': 'LimeGreen'},
                                    {'range': [49.5, 50.5], 'color': 'red'},
                                    {'range': [50.51, 75], 'color': 'Orange'},
                                    {'range': [75, 100], 'color': 'Crimson'}],
                            'threshold': {'line': {'color': 'white', 'width': 10},
                                        'thickness': 0.8,
                                        # Score du client en %
                                        # df_dashboard['SCORE_CLIENT_%']
                                        'value': y_proba_client}})

            fig.update_layout(paper_bgcolor='white',
                                height=400, width=600,
                                font={'color': 'darkblue', 'family': 'Arial'})

            fig.show()


        #   classe_predite = API_data["prediction"]
        #   if classe_predite == 1:
        #       resultat = "client dangereux"
        #   else:
        #       resultat = "client peu risqué"
          
        #   proba = 1- API_data["proba"]
          
        #   #affichage de la prédiction
        #   prediction = API_data['proba']
        #   # classe_reelle = dataframe[dataframe['SK_ID_CURR']==int(chosen_client)]['LABELS'].values[0]
        #   # classe_reelle = str(classe_reelle).replace('0', 'sans défaut').replace('1', 'avec défaut')
        #   chaine = 'Prédiction : **' + resultat +  '** avec **' + str(round(proba*100)) + '%** de risque d''erreur '

        # st.markdown(chaine)