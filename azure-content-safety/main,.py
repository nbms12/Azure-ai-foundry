# %%
# --------------------
# // Copyright (c) Microsoft Corporation.
# // Licensed under the MIT license.
# --------------------

# %% [markdown]
# # Moderate Content and Detect Harm with Azure AI Content Safety
# 
# Contoso Camping Store is developing new AI-powered features for their website to enhance user interaction and safety. As a developer, you are tasked with integrating Azure AI Content Safety features into the store's platform. Your goal is to ensure that all customer support conversations in addition to user-generated content such as product reviews and images adhere to the company's content guidelines, promoting a safe and inclusive environment for all users.

# %% [markdown]
# ## Text Moderation
# 
# Contoso Camping Store provides customers with the ability to speak with an AI-powered customer support agent and post product reviews. We could leverage an AI model to detect whether the text input from our customers is harmful and later use the detection results to implement the necessary precautions.

# %%
# --------------------
# SAFE CONTENT
# --------------------

import os
import requests
from dotenv import load_dotenv
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData, ImageCategory
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory

load_dotenv()

def analyze_text():
    # analyze text
    key = os.environ["CONTENT_SAFETY_KEY"]
    endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Construct request
    request = AnalyzeTextOptions(text="I recently bought a tent, and I have to say, I'm really disappointed. The tent poles seem flimsy, and the zippers are constantly getting stuck. It's not what I expected from a high-end tent. You all suck and are a sorry excuse for a brand.")

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("Analyze text failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

if __name__ == "__main__":
    analyze_text()

# %%
# --------------------
# HARMFUL CONTENT
# --------------------

def analyze_text():
    # analyze text
    key = os.environ["CONTENT_SAFETY_KEY"]
    endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Construct request
    request = AnalyzeTextOptions(text="<Your input text>")

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("Analyze text failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

if __name__ == "__main__":
    analyze_text()

# %%
# --------------------
# VIOLENT CONTENT WITH MISSPELLING
# --------------------

def analyze_text():
    # analyze text
    key = os.environ["CONTENT_SAFETY_KEY"]
    endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Construct request
    request = AnalyzeTextOptions(text="<Your input text>")

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("Analyze text failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

if __name__ == "__main__":
    analyze_text()

# %% [markdown]
# ## Image Moderation
# 
# Contoso Camping Store provides customers with the ability to upload photos to complement their product reviews. Customers have found this feature useful as it provides insight into how products look and function outside of the generic marketing images. We could leverage an AI model to detect whether the images posted by our customers are harmful and later use the detection results to implement the necessary precautions.

# %%
# --------------------
# SAFE IMAGE
# --------------------

def analyze_image():
    endpoint = os.environ.get('CONTENT_SAFETY_ENDPOINT')
    key = os.environ.get('CONTENT_SAFETY_KEY')
    image_path = os.path.join("<sample_data>", "<image.jpg>")

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))


    # Build request
    with open(image_path, "rb") as file:
        request = AnalyzeImageOptions(image=ImageData(content=file.read()))

    # Analyze image
    try:
        response = client.analyze_image(request)
    except HttpResponseError as e:
        print("Analyze image failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == ImageCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == ImageCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == ImageCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == ImageCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

if __name__ == "__main__":
    analyze_image()

# %%
# --------------------
# VIOLENT IMAGE
# --------------------

def analyze_image():
    endpoint = os.environ.get('CONTENT_SAFETY_ENDPOINT')
    key = os.environ.get('CONTENT_SAFETY_KEY')
    image_path = os.path.join("<sample_data>", "<image.jpg>")

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))


    # Build request
    with open(image_path, "rb") as file:
        request = AnalyzeImageOptions(image=ImageData(content=file.read()))

    # Analyze image
    try:
        response = client.analyze_image(request)
    except HttpResponseError as e:
        print("Analyze image failed.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(item for item in response.categories_analysis if item.category == ImageCategory.HATE)
    self_harm_result = next(item for item in response.categories_analysis if item.category == ImageCategory.SELF_HARM)
    sexual_result = next(item for item in response.categories_analysis if item.category == ImageCategory.SEXUAL)
    violence_result = next(item for item in response.categories_analysis if item.category == ImageCategory.VIOLENCE)

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")

if __name__ == "__main__":
    analyze_image()

# %% [markdown]
# ## Groundedness Detection
# 
# Integrating an AI-powered customer support agent has been a game changer for Contoso Camping Store! Customers can ask the support agent for product recommendations and guidance on how to use Contoso Camping Store products. However, we want to ensure that the model provides responses that are grounded in the source material that’s passed onto the model.
# 
# Let’s test some prompts with the model to detect the groundedness of its output.
# 
# **Note**: Up to 55,000 characters of grounding sources can be analyzed in a single request.

# %%
# --------------------
# GROUNDED Q&A
# --------------------

key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

url = f'{endpoint}/contentsafety/text:detectGroundedness?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "domain": "Generic",
    "task": "QnA",
    "qna": {
        "query": "<Your query>"
    },
    "text": "<Your text>",
    "groundingSources": [
        "<Your grounding source>"
    ],
    "reasoning": False
}

response = requests.post(url, headers=headers, json=data)

print(response.json())


# %%
# --------------------
# UNGROUNDED Q&A
# --------------------

url = f'{endpoint}/contentsafety/text:detectGroundedness?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "domain": "Generic",
    "task": "QnA",
    "qna": {
        "query": "<Your query>"
    },
    "text": "<Your text>",
    "groundingSources": [
        "<Your grounding source>"
    ],
    "reasoning": False
}

response = requests.post(url, headers=headers, json=data)

print(response.json()) 

# %%
# --------------------
# SUMMARIZATION Q&A
# --------------------

url = f'{endpoint}/contentsafety/text:detectGroundedness?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "domain": "Generic",
    "task": "Summarization",
    "text": "<Your text>",
    "groundingSources": [
        "<Your grounding source>"
    ],
    "reasoning": False
}

response = requests.post(url, headers=headers, json=data)

print(response.json())

# %% [markdown]
# ## Prompt Shields
# 
# Thus far, we’ve discussed ways that we could both detect harmful content and mitigate harmful content generation from the model. Let’s now add an additional layer of security to the model to prevent prompt injections.

# %%
# --------------------
# USER PROMPT ATTACK
# --------------------

url = f'{endpoint}/contentsafety/text:shieldPrompt?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "userPrompt": "<Your user prompt>"
}

response = requests.post(url, headers=headers, json=data)

print(response.json())


# %%
# --------------------
# DOCUMENT ATTACK
# --------------------

url = f'{endpoint}/contentsafety/text:shieldPrompt?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "documents":["<Your documents>"]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())

# %%
# --------------------
# PROMPT AND DOCUMENT ATTACK
# --------------------

url = f'{endpoint}/contentsafety/text:shieldPrompt?api-version=2024-02-15-preview'
subscription_key = key

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

data = {
    "userPrompt": "<Your user prompt>",
    "documents":["<Your documents>"]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())


