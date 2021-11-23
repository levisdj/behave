# behave
    # Description:
    The idea behind this project is to implement a BDD-Behave using Robot Framework.
    Currently I've mixed (in this same project) a normal "BDD-Behave with Selenium and Python" and a BDD-Behave with Robot Framework;
    Thus I have 2 features file (one to be used with Selenium/Python and one to tbe used with Robot Framework).

    # Execution:
    First of all activate the virtual env running this command: source venv/bin/activate
    Behave/Selenium from terminal: behave features/login.feature
    Robot Framework from terminal: robot features/steps/test_login.robot
    