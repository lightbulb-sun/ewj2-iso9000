.DELETE_ON_ERROR:

PYTHON = python3

SCRIPT = hack.py
TRACK1_HACK = track1-hack.bin

$(TRACK1_HACK): $(SCRIPT)
	$(PYTHON) $<

.PHONY: all clean test
clean:
	rm -rf $(TRACK1_HACK)
