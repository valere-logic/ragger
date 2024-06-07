## Definitions
HELMCHART_DIR := ./0_helmchart
OUT_DIR := ./generated
SOURCE_DIRS := 0_terraform/dev 0_terraform/stg 1_attachments 1_frontend \
1_backend 2_database 2_svc_vectordb 3_conversation_index 3_model

## Phony Targets
.PHONY: all format $(SOURCE_DIRS)

## App Commands

# Formats source code.
format:
	-@for dir in $(SOURCE_DIRS); do \
		(cd $$dir && $(MAKE) -i format); \
	done

## Dependency Commands
setup:
	pip install -r requirements.txt

run:
	docker compose up

#test:
# TODO

docker/images:
	eval $$(minikube docker-env -u) && docker images

clean:
	rm -rf $(OUT_DIR)