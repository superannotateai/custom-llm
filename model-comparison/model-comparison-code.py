### Libraries 
from typing import List, Union
from accessor import getValue, repeatRow, deleteRow, setValue, setLoading, getGroupLength
from environments import open_ai_url, open_ai_api_key, cohere_url, cohere_api_key
from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any
import json

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
        "model": "gpt-4",
        "messages": [{"role": "user", "content": message}]
    }

    ### Create OpenAI headers object
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + open_ai_api_key
    }

    ### Send the request
    fetchedValue = await request(
      open_ai_url,
      "POST",
      json.dumps(questionBody),
      headers
    )

    ### Parse the response
    res = await fetchedValue.json()

    ### Get the completion
    answer = res["choices"][0]["message"]["content"]
    return answer

### Cohere Completion
async def cohereCompletion(message: str):
    ### Create Cohere request body
    questionBody = {
        "prompt": message
    }

    ### Create Cohere headers object
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + cohere_api_key
    }

    ### Send the request
    fetchedValue = await request(
      cohere_url,
      "POST",
      json.dumps(questionBody),
      headers
    )

    ### Parse the response
    res = await fetchedValue.json()

    ### Get the completion
    answer = res["generations"][0]["text"]
    return answer

### HTTP Request Function
async def request(url: str, method: str = "GET", body: Optional[str] = None,
                  headers: Optional[dict[str, str]] = None, **fetch_kwargs: Any) -> FetchResponse:
    kwargs = {"method": method, "mode": "cors"}
    if body and method not in ["GET", "HEAD"]:
        kwargs["body"] = body
    if headers:
        kwargs["headers"] = headers
    kwargs.update(fetch_kwargs)

    response = await pyfetch(url, **kwargs)
    return response
