# agennt

Practice repository for building agent systems as **independent domain packages**.

## Direction

`agennt` is intended to grow as a small **agent ecosystem**, not as one monolithic shared runtime.

Each package stays independently runnable for focused practice, but packages can influence one another by producing and consuming explicit artifacts. The learning target is a connected operating simulation: research briefs can feed marketing copy, ecommerce signals can feed customer support, support cases can feed backoffice work, and incidents or security events can create downstream operational tasks.

The core rule is:

```text
agent -> artifact -> another agent reads the artifact
```

Agents should not depend on direct package-to-package calls as their primary coordination mechanism.

## Layout

- `packages/*`: domain-specific packages with a shared `run(input_data) -> dict` interface.
- `shared/*`: shared schemas, prompts, and utility helpers.
- `docs/architecture.md`: architecture and conventions.
- `docs/ecosystem-architecture.md`: connected agent ecosystem direction.

## Quick start

```bash
make test
make run PKG=cs-agent
```
