### Libraries
from typing import List, Union
from accessor import (
    getValue,
    repeatRow,
    setValue,
    setLoading
)
from environments import url
import requests.asyncs as request_async

### UI Components
textarea_question_input = ['question_input']
button_question_submit = ['question_submit']
avatar_convo_question_avatar = ['convo_group', 0, 'convo_question_avatar']
paragraph_convo_question_text = ['convo_group', 0, 'convo_question_text']
rating_convo_question_rating = ['convo_group', 0, 'convo_question_rating']
select_convo_question_select = ['convo_group', 0, 'convo_question_select']
avatar_convo_answer_avatar = ['convo_group', 0, 'convo_answer_avatar']
paragraph_convo_answer_text = ['convo_group', 0, 'convo_answer_text']
rating_convo_answer_rating = ['convo_group', 0, 'convo_answer_rating']
select_convo_answer_select = ['convo_group', 0, 'convo_answer_select']
select_model_id = ['model_id']
paragraph_used_model_name = ['convo_group', 0, 'used_model_name']

### Submit button event handler
async def on_question_submit_click(path: List[Union[str, int]]):
    ### Get values
    questionText = getValue(textarea_question_input)
    model_name = getValue(select_model_id)

    ### If empty values, return
    if not questionText:
      return

    if not model_name:
      return

    ### Start loading
    setLoading(True)

    ### Add new row in the group
    repeatRow(['convo_group'])

    ### Initialize the row components
    setValue(['convo_group', -1, 'convo_question_text'], questionText)
    setValue(['convo_group', -1, 'convo_question_rating'], 0)
    setValue(['convo_group', -1, 'convo_question_select'], None)
    setValue(['convo_group', -1, 'convo_answer_text'], "Generating an answer ....")
    setValue(['convo_group', -1, 'convo_answer_rating'], 0)
    setValue(['convo_group', -1, 'convo_answer_select'], None)

    ### Create OpenAI request body
    questionBody = {
        "model": model_name,
        "messages": [{"role": "user", "content": questionText}]
    }

    ### Create OpenAI headers object
    headers = {
      "Content-Type": "application/json"
    }

    ### Send the request
    fetchedValue = await request_async.post(
      url,
      json=questionBody,
      headers=headers
    )

    ### Parse the response
    res = fetchedValue.json()

    ### Get the completion
    answer = res["choices"][0]["message"]["content"]

    ### Set the completion value in the UI
    setValue(['convo_group', -1, 'convo_answer_text'], answer)

    ### Empty prompt in the UI
    setValue(textarea_question_input, "")
    setValue(['convo_group', -1, 'used_model_name'], res["model"])

    ### Remove the loading
    setLoading(False)
    return
