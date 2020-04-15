# project 5 Makefile
# CS4700
# Davin Jimeno, Tyler Birn

DNS = dnsserver
HTTP = httpserver

define HTTP_BODY
#!/bin/bash

python3 $(HTTP) $$1 $$2 $$3 $$4
endef

define DNS_BODY
#!/bin/bash

python3 $(DNS) $$1 $$2 $$3 $$4
endef


export HTTP_BODY, DNS_BODY

dns_executable: $(DNS)
	echo "$$DNS_BODY" > $(DNS)
	chmod +x $(DNS)

http_executable: $(HTTP)
	echo "$$HTTP_BODY" > $(HTTP)
	chmod +x $(HTTP)

$(DNS):
	touch $(DNS)

$(HTTP):
	touch $(HTTP)

clean:
	-rm $(DNS)
	-rm $(HTTP)
