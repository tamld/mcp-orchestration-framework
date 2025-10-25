---
handoff_id: HANDOFF-YYYY-MM-DD-NNN
from_aa: [Sending AA name]
to_aa: [Receiving AA name]
task: [Brief task description]
created: YYYY-MM-DDTHH:MM:SSZ
status: pending  # pending | acknowledged | in_progress | completed | blocked
priority: medium  # low | medium | high | critical
---

# Context Handoff: [Task Name]

**From**: [Sending AA] → **To**: [Receiving AA]  
**Date**: YYYY-MM-DD HH:MM  
**Estimated Effort**: [X hours/days]

---

## Summary (TL;DR)

<!-- 2-3 sentence summary of what needs to be done -->

**What**: [What needs to be done]  
**Why**: [Why it's needed]  
**When**: [Deadline or urgency]

---

## Current State

### What's Been Done:
- [ ] [Completed task 1]
- [ ] [Completed task 2]
- [ ] [Completed task 3]

### Key Decisions Made:
1. **[Decision 1]**: [Rationale]
2. **[Decision 2]**: [Rationale]

### Files Modified:
```
path/to/file1.py  # What was changed
path/to/file2.md  # What was changed
```

### Commits:
- `abc123f` - [Commit message]
- `def456g` - [Commit message]

---

## What Needs to Be Done

### Primary Task:
[Detailed description of the main task]

### Sub-tasks:
- [ ] [Sub-task 1] - [Estimate: Xh]
- [ ] [Sub-task 2] - [Estimate: Xh]
- [ ] [Sub-task 3] - [Estimate: Xh]

### Acceptance Criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## Context & Background

### Why This Work?
[Explain the motivation, problem being solved, or feature being built]

### Previous Attempts:
[What was tried before? Why didn't it work?]

### Constraints:
- [Constraint 1: e.g., Must maintain backward compatibility]
- [Constraint 2: e.g., Limited to X hours of work]
- [Constraint 3: e.g., No external dependencies allowed]

### Dependencies:
- **Blocked By**: [List anything blocking this work]
- **Blocks**: [List anything this work blocks]
- **Related To**: [List related tasks or issues]

---

## Technical Details

### Architecture/Design:
[Relevant architecture decisions, design patterns, or approaches to follow]

### Key Files to Review:
```
path/to/important/file1.py   # Why it's important
path/to/important/file2.md   # Why it's important
```

### APIs/Interfaces:
[Document any APIs, interfaces, or contracts to maintain]

### Environment:
```bash
# Setup commands if needed
cd /path/to/project
source venv/bin/activate
export VAR=value
```

### Known Issues:
1. **[Issue 1]**: [Description and potential solution]
2. **[Issue 2]**: [Description and potential solution]

---

## What I Tried (Sending AA)

### Approaches Attempted:
1. **Approach 1**: [What, why it didn't work]
2. **Approach 2**: [What, why it didn't work]

### Debugging Done:
- [What was investigated]
- [What was ruled out]
- [What remains unclear]

### Lessons Learned:
- [Lesson 1]
- [Lesson 2]

---

## Recommended Next Steps

### Step-by-Step Plan:
1. [First, do this because...]
2. [Then, do this because...]
3. [Finally, do this because...]

### Alternative Approaches:
- **Option A**: [Pros/cons]
- **Option B**: [Pros/cons]

### Who to Ask:
- **[Topic]**: Ask [AA/person name]
- **[Topic]**: Reference [document/link]

---

## Evidence & References

### Related Artifacts:
- **Brainstorm Session**: [Link or ID]
- **ADR**: [Link to decision record]
- **Issue/PR**: [Link to GitHub issue/PR]
- **Tests**: [Link to test results]

### Logs/Errors:
```
[Paste relevant error messages or logs]
```

### Screenshots/Diagrams:
[Link or embed if applicable]

---

## Questions for Receiving AA

### Before You Start:
1. [Question 1]
2. [Question 2]

### Clarifications Needed:
- [Clarification 1]
- [Clarification 2]

---

## Progress Tracking (Receiving AA Updates Here)

### [YYYY-MM-DD HH:MM] - [Receiving AA Name]

#### Status Update:
[What's been done, what's in progress, what's next]

#### Completed:
- [x] [Task completed]

#### In Progress:
- [ ] [Task being worked on]

#### Blockers:
- [Blocker description]

#### Questions/Feedback:
- [Question or feedback for sending AA]

---

## Acknowledgment (Receiving AA)

**Acknowledged By**: [Receiving AA Name]  
**Date**: YYYY-MM-DD HH:MM  
**Estimated Completion**: YYYY-MM-DD

### I Understand:
- [x] Task requirements clear
- [x] Acceptance criteria understood
- [x] Context sufficient to proceed
- [x] No blockers prevent starting

### Questions/Concerns:
[Any questions or concerns before starting]

### Revised Plan (if different from recommended):
[If you plan to approach differently, explain why]

---

## Completion (Receiving AA)

**Completed By**: [Receiving AA Name]  
**Date**: YYYY-MM-DD HH:MM  
**Actual Effort**: [X hours]

### What Was Delivered:
- [Deliverable 1]
- [Deliverable 2]

### Changes Made:
```
path/to/modified/file1.py  # What changed
path/to/modified/file2.md  # What changed
```

### Commits:
- `xyz789h` - [Commit message]

### Evidence:
- **Tests**: [Pass/fail status, link to results]
- **Review**: [If applicable]
- **Documentation**: [Updated docs]

### Handoff Back (if needed):
[If work continues with another AA, create new handoff or update this section]

---

## Retrospective (Optional)

### What Went Well:
- [Success 1]

### What Could Improve:
- [Improvement 1]

### Lessons for Future Handoffs:
- [Lesson 1]

---

**Handoff Status**: [pending | acknowledged | in_progress | completed | blocked]  
**Last Updated**: YYYY-MM-DD HH:MM by [AA Name]