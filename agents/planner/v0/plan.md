# Plan

Intent: coordinate v0 schema, dataset, and validation work across per-folder agents to satisfy the tool/ontology/state constraints and example composition targets. Approach: delegate specific deliverables, validate progress, and track any CI gaps for the owning agent to resolve.

## Scope
- In: delegate v0 schema updates, dataset creation (70/15/15 split with required no-op/single-step/multi-step ratios), and validation checks to the owning agents.
- Out: directly modifying schemas owned by other agents, changing existing folders, or implementing CI outside `agents/planner`.

## Action items
[ ] Instruct the schema-owning agent to define any required v0 schema updates in their folder, aligned to ontology/state/tools constraints.
[ ] Instruct the dataset-owning agent to add a small, schema-valid seed set that demonstrates no-op, single-step, and multi-step patterns.
[ ] Instruct the dataset-owning agent to create `train.jsonl`, `eval.jsonl`, and `heldout.jsonl` with the 70/15/15 split and target mix.
[ ] Instruct the dataset-owning agent to ensure all examples use full ontology injection (and state when needed), with no invented IDs or inferred state.
[ ] Instruct the schema/dataset agents to validate new examples against their schema(s) and confirm `schema_version` constants match.
[ ] Instruct the dataset-owning agent to document composition targets and rationale in their folder’s `README.md`.
[ ] Instruct the CI/validation-owning agent to add checks that fail loudly on schema drift and cover new files.

## Open questions
- None.
