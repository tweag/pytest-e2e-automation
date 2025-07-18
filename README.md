pytest-e2e-automation
==================================
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![license](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/tweag/pytest-e2e-automation/api_workflow.yml)
![GitHub repo size](https://img.shields.io/github/repo-size/tweag/pytest-e2e-automation)
![GitHub last commit](https://img.shields.io/github/last-commit/tweag/pytest-e2e-automation)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/tweag/pytest-e2e-automation)


About the Project
-----------------
The pytest-e2e-automation enables you to test Web, API, Visual and Mobile native apps on web and mobile devices.

Usages
-----------------
* UI Web Test Automation with Pytest Selenium & Pytest BDD
* API Test Automation with Pytest & Requests
* Mobile Test Automation with Pytest & Appium
* Cross Browser Testing with BrowserStack/LambdaTest/SouceLabs
* Notifications with Slack & MS Teams
* Reporting with Allure & HTML
* Parallel Execution with Pytest-xdist


Getting Started
---------------
### Prerequisites

* Need a valid GitHub account.
* Having access to `pytest-e2e-automation` repository.
* Having installed your favourite IDEs (VSCode or Pycharm) and/or set up your development environment.

#### MacOS

1. <u><strong>Homebrew</strong></u>

   Make sure that `homebrew` is successfully installed. Check if it is already installed by typing `brew --version` in
   your terminal. for detailed Instructions: [HomeBrew Installation](https://brew.sh/)


2. <u><strong>Xcode</strong></u>

   Xcode tool should be installed. can check if it is already installed using command `xcode-select --version`. If not already
   installed, install by typing command `xcode-select --install` in terminal.


3. <u><strong>Android Studio for Local Android Native App </strong></u>

   Ensure to have Android Studio tool installed. and Install Virtual Device Simulator ("deviceName": "emulator-5554").


4. <u><strong>Git</strong></u>

   Install latest version of Git. Most Mac Machines come with latest version of Git pre-installed. Check if you have git
   installed by typing `git --version` in your terminal.


5. <u><strong>Python</strong></u>

   *Recommended Version of Python: 3.9.12*

    We can use `pyenv` to install latest version of Python by
   following below instructions. Detailed Instructions here: [pyenv](https://github.com/pyenv/pyenv)

   *For any issues faced during installation, please refer pyenv GitHub [here](https://github.com/pyenv/pyenv)*

    ```shell
    brew update
    brew install openssl readline sqlite3 xz zlib
   
    ```
   
   *Manual Python 3.9.12 installer: [here](https://www.python.org/downloads/release/python-3912/)*
<p align="right">(<a href="#about-the-project">back to top</a>)</p>

### Project Installation

1. <u><strong>Clone Project</strong></u>
   Clone the `master` branch from Github to your local machine by following below instructions.

    ```shell
    mkdir project_space && cd project_space
    git clone https://github.com/tweag/pytest-e2e-automation.git
    # alternatively, you could use ssh link if you have setup ssh in your work machine.
    ```

2. <u><strong>Source setup_install.sh</strong></u>
   After successful cloning, execute below commands to install Project (for local, If would like to pypass this script then 
    follow the manual installation through (**pip install -r requirements.txt**)

    ```shell
    cd pytest-e2e-automation/
    pip install -r requirements.txt

3. <u><strong>Environment Variables in `.local.env` & `pytest.ini` files</strong></u>
    Update the environment variables in `.local.env` file and `pytest.ini` file as per your local machine setup.
    The `.local.env` file is used to set up the environment variables for the project. The `pytest.ini` file is used to
    configure pytest settings.
    
     ```shell
     # .local.env
     # Set up your environment variables here
     ```
    
     ```shell
     # pytest.ini
     # Set up your pytest configuration here
     ```
   
4. <u><strong>Appium setup for Mobile apps</strong></u>
    To run mobile tests, you need to install Appium server and start it before running the tests.
   Detailed instructions can be found [here](https://appium.io/docs/en/latest/quickstart/)

5. <u><strong>Local Setup for BrowserStack</strong></u>
    To run tests on BrowserStack, you need to install BrowserStack Local binary and start it before running the tests.
    Detailed instructions can be found [here](https://www.browserstack.com/local-testing/automate#test-localhost-websites)

6. <u><strong>Local Setup for Docker</strong></u>
    you need to install Docker desktop before running the docker-compose.yml file.
    Detailed instructions can be found [here](https://docs.docker.com/desktop/install/mac-install/)

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

### Executing Test Cases in Local Machine

`pytest` to run ui tests in Chrome browser with 1 threads in parallel:

```shell
python -m pytest -vv -s  --gherkin-terminal-reporter --driver=Chrome  --html="./output_data/reports/" --self-contained-html  --capability headless True  --reruns 1 --reruns-delay 2 --tags="test1" -n 1
```

pytest-e2e-automation framework uses built-in driver manager to handle the driver binaries for each browser.


### Project Structure

```bash
.
├── /                                         # root directory with project-wide env_configs and folders
├── /mobile_app                               # directory with all android and ios builds
├── /browserstack_local                                # directory contains all the driver binaries / Browserstack local binary
├── /main                                     # directory contains all the base code (utils, plugins, common steps...) for the framework
├── /env_configs/                             # Configurations related to framework & browser specific
├── /e2e/                                     # Project specific files (locators, page objects, step definitions, feature files... etc)
├── /e2e/demo_project/features/*                           # Test cases written in Gherkin language
├── /e2e/demo_project/locators/*                           # Web locators for the project
├── /output_data/                                  # Reports, downloads.... etc)
├── /test_data/                               # All project test data for API, WEB, Mobile tests)
│   ├── /conftest.py                          # Step up and tear down for the tests
│   ├── /pytest.ini                           # Project init file
│   ├── /docker-compose.yml                   # To build the docker image
│   ├── /README.md                            # Instructions for the project
│   ├── /requirements.txt                     # Dependencies

```
### Browserstack Interaction

#### Browserstack execution through command line params

Run tests on different browsers using the below command:
```shell
# Usage example for Windows 11 - Chrome
username@hostname pytest-e2e-automation % python -m pytest -v --reruns 1 --reruns-delay 1 --gherkin-terminal-reporter --driver Remote --selenium-host '[BS_USERNAME]:[BS_KEY]@hub-cloud.browserstack.com' --capability browserName 'Chrome' --capability os 'Windows' --capability osVersion '11' --capability build 'qa' --capability browserstack 'True' --tags="api"
```

3. For running parallel test from local in the browserstack you can add **-n [parallel threads value] -> e.g.: "-n '2'"]** to your command.
   -n represents the number of processes to execute the test cases in parallel mode.
   We can also pass "**auto**" to use as many processes as your computer has CPU cores. This can lead to considerable
   speed ups, especially if your test suite takes a noticeable amount of time.

Reference Link - https://pypi.org/project/pytest-xdist/

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

#### Browserstack Mobile

* First upload your Android app (.apk) or iOS app (.ipa file) to BrowserStack servers using Browserstack portal or using
  BrowserStack API.

* We will get a app_url from the BrowserStack portal or API. This app_url will be used in the test cases to run the tests.

```shell
{
    "app":"bs://j3c874f21852ba57957a3fdc33f47514288c4ba4"
}
```

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

Command for local run on chrome (also ./local_run_web.sh)
```shell
-v -s  --gherkin-terminal-reporter --driver=Chrome  --html="./output_data/reports/" --self-contained-html --capability headless True --tags="web_tests" --reruns 1 --reruns-delay 2 -n=2
```
Command for local run on firefox
```shell
-v -s  --gherkin-terminal-reporter --driver=Firefox --capability headless True --html="./output_data/reports/" --tags="web_tests" --self-contained-html --reruns 1 --reruns-delay 2 -n=1
```
Command for local run on BS with Chrome:
```shell
-v -s  --gherkin-terminal-reporter --driver=Remote --selenium-host '[BS_USERNAME]:[BS_KEY]@hub-cloud.browserstack.com' --variables="env_configs/mac_chrome.json" --html="./output_data/reports/" --tags="web_tests" --reruns 1 --reruns-delay 2 --self-contained-html
```
Command for local run on local appium server:
```shell
-v -s  --gherkin-terminal-reporter --driver=Appium --html="./output_data/reports/" --tags="mobile_test and android" --variables="env_configs/android_mobile_local.json" --self-contained-html --reruns 1 --reruns-delay 2
```
Command for local run on BS with IOS:
```shell
-v -s --gherkin-terminal-reporter --disable-warnings --driver=Appium --html="./output_data/reports/" --selenium-host '[BS_USERNAME]:[BS_KEY]@hub-cloud.browserstack.com' --variables="env_configs/ios_mobile_BS.json" --self-contained-html --tags="mobile_test and ios" --reruns 1 --reruns-delay 2
```
There is a param in .local.env file to set the integration:
```shell
# BROWSERSTACK , SAUCELABS, DOCKER
USING_ENV=SAUCELABS
```
### Html Test Reports
To generate a html report please add following arguments to your command:
```shell
--html=<path_to_report> and --self-contained-html
```
`<path_to_report>` - Project path where the html report will be created.
</br>
For example:
</br>
`--html=./output_data/reports/`

Example of full command to generate html reports:
```shell
python -m pytest -v --tags="sample-ui-tests" -n=3 --variables=./env_configs/web_local.json --driver=chrome --html=./output_data/reports/ --self-contained-html
```
Please avoid adding `-s` in the CLI since it will not include any logs in the html report.
</br>
</br>

### Allure Reports
by default allure report generates at output_data/allure/reports at the end of test execution, results are inside /output/allure/results folder. 

### Github Workflows
A list of workflows are added in the .github/workflows folder. e.g
Docker execution, Browserstack execution, Local execution, Mobile execution etc.
** about billing of github actions, please check the github documentation. (https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)

Notifications
---------------------
**Slack and MS Teams notifications support is available, we can set webhooks in pytest.ini file**

# Slack Notification:
    --slack-webhook-url=https://hooks.slack.com/services/....
    --slack-channel=pytest-test-automation
    --slack-failure-only=true
    --slack-results-url=http://localhost:63342/pytest-e2e-automation/output_data/allure/reports/index.html
# Teams Notification:
    --teams-webhook-url=https://moduscreate.webhook.office.com/...
    --teams-failure-only=true
    --teams-results-url=http://localhost:63342/pytest-e2e-automation/output_data/allure/reports/index.html

** Local web driver warnings (if any) resolution for Safari browser on mac**
```shell
/usr/bin/safaridriver --enable
```
For chrome webdriver warning (if any):
```shell
xattr -d com.apple.quarantine $(which chromedriver)
```


Project update
---------------------
<b>To be decided soon...</b>

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

------------
