FORMAT_DIRS=$(wildcard ./data/*/)
ARCHIVES=$(patsubst ./data/%/, %.tar.gz, $(FORMAT_DIRS))

## help		: display help for this Makefile.
help: Makefile
	@sed -n 's/^##//p' $<

## archive	: make format directories into compressed archives (.tar.gz files)
archive: $(ARCHIVES)

%.tar.gz : ./data/%/
	tar -czvf $@ --directory=./data/ $*/

## upload      	: upload .tar.gz files to figshare
upload:
	@echo 'not implemented'

# clean		: Remove auto-generated files.
clean:
	rm -rf $(ARCHIVES)

## variables 	: Print variables defined in this Makefile.
variables:
	@echo FORMAT_DIRS: $(FORMAT_DIRS)
	@echo TAR_GZ: $(TAR_GZ)

.PHONY: help archive upload clean variables
