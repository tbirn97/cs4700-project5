# project 5 Makefile
# CS4700
# Davin Jimeno, Tyler Birn

DNS_NAME = dnsserver
HTTP_NAME = httpserver
DNS_PROGRAM = dnsserver.py
HTTP_PROGRAM = httpserver.py

define HTTP_BODY
#!/bin/bash

python3 $(HTTP_PROGRAM) $$1 $$2 $$3 $$4
endef

define DNS_BODY
#!/bin/bash

python3 $(DNS_PROGRAM) $$1 $$2 $$3 $$4
endef


export HTTP_BODY DNS_BODY

all: dns_executable http_executable

dns_executable: $(DNS_NAME)
	echo "$$DNS_BODY" > $(DNS_NAME)
	chmod +x $(DNS_NAME)

http_executable: $(HTTP_NAME)
	echo "$$HTTP_BODY" > $(HTTP_NAME)
	chmod +x $(HTTP_NAME)

$(DNS_NAME):
	touch $(DNS_NAME)

$(HTTP_NAME):
	touch $(HTTP_NAME)

clean:
	-rm $(DNS_NAME)
	-rm $(HTTP_NAME)
