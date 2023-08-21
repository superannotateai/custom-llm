### Libraries
from typing import List, Union
from accessor import getValue, repeatRow, deleteRow, setValue, setLoading, getGroupLength
from environments import url, key
from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any
import json

### UI Components
input_prompt = ['prompt']
image_img1 = ['img1']
image_img2 = ['img2']
image_img3 = ['img3']
image_img4 = ['img4']
select_style = ['style']
button_generate = ['generate']

### Generate button event handler
async def on_generate_click(path: List[Union[str, int]]):
    ### Start loading
    setLoading(True)

    ### Get values
    prompt = getValue(input_prompt)
    style = getValue(select_style)

    ### Generate images
    images = await generateImage(prompt, style)

    ### Set values
    for index in range(4):
        setValue(["img"+str(index+1)], "data:image/png;base64,"+images[index]["base64"])
    
    ### Remove loading
    setLoading(False)
    return

### StabilityAI Image Generation
async def generateImage(prompt: str, style: str= "enhance"):
    ### Create request body
    questionBody = {
        "text_prompts": [
            {
                "text": prompt
            }
        ],
        "samples": 4,
        "cfg_scale": 16,
        "style_preset": style
        
    }

    ### Create headers object
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + key
    }

    ### Send the request
    fetchedValue = await request(
      url,
      "POST",
      json.dumps(questionBody),
      headers
    )

    ### Parse the response
    res = await fetchedValue.json()

    ### Get generated images
    images = res["artifacts"]
    return images

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