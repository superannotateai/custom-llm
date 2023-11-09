# Introduction

SuperAnnotate's LLM Toolkit is a web based, low-code application integrated into the SuperAnnotate platform. It allows users to create and manage rich web interfaces for data manipulation, which is needed for cases such as high quality LLM fine-tuning, prompt engineering, testing, etc.

The LLM Toolkit consists of three main parts:
1. [No-code user interface builder](#ui-builder)
2. [Python-based user experience builder](#code-editor)
3. [Integration with the SuperAnnotate platform](#integration-with-the-superannotate-platform)

## UI Builder

This is the builder that you'll use to create your LLMs and GenAI form. The builder is separated into two sections that will help you build and edit your form based on your project's requirements. These sections are the **UI builder** and the **Code editor**. Building the form involves the use of various **UI components** and their customized functionality.

### UI Components

There are multiple components available in the UI builder. Each component on the UI should have its own unique ID. Initially the component is created with an auto-generated ID, but it is possible to change it to a more defining value.

#### **`Group`**

The Group is a container component which can be used to create multiple rows of itself. It is useful for creating conversation-like experiences where you need to have multiple rows of same selection of components.

##### Parameters

- `Initially hidden` - Checkbox. Disabled by default. When enabled, one row of the group is created during the initialization stage of the editor.
- `Removable` - Checkbox. Disabled by default. When enabled, an `X` button will be added to each row of the group, providing the option to delete the row.

##### Related Functions

- `repeatRow(path: List[Union[str, int]])` - Appends a row to the group, returns the path of the newly created row.
- `deleteRow(path: List[Union[str, int]])` - Deletes the row of the group, specified by the row index in the `path`.
- `getGroupLength(path: List[Union[str, int]])` - Returns the length of the group (the number of rows).

##### Related Events

- `on_<component id>change(path: List[Union[str, int]]):` - Fired when a group row is deleted by the user by pressing the `X` button, receives the path of the newly deleted row.

![Group example in playground](https://public-static-files.superannotate.com/documentation/images/group_component.gif "Group example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/group.json)

#### **`Grid`**

The Grid is a container component which provides the ability to horizontally arrange content in the UI.

##### Parameters

- `Resizable` - Checkbox. Disabled by default. When enabled, it is possible to resize the width of each column in the grid.
- `Columns` - Manipulation menu. Here you can add or remove columns, and set their height.
- `+ Add column` - Clicking this will add another column. You can remove them again by clicking the delete button on the right side of each column.

![Grid example in playground](https://public-static-files.superannotate.com/documentation/images/grid_component.gif "Grid example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/grid.json)

#### **`Tabs`**

Tabs are a container component that allows you to organize and structure your content into separate tabs. Each tab's content is only visible when that tab is selected.

##### Parameters

- `Tabs` - Manipulation menu. Here you can add, remove, and rename tabs.
- `+ Add tab` - Clicking this will add another tab. You can remove them again by clicking the delete button on the right side of each tab.

![Tabs example in playground](https://public-static-files.superannotate.com/documentation/images/tab_component.gif "Tabs example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/tab.json)

#### **`Primary`**

This button is a simple component that can be programmed to respond in any given way when clicked.

##### Parameters

- `Button text` - Text input indicating the button text.

##### Related Events

- `on_<component id>click(path: List[Union[str, int]]):` - Fired when the button is clicked.

![Primary button example in playground](https://public-static-files.superannotate.com/documentation/images/button_component.gif "Primary button example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/button.json)

#### **`Secondary`**

This button is a simple component that can be programmed to respond in any given way when clicked.

##### Parameters

- `Button text` - Text input indicating the button text.

##### Related Events

- `on_<component id>click(path: List[Union[str, int]]):` - Fired when the button is clicked.

![Secondary button example in playground](https://public-static-files.superannotate.com/documentation/images/button_component.gif "Secondary button example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/button.json)


#### **`Text input`**

This field can be used for any case (name, email, etc.) and can be further edited by label, placeholder and more.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Placeholder` - Text input indicating the placeholder.
- `Min length` - Minimum text length to consider the input as valid.
- `Max length` - Maximum text length to consider the input as valid.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Hide during labeling` - Checkbox. Disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the background.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the text value is changed by the user, receives the component's path and the text value.

![Text input example in playground](https://public-static-files.superannotate.com/documentation/images/input_component.gif "Text input example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/text-input.json)

#### **`Text area`**

This is a text box that gives the user a large area to input text into. This can be used for cases where longer/bigger answers are required.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Placeholder` - Text input indicating the placeholder.
- `Min length` - Minimum text length to consider the input as valid.
- `Max length` - Maximum text length to consider the input as valid.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Hide during labeling` - Checkbox. Disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the background.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the text value is changed by the user, receives the component's path and the text value.

![Text area example in playground](https://public-static-files.superannotate.com/documentation/images/text_area_component.gif "Text area example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/text-area.json)


#### **`Number`**

This is a numeric input field. The number entered here can be increased or decreased by using the arrows on the right side of the input field.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Min length` - Minimum text length to consider the input as valid.
- `Max length` - Maximum text length to consider the input as valid.
- `Step` - Increment by which the number is modified.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Hide during labelimg` - Checkbox. Disabled by default. When enabled, this component will be hidden on the main form. This option is useful when you want to store any data in the background.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: Union[int, float])` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: Union[int, float]):` - Fired when the number value is changed by the user, receives the component's path and the number value.

![Number example in playground](https://public-static-files.superannotate.com/documentation/images/numeric_component.gif "Number example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/number.json)


#### **`Code`**

This is a code component that allows the user to write or edit any kind of code. If you type in a default code block, it can later be edited when viewed in the form.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the code value is changed by the user, receives the component's path and the code value.

![Code example in playground](https://public-static-files.superannotate.com/documentation/images/code_component.gif "Code example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/code.json)

#### **`Paragraph`**

This is a text component. You can have a paragraph of text on your form, with or without a label.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Text` - The text content of the paragraph.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value)` - Sets the data of the component.

![Paragraph example in playground](https://public-static-files.superannotate.com/documentation/images/paragraph_component.gif "Paragraph example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/paragraph.json)

#### **`Select`**

This allows you to add a dropdown menu to your form with selectable options.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Placeholder` - Text input indicating the placeholder.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.
- `Select type` - Radio button. You can specify if the options should be single or multi-select.
- `Options` - Manipulation menu. Here you can add, remove and rename options. You can define default values as well.
- `+ Add option` - Clicking this will add another option. You can remove them again by clicking the delete button on the right side of each option.
- `Reset defaults` - If you have one or multiple options selected as the default, this will reset the selection.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value)` - Sets the data of the component. For single-select: `value: str`. For multi-select: `value: List[str]`.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value):` - Fired when the checkbox value is changed by the user, receives the component's path and the checkbox value. For single-select: `value: str`. For multi-select: `value: List[str]`.

![Select example in playground](https://public-static-files.superannotate.com/documentation/images/select_component.gif "Select example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/select.json)

#### **`Slider`**

This slider can be used to set a range between two numbers.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Min value` - Minimum value of the slider.
- `Max value` - Maximum value of the slider.
- `Step` - Increment by which the number is modified.
- `Suffix` - A suffix appended to the slider value popup.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.
- `Slider type` - Radio button. Specify if the slider represents a single value or a range.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: Union[int, float])` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: Union[int, float]):` - Fired when the slider value is changed by the user, receives the component's path and the slider value.

![Slider example in playground](https://public-static-files.superannotate.com/documentation/images/slider_component.gif "Slider example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/slider.json)

#### **`Checkbox`**

This component provides text label to input a name, sentence or question, as well as a list of multiple selection options.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.
- `Options` - Manipulation menu. Here you can add, remove and rename options. You can define default values as well.
- `+ Add option` - Clicking this will add another option. You can remove them again by clicking the delete button on the right side of each option.
- `Reset defaults` - If you have one or multiple options selected as the default, this will reset the selection.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: List[str])` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: List[str]):` - Fired when the checkbox value is changed by the user, receives the component's path and the checkbox value.

![Checkbox example in playground](https://public-static-files.superannotate.com/documentation/images/checkbox_component.gif "Checkbox example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/checkbox.json)


#### **`Radio`**

This component provides text label to input a name, sentence or question, as well as a list of single selection options.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.
- `Options` - Manipulation menu. Here you can add, remove and rename options. You can define default values as well.
- `+ Add option` - Clicking this will add another option. You can remove them again by clicking the delete button on the right side of each option.
- `Reset defaults` - If you have one or multiple options selected as the default, this will reset the selection.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the radio value is changed by the user, receives the component's path and the radio value.

![Radio example in playground](https://public-static-files.superannotate.com/documentation/images/radio_component.gif "Radio example in playground")

[Try in Playground](https://llm.superannotate.com/builder?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/radio.json)


#### **`Voting`**

With this component, you can add an approval response.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Required` - Checkbox. Disabled by default. When enabled, input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: int)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: int):` - Fired when the voting value is changed by user, receives the component's path and the voting value - `0` or `1`.

![Voting example in playground](https://public-static-files.superannotate.com/documentation/images/voting_component.gif "Voting example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/voting.json)


#### **`Rating`**

This component allows you to add a rating to your form.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Number of stars` - Number of stars to use in the rating.
- `Required` - Checkbox. Disabled by default. When enabled, the input is considered invalid if left empty (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: int)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: int):` - Fired when the rating value is changed by the user, receives the component's path and rating.

![Rating example in playground](https://public-static-files.superannotate.com/documentation/images/rating_component.gif "Rating example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/rating.json)


#### **`Date`**

This component allows you to choose a specific time or date.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Include time` - Checkbox. Disabled by default. When enabled, the time picker is visible.
- `Required` - Checkbox. Disabled by default. When enabled, the input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the date/time value is changed by the user, receives the component's path and the date/time value.

![Date example in playground](https://public-static-files.superannotate.com/documentation/images/date_component.gif "Date example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/date_time.json)


#### **`Time`**

This component allows you to choose a specific time.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Required` - Checkbox. Disabled by default. When enabled, the input is considered invalid when there is no text (it is impossible to complete items with invalid inputs).
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when the time value is changed by the user, receives the component's path and the time value.

![Time example in playground](https://public-static-files.superannotate.com/documentation/images/date_component.gif "Time example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/date_time.json)


#### **`Image`**

This is an image component. It displays any image, whether you provide the source for it or if the user uploads one.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Source URL` - A source URL of the image.
- `Alt text` - Alternative text.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the url of the image component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the url of the image component.

![Image example in playground](https://public-static-files.superannotate.com/documentation/images/image_component.gif "Image example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/image.json)


#### **`Web`**

With this component, you can either provide a URL or your own code to display a webpage in the form.

##### Parameters

- `Source` - There are two options to build your web component with: **Source URL**, and **Code**.
- `URL` - This is visible when `URL` is selected under `Source`. In this field, you can provide the url of the webpage you want to show in your form.
- `Code` - This will change the component into a code editor that you can write your web code in. You'll also be able to switch to a `Preview` tab so that you can see what it'll look like before creating the form.
- `Height` - Numeric input that defines the height of the web component.
- `Exclude from export` - Checkbox. Enabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the code's source url or the code itself based on the web component configuration.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the code's source url or the code itself based on the web component configuration.
- `postMessageToWebComponent(path: List[Union[str, int]], message: Union[str, dict])` - Sends the `message` string to the web component.

##### Related Events

- `on_<component id>_message(path: List[Union[str, int]], value: Union[str, dict]):` - Fired when there is a message from the web component, receives the component's path and the value of the incoming message.

##### Sending messages from web component

- `window.parent.postMessage({ action: 'topy', data }, "*");` - Use this JavaScript function to send a message to the main editor. Use `topy` as an action identifier.

![Web example in playground](https://public-static-files.superannotate.com/documentation/images/web_component.gif "Web example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/web.json)


#### **`Video`**

This is a video component. It displays any video, whether you provide the source for it or if the user uploads one.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Source URL` - A source URL of the video.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the url of the video component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the url of the video component.

![Video example in playground](https://public-static-files.superannotate.com/documentation/images/video_component.gif "Video example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/video.json)


#### **`Audio`**

This is an audio component. It displays any audio clip, whether you provide the source for it or if the user uploads one.

##### Parameters
- `Label` - Text input indicating the label of the component visible in the UI.
- `Source URL` - A source URL of the audio.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the url of the audio component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the url of the audio component.

![Audio example in playground](https://public-static-files.superannotate.com/documentation/images/audio_component.gif "Audio example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/audio.json)


#### **`Avatar`**

This component is an avatar icon display. It displays an avatar image, whether you provide the source for it or if the user uploads one.

##### Parameters

- `Label` - Text input indicating the label of the component visible in the UI.
- `Source URL` - A source URL of the avatar image.
- `Alt text` - Alternative text.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the url of the avatar component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the url of the avatar component.

![Avatar example in playground](https://public-static-files.superannotate.com/documentation/images/avatar_component.gif "Avatar example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/avatar.json)


#### **`CSV`**

This component allows you to display editable CSV grids in your forms.

##### Parameters:
- `Label` - Text input indicating the label of the component visible on the UI.
- `Value` - Text input field where the CSV data can be filled. The delimiter can be used to divide the data into columns.
- `Delimiter` - This is where you can select what symbol to use to divide your data into columns.
- `Exclude from export` - Checkbox. Disabled by default. When enabled, the value of the component will be excluded from the exported annotation JSON.

##### Related Functions

- `getValue(path: List[Union[str, int]])` - Returns the data of the component.
- `setValue(path: List[Union[str, int]], value: str)` - Sets the data of the component.

##### Related Events

- `on_<component id>change(path: List[Union[str, int]], value: str):` - Fired when there is a change in the component's CSV data, receives the component's path and the CSV content.

![CSV example in playground](https://public-static-files.superannotate.com/documentation/images/csv_component.gif "CSV example in playground")

[Try in Playground](https://llm.superannotate.com/editor?url=https://github.com/superannotateai/custom-llm/blob/main/documentation/examples/csv.json)


## User Experience Builder

In the User Experience Builder, you can define the functionality behind your form. On the lefthand side, you can see your form preview and your variables, and on the righthand side you can see the Code editor. There, you can input custom code and call custom variables so that your form can function the way you need it to.

## Code Editor

This is your code editor. Using Python, you can customize your form's code extensively to produce the functionality you want. Based on the components you chose in the **UI builder**, their layout and their individual property values and settings, the builder will automatically generate a base code structure that outlines your form. You can use this and build on it as you like by manipulating the existing code or using any of your custom variables.

Above the code editor, you have two buttons that you can use: **Regenerate** and **Run**.

### Run

To test your code after editing, you must click **Run** to update the form preview.

### Regenerate

After your form's base code is generated, when you make changes to your form in the UI builder, the code editor will be modified accordingly. Clicking **Regenerate** will replace the code with an initial state based on the updated form UI. If there are any lines of custom code that you want to keep, make sure to have a copy of them with you before regenerating the code editor.

### Component Path

Each component is accessed through its own unique path. In the case of a component that isn't placed in any group, the path is simply one element array containing the component’s ID:<br>

```python
['component_id']
```

If a component is placed within a group, the component's path is an array of the parent group's ID, the group's row index, and the component's ID:

```python
['parent_group_id', <group_row_index>, 'component_id']
```

If a component is placed within a nested group (`group_1 -> group_2 -> group_3`), the component's path is an array of the parent group's IDs, the group's row indexes, and the component's ID:

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
    - path - the path of the trigger component
    - value - updated value of the trigger component
- Button click event - ```event = click```, in this case the function receives one argument:
    - path - the path of the trigger button
- Message event - ```event = message```, in this case the function receives two arguments:
    - path - the path of the trigger component
    - value - received message from the trigger component
- Group row deleted event - ```event type = deleted```, this event is fired when a row in a group is being deleted by pressing `X` button. The handler function receives one argument:
    - path - the path of the trigger row
- ```pre_hook()``` - Fired when an item is being opened in the editor.
- ```post_hook()``` - Fired when an item is being closed in the editor.

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

In the code editor, you can use following custom functions:

- `getValue(path: List[Union[str, int]])` - Returns the current value of the component by the provided path. *For more information about components and value types, please refer to the component descriptions.*

- `setValue(path: List[Union[str, int]], value)` - Sets the value of the component by the provided path. *For more information about components and value types, please refer to the component descriptions.*

- `repeatRow(path: List[Union[str, int]])` - Appends a row to the group by the provided path. This function returns the path of newly created row. *For more information about the group component's structure, please refer to the component descriptions.*

- `deleteRow(path: List[Union[str, int]])` - Deletes the row of the group specified by path. Here, the path should include the row index. *For more information about the group component's structure, please refer to the component descriptions.*

- `getGroupLength(path: List[Union[str, int]])` - Returns the number of rows in the group by its path. *For more information about the group component's structure, please refer to the component descriptions.*

- `postMessageToWebComponent(path: List[Union[str, int]], message)` - Sends a message to a web component specified by the provided path. *For more information about the web component's structure, please refer to the component descriptions.*

- `setLoading(on_off: bool)` - Enables/disables the loading icon. The icon replaces the page's layout when enabled.

- `getPayload()` - Returns data attached to the item when the function is called in the editor. Returns no data when in build mode. *For more information, refer to the [Integration with the SuperAnnotate platform](#integration-with-the-superannotate-platform) section.*

### HTTP Requests from The Code

To send HTTP requests, it is recomended to use the `requests` module, which was created by SuperAnnotate to replicate the [Python requests module](https://pypi.org/project/requests/). The only difference is the browser limitation. In most cases, you will not see any difference.

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

There is one important thing you need to remember while using this module - all the methods are asynchronous, meaning during the execution the UI will be blocked. Therefore, you should only use it with cases where the HTTP requests are fast enough. To use the asynchronous functionality, you can use `asyncs` sub module and add `await` to the function call to make it asynchronous.

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

## Environment Variables

In the variables tab, you can define as many custom variables as you need that can then be used in the code editor. 

To add a new variable:

1. Click **+ Add Variable**.
2. Type in a name for your variable.
3. Type in a value.
4. Check **Secure** to keep this value private when exporting templates (Optional).

You can delete a variable by clicking its corresponding **Delete** button on the right side.

The variables will be imported into your code as follows:

```python
from environments import (
    variable_name_1,
    variable_name_2,
    variable_name_3
)
```

## Integration with the SuperAnnotate platform

### Data Input

There are two main ways of data input:

1. Add an item to the SuperAnnotate platform using one of the following methods:
    - [Import data with cloud integrations](https://doc.superannotate.com/docs/integrations)
    - [Import data with Python SDK](https://doc.superannotate.com/docs/sdk-import-other)

    Each data item should be a valid JSON file. A key advantage here is that you can specify your own schema and modify the values in the UI builder or in the code editor.

    **Example**. Let’s assume we have a JSON file imported from an AWS S3 bucket using the cloud integration method.

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

    Let’s assume you want to display the **name** and **category** values as paragraphs on the UI. To do this, you simply need to add the `{{metadata.name}}` and `{{metadata.category}}` expressions in the component configuration field, as it is shown below:

    ![Text expression](https://public-static-files.superannotate.com/documentation/images/data_in_0.png "Text expression")

    For cases that include a data item that should be signed as an integration item, you need to use a specific function: `{{sign(metadata.image_url)}}`

    ![Signed url expression](https://public-static-files.superannotate.com/documentation/images/data_in_1.png "Signed url expression")

2. Add an item to the SuperAnnotate platform using [item generation](https://doc.superannotate.com/docs/generate-items). In this case, you will need to input data manually from the code editor.

### Data Output
