# Các Vấn Đề Chưa Đồng Thuận

**Session ID**: TA-2025-10-25-001  
**Updated**: 2025-10-25T18:45:00Z  
**Status**: 5 items pending moderator decision

---

## TL;DR: 5 ITEMS CẦN QUYẾT ĐỊNH

```yaml
CRITICAL (Cần quyết định ngay):
  1. ADR template có add vào Phase 1A không? (từ feedback.md)
  2. Sprint structure có add vào Phase 1A không? (từ feedback.md)

MINOR (Có thể defer):
  3. Automation timing criteria (when Phase 1 → Phase 2?)
  4. Production architecture choice (post-PoC)
  5. Checklist link cho AA behavior standards

PoC_Scope: ✅ APPROVED (Hybrid)
Implementation_Ready: ⏳ Pending moderator on items 1-2
```

---

## 🔴 CRITICAL: Cần Quyết Định Ngay (2 items)

### **1. ADR Template + Consensus Rules**

```yaml
Source: Feedback.md (Copilot recommendation)
Priority: TIER 1 Critical

Copilot_Says:
  "Need formal decision-making process"
  "AA behavior standards stuck at pending consensus"
  "No mechanism to resolve disagreements"

Recommendation:
  Add to Phase 1A (2 hours effort)

Components:
  - memory/templates/adr_template.md
  - docs/briefs/consensus_protocol.md
  - Basic consensus rules documented

Benefits:
  + Formalizes what we're already doing
  + Scales to more AAs
  + Clear decision lifecycle
  + Historical record of decisions

Trade-offs:
  - Extra 2 hours in Phase 1A
  - More process overhead (minimal)

Current_Status: NOT in Phase 1A plan
Consensus_Status: ❌ CHƯA QUYẾT ĐỊNH
```

**Your Decision:**
- [ ] ✅ YES - Add to Phase 1A
- [ ] ❌ NO - Defer to Phase 1B or 2
- [ ] 🤔 MODIFY - What changes?

---

### **2. Sprint Structure + Tracking**

```yaml
Source: Feedback.md (Copilot recommendation)
Priority: TIER 1 Critical

Copilot_Says:
  "Excellent ideas không được execute"
  "No bridge từ brainstorm → implementation"
  "Need execution framework"

Recommendation:
  Add to Phase 1A (2 hours effort)

Components:
  - plans/sprints/sprint-001-hybrid-poc/
  - Sprint plan.md with goals, tasks, acceptance criteria
  - Basic tracking structure (no automation yet)

Benefits:
  + Bridges brainstorm → implementation gap
  + Execution accountability
  + Progress tracking
  + Foundation for future sprints

Trade-offs:
  - Extra 2 hours in Phase 1A
  - More structure (might slow initial velocity)

Current_Status: NOT in Phase 1A plan
Consensus_Status: ❌ CHƯA QUYẾT ĐỊNH
```

**Your Decision:**
- [ ] ✅ YES - Add to Phase 1A
- [ ] ❌ NO - Defer to Phase 1B or 2
- [ ] 🤔 MODIFY - What changes?

---

## 🟡 MINOR: Có Thể Defer (3 items)

### **3. Automation Timing Criteria**

```yaml
Conflict:
  Claude: "Phase-based (Phase 1 manual, Phase 2 automate)"
  Codex: "Milestone-based (when safeguards proven)"

Not_Really_Conflict: Different emphasis

Current_Resolution:
  - Hybrid PoC approved (manual Phase 1A)
  - Automation deferred to Phase 1B/2
  - No urgent need to decide exact criteria NOW

Proposed_Resolution:
  Define criteria when approaching Phase 1 completion:
  1. PoC demonstrates value ✅
  2. Scripts cover auth, rate limits, retries ⏳
  3. Dogfooding completed successfully ⏳
  4. Moderator approves transition ⏳

Consensus_Status: ⏳ CAN DEFER (decide later)
Impact: LOW (doesn't block PoC)
```

**Your Decision:**
- [ ] ✅ DEFER - Decide when Phase 1A nears completion
- [ ] ❌ DECIDE NOW - Set criteria: [your criteria]

---

### **4. Production Architecture Choice**

```yaml
Conflict:
  Gemini: "Dedicated Git Identities ideal for production"
  Codex: "Consider message queue broker post-PoC"

Not_Really_Conflict: Both are post-PoC considerations

Current_Resolution:
  - Hybrid PoC uses GPG + Attestation
  - Production architecture DEFERRED
  - Will decide after PoC validation

When_To_Decide:
  After PoC successfully demonstrates:
  1. Multi-AA coordination works
  2. Evidence quality sufficient
  3. Scalability needs clear
  4. Operational pain points identified

Consensus_Status: ⏳ DEFERRED (post-PoC)
Impact: NONE (PoC unaffected)
```

**Your Decision:**
- [ ] ✅ DEFER - Revisit after PoC completion
- [ ] ❌ DECIDE NOW - Choose: [Dedicated Git IDs / Message Queue / Other]

---

### **5. Checklist Link for AA Behavior Standards**

```yaml
Request: Codex asked for explicit link to pre-flight checklist

Context:
  "Can we explicitly call out that the pre-session commitment
   should reference the pre-flight checklist we're drafting 
   in brainstorm-playbook-refresh?"

Resolution_Needed:
  Add cross-reference link in AA behavior standards proposal
  (trivial edit, 5 minutes)

Current_Status:
  aa-behavior-standards-proposal.md exists
  brainstorm-playbook-refresh has pre-flight checklist
  Just need to link them

Consensus_Status: ⏳ TRIVIAL (easy to resolve)
Impact: VERY LOW (cosmetic)
```

**Your Decision:**
- [ ] ✅ YES - Add link now (5 min)
- [ ] ❌ NO - Not important
- [ ] 🤔 DEFER - Add during implementation

---

## Summary: What Needs Your Decision?

### **Option A: Conservative (Original Plan)**
```yaml
Phase_1A:
  - GPG setup (2-3h)
  - Context structure (30min)
  - Commit template (15min)
  - Helper script (2-3h)

Total: 5-7 hours
Defer: ADR + Sprint to Phase 1B

Pros: Faster Phase 1A completion
Cons: Miss Copilot's critical recommendations
```

### **Option B: Enhanced (Recommended by Copilot)**
```yaml
Phase_1A:
  - GPG setup (2-3h)
  - Context structure (30min)
  - Commit template (15min)
  - Helper script (2-3h)
  - ADR template + rules (2h) 🆕
  - Sprint-001 structure (2h) 🆕

Total: 9-11 hours
Includes: Copilot's Tier 1 recommendations

Pros: Foundation for scaling, execution framework
Cons: More work upfront (still reasonable)
```

### **Option C: Minimal Add**
```yaml
Phase_1A:
  - Original items (5-7h)
  - ADR template only (2h) 🆕

Total: 7-9 hours
Defer: Sprint structure to Phase 1B

Pros: Balance foundation + speed
Cons: Still missing execution bridge
```

---

## Recommendation (Claude's Operator View)

```yaml
Recommended: Option B (Enhanced)

Why:
  1. Copilot's expert review identified these as CRITICAL
  2. Both are lightweight (just templates & docs)
  3. Both are foundational (not automation)
  4. 9-11 hours still doable in 1 week
  5. Prevents future bottlenecks

Copilot_Right_On:
  - "Ideas stuck without execution framework" ✅
  - "No formal decision process" ✅
  - Both are TIER 1 for scaling ✅

Risk_If_Not_Added:
  - More ideas die in brainstorm
  - Consensus bottlenecks repeat
  - Can't scale to more AAs efficiently
```

---

## **YOUR TURN: Which Option?** 🎯

**A, B, or C?**

```yaml
Your_Choice: _____

If_MODIFY:
  - Keep: [which items?]
  - Remove: [which items?]
  - Add: [anything else?]
  - Rationale: [your reasoning]
```

---

**Commit: Summarizing unresolved items...**