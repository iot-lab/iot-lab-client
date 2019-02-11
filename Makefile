SWAGGER ?= ${PWD}/swagger.yaml
GENERATOR ?= openapitools/openapi-generator-cli:v3.3.4

# The FIT IoT-LAB spec failed to generate a correct client
# with version 3.3.4
# it necessitates some merged PR before it works, might be
# working with openapi-generator 4.0.0 once it releases
# in the meantime, generated code is commited
# PR code on openapitools/openapi-generator used: #2122 #2121 #2112 #2016

iotlabclient/client: Makefile ${SWAGGER}
	docker run --rm --user $$(id -u):$$(id -g) \
	-v ${PWD}:/output -v ${SWAGGER}:/input/swagger.yaml \
	${GENERATOR} \
	generate -g python -i /input/swagger.yaml -o /output/ \
	--git-user-id iot-lab --git-repo-id iot-lab-client \
	-DgenerateSourceCodeOnly=true -DpackageName=iotlabclient.client
	# workaround before this merge https://github.com/OpenAPITools/openapi-generator/pull/2016
	cp -R iotlabclient.client/* iotlabclient/client/
	mv iotlabclient.client_README.md iotlabclient/client/README.md
	rm -r iotlabclient.client
