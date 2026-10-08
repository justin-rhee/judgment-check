---
name: judgment-loop
description: Record predictions before decisions, score outcomes independently, and review accepted decisions from evidence without revealing earlier verdicts. Use for decision calibration and evidence audits.
---

# Judgment loop

A prediction register and an independent evidence review answer different questions. The register measures the gap between an expected outcome and what happened. An evidence-only review tests whether the recorded evidence justified a decision at all. Keep their results separate.

## Before the outcome

Record a stable decision id, author, timestamp, expected outcome, confidence from 0 to 1, and a falsifier that names a checkable observation. Use the existing approved record and writer. Do not silently create another system of record or modify a prediction after learning its outcome.

Name the reviewer and the event or date that will trigger scoring. An unassigned future review is not a scheduled check.

## After the outcome

An independent reviewer records the prediction id, reviewer, timestamp, observed evidence, verdict and failure class if relevant. Use accurate, partial or inaccurate only when the outcome is observable. Use too-early or cant-tell when it is not. Keep unresolved outcomes out of calibration and schedule a later check explicitly if one is needed.

Compare stated confidence with scored outcomes across comparable decisions. If partial outcomes receive a fractional target, describe the result as a Brier-style summary, not a binary calibration study. State exclusions and sample sizes. The record does not establish that a reviewer was right.

Before repeating a class of decision, retrieve a previous case: expected outcome, falsifier and observed result. Use that evidence to reconsider the current call, rather than adding another broad rule automatically.

## Evidence-only review

Prepare a bounded packet with the acceptance condition, underlying evidence and an explicit list of what was withheld. Exclude the original verdict, maker's reasoning and prior reviewers' verdicts. Check the generated packet for those disclosures.

Use a reviewer without access to the withheld record. A prompt saying not to read it is insufficient when the tools still expose it. If access cannot be restricted, label the exercise a verification review, not a blind review.

Record agree, disagree or partial with reasons. Disagreement means the packet did not support the same decision, not that misconduct or a defect has been proved. Skip evidence-free packets and report the skip count. Do not count repeated reviews of the same decision as independent new cases.

## State claims

Before relaying a decision's status, name its current record and verify the relevant row. A matching identifier proves only that text exists, not that the row is current or correct. Check for a superseding instruction before acting on a saved execution packet.
