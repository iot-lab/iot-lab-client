SWAGGER ?= ${PWD}/swagger.yaml
GENERATOR ?= openapitools/openapi-generator-cli:v3.3.4

iotlabclient/client: Makefile
	docker run --rm --user $$(id -u):$$(id -g) \
	-v ${PWD}:/output -v ${SWAGGER}:/input/swagger.yaml \
	${GENERATOR} \
	generate -g python -i /input/swagger.yaml -o /output/ \
	--git-user-id iot-lab --git-repo-id cli-tools \
	-DgenerateSourceCodeOnly -DpackageName=iotlabclient.client
