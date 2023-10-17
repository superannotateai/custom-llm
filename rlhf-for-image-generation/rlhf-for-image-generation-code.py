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
        "style_preset": style,
        "image": True
    }

    ### Create headers object
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

    ### Get generated images
    images = res["artifacts"]
    return images
