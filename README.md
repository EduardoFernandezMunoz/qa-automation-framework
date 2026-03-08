# QA Automation Framework

Automated testing framework built with **Python, Selenium, Pytest, and Requests** to validate both **UI workflows and REST APIs** in a single project.

The framework uses **Page Object Model (POM)** for UI automation and a **client-based structure** for API testing.
Tests are automatically executed through **GitHub Actions CI**.


## Features

* UI automation with **Selenium WebDriver**
* API testing with **Requests**
* **Pytest** test runner
* **Page Object Model (POM)** architecture
* **Data-driven testing** using JSON
* **GitHub Actions CI integration**
* Automatic **HTML and JUnit test reports**
* Clear separation between **UI and API test layers**


## Project Structure

```
qa-automation-framework
│
├── api
├── pages
├── tests
│   ├── api
│   └── ui
├── data
├── utils
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Technologies

* Python
* Selenium WebDriver
* Pytest
* Requests
* GitHub Actions


## Test Coverage
### UI Testing
Automates the purchase workflow of the demo e-commerce site:

https://www.saucedemo.com

Covered scenarios:
* User login
* Product selection
* Add products to cart
* Cart validation
* Checkout process
* Order completion
* Full end-to-end purchase flow

UI automation follows the **Page Object Model** to separate test logic from page interactions.


### API Testing
API tests validate endpoints from:

https://jsonplaceholder.typicode.com

Covered endpoints:

```
GET /users
GET /users/{id}
GET /posts?userId={id}
POST /posts
```

Validations include:
* Response status codes
* JSON structure
* Expected fields
* Payload validation


## Continuous Integration
Tests run automatically through **GitHub Actions** on every push and pull request.
The pipeline installs dependencies, executes UI and API tests, and uploads test reports as artifacts.