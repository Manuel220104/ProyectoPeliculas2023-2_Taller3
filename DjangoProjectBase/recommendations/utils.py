#importar librerías
from dotenv import load_dotenv, find_dotenv
import os
import openai
import json
from dotenv import load_dotenv, find_dotenv
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def Generar_respuesta(entrada):
    #Se lee del archivo .env la api key de openai
    # api_key = "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"
    # openai.api_key = api_key
    #Se lee del archivo .env la api key de openai
    _ = load_dotenv('openAI.env')
    openai.api_key  = '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'


    #Se genera una función auxiliar que ayudará a la comunicación con la api de openai
    #Esta función recibe el prompt y el modelo a utilizar (por defecto gpt-3.5-turbo)
    #devuelve la consulta hecha a la api

    def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        return response.choices[0].message["content"]

    #Definimos una instrucción general que le vamos a dar al modelo 

    instruction = "Describe una película de ciencia ficción que te guste."

    # Definimos el prompt
    prompt = f"{instruction} Di el nombre y la descripción de la película: {entrada}"

    print(prompt)

    #Utilizamos la función para comunicarnos con la api
    text = get_completion(prompt)
    text2 = text[0:999]

    response = openai.Image.create(
        prompt=f"{text2}",
        n=1,
        size="256x256"
    )
    print(response)
    image_url = response['data'][0]['url']
    print(image_url)
    

    return text, image_url




