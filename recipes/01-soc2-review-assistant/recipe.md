---
id: <auto>
title: "Third-Party SOC 2 Review Assistant"
category: "audit"
level: "intermediate"
estimated_time: "45-60 minutes"
tools:
  - ChatGPT / GPT-5
  - Custom GPT tuned for SOC analysis (knowledge base includes SOC 2 review checklist)
  - PDF parser or uploader (optional)
inputs:
  - "SOC 2 Type 2 report (PDF) for key service provider"
  - "User control considerations (if separate from report)"
  - "Client follow-up notes or email responses"
  - "SOC 2 review checklist (firm or company template)"
outputs:
  - "Risk table summarizing control gaps and audit implications"
  - "Draft client questions covering required user controls"
  - "User-control assessment memo"
  - "Residual risk memo"
video_url: https://youtu.be/w9rqjeFXxSY
tags: [audit, third-party-risk, automation]
license: CC-BY-4.0
---

## Problem
Auditors and internal finance teams rely on third-party service providers to process sensitive financial data, and rely on SOC 2 Type 2 reports to provide critical information about controls design and effectiveness at those organizations. However, the reports are lengthy and time-consuming to review, and important information can be missed. In addition to analyzing the results of the testing, the user controls are required to be in place at the end user organization in order for the controls identiifed in the SOC 2 report to be adequate. Teams therefore must identify and extract control gaps both from testing failures and from limits in testing scope, determine audit impact, verify assumed user controls, and document residual risks to determine what remaining testing and risk remain. Manual review of the SOC 2 is slow, error-prone, and sometimes prioritized below other critical tasks despite being a very important part of the risk assessment and testing process.

## Solution (at a glance)
1. Upload a SOC 2 report, supporting user-control documentation, and the if applicable, a SOC 2 review checklist to a custom GPT workspace.
2. Generate a risk table that identifies findings, control gaps, and potential audit impacts.
3. Produce questions that cover all user control considerations needing validation.
4. Ingest client responses and evaluate whether user controls are designed effectively, and consider testing for effectiveness if necessary; identify residual risk and recommend next steps.
5. Export the risk table, question list, user-control assessment memo, and residual risk memo for human review and sign-off by the audit team or internal risk management.

## Prompt
```text
You are "SOC 2 Audit Copilot," supporting an external audit team. Follow the three-phase workflow below.

Inputs you may receive:
- SOC 2 Type 2 report (PDF text) for the service provider.
- User control considerations (if listed separately).
- Client responses describing their controls.
- Firm-specific SOC 2 review checklist for consistency across engagements.

Phase 1 – Report Review
1. Summarize notable findings, exceptions, or scope limitations.
2. Build a risk table with columns: control_area, issue_summary, severity (Low/Medium/High), potential_audit_impact, recommended_next_step.
3. Note any complementary user entity controls (CUECs) the client must operate.

Phase 2 – Client Outreach Plan
1. Draft clear, professional questions for the client to validate each CUEC.
2. Group questions by control area; keep each question actionable and concise.

Phase 3 – Response Assessment
1. When client responses are provided, map each response to the related CUEC.
2. Assess whether the described control is adequate. Flag gaps or missing evidence.
3. Summarize residual risks and recommend follow-up actions.

Output format
- Section A: Risk Table (Markdown table)
- Section B: Client Questions (numbered list)
- Section C: User-Control Assessment Memo (1–2 paragraphs per control area)
- Section D: Residual Risk Memo (bulleted findings + recommended next steps)

Important
- Cite page numbers or report sections when referencing SOC 2 content.
- Highlight any assumptions made because of missing context.
- End each section with a reminder: "Human review required—do not rely solely on this output."
```

## Guardrails
- Treat SOC 2 reports and client communications as confidential; store them in secure, access-controlled workspaces.
- Verify extracted findings against the source document before acting; cite report sections to ease review.
- Flag low-confidence interpretations and scope limitations explicitly for auditor judgment.
- Never send client outreach without engagement manager approval; maintain professional tone and regulatory compliance.
- Ensure responses are reviewed by licensed auditors or internal risk owners—GenAI output is advisory only.

## Implementation Notes (optional)
- Load the SOC 2 review checklist into the custom GPT knowledge base alongside the report so required control steps are always referenced.
- Configure the custom GPT with retrieval on deposited SOC 2 PDFs so citations resolve to actual pages.
- Use structured output validation (e.g., Markdown schema or JSON) if integrating with downstream audit workpapers.
- Consider pairing with an email draft assistant for distributing the client questions while retaining human approval steps.

## Evaluation & Handoff (optional)
- Cross-check the risk table against the SOC 2 report to confirm all findings and CUECs were captured.
- Reconcile client responses with the outreach log; ensure every CUEC has an assessed status.
- Review residual risk memo with the engagement partner and include in audit documentation.
- Store finalized memos and evidence in the audit binder or workpaper system per firm policy.

## Checklist
- [ ] Sample SOC 2 report processed end-to-end with citations verified
- [ ] Client outreach questions reviewed by engagement manager
- [ ] User-control assessment and residual risk memos approved by audit lead
- [ ] Prompt customized with firm-specific terminology and retention policies
