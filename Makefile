SWAGGER ?= ${PWD}/swagger.yaml
SWAGGER_ADMIN ?= ${PWD}/swagger-admin.yaml
GENERATOR ?= openapitools/openapi-generator-cli\:latest

.PHONY: api admin_api ${SWAGGER} ${SWAGGER_ADMIN}

# The FIT IoT-LAB spec failed to generate a correct client
# with version 3.3.4
# it necessitates some merged PR before it works, might be
# working with openapi-generator 4.0.0 once it releases
# in the meantime, generated code is commited
# PR code on openapitools/openapi-generator used: #2122 #2121 #2112

api: Makefile ${SWAGGER}
	docker run --rm --user $$(id -u):$$(id -g) \
	-v ${PWD}:/output -v ${SWAGGER}:/input/swagger.yaml \
	${GENERATOR} \
	generate -g python -i /input/swagger.yaml -o /output/ \
	--git-user-id iot-lab --git-repo-id iot-lab-client \
	-DgenerateSourceCodeOnly=true -DpackageName=iotlabclient.client

admin_api: Makefile ${SWAGGER_ADMIN}
	docker run --rm --user $$(id -u):$$(id -g) \
	-v ${PWD}:/output -v ${SWAGGER_ADMIN}:/input/swagger.yaml \
	${GENERATOR} \
	generate -g python -i /input/swagger.yaml -o /output/ \
	--git-user-id iot-lab --git-repo-id iot-lab-client \
	-DgenerateSourceCodeOnly=true -DpackageName=iotlabadminclient.client
