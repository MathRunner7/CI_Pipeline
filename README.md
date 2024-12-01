# CI_Pipeline

Continuous Integration Pipeline

# How to write Unit tests

Unit tests are test which verifies individul function output with desired output

1. Create Python file and write desired code
   ![image.png](assets/create_python_file.png)
2. Create another python file to write function to test methods in existing python file
   ![image.png](assets/create_test_file.png)
3. Go to terminal, execute `pytest` to conduct a test and verify result
   ![image.png](assets/pytest.png)
4. Repeat step-1 to 3 for all other python files in project.![image.png](assets/another_python_file.png)![image.png](assets/another_test_file.png)![image.png](assets/another_pytest.png)

# Testing Flask Application with `fixture`

1. Create python file and write a code for Flask API
2. Create another python file to write function to test Flask APIs
   ![image.png](assets/flask_app_test.png)
3. Run `pytest` from terminal to check test result summary![image.png](assets/flask_pytest.png)
4. Test case for POST requests![image.png](assets/flask_app_POST_test.png)![flask_app_POST_pytest.png](assets/flask_app_POST_pytest.png?t=1733052785775)

# Automate the test with YAML file

1. Create a directory `.github\Workflows` if not available in project
   ![image.png](assets/Workflow_directory.png)
2. Inside `Workflows` directory, create new file `filename.yml`
   ![image.png](assets/new_yml_file.png?t=1733053950320)
3. Order of execution: Event -> Workflow -> Job -> Steps -> Actions
   1. The `action` tab in GitHub is triggered when an event occours.
   2. The triggered event cause the workflow to run. The workflow contains individuals tasks which are called actions.
   3. These actions are pre defined commands that perform specific tasks(job) like testing code.
   4. Each action can be further subdivided into steps. Steps contain of one or more command(actions) that are executed in order.
5.
