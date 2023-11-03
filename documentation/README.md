# Introduction

SuperAnnotate LLM Toolkit is a web based low code application integrated into the SuperAnnotate platform. It allows users to create and manage rich web interfaces for data manipulation which is needed for high quality LLM fine tuning, prompt engineering, testing, etc.

LLM Toolkit consist of three main parts:
1. [No code user interface builder](#ui-builder)
2. [Python based user experience builder](#code-editor)
3. [Integration with the SuperAnnotate platform](#integration-with-the-superannotate-platform)

## UI Builder

<font color="red">TODO - UI builder structure<br></font>

### UI Components

There are multiple components available in the UI builder. Each component on the UI should have its own unique ID. Initially the component is created with auto generated ID, but it is possible to change it to a more meaningful value.

#### **`Group`**

Group is a container component which allows to create multiple rows of itself. It is usefull for creating converation-like experiences where you need to have multiple rows of same type of components.

##### Parameters

- `Initially hidden` - checkbox. Is disabled by default. When enabled, one row of the group is created during the initialization stage of the editor.
- `Removable` - checkbox. Is disabled by default. When enabled an `X` button will be added to each row of the group allowing to delete the row.

##### Related Functions

- `repeatRow(path: List[Union[str, int]])` - appends a row to the group, returns the path of the newly created row
- `deleteRow(path: List[Union[str, int]])` - deletes the row of the group, specified by the row index in the `path`
- `getGroupLength(path: List[Union[str, int]])` - returns the length of the group (the number of rows)

##### Related Events

- `on_<component id>change(path: List[Union[str, int]]):` - fired when a group row is deleted by user by prssing `X` button, receives the path of the newly deleted row.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/group.json)

#### **`Grid`**

Grid is a container component which allows to horisontally arrange the content on the UI.

##### Parameters

- `Resizable` - checkbox. Is disabled by default. When enabled, it is possible to resize the width of each column of the grid.
- `Columns` - manipulation menu. Here you can add/remove columns set the horizontal sizes.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/grid.json)

#### **`Tabs`**

Tab is a container component which allows to easyly organize your experience in more structured way. The content of the tab is visible only when it is selected as active.

##### Parameters

- `Tabs` - manipulation menu. Here you can add, remove and rename tabs.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/tab.json)

#### **`Button`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Button Text` - text input indicating the button text

##### Related Events

- `on_<component id>click(path: List[Union[str, int]]):` - fired when the button is clicked.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/button.json)


#### **`Text input`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Placeholder` - text input indicating the placeholder
- `Min length` - minimum text length to consider the input as valid
- `Max length` - maximum text length to consider the input as valid
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Hide from form` - checkbox. Is disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the backgroud
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when text value is changed by user, receives component path and the text value.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/text-input.json)

#### **`Text area`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Placeholder` - text input indicating the placeholder
- `Min length` - minimum text length to consider the input as valid
- `Max length` - maximum text length to consider the input as valid
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Hide from form` - checkbox. Is disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the backgroud
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when text value is changed by user, receives component path and the text value.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/text-area.json)


#### **`Number`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Min length` - minimum text length to consider the input as valid
- `Max length` - maximum text length to consider the input as valid
- `Step` - step of the increment/decrement
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Hide from form` - checkbox. Is disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the backgroud
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: Union[int, float])` - sets the data of the component

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: Union[int, float]):` - fired when number value is changed by user, receives component path and the number value.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/number.json)


#### **`Code`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when code value is changed by user, receives component path and the code value.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/code.json)

#### **`Paragraph`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Text` - the visible text of the paragraph
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value)` - sets the data of the component

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/paragraph.json)

#### **`Select`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Placeholder` - text input indicating the placeholder
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package
- `Select type` - radio button. Specify if the select should be single or multi select.
- `Options` - manipulation menu. Here you can add, remove and rename option. You can define a default value(s) as well

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value)` - sets the data of the component, for single-select `value: str`, for multi-select `value: List[str]`

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value):` - fired when checkbox value is changed by user, receives component path and the checkbox value. For single-select `value: str`, for multi-select `value: List[str]`.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/select.json)


#### **`Checkbox`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Placeholder` - text input indicating the placeholder
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package
- `Options` - manipulation menu. Here you can add, remove and rename option. You can define a default value(s) as well

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: List[str])` - sets the data of the component

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: List[str]):` - fired when checkbox value is changed by user, receives component path and the checkbox value

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/checkbox.json)


#### **`Radio`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Placeholder` - text input indicating the placeholder
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package
- `Options` - manipulation menu. Here you can add, remove and rename option. You can define a default value(s) as well

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when radio value is changed by user, receives component path and the radio value

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/checkbox.json)


#### **`Slider`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Min value` - minimum value of the slider
- `Max value` - maximum value of the slider
- `Step` - step of the increment/decrement
- `Suffix` - a suffix appended to the slider value popup
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package
- `Slider Type` - radio button. Specify if the slider represents a single value or a range.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: Union[int, float])` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: Union[int, float]):` - fired when slider value is changed by user, receives component path and the slider value

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/slider.json)


#### **`Voting`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: int)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: int):` - fired when voting value is changed by user, receives component path and the voting value - `0` or `1`

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/voting.json)


#### **`Rating`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Number of stars` - number of start of the rating
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: int)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: int):` - fired when rating value is changed by user, receives component path and the rating.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/rating.json)


#### **`Date`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `include time` - checkbox. Is disabled by default. When enabled time picker is visible
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when date/time value is changed by user, receives component path and the date/time value

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/date_time.json)


#### **`Time`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Required` - checkbox. Is disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs)
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when time value is changed by user, receives component path and the time value

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/date_time.json)


#### **`Image`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Source URL` - URL of the image
- `Alt text` - Alternate text
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the url of the image component
- `setValue(path: List[Union[str, int]], value: str)` - sets the url of the image component 

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/image.json)


#### **`Video`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Source URL` - URL of the video
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the url of the video component
- `setValue(path: List[Union[str, int]], value: str)` - sets the url of the video component

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/video.json)


#### **`Audio`**

<font color="red">TODO - Add description<br></font>

##### Parameters
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Source URL` - URL of the audio
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the url of the audio component
- `setValue(path: List[Union[str, int]], value: str)` - sets the url of the audio component

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/audio.json)


#### **`Avatar`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Label` - text input indicating the label of thecomponent visible on the UI
- `Source URL` - URL of the avatar image
- `Alt text` - Alternate text
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the url of the avatar component
- `setValue(path: List[Union[str, int]], value: str)` - sets the url of the avatar component 

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/avatar.json)


#### **`CSV`**

<font color="red">TODO - Add description<br></font>

##### Parameters:
- `Label` - text input indicating the label of thecomponent visible on the UI
- `Source URL` - URL of the avatar image
- `Alt text` - Alternate text
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the data of the component
- `setValue(path: List[Union[str, int]], value: str)` - sets the data of the component 

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - fired when there is a change in csv data of the component, receives component path and the csv content

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/csv.json)


#### **`Web`**

<font color="red">TODO - Add description<br></font>

##### Parameters

- `Source` - there are two options to bring your web component: 1. source url, 2. code
- `Height` - Height of the web component
- `Exclude from annotation` - checkbox. Is disabled by default. When enabled, the value of the component will be excluded from annotation export package

##### Related Functions

- `getValue(path: List[Union[str, int]])` - returns the code source url or the code itself based on the web component configuration
- `setValue(path: List[Union[str, int]], value: str)` - set the code source url or the code itself based on the web component configuration
- `postMessageToWebComponent(path: List[Union[str, int]], message: Union[str, dict])` - sends the `message` string to the web component

##### Related Events

- `on_<component id>_message(path: List[Union[str, int]], value: Union[str, dict]):` - fired when there is a message from web component, receives component path and the value of the incoming message

##### Sending messages from web component

- `window.parent.postMessage({ action: 'topy', data }, "*");` - from the JavaScrips use this function to send a message to the main editor. Use `topy` as an action identifier.

<font color="red">TODO - add a gif<br></font>

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/web.json)



## User Experience Builder

<font color="red">TODO - UX builder structure - Left side - preview, variables. Right side - code editor</font>

## Code Editor

Here you can describe the functionality of your UI using Python. 

### Component Path

Each component is accessed through its own unique path. In case of components not placed in any group,  path is simply one element array containing the component’s id:<br>

```python
['component_id']
```

In case a component placed within a group, the component path is an array of parent group id, group row index and it’s own id:

```python
['parent_group_id', <group_row_index>, 'component_id']
```

In case a component placed within a group hierarchy (`group_1 -> group_2 -> group_3`), the component path is an array of parent group ids, group row indexes and it’s own id:

```python
['group_1', <group_1_row_index>, 'group_2', <group_2_row_index>, 'group_3', <group_3_row_index>, 'component_id']
```

-1 index points to the last row of the group:

```python
['parent_group_id', -1, 'component_id']
```

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/group-paths.json)


### Event Handlers

Event handlers are special functions that allow users to add custom functionality on user-triggered and other events.
Event handler function name should have a strict format:
```python
on_<component id>_<event type>
```

There are four types of events:

- Component value change event - ```event type = change```, in this case the function receives two arguments:
path - the path of the trigger component
value - updated value of the trigger component
- Button click event - ```event = click```, in this case the function receives one argument:
path - the path of the trigger button
- Message event - ```event = message```, in this case the function receives two arguments:
path - the path of the trigger component
value - received message from the trigger component
- Group row deleted event - ```event type = deleted```, this event is fired when a row in a group is being deleted by pressing `X` button. The handler function receives one argument:
path - the path of the trigger row

Example:
```python
### Value change event handler of the component with "prompt" id
def on_prompt_change(path, value):
   ### your custom code
   return

### Button click event handler of the button with "submit" id
def on_submit_click(path):
   ### your custom code
   return

### Message event handler of the component with "custom_web_component" id
def on_custom_web_component_message(path):
   ### your custom code
   return

### Group row deleted event handler of the component with "my_group" id
def on_my_group_deleted(path):
   ### your custom code
   return
```

### Custom functions

In the code editor you can use following custom functions:

- `getValue(path: List[Union[str, int]])` - returns the current value of the component by its provided path. *For more information about componets and value types please refer to component describtion.*

- `setValue(path: List[Union[str, int]], value)` - sets the value of the component by provided path. *For more information about componets and value types please refer to component describtion.*

- `repeatRow(path: List[Union[str, int]])` - appends a row to the group by provided path. This function return the path of newly created row. *For more information about group component structure please refer to component describtion.*

- `deleteRow(path: List[Union[str, int]])` - deletes the row of the group specified by path. Here the path should include the row index. *For more information about group component structure please refer to component describtion.*

- `getGroupLength(path: List[Union[str, int]])` - returns the number of rows in the group by its path. *For more information about group component structure please refer to component describtion.*

- `postMessageToWebComponent(path: List[Union[str, int]], message)` - sends a message to a web component specified by provided path. *For more information web component structure please refer to component describtion.*

- `setLoading(on_off: bool)` - sets/removes a full page overlay with a spinner.

- `getPayload()` - returns a data attached to the item opened in the editor. Returns None in build mode. *For more information refer to [Integration with the SuperAnnotate platform](#integration-with-the-superannotate-platform) section*

### HTTP Requests from The Code

To send http requests it is recomended to use `requests` module, which was created by SuperAnnotate to replicate [Python requests module](https://pypi.org/project/requests/), the only difference is the browser limitation. In majority of cases you will not see any difference.

Example:

```Python
import requests

def on_submit_click(path: List[Union[str, int]]):
    response = requests.request(
        url='https://your.domain.com/your/path',
        method ="GET",
        headers = None
    )

    ### Return response as a JSON object
    return response.json()
```

There is one important thing you need to remember while using this module - all the methods are asyncrounous, meaning during the execution the UI will be blocked, therefore use it only with cases where http requests are fast enough. To use asyncronous functionality you can use `asyncs` sub module and add `await` to the function call to make it async.

Example:

```Python
import requests.asyncs as requests

async def on_submit_click(path: List[Union[str, int]]):
    response = await requests.request(
        url='https://your.domain.com/your/path',
        method ="GET",
        headers = None
    )

    ### Return response as a JSON object
    return response.json()
```

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/request.json)

### Environment Variables

You can specify environment variables instead of hardcoding. In the variables tab you can add as many variables as you need.
You can access to the variables in following way:

```python
from environments import (
    variable_name_1,
    variable_name_2,
    variable_name_3
)
```

It is possible to store secret values by checking the **Secure** checkbox, while creating a variable. This will exclude the variable value from the exported template.

## Integration with the SuperAnnotate platform

### Data Input

There are two main ways of data input:

1. Add an item to the SuperAnnotate platform using one of the following methods:
    - [Import data with cloud integrations](https://doc.superannotate.com/docs/integrations)
    - [Import data with Python SDK](https://doc.superannotate.com/docs/sdk-import-other)

    Each data item should be a valid JSON file. Key advantage here is that you can specify 
    your own schema and access the values in the UI builder or in the code editor.

    **Example**. Let’s assume we have an JSON file  imported from an AWS S3 bucket using the cloud integration method.

    JSON file:

    ```json
    {
        "metadata":
            {
                "name": "My conversation",
                "category": "Cooking",
                "image_url": "https://your_bucket.s3.us-west-2.amazonaws.com/data/conversation.json"
            }
    }
    ```

    Let’s assume you want to display **name** and **category** values as paragraphs on the UI. To do this you need to simply add an expression `{{metadata.name}}` and `{{metadata.category}}` in the component configuration field, as it is shown below:

    ![Text expression](https://public-static-files.superannotate.com/documentation/images/data_in_0.png "Text expression")

    For cases, when there is included a data item, which should be signed as an integration item, you need to use a special function: `{{sign(metadata.image_url)}}`

    ![Signed url expression](https://public-static-files.superannotate.com/documentation/images/data_in_1.png "Signed url expression")

2. Add an item to the SuperAnnotate platform using [item generation](https://doc.superannotate.com/docs/generate-items). In this case you need to input data manually from the LLM editor.

### Data Output
