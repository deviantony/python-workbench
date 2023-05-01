# Note: these can be overriden on the command line e.g. `make PLATFORM=<platform> ARCH=<arch>`
PLATFORM="linux"
ARCH="amd64"

.PHONY: image

image := deviantony/pi3-sensehat:hello

image:
	docker buildx build --platform=$(PLATFORM)/$(ARCH) -t $(image) .
