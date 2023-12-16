# {{ cookiecutter.project_name }}

## 1. Overview

{{ cookiecutter.project_description}}

## 2. Usage

### 2.1 init project

```bash
poetry install -v
```

### 2.2 usage

TODO

## 3. Develop

You may need to read the [develop document](./docs/development.md) to use SRC Layout in your IDE.

## vscode launch configuration

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "start",
            "type": "python",
            "request": "launch",
            "program": "src/{{cookiecutter.project_name}}/cmdline.py",
            "args": ["run"],
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```