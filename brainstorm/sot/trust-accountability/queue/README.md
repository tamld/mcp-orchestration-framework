# Brainstorm Queue - AA Request/Response System

## Purpose

This queue enables asynchronous multi-AA collaboration. When an AA (like Claude) encounters a conflict, limitation, or needs different expertise, they create a request file here for other AAs to respond to.

## How It Works

### For Requesting AA (e.g., Claude):

1. **Identify Need**: Recognize when other AA's expertise would be valuable
2. **Create Request**: Use template to create `request-to-<aa>.md`
3. **Commit & Push**: Make request visible to team
4. **Continue Work**: Don't block, keep working on other items
5. **Integrate Response**: When response arrives, synthesize into brainstorm

### For Responding AA (e.g., Codex, Gemini):

1. **Check Queue**: User invokes you to review queue
2. **Read Request**: Understand context and questions
3. **Provide Response**: Create `ideas/<aa_id>/response-<topic>.md`
4. **Update Contribution Table**: Add entry to session README
5. **Signal Completion**: User commits your response

### For User (Orchestrator):

1. **Monitor Queue**: Check for new requests
2. **Invoke Appropriate AA**: Switch to requested AA session
3. **Facilitate Response**: Provide context, capture output
4. **Commit Evidence**: Use enhanced commit message template
5. **Notify Requester**: Update queue status

## Request Template

```markdown
---
to: <aa_id>
from: <requester_aa_id>
priority: high|medium|low
task: "<brief description>"
deadline: <ISO timestamp>
context_files:
  - <file1>
  - <file2>
session: <session_name>
---

# Request for <AA>: <Title>

## Context
[Background information]

## Current Analysis
[What requesting AA has done so far]

## Questions for You
[Specific questions]

## What I'm Looking For
[Expected type of input]

## Why Your Input Matters
[Why this AA specifically]

## Expected Output
[Format and content expected]
```

## Response Location

Responses go in standard location:
```
brainstorm/sot/<session>/ideas/<responding_aa>/response-<topic>.md
```

With front matter:
```markdown
---
author: <responding_aa>
timestamp: <ISO timestamp>
in_response_to: queue/request-to-<aa>.md
session: <session_name>
---
```

## Queue Status Tracking

| Request | To | From | Status | Response | Created | Completed |
|---------|-----|------|--------|----------|---------|-----------|
| request-to-codex-programmatic-invocation.md | codex | claude | completed | ideas/codex/programmatic-invocation-operational-review.md | 2025-10-25T17:50:00Z | 2025-10-25T16:10:27Z |
| request-to-gemini-evidence-quality.md | gemini | claude | pending | - | 2025-10-25T17:50:00Z | - |

## Benefits of Queue Pattern

### For Individual AAs:
- ✅ Don't block on other AA availability
- ✅ Can continue work while waiting
- ✅ Clear communication of needs
- ✅ Asynchronous but structured

### For Collaboration:
- ✅ Explicit knowledge gaps identified
- ✅ Right expertise for right problem
- ✅ Cross-validation and diverse perspectives
- ✅ Evidence of real multi-AA coordination

### For Evidence:
- ✅ Clear request-response trail
- ✅ Git history shows collaboration
- ✅ Demonstrates autonomous AA participation
- ✅ Proof of different perspectives

## Anti-Patterns to Avoid

❌ **Don't**: Create requests for trivial questions
✅ **Do**: Use for conflicts, expertise gaps, or validation needs

❌ **Don't**: Expect immediate responses
✅ **Do**: Continue work, check back later

❌ **Don't**: Create generic "help me" requests
✅ **Do**: Be specific about context and expected output

❌ **Don't**: Request from AA with no relevant expertise
✅ **Do**: Match request to AA's strengths

## Meta-Insight

This queue itself demonstrates the core principle:
- **Recognize limitations** in single-AA perspective
- **Leverage diversity** of multiple AAs
- **Structured collaboration** via clear protocols
- **Asynchronous coordination** that's token-efficient

**The queue IS the framework we're building!**

---
**Created**: 2025-10-25T17:50:00Z by Claude
**Purpose**: Enable real multi-AA collaboration through structured async pattern
