import streamlit as st
import st_pages
from st_pages import show_pages_from_config, add_page_title
import pandas as pd
import numpy as np
import pickle
from urllib.request import urlopen
import json
# from PIL import Image
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
#  pour les raisons et les modalités https://docs.python.org/fr/3/library/warnings.html


show_pages_from_config (".streamlit/pages.toml")

st.markdown(
    """
    <style>
    .main{
        background-color:#F5F5F5;
    }
    <style>
    """
)

# Main sections
header = st.container()
dataset= st.container()
# features = st.container()

model_training = st.container()
model = pickle.load(open('./Datas/model.pkl','rb'))

# #Load Dataframe

# X_test=pd.read_csv('./Datas/X_test.csv')
# y_test=pd.read_csv('./Datas/y_test.csv')
dataframe=pd.read_csv('./Datas/dFreduced.csv')


def credit(id_client):
    
    ID = int(id_client)   
    
# récupération des données clients
    X = dataframe[dataframe['SK_ID_CURR'] == ID]
    X = X.drop(['TARGET', 'SK_ID_CURR'], axis=1)
    
    prediction = model.predict(X)
    
    y_probabiliste = model.predict_proba(X)
    
    dict_final = {
        'prediction' : int(prediction),
        'proba' : float(y_probabiliste[0][0])
        }

    print('Nouvelle Prédiction : \n', dict_final)


### Sidebar
st.sidebar.title("Menus")
sidebar_selection = st.sidebar.radio(
    'Select Menu:',
    ['Overview', 'Model & Prediction','Explication and Comparison'],
    )


with header:
    st.title("Make sure a client is  sure client!") 
    

    
with dataset:
    st.header("The train dataset is made of a selection of relevant features chosen after EDA")
    credit_data = dataframe
    st.write (credit_data.head())

    
    
# with model_training:
#     # st.header("Time to train our chosen model!")
#     # st.text("You can choose some hyperparameters for the chosen model")
    
#     model_selection_column, display_column = st.columns(2)
#     test_clients = pd.read_csv('./Datas/dFreduced.csv')
#     liste_id = test_clients['SK_ID_CURR'].tolist()

#      # Choose a client

#     # chosen_client = str(model_selection_column.selectbox("Please chose your client ID", test_clients['SK_ID_CURR']))
#     chosen_client = st.text_input('Veuillez saisir l\'identifiant d\'un client:', )

#     st.success("client chosen")
    
#     if chosen_client == '':
#         st.write('Veuillez recommencer')
    
#     # Si le numéro de client est un numéro valide:
#     elif (int(chosen_client) in liste_id) :
          
#         # On peut appeler l'API
#         API_url = "http://127.0.0.1:5000/credit/" + chosen_client
          
#         with st.spinner('Attente du score du client choisi ...'):
            
#           json_url = urlopen(API_url)
          
#           API_data = json.loads(json_url.read())
#           classe_predite = API_data["prediction"]
#           if classe_predite == 1:
#               resultat = "client dangereux"
#           else:
#               resultat = "client peu risqué"
          
#           proba = 1- API_data["proba"]
          
#           #affichage de la prédiction
#           prediction = API_data['proba']
#           # classe_reelle = dataframe[dataframe['SK_ID_CURR']==int(chosen_client)]['LABELS'].values[0]
#           # classe_reelle = str(classe_reelle).replace('0', 'sans défaut').replace('1', 'avec défaut')
#           chaine = 'Prédiction : **' + resultat +  '** avec **' + str(round(proba*100)) + '%** de risque d''erreur '

#         st.markdown(chaine)

st.subheader("Caractéristiques influençant le score")
          
          
#MLFLOW tracking    
# Set the experiment
# Mlflow tracking

    # track_with_mlflow = st.checkbox(
    #     "📈 Track with mlflow? ", help="Mark to track experiment with MLflow"
    # )

#     # Model training
#     start_training = st.button("💪 Start training", help="Train and evaluate ML model")
#     if not start_training:
#         st.stop()

#     if track_with_mlflow:
#         mlflow.set_experiment(data_choice)
#         mlflow.start_run()
#         mlflow.log_param("model", model_choice)
#         mlflow.log_param("features", feature_choice)


# mlflow.set_experiment("optimized_RF_Classifier")

# # Log a metric
# accuracy = 0.9
# mlflow.log_metric("accuracy", accuracy)

# # Log an artifact
# model = pickle.dumps(my_model)
# mlflow.log_artifact("model", model)

# # Display the metrics and artifacts
# st.write("Accuracy:", accuracy)
# st.write("Model:", model)
    
    