


# Dont copy paste - Just Automate


Fed up with the code editor where copy paste has been disabled we have a solution for you Just automate typing in the online editor.
Code in your editor and then automate the typing in the online editor using our code.




## Requirements

A code editor of your choice, in case you dont have it download [PyCharm](https://www.jetbrains.com/pycharm/).

You need to have python in our device,in case you dont have it download python from [here](https://www.python.org/downloads/)

Most version of python come with bulit-in pip installed, if it isn't installed download it from [here](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/)  

Finally install PyAutoGUI using the below command

```bash
  pip install PyAutoGUI
```


    
## Run Locally

Copy the code from main.py into your IDE. Place the code that you want to type in variable '''code_to_type''' of main.py. Look at an example below
```
code_to_type = """
def print_greetings():
    print("Hello World")```

print_greetings()
"""
```

set the variable ```wait_time``` (in seconds). This is time before auto typing starts.
Run the code in your editor.
Then place your caret(text cursor) in the text box that you want the code to be auto typed.
