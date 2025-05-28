import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

## Langsmith Tracking And Tracing
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"


model = ChatGroq(model="gemma2-9b-it",temperature=0.7)


# Defining data structure.
class ProductInfo(BaseModel):
    product_name: str = Field(..., description="Name of the product")
    product_details: str = Field(..., description="Brief description of the product")
    price_int: int = Field(..., description="Tentative price in INR")

parser = JsonOutputParser(pydantic_object=ProductInfo)
# And a query intented to prompt a language model to populate the data structure.
product_query = "Tell me about Iphone 15."

# prompt = PromptTemplate(
#     template=''' You are a helpful product assistant (Indian Market).Return output in the following JSON format.provide rupees symbol for price_int.\n{format_instructions}\n{query}\n ''',
#     input_variables=["query"],
#     partial_variables={"format_instructions": parser.get_format_instructions()},
# )
prompt = ChatPromptTemplate([
    ("system", 
     "You are a helpful product assistant for the Indian Market. "
     "Return output in the following JSON format. "
     "Provide prices with USD symbol using the 'price_int' field. "
     "Only provide three products with fields: 'product_name', 'product_details', and 'price_int'. "
     "No extra information."),
    
    ("user", "{input}"),
    
    ("assistant", "{format_instructions}")
],
partial_variables={"format_instructions": parser.get_format_instructions()},
)


chain = prompt | model | parser

try:
    product_query = "Tell me about Iphone 15."
    response = chain.invoke({"input": product_query})
    print(response)

except Exception as e:
    print(f"Error: {e}")