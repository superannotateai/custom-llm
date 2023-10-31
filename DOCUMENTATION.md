# Introduction

SuperAnnotate LLM Toolkit is a web based low code application integrated into the SuperAnnotate platform. It allows users to create and manage rich web interfaces for data manipulation which is needed for high quality LLM fine tuning, prompt engineering, testing, etc.

LLM Toolkit consist of three main parts:
1. [No code user interface builder](#ui-builder)
2. [Python based user experience builder](#code-editor)
3. [Integration with the SuperAnnotate platform](#integration-with-the-superannotate-platform)

## UI Builder

<font color="red">
TODO - UI builder structure<br>
</font>

### UI Components

There are multiple components available in the UI builder. Each component on the UI should have its own unique ID. Initially the component is created with auto generated ID, but it is possible to change it to a more meaningful value.

#### 

## User Experience Builder

<font color="red">TODO - UX builder structure - Left side - preview, variables. Right side - code editor</font>

## Code Editor

Here you can describe the functionality of your UI using Python. 

### Component Path

Each component is accessed through its own unique path. In case of components not placed in any group,  path is simply one element array containing the component’s id:<br>

```python
['component_id']
```

In case a component placed within a group (or multiple groups), the component path is an array of parent group ids, group row indexes and it’s own id:

```python
['parent_group_id', <group_row_index>, 'component_id']
```

**Example**. Let’s assume we have following UI:

![Nested groups UI](https://public-static-files.superannotate.com/documentation/images/component_paths_1.png "Nested groups UI")

Here we have a parent group *group_1*, in this group we have one text area *prompt*, another group *group_2* and in the *group_2* we have a text input *comment*. 
Now let’s assume we have three rows of *group_2* in the editor (for more information about how to add rows of a specific group refer to the group component description <font color="red">TODO add a link</font>):

![Nested groups UI on the editor](https://public-static-files.superannotate.com/documentation/images/component_paths_2.png "Nested groups UI on the editor")

Now let’s write paths for each component in the UI:

`group_1`:
```python
path = ['group_1']
```

prompt of the first row of its parent group `group_1` (actually there is only one row of this group):
```python
path = ['group_1', 0, 'parent']
```
here 0 (`path[1]`) points to the first row of the `group_1`.

comment of the second row of its parent group `group_2` (there are three rows of this group):
```python
path = ['group_1', 0, 'parent', 1, 'comment']
```
here 0 (`path[1]`) points to the first row of the `group_1` and 1 (`path[3]`) points to the second row of the `group_2`.

### Event Handlers

Event handlers are special functions that allow users to add custom functionality on user-triggered and other events.
Event handler function name should have a strict format:
```python
on_<component id>_<event type>
```

There are three types of events:

- Component value change event - ```event type = change```, in this case the function receives two arguments:
path - the path of the trigger component
value - updated value of the trigger component
- Button click event - ```event = click```, in this case the function receives one argument:
path - the path of the trigger button
- Message event - ```event = message```, in this case the function receives two arguments:
path - the path of the trigger component
value - received message from the trigger component

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
```

### Custom functions

In the code editor you can use following custom functions:

- `getValue(path: List[Union[str, int]])` - returns the current value of the component by its provided path. *For more information about componets and value types please refer to component describtion.*

- `setValue(path: List[Union[str, int]], value)` - sets the value of the component by provided path. *For more information about componets and value types please refer to component describtion.*

- `repeatRow(path: List[Union[str, int]])` - appends a row to the group by provided path. *For more information about group component structure please refer to component describtion.*

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

    ### Get response as a JSON object
    response.json()

    return
```

There is one important thing you need to remember while using this module - all the methods are asyncrounous, meaning during the execution the UI will be blocked, therefore use it only with cases where http requests are fast enough. To use asyncronous functionality you can use `asyncs` sub module and add `await` to the function call to make it async.

Example:

```Python
import requests.asyncs as requests

def on_submit_click(path: List[Union[str, int]]):
    response = await requests.request(
        url='https://your.domain.com/your/path',
        method ="GET",
        headers = None
    )

    ### Get response as a JSON object
    response.json()

    return
```


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
# Introduction

SuperAnnotate LLM Toolkit is a web based low code application integrated into the SuperAnnotate platform. It allows users to create and manage rich web interfaces for data manipulation which is needed for high quality LLM fine tuning, prompt engineering, testing, etc.

LLM Toolkit consist of three main parts:
1. No code user interface builder
2. Python based user experience builder
3. Integration with the SuperAnnotate platform

## UI Builder

<font color="red">
TODO - UI builder structure<br>
</font>

### UI Components

There are multiple components available in the UI builder. Each component on the UI should have its own unique ID. Initially the component is created with auto generated ID, but it is possible to change it to a more meaningful value.

## User Experience Builder

<font color="red">TODO - UX builder structure - Left side - preview, variables. Right side - code editor</font>

## Code Editor

Here you can describe the functionality of your UI using Python. 

### Component Path

Each component is accessed through its own unique path. In case of components not placed in any group,  path is simply one element array containing the component’s id:<br>

```python
['component_id']
```

In case a component placed within a group (or multiple groups), the component path is an array of parent group ids, group row indexes and it’s own id:

```python
['parent_group_id', <group_row_index>, 'component_id']
```

**Example**. Let’s assume we have following UI:

![Nested groups UI](https://public-static-files.superannotate.com/documentation/images/component_paths_1.png "Nested groups UI")

Here we have a parent group *group_1*, in this group we have one text area *prompt*, another group *group_2* and in the *group_2* we have a text input *comment*. 
Now let’s assume we have three rows of *group_2* in the editor (for more information about how to add rows of a specific group refer to the group component description <font color="red">TODO add a link</font>):

![Nested groups UI on the editor](https://public-static-files.superannotate.com/documentation/images/component_paths_2.png "Nested groups UI on the editor")

Now let’s write paths for each component in the UI:

`group_1`:
```python
path = ['group_1']
```

prompt of the first row of its parent group `group_1` (actually there is only one row of this group):
```python
path = ['group_1', 0, 'parent']
```
here 0 (`path[1]`) points to the first row of the `group_1`.

comment of the second row of its parent group `group_2` (there are three rows of this group):
```python
path = ['group_1', 0, 'parent', 1, 'comment']
```
here 0 (`path[1]`) points to the first row of the `group_1` and 1 (`path[3]`) points to the second row of the `group_2`.

### Event Handlers

Event handlers are special functions that allow users to add custom functionality on user-triggered and other events.
Event handler function name should have a strict format:
```python
on_<component id>_<event type>
```

There are three types of events:

- Component value change event - ```event type = change```, in this case the function receives two arguments:
path - the path of the trigger component
value - updated value of the trigger component
- Button click event - ```event = click```, in this case the function receives one argument:
path - the path of the trigger button
- Message event - ```event = message```, in this case the function receives two arguments:
path - the path of the trigger component
value - received message from the trigger component

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
```

### Custom functions

In the code editor you can use following custom functions:

- `getValue(path: List[Union[str, int]])` - returns the current value of the component by its provided path. *For more information about componets and value types please refer to component describtion.*

- `setValue(path: List[Union[str, int]], value)` - sets the value of the component by provided path. *For more information about componets and value types please refer to component describtion.*

- `repeatRow(path: List[Union[str, int]])` - appends a row to the group by provided path. *For more information about group component structure please refer to component describtion.*

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

    ### Get response as a JSON object
    response.json()

    return
```

There is one important thing you need to remember while using this module - all the methods are asyncrounous, meaning during the execution the UI will be blocked, therefore use it only with cases where http requests are fast enough. To use asyncronous functionality you can use `asyncs` sub module and add `await` to the function call to make it async.

Example:

```Python
import requests.asyncs as requests

def on_submit_click(path: List[Union[str, int]]):
    response = await requests.request(
        url='https://your.domain.com/your/path',
        method ="GET",
        headers = None
    )

    ### Get response as a JSON object
    response.json()

    return
```


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
