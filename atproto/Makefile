ACCOUNT=unum
IMAGE=aproto
VERSION?=0.0.1
DEBUG_PORT=16738
TTY=$(shell if tty -s; then echo "-it"; fi)
VOLUMES=-v ${PWD}/bin/:/opt/service/bin/ \
        -v ${PWD}/lib/:/opt/service/lib/ \
        -v ${PWD}/config/:/opt/service/config/ \
        -v ${PWD}/secret/:/opt/service/secret/
ENVIRONMENT=-e test="python -m unittest -v " \
			-e debug="python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m unittest -v " \
			-e PYTHONDONTWRITEBYTECODE=1 \
			-e PYTHONUNBUFFERED=1

.PHONY: build shell post basesheet ohsheet sheetpost

build:
	docker build . -t $(ACCOUNT)/$(IMAGE):$(VERSION)

shell:
	-docker run $(TTY) --rm $(VOLUMES) $(ENVIRONMENT) -p 127.0.0.1:$(DEBUG_PORT):5678 $(ACCOUNT)/$(IMAGE):$(VERSION) sh

post:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "bin/post.py"

basesheet:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "bin/basesheet.py"

ohsheet:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "bin/ohsheet.py"

sheetpost:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "bin/sheetpost.py"

sheetree:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "bin/sheetree.py"
