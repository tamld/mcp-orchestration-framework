# PoC Scope Decision: Hybrid Approach

**Decision ID**: D-POC-SCOPE-001  
**Session**: TA-2025-10-25-001  
**Decision Date**: 2025-10-25T18:15:00Z  
**Decision Maker**: tamld (moderator)  
**Rationale**: Balances all AA perspectives - operational concerns (Codex), evidence quality (Gemini), and practicality (Claude)

---

## Decision: HYBRID POC SCOPE ✅

### **What's Included:**

#### **Core Foundation (Must Have):**
1. **Queue Pattern** - Already working
   - File-based async collaboration
   - Git as coordination backbone
   - Request/response workflow
   - Evidence: This session proves it works

2. **Enhanced Evidence (GPG Signing)** - Low effort, high value
   - Per-AA GPG keys generated
   - Operator signs commits with AA's key
   - `git log --show-signature` verifies authorship
   - Complexity: Low (one-time setup)
   - Value: Strong cryptographic proof

3. **Basic Operational Safeguards** - Essential for reliability
   - Auth/secrets management (env vars)
   - Basic rate limiting awareness
   - Error logging to evidence/
   - Simple retry on transient errors

4. **Context Handoff Files** - Reduce manual overhead
   - `context/for-<aa>.md` structure
   - `context/from-<aa>.md` responses
   - Standardized handoff format
   - Codex will pilot and share

5. **Enhanced Commit Messages** - Link to evidence
   - Template with evidence references
   - Session metadata included
   - Clear AA attribution
   - Git history shows coordination

#### **Deferred to Phase 2:**
- API Attestation (Gemini's second factor)
- Full automation with mcpctl
- Dedicated Git identities per AA
- Message queue infrastructure
- Complete observability stack

---

## Rationale: Why Hybrid?

### **Addresses All AA Perspectives:**

**Codex (Operational):**
✅ Basic safeguards included (auth, rate limits, logging)
✅ Context handoff reduces friction
✅ Evidence preservation in Git
✅ Operational sustainability from day 1

**Gemini (Evidence Quality):**
✅ GPG signing provides cryptographic proof
✅ Stronger than front matter alone
✅ Sets foundation for Phase 2 enhancements
✅ Demonstrates verification mindset

**Claude (Practicality):**
✅ Keeps PoC scope manageable
✅ Builds on what's already working (queue)
✅ Low-hanging fruit (GPG setup is quick)
✅ Proves concept without over-engineering

**User (Business Value):**
✅ Demonstrable multi-AA coordination
✅ Strong evidence for client presentation
✅ Foundation for production scaling
✅ Risk-managed approach

---

## Implementation Plan

### **Phase 1A: Immediate (This Week)**

#### **1. GPG Key Setup** (2-3 hours)
```bash
# Generate keys for each AA
gpg --full-generate-key
# Name: Claude Agent
# Email: claude@mcp-poc.local

gpg --full-generate-key
# Name: Codex Agent
# Email: codex@mcp-poc.local

gpg --full-generate-key
# Name: Gemini Agent
# Email: gemini@mcp-poc.local

# Export public keys
gpg --armor --export claude@mcp-poc.local > evidence/gpg/claude-pubkey.asc
gpg --armor --export codex@mcp-poc.local > evidence/gpg/codex-pubkey.asc
gpg --armor --export gemini@mcp-poc.local > evidence/gpg/gemini-pubkey.asc

# Document key IDs
gpg --list-keys > evidence/gpg/KEY_REGISTRY.md
```

#### **2. Context Directory Structure** (30 minutes)
```bash
mkdir -p context evidence/{gpg,sessions,invocations}

# Create templates
cat > context/README.md
cat > context/handoff-template.md
```

#### **3. Enhanced Commit Template** (15 minutes)
```bash
# Update git commit template
cat > .git/commit-template.txt <<'EOF'
<type>(brainstorm): <AA> contribution - <topic>

AA Session Evidence:
- Session: <AA-name> invoked at <timestamp>
- GPG Signature: <key-id>
- Context: context/for-<aa>.md
- Response: ideas/<aa>/<response>.md
- Duration: <minutes> minutes
- Verified by: tamld (user witness)

Front Matter:
author: <aa>
timestamp: <timestamp>
signed_by: <key-id>
verified_by: tamld
EOF

git config commit.template .git/commit-template.txt
```

#### **4. Basic Safeguards Script** (2-3 hours)
```bash
# Create tools/aa_invoke_helper.sh
# - Load API keys from env
# - Basic rate check
# - Error logging
# - Evidence capture
```

**Deliverables:**
- [ ] GPG keys generated and documented
- [ ] context/ directory structure created
- [ ] Enhanced commit template configured
- [ ] Basic helper script (v1)
- [ ] Documentation: IMPLEMENTATION_GUIDE.md

---

### **Phase 1B: Validation (Next Week)**

#### **5. Test with Real AA Contributions**
```yaml
Test_Cases:
  1. Codex responds to queue request using new pattern
  2. Gemini responds to queue request using new pattern
  3. Verify GPG signatures in git log
  4. Validate evidence trail completeness
  5. Measure time savings vs. previous manual flow

Success_Criteria:
  - GPG signatures verify correctly
  - Context handoff reduces explanation time
  - Evidence trail clear and complete
  - No major friction or blockers
  - Time savings: 20-30% minimum
```

#### **6. Documentation & Training**
```yaml
Documents_To_Create:
  - User guide: How to invoke AA with new pattern
  - Evidence guide: What to capture and where
  - Troubleshooting: Common issues and solutions
  - Quick reference: Command cheat sheet

Share_With_Team:
  - Codex: Will integrate into brainstorm playbook
  - Update session README with new pattern
  - Add to .agents/training/ for future AAs
```

**Deliverables:**
- [ ] 2+ successful AA contributions with new pattern
- [ ] Evidence verified
- [ ] Documentation complete
- [ ] Pattern ready for regular use

---

### **Phase 2: Semi-Automation (Post-PoC Success)**

**Conditional on Phase 1 success:**
- API Attestation (Gemini's recommendation)
- Full mcpctl implementation
- Advanced observability
- Production-grade error handling

**Timeline:** 2-4 weeks after PoC validation

---

## Success Metrics

### **PoC Success = All of:**
1. ✅ Multi-AA coordination demonstrated (queue pattern)
2. ✅ Evidence quality improved (GPG signatures)
3. ✅ Workflow friction reduced (context handoff, templates)
4. ✅ Operational sustainability (basic safeguards)
5. ✅ Client presentation ready (docs/showcase/ populated)
6. ✅ Time savings measured (20-30% vs manual)

### **Evidence Required:**
- 3+ AA contributions using new pattern
- GPG signatures verifying correctly
- Evidence trail complete (git + context + transcripts)
- User testimony: "This is faster and more reliable"
- Client demo materials ready

---

## Risk Mitigation

### **Identified Risks:**

1. **GPG Setup Complexity**
   - Mitigation: Clear step-by-step guide
   - Fallback: Defer GPG if blocks progress

2. **Workflow Changes Disrupt AAs**
   - Mitigation: Make pattern optional initially
   - Fallback: Revert to pure manual if needed

3. **Time Investment Exceeds Value**
   - Mitigation: Track time carefully, stop if ROI poor
   - Fallback: Minimal PoC (Option A)

### **Go/No-Go Checkpoints:**

**Checkpoint 1 (After setup):**
- Decision: Continue or simplify?
- Criteria: Setup took <4 hours, pattern looks usable

**Checkpoint 2 (After 1st test):**
- Decision: Continue or pivot?
- Criteria: Pattern works, no major blockers

**Checkpoint 3 (After validation):**
- Decision: Proceed to Phase 2 or stop?
- Criteria: Success metrics met, value demonstrated

---

## What We're NOT Doing (Explicitly Out of Scope)

❌ **Not in Hybrid PoC:**
- API Attestation (Phase 2)
- Full automation with background processes
- Dedicated Git identities per AA (Production)
- Message queue infrastructure
- Complete CI/CD pipeline
- Helm charts or containerization
- Full observability stack (Prometheus, Grafana)
- Complex policy engine
- Production-grade RBAC

**Rationale:** These are valuable but not required to prove the PoC concept. We can add them in Phase 2/Production based on PoC learnings.

---

## Approval & Sign-off

**Decision Maker:** tamld ✅  
**Date:** 2025-10-25T18:15:00Z

**AA Consensus:**
- Claude: Recommended Hybrid ✅
- Codex: Operational concerns addressed ✅
- Gemini: Evidence quality improved ✅

**Implementation Lead:** Claude (operator)  
**Start Date:** 2025-10-25  
**Target Completion:** Phase 1A by 2025-10-26, Phase 1B by 2025-11-01

---

## References

- Consensus Analysis: `CONSENSUS_ANALYSIS.md` (commit 3348656)
- Session Log: `SESSION_LOG.md`
- Codex Response: `ideas/codex/programmatic-invocation-operational-review.md`
- Gemini Response: `ideas/gemini/evidence-verification-solutions.md`
- Queue Pattern: `queue/README.md`

---

**Status:** ✅ APPROVED - Ready for Implementation  
**Next Action:** Execute Phase 1A (GPG setup + context structure)