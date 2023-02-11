# Introduction
Python Flask applicaion with Azure AD

# Components
- Python
- Flask
- Azure AD

# Directory structure
\docs\scripts\azure\flaskapp-aad
|-- app/
    |-- __init__.py
    |-- db.py
    |-- schema.sql
    |-- templates/
    |   |-- base.html
    |   |-- auth/
    |       |-- register.html
    |       |-- login.html
    |   |__ dashboard/
    |       |-- index.html
    |-- static/
        |-- style.css
|-- tests/
    |-- conftest.py
    |-- test_db.py
|-- setup.py
|-- MANIFEST.in

# Running in debug mode
```shell
$ flask --app hello run
$ flask --app hello --debug run
```
- assuming hello.py file is present in the directory

# Azure ad
- app registration name: flaskapp-aad-onprem-auth
![Azure Auth flow](https://registeredapps.hosting.portal.azure.net/registeredapps/Content/1.0.0220094/Quickstarts/en/media/quickstart-v2-python-webapp/python-quickstart.svg)

## Step1:
- Add a reply URL as http://localhost:5000/getAToken
- add client secret
- Add Microsoft Graph API's User.ReadBasic.All delegated permission.



# reference
- MSAL - https://github.com/AzureAD/microsoft-authentication-library-for-python
- Flaskapp redirect - https://www.askpython.com/python-modules/flask/flask-redirect-url
- MSAL python documentation - https://msal-python.readthedocs.io/en/latest/
- Microsoft Identity platform code samples - https://learn.microsoft.com/en-us/azure/active-directory/develop/sample-v2-code#web-applications

# Issues - how to fix
- The redirect URI specified in the request does not match - https://learn.microsoft.com/en-gb/troubleshoot/azure/active-directory/error-code-aadsts50011-redirect-uri-mismatch
    - use the Flaskapp redirect mentioned above to fix the reply url

- invalid token. 
    - add another platform in Azure AD - App registration - Authentication - Add platform - Mobile and desktop applications (https://github.com/MicrosoftDocs/azure-docs/issues/61446)


# git setup
Push exting repo to github

```shell
git remote add origin https://github.com/mycloudops-work/azureadauth.git
git branch -M main
git push -u origin main
```