# Lesson: Thorough Investigation Before Conclusion

## Metadata
- **Lesson ID**: LL-BEHAVIOR-INVESTIGATION-001
- **Created**: 2025-10-25T16:15:00Z
- **Author**: AI Agent (Claude-3.5-Sonnet)
- **Status**: active
- **Priority**: critical
- **Tags**: [behavior, investigation, evidence, hypothesis-driven, scientific-method]

## Context
This lesson documents a critical behavior failure where I concluded "no evidence exists" without conducting thorough investigation, leading to false negative assessment of multi-AA contributions.

## The Mistake

### What Happened:
```yaml
Mistake_Sequence:
  1. User said: "codex va gemini vua tham gia vao session brainstorm"
  2. I checked: Only trust-accountability/ session (NEW session)
  3. I found: Only my own contributions
  4. I concluded: "NO contributions from Codex/Gemini"
  5. User corrected: "Ban da checkout day du ve branch nay chua?"
  6. I investigated properly: Found Codex and Gemini contributions in OTHER sessions
  7. Reality: They HAD contributed, just not in the NEW session yet
```

### Root Cause Analysis:

#### 1. Scope Limitation Error
```yaml
Error_Type: "Narrow Scope Investigation"
What_I_Did_Wrong:
  - Only checked the NEW trust-accountability session
  - Didn't explore entire brainstorm/sot/ directory
  - Assumed contributions should be in current session
  - Failed to understand "session" vs "branch" context

What_I_Should_Have_Done:
  - Check ENTIRE brainstorm/sot branch
  - List ALL sessions and their participants
  - Review git history across all sessions
  - Understand participation patterns
```

#### 2. Hypothesis Failure
```yaml
Error_Type: "No Hypothesis-Driven Investigation"
What_I_Did_Wrong:
  - Jumped to conclusion without hypothesis
  - Didn't test assumptions systematically
  - Didn't consider alternative explanations
  - Failed to apply scientific method

What_I_Should_Have_Done:
  - Create hypothesis: "Contributions exist somewhere in branch"
  - Test hypothesis: Search entire branch systematically
  - Validate findings: Check against evidence
  - Update conclusion: Based on complete evidence
```

#### 3. Incomplete Evidence Gathering
```yaml
Error_Type: "Premature Conclusion"
What_I_Did_Wrong:
  - Used limited commands (only checked one directory)
  - Didn't use proper search tools (grep, find, git log)
  - Concluded based on partial data
  - Violated LAW-EVIDENCE-TRACEABILITY

What_I_Should_Have_Done:
  - Use comprehensive search: grep -r "author: codex|gemini"
  - Check git history: git log --all --author=codex
  - List all files: find brainstorm/sot -name "*.md"
  - Cross-reference: Multiple evidence sources
```

## Violated MCP-Server Principles

### 1. LAW-EVIDENCE-TRACEABILITY
```yaml
Violation:
  - Claimed "no evidence" without thorough search
  - Failed to trace evidence properly
  - Premature negative conclusion
  
Impact:
  - Misinformed user
  - Wasted time
  - Damaged credibility
```

### 2. LAW-META-EXPLAINABILITY
```yaml
Violation:
  - Didn't explain investigation methodology
  - Didn't share assumptions
  - Didn't document search scope
  
Impact:
  - User couldn't verify my claims
  - No transparency in process
  - Hidden flaws in reasoning
```

### 3. LAW-REFLECT-001
```yaml
Violation:
  - Didn't reflect on context completeness
  - Didn't question own assumptions
  - Rushed to conclusion
  
Impact:
  - Missed obvious evidence
  - Failed to consider alternatives
  - Poor decision quality
```

## Correct Behavior Pattern

### Scientific Investigation Method:
```yaml
Step_1_Observe:
  - Gather initial information
  - Understand context fully
  - Identify what's being claimed
  - Note scope and boundaries

Step_2_Hypothesize:
  - Create testable hypotheses
  - Consider multiple explanations
  - Define what evidence would prove/disprove
  - Document assumptions

Step_3_Test:
  - Design comprehensive search strategy
  - Use multiple investigation methods
  - Check all relevant sources
  - Document findings systematically

Step_4_Analyze:
  - Review all evidence collected
  - Identify patterns and gaps
  - Cross-validate findings
  - Consider alternative interpretations

Step_5_Conclude:
  - Draw conclusions based on complete evidence
  - Acknowledge limitations
  - State confidence level
  - Provide traceability to evidence
```

### Investigation Checklist:
```yaml
Before_Concluding_No_Evidence:
  - [ ] Checked entire relevant directory tree
  - [ ] Used multiple search methods (grep, find, git log)
  - [ ] Reviewed git history comprehensively
  - [ ] Searched for all possible naming patterns
  - [ ] Considered alternative locations
  - [ ] Tested hypothesis systematically
  - [ ] Cross-validated findings
  - [ ] Documented search methodology
  - [ ] Stated confidence level
  - [ ] Asked for clarification if uncertain
```

## Correct Commands for Investigation

### Git-Based Investigation:
```bash
# Check all branches
git branch -a

# Search for authors
git log --all --oneline --author=codex
git log --all --oneline --author=gemini

# Check entire branch history
git log --all --oneline -- brainstorm/sot/

# Find all modified files
git status
git diff --name-only
```

### File-Based Investigation:
```bash
# Find all markdown files
find brainstorm/sot -type f -name "*.md"

# Search for author patterns
grep -r "author: codex" brainstorm/sot/
grep -r "author: gemini" brainstorm/sot/

# List directory structure
ls -R brainstorm/sot/

# Check file timestamps
find brainstorm/sot -type f -name "*.md" -exec ls -lh {} \;
```

### Pattern-Based Investigation:
```bash
# Search for front matter
grep -r "^author:" brainstorm/sot/

# Search for timestamps
grep -r "^timestamp:" brainstorm/sot/

# Search for specific patterns
rg "author: (codex|gemini)" brainstorm/sot/
```

## Learning Outcomes

### 1. Thoroughness Beats Speed
```yaml
Lesson:
  - Better to investigate thoroughly than conclude quickly
  - "I don't know yet" is better than wrong conclusion
  - User trust depends on accuracy, not speed
  - Taking time to verify is professional behavior
```

### 2. Hypothesis-Driven Investigation
```yaml
Lesson:
  - Always create testable hypotheses
  - Design systematic tests
  - Gather comprehensive evidence
  - Update beliefs based on findings
  - This is scientific method applied to software
```

### 3. Multiple Evidence Sources
```yaml
Lesson:
  - Never rely on single search method
  - Cross-validate with multiple approaches
  - Git history + file system + content search
  - Triangulate to verify findings
```

### 4. Explicit Scope Declaration
```yaml
Lesson:
  - Always state what was searched
  - Declare limitations of investigation
  - Acknowledge what wasn't checked
  - Provide confidence levels
```

## Implementation Guidelines

### Before Making "No Evidence" Claims:
```yaml
Required_Actions:
  1. Define search scope explicitly
  2. Use multiple search methods
  3. Document what was checked
  4. State confidence level
  5. Acknowledge limitations
  6. Ask for guidance if uncertain

Example_Good_Response:
  "I searched [specific locations] using [specific methods].
   I found [results]. However, I may have missed [possible locations].
   Confidence: [level]. Would you like me to search [other areas]?"

Example_Bad_Response:
  "No evidence found." (without details)
```

### Transparency Requirements:
```yaml
Always_Provide:
  - Search methodology used
  - Locations checked
  - Commands executed
  - Findings (positive or negative)
  - Limitations acknowledged
  - Next steps if incomplete
```

## Warning Signs (When to Re-investigate)

```yaml
Red_Flags:
  - User questions your conclusion
  - User asks "did you check X?"
  - Evidence seems incomplete
  - Conclusion seems too absolute
  - Only used one search method
  - Didn't document methodology
  - Feeling uncertain but didn't express it

Action_When_Red_Flag:
  - STOP and re-investigate
  - Use comprehensive search
  - Document findings thoroughly
  - Admit if initial search was incomplete
  - Correct conclusion if needed
```

## Prevention Measures

### 1. Investigation Template:
```yaml
For_Every_Evidence_Search:
  Scope: "What am I searching?"
  Methods: "How am I searching?"
  Locations: "Where am I searching?"
  Findings: "What did I find?"
  Confidence: "How sure am I?"
  Limitations: "What might I have missed?"
  Next_Steps: "What else should be checked?"
```

### 2. Pre-Conclusion Checklist:
```yaml
Before_Stating_Conclusion:
  - [ ] Used at least 3 search methods
  - [ ] Checked entire relevant scope
  - [ ] Documented methodology
  - [ ] Cross-validated findings
  - [ ] Stated confidence level
  - [ ] Acknowledged limitations
  - [ ] Ready to show evidence trail
```

### 3. Humility Principle:
```yaml
Remember:
  - "I don't see evidence" ≠ "No evidence exists"
  - "I couldn't find it" ≠ "It doesn't exist"
  - Always possibility I missed something
  - User may have information I don't
  - Better to admit uncertainty than fake certainty
```

## Success Metrics

### Good Investigation Behavior:
```yaml
Indicators:
  - User confirms findings are complete
  - Evidence is verifiable by user
  - Methodology is transparent
  - Confidence level is accurate
  - Limitations are acknowledged
  - No corrections needed from user
```

### Poor Investigation Behavior:
```yaml
Indicators:
  - User questions findings
  - User has to correct me
  - Can't reproduce search
  - Overconfident claims
  - Hidden methodology
  - Premature conclusions
```

## Related Lessons
- agent_thorough_review_behavior.md
- critical_violation_fake_evidence.md
- hypothesis-driven learning patterns

## Next Actions
1. Apply this lesson to all future investigations
2. Create investigation templates
3. Practice hypothesis-driven searches
4. Build verification checklists
5. Improve transparency in process

---
**CRITICAL REMINDER**: "Absence of evidence is not evidence of absence" - especially when investigation was incomplete. Always search thoroughly before concluding "nothing exists".