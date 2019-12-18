.PHONY: help
help:  ## prints this help message
	grep -hr "^[a-z].*\:" makefiles Makefile | sort | sed -nE 's/\:.+\#\#/:\n\t/p'
