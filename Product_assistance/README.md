# _**🧠 GenAI Product Assistant (Indian Market)**_

This is a GenAI-powered product assistant tailored for the Indian market. It uses `LangChain`, `Groq (Gemma 2B model)`, and `Pydantic` to return structured product data in JSON format. The assistant provides product name, description, and price (in INR format).



## **📦 Features**

- ✨ Query product details using natural language
- 🧾 Returns structured JSON with:
  - `product_name`
  - `product_details`
  - `price_int` (with USD symbol)
- ⚙️ Built with:
  - [`LangChain`](https://docs.langchain.com/)
  - [`Groq` via `langchain-groq`](https://pypi.org/project/langchain-groq/)
  - [`Pydantic`](https://docs.pydantic.dev/)
  - `.env` file for secure API key handling


## 🚀 Quick Start

### 1. Clone this repo

```bash```
git clone https://github.com/VinodhkumarBaskaran/GenAI-Work.git
cd GenAI-Work

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set up your .env file

Create a **.env** file with:

GROQ_API_KEY = <**your_groq_api_key**>   
LANGCHAIN_API_KEY = <**your_langchain_api_key**>   
LANGCHAIN_PROJECT = <**your_project_name**>  



## 🧠 Example Code Usage
product_query = "Tell me about iPhone 15."  
response = chain.invoke({"input": product_query})  
print(response)

## 🔎 Sample Output
{'product_name': 'iPhone 15', 
'product_details': 'Latest smartphone from Apple with advanced camera features and powerful processor.', 
'price_inr': 79900}


## 📄 License

MIT License

Copyright (c) 2024 Vinodhkumar B.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...


## 📬 Contact

https://www.linkedin.com/in/vinodhb95/

