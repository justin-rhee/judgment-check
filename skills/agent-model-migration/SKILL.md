---
name: agent-model-migration
description: Plan and verify a change to an agent session's model or subscription tier without losing active work or silently changing other sessions. Use for authorized model or plan migrations.
---

# Model and plan migration

Preserve active work, scope configuration to the intended session, and keep enough evidence to judge whether the change was worthwhile. This procedure does not authorize purchases, restarts or configuration changes on its own.

## Before a change

Verify the current runtime, model, active work and live child processes from current state. A stale roster or a display label is not a runtime readback. Wait for a clean boundary and durable handoff if changing the session would interrupt work.

Confirm the target's literal model identifier using the installed runtime's supported listing or documentation. A product display name is not necessarily an accepted CLI value.

Predeclare the trial's acceptance criteria, such as delivery quality, rework rate, tests and quota use. Capture a comparable baseline before switching when possible. If authorized urgency prevents that, retain the historical baseline and state the weaker comparison.

Inspect configuration scope before editing. A user-wide default can change every session on its next restart. Prefer a supported per-session setting for a one-session trial. Record any broader effect and obtain authorization for that scope before applying it.

Write the exact rollback procedure using commands verified for the installed runtime. Preserve necessary backups. Do not guess a universal restart command across different tools.

## Apply and verify

Change only the authorized settings, then restart only if required by the runtime. Verify the selected model from inside the new session. Successful startup alone does not prove the intended model is active.

Confirm that open task references and handoff files are accessible, permissions have not broadened, and unrelated sessions retain their defaults. If a user-scope setting changed incidentally, restore it from the saved state before treating the migration as complete.

Record old and new runtime/model, configuration scope, the verification evidence, any pending work, and the tested rollback. Do not infer permission to bypass prompts or disable safety controls.

## Decide the trial

Use a decision date tied to the actual model or plan choice. Compare verified outcomes, rework and costs on the declared basis. Subscription capacity, quotas and metered overflow are different costs, not interchangeable token counters.

A model change that does not alter the decision or cost profile need not become a recurring evaluation ceremony. Unknown usage or weak historical comparisons remain explicit in the result.
