.PHONY: all build wheel source clean install uninstall

all: clean wheel install

build: clean setup.py
	@echo "Building"
	@python3 -B setup.py sdist bdist_wheel >/dev/null

wheel: setup.py
	@echo "Building wheel"
	@python3 -B setup.py bdist_wheel >/dev/null

source: setup.py
	@echo "Building source"
	@python3 -B setup.py sdist >/dev/null

clean:
	@if ls | grep 'build\|dist\|.*egg-info' >/dev/null; then \
		echo "Removing build files"; \
		rm -fr dist/ build/ *.egg-info; \
	fi

install: dist/$(wildcard *.[whl|tar.gz])
	@echo "Installing"
	@pip3 install --force-reinstall dist/* >/dev/null

uninstall:
	@echo "Uninstalling"
	@pip3 uninstall -y eponym-alloy >/dev/null

%.whl %.tar.gz: setup.py
	@echo "Building $@"
	@python3 -B setup.py sdist bdist_wheel >/dev/null

setup.py dist/:
	$(error Missing $@)
