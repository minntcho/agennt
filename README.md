# agennt

Practice repository for building agent systems as **independent domain packages**.

## Layout
- `packages/*`: domain-specific packages with a shared `run(input_data) -> dict` interface.
- `shared/*`: shared schemas, prompts, and utility helpers.
- `docs/architecture.md`: architecture and conventions.

## Quick start
```bash
make test
make run PKG=cs-agent
```
