# 0x01-caching
An introductory project on:
- Parametrize Flask templates to display different languages
- Infer the correct locale based on URL parameters, user settings or request headers
- Localize timestamps

## Requirements
- All files should be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- The first line of all files is exactly #!/usr/bin/env python3
- All modules and functions are documented

## File Descriptions
### Mandatory
1. [0-app.py](./0-app.py) [templates/0-index.html](./templates/0-index.html) - a single `/` route and an `index.html` template that simply outputs `“Welcome to Holberton”` as page title (`<title>`) and `“Hello world”` as header (`<h1>`).

2. [1-app.py](./1-app.py) [templates/1-index.html](./templates/1-index.html) - creates a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
   - Uses Config to set Babel’s default locale ("en") and timezone ("UTC").
   - Uses that class as config for the Flask app.

3. [2-app.py](./2-app.py) [templates/2-index.html](./templates/2-index.html) - a `get_locale` function with the `babel.localeselector` decorator. Uses `request.accept_languages` to determine the best match with our supported languages.
