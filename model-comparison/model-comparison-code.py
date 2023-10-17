### Libraries 
from typing import List, Union
from accessor import (
    getValue,
    setValue,
    setLoading
)
from environments import url
import requests.asyncs as requests

### UI Components
input_prompt = ['prompt']
button_button = ['button']
textarea_model1_res = ['model1_res']
textarea_model2_res = ['model2_res']

### Submit button event handler
async def on_button_click(path: List[Union[str, int]]):
    ### Start loading
    setLoading(True)

    ### Get values
    prompt = getValue(input_prompt)

    ### Request with prompts
    completionCohere = await cohereCompletion(prompt)
    completionOpenAi = await openAiCompletion(prompt)

    ### Set the completion values in the UI
    setValue(textarea_model1_res, completionCohere)
    setValue(textarea_model2_res, completionOpenAi)

    ### Remove the loading
    setLoading(False)
    return

### OpenAI Completion
async def openAiCompletion(message: str):
    ### Create OpenAI request body
    questionBody = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }

    ### Create OpenAI headers object
    headers = {
      "Content-Type": "application/json"
    }

    ### Send the request
    fetchedValue = await requests.post(
      url,
      json=questionBody,
      headers=headers
    )

    ### Parse the response
    res = fetchedValue.json()

    ### Get the completion
    answer = res["choices"][0]["message"]["content"]
    return answer

### Cohere Completion
async def cohereCompletion(message: str):
    ### Create Cohere request body
    questionBody = {
        "cohere": True,
        "prompt": message
    }

    ### Create Cohere headers object
    headers = {
      "Content-Type": "application/json"
    }

    ### Send the request
    fetchedValue = await requests.post(
      url,
      json=questionBody,
      headers=headers
    )

    ### Parse the response
    res = fetchedValue.json()

    ### Get the completion
    answer = res["generations"][0]["text"]
    return answer
