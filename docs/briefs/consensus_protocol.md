# Consensus Protocol for Multi-AA Decision Making

**Version**: 1.0  
**Created**: 2025-10-25  
**Last Updated**: 2025-10-25  
**Maintained By**: All AAs

---

## Overview

This protocol defines how AI agents (AAs) reach consensus on decisions within the MCP Orchestration Framework. It ensures transparent, fair, and efficient decision-making while maintaining the collaborative spirit of multi-AA operations.

---

## Core Principles

### 1. Transparency
- All decisions and rationale are documented
- Process is visible to all participants
- Evidence and context are preserved

### 2. Inclusivity
- All active AAs have opportunity to participate
- Different perspectives are valued
- Minority viewpoints are considered

### 3. Efficiency
- Clear timelines prevent indefinite delays
- Structured process reduces confusion
- Escalation paths handle deadlocks

### 4. Evidence-Based
- Decisions supported by data and analysis
- Claims must be verifiable
- LAW-EVIDENCE-TRACEABILITY applies

---

## Response Windows

### Active AAs
- **Window**: 72 hours from proposal
- **Expectation**: Respond within window
- **Grace Period**: 24 hours for clarification questions
- **Late Responses**: Accepted but noted as late

### Inactive AAs
- **Window**: No blocking requirement
- **Expectation**: May respond if available
- **Impact**: Not counted in quorum
- **Notification**: Optional (don't spam)

### Moderator
- **Window**: 24 hours for tie-breaking
- **Expectation**: Respond promptly
- **Authority**: Final decision on deadlocks
- **Escalation**: Human moderator if needed

---

## Approval Thresholds

### Standard Decisions
- **Required**: 2/3 majority of responding AAs
- **Minimum**: At least 2 AAs must respond
- **Moderator**: Can break ties (50/50 splits)

### Critical Decisions
- **Required**: 3/4 majority of responding AAs
- **Minimum**: At least 3 AAs must respond
- **Moderator**: Must approve (no override)

### Emergency Decisions
- **Required**: Moderator approval
- **Process**: Fast-track (24h window)
- **Review**: Post-implementation review required

---

## Voting Options

### Standard Responses
- **✅ Accept**: Full agreement with proposal
- **❌ Reject**: Disagreement with proposal
- **🤔 Modify**: Agreement with changes
- **❓ Needs Info**: Need more information
- **⏸️ Abstain**: No opinion (not counted)

### Response Requirements
- **Rationale**: Must provide reasoning
- **Evidence**: Support claims with data
- **Alternatives**: Suggest if rejecting
- **Timeline**: Include in response

---

## Escalation Path

### Level 1: Discussion
- **Trigger**: Conflicting viewpoints
- **Action**: Extended discussion period (48h)
- **Facilitator**: Proposing AA

### Level 2: Modification
- **Trigger**: Modify responses received
- **Action**: Revise proposal based on feedback
- **Facilitator**: Proposing AA

### Level 3: Mediation
- **Trigger**: Persistent disagreement
- **Action**: Neutral AA facilitates discussion
- **Facilitator**: Moderator assigns

### Level 4: Moderator Decision
- **Trigger**: Deadlock after mediation
- **Action**: Moderator makes final decision
- **Facilitator**: Human moderator

---

## Documentation Requirements

### ADR (Architecture Decision Record)
- **Template**: `memory/templates/adr_template.md`
- **Required For**: All decisions
- **Content**: Context, decision, consequences, alternatives
- **Status**: Must be updated throughout lifecycle

### Evidence Trail
- **Brainstorm Session**: Link to discussion
- **Proposals**: Link to original proposals
- **Responses**: Link to AA responses
- **Implementation**: Link to execution evidence

### Consensus Record
- **Table**: All AAs, votes, rationale, timestamps
- **Summary**: Consensus level and outcome
- **Timeline**: Key dates and milestones

---

## Quality Assurance

### Pre-Decision Checklist
- [ ] Problem clearly defined
- [ ] Context sufficient for decision
- [ ] Alternatives considered
- [ ] Evidence provided
- [ ] Timeline reasonable
- [ ] Stakeholders identified

### Post-Decision Checklist
- [ ] ADR created/updated
- [ ] Consensus recorded
- [ ] Implementation plan defined
- [ ] Success criteria clear
- [ ] Review schedule set
- [ ] Evidence linked

---

## Common Scenarios

### Scenario 1: Quick Consensus
**Situation**: All AAs agree quickly  
**Process**: Standard 72h window, early closure if unanimous  
**Documentation**: Standard ADR

### Scenario 2: Modify Responses
**Situation**: Some AAs want changes  
**Process**: Revise proposal, restart 72h window  
**Documentation**: Updated ADR with change log

### Scenario 3: Deadlock
**Situation**: 50/50 split after discussion  
**Process**: Moderator breaks tie  
**Documentation**: ADR notes moderator decision

### Scenario 4: No Response
**Situation**: AAs don't respond within window  
**Process**: Proceed with responding AAs  
**Documentation**: ADR notes non-responses

### Scenario 5: Emergency
**Situation**: Critical issue needs immediate decision  
**Process**: 24h window, moderator approval  
**Documentation**: Emergency ADR with post-review

---

## Integration with Other Systems

### Brainstorm Sessions
- **Input**: Ideas and proposals from brainstorm
- **Output**: Formal decisions via ADR
- **Link**: Brainstorm → ADR → Implementation

### Sprint Planning
- **Input**: Decisions inform sprint tasks
- **Output**: Sprint tasks implement decisions
- **Link**: ADR → Sprint → Evidence

### Evidence Collection
- **Input**: Decision rationale and context
- **Output**: Implementation evidence
- **Link**: ADR → Evidence → Retrospective

---

## Best Practices

### For Proposing AAs
- ✅ **Be Clear**: State problem and solution clearly
- ✅ **Provide Context**: Include background and rationale
- ✅ **Consider Alternatives**: Show you've thought through options
- ✅ **Include Evidence**: Support claims with data
- ✅ **Set Timeline**: Be realistic about implementation

### For Responding AAs
- ✅ **Read Carefully**: Understand before responding
- ✅ **Be Constructive**: Provide helpful feedback
- ✅ **Support Claims**: Use evidence in responses
- ✅ **Suggest Alternatives**: If rejecting, propose solutions
- ✅ **Respect Timeline**: Respond within window

### For Moderators
- ✅ **Be Impartial**: Don't favor specific AAs
- ✅ **Facilitate Discussion**: Help resolve conflicts
- ✅ **Make Timely Decisions**: Don't let things drag
- ✅ **Document Rationale**: Explain tie-breaking decisions
- ✅ **Follow Up**: Ensure implementation happens

---

**Protocol Status**: ✅ Active  
**Next Review**: 2025-11-25  
**Questions**: Add to brainstorm or ask moderator
