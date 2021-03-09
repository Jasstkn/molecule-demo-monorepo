install_dependencies:
	poetry install

MOLECULE_DISTRO ?= ubuntu2004

test:
	MOLECULE_DISTRO=$(MOLECULE_DISTRO) molecule test --all

test-scenario:
	MOLECULE_DISTRO=$(MOLECULE_DISTRO) molecule test -s $(scenario)