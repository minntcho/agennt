PYTHON ?= python3
PKG ?= cs-agent
MOD := $(subst -,_,$(PKG))

.PHONY: run test test-all lint support-desk-api

run:
	PYTHONPATH=packages/$(PKG)/src $(PYTHON) -c "from $(MOD) import run; print(run({'task':'demo'}))"

test:
	@if [ "$(PKG)" = "all" ]; then \
		$(MAKE) test-all; \
	else \
		PYTHONPATH=packages/$(PKG)/src $(PYTHON) -m pytest -q packages/$(PKG)/tests; \
	fi

test-all:
	@for pkg in cs-agent devops-agent research-agent sales-marketing-agent backoffice-agent ecommerce-agent security-assist-agent eval-benchmark; do \
		echo "==> $$pkg"; \
		PYTHONPATH=packages/$$pkg/src $(PYTHON) -m pytest -q packages/$$pkg/tests || exit 1; \
	done

support-desk-api:
	$(PYTHON) -m apps.support_desk_demo.backend.server

lint:
	$(PYTHON) -m compileall -q packages shared apps
