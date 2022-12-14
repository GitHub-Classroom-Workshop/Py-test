# Py-test

## Overview

In this session, we will learn about workflows for unit testing by doing some hands-on examples to get a feel for how this works.  In our examples, we are using a workflow to automatically perform unit testing on python scripts.

Getting workflows and unit testing right can be fiddly, but it is incredibly powerful and is an important aspect of programming and software development.

## Part I: fixing a script

In this repository you will find:

- this `README.md` file;
- a python script `index.py`, which contains user-defined functions that must pass specific tests;
- a test script `test.py`, which specifies the unit tests that `index.py` must pass.

Your repository will *fail* the unit tests.  You can see what happened when the tests were triggered by navigating to the `Actions` menu.  There you will see a list of instances when the repository workflow was triggered - find the most recent one and click through the tests to try to understand why the workflow run failed.


#### Exercise 1
1. Edit the following functions(`woord_count`, `char_count`, `first_char`, `last_char`) in `index.py` so that the workflow run passes.

**Note :** If you are to use Codespace, to test your code, run the following code in the terminal  
- Neglect all prompt
- `pip install pytest`   to install pytest module
- `python3 -m pytest test.py` to run test.py script
- Navigate to the side bar to locate `Source Control`, name/commit your changes and Sync Chnages.
- Go back to your github tab to confirm the changes by clicking `Actions`. Your commit name appeares which turns green if all test is passed.
