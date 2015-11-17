#todomvc-test
Proof of concept automation testing using selenium and py.test for TodoMVC applications.
The target URL are:
- TodoMVC-AngularJS http://todomvc.com/examples/angularjs/#/
- TodoMVC-ReactJS http://todomvc.com/examples/react/#/


###Requirements

1. Python 2.7
2. Selenium Webdriver 0.2.11
3. Selenium standalone server http://www.seleniumhq.org/download/
3. Py.test 2.8.2
   ```
   pip install pytest
   ```
4. Fake-Factory 0.5.3
   ```
   pip install fake-factory
   ```
5. Supported browser: Crome, Firefox, and PhantomJS (dev). You can add other browser by add the driver configuration in the conftest.py


###How to Use

Run the Selenium server in your console
```
java -jar selenium-server-standalone-2.48.2.jar
```

Execute all test in all browser (except the headless). Open a console, the type the command below:
```
cd todomvc-test
py.test
```
The above command will run all test case both of TodoMVC-AngularJS and TodoMVC-ReactJS in chrome and firefox browser. If you want to execute in the specific browser or specific apps, use the command line option --browseropt or --appopt

#####Execute the Specific Apps
Execute test cases only for TodoMVC-ReactJS
```
py.test --appopt=react
```
Execute test cases only for TodoMVC-AngularJS
```
py.test --appopt=angular
```
If the --appopt is not specified, the test will be run for both of applications.

#####Execute in Specific Browser
Execute only in Firefox browser
```
py.test --browseropt=firefox
```
Execute only in Chrome browser
```
py.test --browseropt=chrome
```

#####Execute specific apps in specific browser
Execute TodoMVC-ReactJS in chrome browser
```
py.test --browseropt=chrome --appopt=react
```

#####Execute specific files
Only execute the todos creation test cases
```
py.test tests/test_creating_todos.py --browseropt=chrome --appopt=react
```

###How to Verify the test result
The pytest will report the test result in the console. If the test failed, the trace result will be displayed in the console, so you can check whether the failure is caused by the defect or false negative.

#####Success
All of the test cases should be succed.

#####Failure
Sometimes, failure will occurs because unexpected factors like bad internet connection, or changes on the website. If you found the failed test case, please re-run the test and see the playback. The pytest will displaying the trace where the test failed. It can help you find the reason why the test failed.

#####False Positive
Test is marked as failed even in reality it is passed, or the functionality works properly. When we face this case, re-run the automation test. If still failed, see the trace result. Or you can run the test manually to ensure that the applications is working properly.

#####False Negative
Test is marked as passed even in reality it is failed or there is some problem in functionality or there is a bug.False negatives are more dangerous than false positives because it can lead to sever problem after the software is released or in case of web apps the site may be hacked or user data may be compromised.
