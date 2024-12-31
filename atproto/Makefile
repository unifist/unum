ACCOUNT=unum
IMAGE=aproto
VERSION?=0.0.1
DEBUG_PORT=16738
TTY=$(shell if tty -s; then echo "-it"; fi)
VOLUMES=-v ${PWD}/bin/:/opt/service/bin/ \
        -v ${PWD}/secret/:/opt/service/secret/
ENVIRONMENT=-e test="python -m unittest -v " \
			-e debug="python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m unittest -v " \
			-e PYTHONDONTWRITEBYTECODE=1 \
			-e PYTHONUNBUFFERED=1

.PHONY: build shell run test lint push

build:
	docker build . -t $(ACCOUNT)/$(IMAGE):$(VERSION)

shell:
	-docker run $(TTY) --rm $(VOLUMES) $(ENVIRONMENT) -p 127.0.0.1:$(DEBUG_PORT):5678 $(ACCOUNT)/$(IMAGE):$(VERSION) sh

run:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION)

test:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "coverage run -m unittest discover -v test && coverage report -m --include 'lib/*.py'"

lint:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "pylint --rcfile=.pylintrc lib/"
