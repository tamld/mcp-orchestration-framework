# Phase 1A Implementation Plan (ENHANCED)

**Decision**: Option B - Enhanced (Approved by moderator)  
**Decision Date**: 2025-10-25T19:20:00Z  
**Timeline**: 1 week (9-11 hours total)  
**Status**: ✅ **READY TO START**

---

## 📋 **Complete Task List (6 items)**

### **Original Items (5-7 hours):**

1. **GPG Key Setup** (2-3 hours)
2. **Context Directory Structure** (30 min)
3. **Enhanced Commit Template** (15 min)
4. **Basic Safeguards Helper Script** (2-3 hours)

### **Added Items (4 hours):**

5. **ADR Template + Consensus Rules** (2 hours) 🆕
6. **Sprint-001 Structure** (2 hours) 🆕

---

## 🎯 **Task Breakdown with Acceptance Criteria**

### **Task 1: GPG Key Setup** (2-3h)

#### **Deliverables:**
```bash
.gpg/
  ├── claude-key.asc (public key export)
  ├── codex-key.asc (public key export)
  ├── gemini-key.asc (public key export)
  └── README.md (key IDs, fingerprints, usage)
```

#### **Steps:**
```bash
# 1. Generate keys for each AA
gpg --full-generate-key
  - Name: Claude-3.5-Sonnet, Codex, Gemini
  - Email: claude@aa.local, codex@aa.local, gemini@aa.local
  - Key type: RSA 4096
  - Expiration: 1 year

# 2. Export public keys
gpg --armor --export claude@aa.local > .gpg/claude-key.asc
gpg --armor --export codex@aa.local > .gpg/codex-key.asc
gpg --armor --export gemini@aa.local > .gpg/gemini-key.asc

# 3. Configure git to use keys
git config user.signingkey <key-ID>

# 4. Test signing
git commit --amend --no-edit -S
git log --show-signature
```

#### **Acceptance Criteria:**
- [ ] 3 GPG keys generated (Claude, Codex, Gemini)
- [ ] Public keys exported to `.gpg/` directory
- [ ] `.gpg/README.md` documents key IDs and usage
- [ ] Test commit signed successfully
- [ ] `git log --show-signature` verifies signature
- [ ] Added `.gpg/` to `.gitignore` (private keys protected)

#### **Evidence Required:**
- `.gpg/` directory with 3 public keys + README
- Screenshot of `git log --show-signature` passing
- Commit demonstrating signed commit

---

### **Task 2: Context Directory Structure** (30min)

#### **Deliverables:**
```bash
context/
  ├── README.md (usage guide)
  ├── handoff-template.md (standardized handoff format)
  └── sessions/
      └── .gitkeep
```

#### **Steps:**
```bash
# 1. Create directory structure
mkdir -p context/sessions

# 2. Create handoff template
# (standardized format for AA-to-AA context transfer)

# 3. Document usage in README
```

#### **Template Format:**
```markdown
# Context Handoff: [From AA] → [To AA]

## Session Context
- **Date**: YYYY-MM-DD HH:MM
- **From**: [AA name]
- **To**: [AA name]
- **Task**: [Brief description]

## Current State
- Files modified: [list]
- Pending decisions: [list]
- Blockers: [list]

## Next Actions
- [ ] [Action 1]
- [ ] [Action 2]

## References
- [Relevant files/commits]
```

#### **Acceptance Criteria:**
- [ ] `context/` directory created
- [ ] `handoff-template.md` with standardized format
- [ ] `README.md` explains usage
- [ ] Example handoff file created for demonstration

#### **Evidence Required:**
- `context/` directory structure
- Handoff template with clear format
- Usage documentation

---

### **Task 3: Enhanced Commit Template** (15min)

#### **Deliverables:**
```bash
.git/commit-template.txt
```

#### **Template Format:**
```
[type](scope): brief summary (max 72 chars)

## Context
[Why this change is needed]

## Changes
- [Change 1]
- [Change 2]

## Evidence
- Files: [list of modified files]
- Tests: [pass/fail status]
- Related: [commit/issue references]

## AA Info
- AA: [Claude/Codex/Gemini]
- Session: [session ID if applicable]
- Signed-off-by: [AA name] <[email]>
```

#### **Steps:**
```bash
# 1. Create template file
vim .git/commit-template.txt

# 2. Configure git to use it
git config commit.template .git/commit-template.txt

# 3. Test with next commit
git commit
# (should open editor with template pre-filled)
```

#### **Acceptance Criteria:**
- [ ] Template file created at `.git/commit-template.txt`
- [ ] Git configured to use template
- [ ] Test commit uses template successfully
- [ ] Template includes all required sections

#### **Evidence Required:**
- Template file content
- Git config verification
- Example commit using template

---

### **Task 4: Basic Safeguards Helper Script** (2-3h)

#### **Deliverables:**
```bash
tools/aa_invoke_helper.sh
tests/test_aa_invoke_helper.sh
```

#### **Features:**
```bash
# 1. Authentication check
- Verify API keys exist
- Check credentials validity

# 2. Rate limiting
- Token bucket algorithm
- Configurable limits (e.g., 5 calls/min)

# 3. Error logging
- Log all invocations to evidence/invocations/*.jsonl
- Track: timestamp, AA, provider, cost, result

# 4. Retry logic
- Classify errors (client/server)
- Exponential backoff for server errors
- No retry for client errors

# 5. Evidence capture
- Auto-create evidence entry
- Link to queue request
```

#### **Script Interface:**
```bash
# Usage
./tools/aa_invoke_helper.sh \
  --aa codex \
  --task "Review programmatic invocation" \
  --context context/sessions/session-001.md \
  --queue queue/request-to-codex-*.md

# Output
{
  "status": "success",
  "aa": "codex",
  "timestamp": "2025-10-25T20:00:00Z",
  "evidence": "evidence/invocations/INV-001.jsonl",
  "response": "ideas/codex/response-001.md"
}
```

#### **Acceptance Criteria:**
- [ ] Script checks auth before invocation
- [ ] Rate limiter prevents >5 calls/min
- [ ] All invocations logged to `evidence/invocations/`
- [ ] Retry logic handles errors correctly
- [ ] Test suite passes
- [ ] Documentation in script header

#### **Evidence Required:**
- Working script at `tools/aa_invoke_helper.sh`
- Test suite at `tests/test_aa_invoke_helper.sh`
- Example invocation log in `evidence/invocations/`
- Test run showing rate limiter working

---

### **Task 5: ADR Template + Consensus Rules** (2h) 🆕

#### **Deliverables:**
```bash
memory/templates/adr_template.md
docs/briefs/consensus_protocol.md
```

#### **ADR Template Format:**
```markdown
# ADR-NNN: [Decision Title]

**Status**: [proposed | reviewing | accepted | rejected | superseded]  
**Date**: YYYY-MM-DD  
**Deciders**: [List of AAs/moderator]

## Context
[Problem statement and background]

## Decision
[What we decided to do]

## Consequences

### Positive
- [Benefits]

### Negative
- [Trade-offs]

### Risks
- [Known risks and mitigations]

## Alternatives Considered
1. [Alternative 1] - Rejected because...
2. [Alternative 2] - Rejected because...

## Related Artifacts
- [Links to brainstorm sessions, proposals, etc.]

## Participants & Consensus
| AA | Vote | Rationale | Timestamp |
|----|------|-----------|-----------|
| codex | ✅ Accept | ... | 2025-10-25T10:00Z |
| claude | ✅ Accept | ... | 2025-10-25T11:00Z |
| gemini | ❓ Needs info | ... | 2025-10-25T12:00Z |

**Consensus**: [Achieved / Pending / Rejected] on [date]
```

#### **Consensus Protocol:**
```markdown
# Consensus Protocol

## Response Windows
- **Active AAs**: 72 hours to respond
- **Inactive AAs**: No blocking (proceed without)

## Approval Thresholds
- **2/3 majority**: Required for acceptance
- **1/3 objections**: Requires discussion/modification
- **No response**: Treated as abstain (not blocking)

## Moderator Role
- **Tie-breaking**: If 50/50 split
- **Escalation**: Resolve deadlocks
- **Final approval**: For critical decisions

## Escalation Path
1. Discussion in brainstorm session
2. Modified proposal if needed
3. Re-vote with 48h window
4. Moderator decides if still deadlocked

## Decision Lifecycle
proposed → reviewing (72h) → accepted/rejected → implementing → completed
```

#### **Steps:**
```bash
# 1. Create ADR template
vim memory/templates/adr_template.md

# 2. Write consensus protocol
vim docs/briefs/consensus_protocol.md

# 3. Apply to pending decision (AA behavior standards)
cp memory/templates/adr_template.md docs/decisions/ADR-001-aa-behavior-standards.md
# Fill in with current consensus data

# 4. Update brainstorm playbook
# Add reference to consensus protocol
```

#### **Acceptance Criteria:**
- [ ] ADR template created at `memory/templates/adr_template.md`
- [ ] Consensus protocol documented at `docs/briefs/consensus_protocol.md`
- [ ] ADR-001 created for AA behavior standards (example)
- [ ] Brainstorm playbook references consensus protocol
- [ ] All sections of template explained

#### **Evidence Required:**
- Both template files created
- ADR-001 as working example
- Documentation clear and actionable

---

### **Task 6: Sprint-001 Structure** (2h) 🆕

#### **Deliverables:**
```bash
plans/sprints/sprint-001-hybrid-poc/
  ├── plan.md (sprint goals, tasks, acceptance criteria)
  ├── daily_logs/ (daily progress tracking)
  ├── evidence/ (implementation evidence)
  └── retro.md (retrospective template)
```

#### **Sprint Plan Format:**
```markdown
# Sprint 001: Hybrid PoC Implementation

## Sprint Goal
Implement Phase 1A foundation: GPG signing, context handoff, 
safeguards helper, ADR/Sprint frameworks.

## Timeline
- **Start**: 2025-10-26
- **End**: 2025-11-02
- **Duration**: 1 week

## Selected Ideas
From brainstorm session TA-2025-10-25-001:
1. GPG signing for evidence (Gemini)
2. Context handoff optimization (Claude)
3. Basic operational safeguards (Codex)
4. ADR template (Copilot/feedback.md)
5. Sprint framework (Copilot/feedback.md)

## Task Breakdown
| ID | Task | Owner | Effort | Status |
|----|------|-------|--------|--------|
| T1 | GPG key setup | Claude | 2-3h | ⏳ Pending |
| T2 | Context structure | Claude | 30m | ⏳ Pending |
| T3 | Commit template | Claude | 15m | ⏳ Pending |
| T4 | Helper script | Claude | 2-3h | ⏳ Pending |
| T5 | ADR template | Claude | 2h | ⏳ Pending |
| T6 | Sprint structure | Claude | 2h | ⏳ Pending |

## Acceptance Criteria
- [ ] All 6 tasks completed with evidence
- [ ] Test commits signed with GPG
- [ ] Context handoff demonstrated
- [ ] Helper script functional
- [ ] ADR-001 created as example
- [ ] Sprint framework documented

## Evidence Checklist
- [ ] GPG keys exported + README
- [ ] Context template + example
- [ ] Commit template configured
- [ ] Helper script + tests
- [ ] ADR template + protocol doc
- [ ] This sprint plan itself!

## Daily Standup Format
```yaml
Date: YYYY-MM-DD
Completed_Yesterday:
  - [Task completed]
Planned_Today:
  - [Task planned]
Blockers:
  - [Any blockers]
```

## Sprint Retrospective
(To be filled at end of sprint)

### What Went Well
- [Success 1]

### What Could Improve
- [Improvement 1]

### Action Items
- [Action for next sprint]
```

#### **Steps:**
```bash
# 1. Create sprint directory structure
mkdir -p plans/sprints/sprint-001-hybrid-poc/{daily_logs,evidence}

# 2. Create sprint plan
vim plans/sprints/sprint-001-hybrid-poc/plan.md

# 3. Create retro template
vim plans/sprints/sprint-001-hybrid-poc/retro.md

# 4. Create daily log for today
vim plans/sprints/sprint-001-hybrid-poc/daily_logs/2025-10-26.md
```

#### **Acceptance Criteria:**
- [ ] Sprint directory structure created
- [ ] `plan.md` with all sections filled
- [ ] `retro.md` template ready
- [ ] First daily log created
- [ ] Task tracking table functional

#### **Evidence Required:**
- Complete sprint directory structure
- Sprint plan with all 6 tasks listed
- Retro template
- Example daily log

---

## 📊 **Implementation Timeline**

### **Day 1 (Mon): Foundation**
```yaml
Tasks:
  - Task 3: Commit template (15m) ✅
  - Task 2: Context structure (30m) ✅
  - Task 6: Sprint structure (2h) ✅
  - Task 5: ADR template (2h) ✅

Total: ~5 hours
Output: Templates & frameworks ready
```

### **Day 2-3 (Tue-Wed): Core Implementation**
```yaml
Tasks:
  - Task 1: GPG key setup (2-3h) ✅
  - Task 4: Helper script (2-3h) ✅

Total: 4-6 hours
Output: GPG working, helper script functional
```

### **Day 4 (Thu): Testing & Validation**
```yaml
Tasks:
  - Test all components
  - Create example ADR-001
  - Demonstrate context handoff
  - Validate helper script

Total: 2-3 hours
Output: Everything validated with evidence
```

### **Day 5 (Fri): Documentation & Wrap-up**
```yaml
Tasks:
  - Complete evidence collection
  - Sprint retrospective
  - Update documentation
  - Prepare Phase 1B plan

Total: 2 hours
Output: Sprint complete, Phase 1B ready
```

---

## ✅ **Success Metrics**

```yaml
Completion_Criteria:
  - All 6 tasks completed ✅
  - All acceptance criteria met ✅
  - Evidence collected for each task ✅
  - No P0 blockers remaining ✅
  - Sprint retrospective completed ✅

Quality_Metrics:
  - ≥3 GPG-signed commits
  - Helper script test coverage >80%
  - All templates used successfully
  - Context handoff demonstrated
  - ADR-001 as working example

Timeline_Metrics:
  - Complete within 1 week
  - Total effort: 9-11 hours
  - No major delays (>1 day)
```

---

## 🚀 **Ready to Start!**

```yaml
Status: ✅ APPROVED (Option B - Enhanced)
Decision_By: tamld (moderator)
Decision_Date: 2025-10-25T19:20:00Z
Timeline: 1 week (Oct 26 - Nov 2)
Total_Effort: 9-11 hours

Next_Action: START Task 3 (Commit template) - quickest win!
```

---

**Prepared by**: Claude (operator)  
**Approved by**: tamld (moderator)  
**Sprint ID**: SPRINT-001-HYBRID-POC