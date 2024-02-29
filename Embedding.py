import openai
import pandas
import configparser
from openai import OpenAI

#defining embedding for df.apply
def compute_embeddings(x):
    text = (x['combined'])
    chat_embeddings = client.embeddings.create(input=text, model="text-embedding-3-small")
    return(chat_embeddings.data[0].embedding)

#Getting API key from config file
config = configparser.ConfigParser()
config.read('config.ini')

#connectiong to OpenAPI
OPENAI_API_KEY: str = config['openai']['api_key']
client = OpenAI(api_key=OPENAI_API_KEY, max_retries=5)

#importing and prepping local data
df = pandas.read_csv('data/trainingdata.csv', encoding='latin-1')
df = df[["Link", "Title", "Content"]]
df = df.dropna()
df["combined"] = (
    "Title: " + df.Title.str.strip() + "; Content: " + df.Content.str.strip()
)

#Applying function to dataset and saving
df['embedding'] = df.apply(compute_embeddings,axis=1)
df.to_csv('data/trainingdata_with_embedding.csv')
