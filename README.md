# molecule-demo-monorepo

Related article on [Medium](https://mariarti0644.medium.com/using-ansible-molecule-to-test-roles-in-monorepo-5f711c716666)

## Run tests

Run tests again all scenarios

```bash
make test
```

Run test again specific scenario

```bash
make scenario=lint test-scenario
```

## Local usage

1. Install [poetry][1]
2. Install venv
3. Create a virtual environment
```bash
virtualenv .venv
```
4. Activate virtual environment
```bash
source .venv/bin/activate
```
5. Install dependencies via poetry
```bash
poetry install
```

or using Makefile
```
make install_dependencies
```

[1]: https://python-poetry.org/docs/#installation
[2]: https://virtualenv.pypa.io/en/latest/installation.html
