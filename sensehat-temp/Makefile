# Note: these can be overriden on the command line e.g. `make PLATFORM=<platform> ARCH=<arch>`
PLATFORM="linux"
ARCH="aarch64"

.PHONY: image

image := deviantony/cookiefactory-ovencollector:latest

image:
	docker buildx build --platform=$(PLATFORM)/$(ARCH) -t $(image) .
