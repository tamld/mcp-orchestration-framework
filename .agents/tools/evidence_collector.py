#!/usr/bin/env python3
"""
Evidence Collector for Implementation Tracking
Captures evidence before, during, and after implementation changes
"""

import json
import os
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import hashlib
import shutil

class EvidenceCollector:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.evidence_dir = self.project_root / ".agents" / "evidence"
        self.evidence_dir.mkdir(parents=True, exist_ok=True)
        self.session_id = f"IMPL-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
    def start_session(self, context: str, purpose: str) -> str:
        """Start a new evidence collection session"""
        session_data = {
            "session_id": self.session_id,
            "context": context,
            "purpose": purpose,
            "start_time": datetime.now().isoformat(),
            "status": "active",
            "evidence": []
        }
        
        session_file = self.evidence_dir / f"{self.session_id}.json"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"🔍 Evidence session started: {self.session_id}")
        return self.session_id
    
    def capture_before_state(self, description: str, files: List[str] = None) -> Dict[str, Any]:
        """Capture current state before implementation"""
        evidence = {
            "type": "before_state",
            "description": description,
            "timestamp": datetime.now().isoformat(),
            "git_status": self._get_git_status(),
            "file_checksums": self._get_file_checksums(files) if files else {},
            "test_results": self._run_tests(),
            "lint_results": self._run_linting(),
            "coverage": self._get_coverage()
        }
        
        self._add_evidence(evidence)
        print(f"📸 Before state captured: {description}")
        return evidence
    
    def capture_implementation_step(self, step: str, changes: List[str], rationale: str) -> Dict[str, Any]:
        """Capture implementation step with changes"""
        evidence = {
            "type": "implementation_step",
            "step": step,
            "changes": changes,
            "rationale": rationale,
            "timestamp": datetime.now().isoformat(),
            "git_diff": self._get_git_diff(),
            "test_results": self._run_tests(),
            "lint_results": self._run_linting()
        }
        
        self._add_evidence(evidence)
        print(f"🔧 Implementation step captured: {step}")
        return evidence
    
    def capture_after_state(self, description: str, success_criteria: List[str]) -> Dict[str, Any]:
        """Capture final state after implementation"""
        evidence = {
            "type": "after_state",
            "description": description,
            "success_criteria": success_criteria,
            "timestamp": datetime.now().isoformat(),
            "git_status": self._get_git_status(),
            "test_results": self._run_tests(),
            "lint_results": self._run_linting(),
            "coverage": self._get_coverage(),
            "success_validation": self._validate_success_criteria(success_criteria)
        }
        
        self._add_evidence(evidence)
        print(f"✅ After state captured: {description}")
        return evidence
    
    def capture_screenshot(self, description: str, file_path: str) -> str:
        """Capture screenshot (placeholder for actual screenshot)"""
        screenshot_path = self.evidence_dir / f"{self.session_id}_{description.replace(' ', '_')}.txt"
        
        # For now, create a text file with description
        with open(screenshot_path, 'w') as f:
            f.write(f"Screenshot: {description}\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"File: {file_path}\n")
        
        evidence = {
            "type": "screenshot",
            "description": description,
            "file_path": str(screenshot_path),
            "timestamp": datetime.now().isoformat()
        }
        
        self._add_evidence(evidence)
        print(f"📷 Screenshot captured: {description}")
        return str(screenshot_path)
    
    def capture_error(self, error: str, resolution: str = None) -> Dict[str, Any]:
        """Capture error and resolution"""
        evidence = {
            "type": "error",
            "error": error,
            "resolution": resolution,
            "timestamp": datetime.now().isoformat(),
            "git_status": self._get_git_status()
        }
        
        self._add_evidence(evidence)
        print(f"❌ Error captured: {error}")
        return evidence
    
    def generate_report(self) -> str:
        """Generate comprehensive evidence report"""
        session_file = self.evidence_dir / f"{self.session_id}.json"
        
        if not session_file.exists():
            return "No session data found"
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        report = f"""
# Evidence Report - {self.session_id}

## Session Overview
- **Context**: {session_data['context']}
- **Purpose**: {session_data['purpose']}
- **Start Time**: {session_data['start_time']}
- **Status**: {session_data['status']}

## Evidence Summary
- **Total Evidence Items**: {len(session_data['evidence'])}
- **Before States**: {len([e for e in session_data['evidence'] if e['type'] == 'before_state'])}
- **Implementation Steps**: {len([e for e in session_data['evidence'] if e['type'] == 'implementation_step'])}
- **After States**: {len([e for e in session_data['evidence'] if e['type'] == 'after_state'])}
- **Errors**: {len([e for e in session_data['evidence'] if e['type'] == 'error'])}

## Detailed Evidence
"""
        
        for i, evidence in enumerate(session_data['evidence'], 1):
            report += f"\n### {i}. {evidence['type'].replace('_', ' ').title()}\n"
            report += f"- **Timestamp**: {evidence['timestamp']}\n"
            report += f"- **Description**: {evidence.get('description', 'N/A')}\n"
            
            if evidence['type'] == 'implementation_step':
                report += f"- **Step**: {evidence.get('step', 'N/A')}\n"
                report += f"- **Changes**: {', '.join(evidence.get('changes', []))}\n"
                report += f"- **Rationale**: {evidence.get('rationale', 'N/A')}\n"
            
            if 'success_validation' in evidence:
                report += f"- **Success Validation**: {evidence['success_validation']}\n"
        
        report_file = self.evidence_dir / f"{self.session_id}_report.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"📊 Evidence report generated: {report_file}")
        return str(report_file)
    
    def _add_evidence(self, evidence: Dict[str, Any]):
        """Add evidence to current session"""
        session_file = self.evidence_dir / f"{self.session_id}.json"
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        session_data['evidence'].append(evidence)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    
    def _get_git_status(self) -> str:
        """Get git status"""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                 capture_output=True, text=True, cwd=self.project_root)
            return result.stdout
        except:
            return "Git not available"
    
    def _get_git_diff(self) -> str:
        """Get git diff"""
        try:
            result = subprocess.run(['git', 'diff'], 
                                 capture_output=True, text=True, cwd=self.project_root)
            return result.stdout
        except:
            return "Git diff not available"
    
    def _get_file_checksums(self, files: List[str]) -> Dict[str, str]:
        """Get checksums for specified files"""
        checksums = {}
        for file_path in files:
            full_path = self.project_root / file_path
            if full_path.exists():
                if full_path.is_file():
                    with open(full_path, 'rb') as f:
                        checksums[file_path] = hashlib.md5(f.read()).hexdigest()
                elif full_path.is_dir():
                    # For directories, get checksum of all files recursively
                    dir_checksums = []
                    for sub_file in full_path.rglob('*'):
                        if sub_file.is_file():
                            with open(sub_file, 'rb') as f:
                                dir_checksums.append(hashlib.md5(f.read()).hexdigest())
                    if dir_checksums:
                        checksums[file_path] = hashlib.md5(''.join(dir_checksums).encode()).hexdigest()
        return checksums
    
    def _run_tests(self) -> Dict[str, Any]:
        """Run tests and return results"""
        try:
            result = subprocess.run(['python', '-m', 'pytest', '--tb=short'], 
                                 capture_output=True, text=True, cwd=self.project_root)
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except:
            return {"error": "Tests not available"}
    
    def _run_linting(self) -> Dict[str, Any]:
        """Run linting and return results"""
        try:
            result = subprocess.run(['ruff', 'check', '.'], 
                                 capture_output=True, text=True, cwd=self.project_root)
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except:
            return {"error": "Linting not available"}
    
    def _get_coverage(self) -> Dict[str, Any]:
        """Get test coverage"""
        try:
            result = subprocess.run(['python', '-m', 'pytest', '--cov=src', '--cov-report=json'], 
                                 capture_output=True, text=True, cwd=self.project_root)
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        except:
            return {"error": "Coverage not available"}
    
    def _validate_success_criteria(self, criteria: List[str]) -> Dict[str, bool]:
        """Validate success criteria"""
        validation = {}
        for criterion in criteria:
            # Simple validation logic - can be enhanced
            validation[criterion] = True  # Placeholder
        return validation

def main():
    """Test the evidence collector"""
    collector = EvidenceCollector()
    
    # Start session
    session_id = collector.start_session(
        context="PoC Project Review & Improvement",
        purpose="Implement testing framework and CI/CD improvements"
    )
    
    # Capture before state
    collector.capture_before_state(
        description="Current state before testing framework implementation",
        files=["src/mcp_poc_framework/", "tests/", "requirements.txt"]
    )
    
    # Generate report
    report_file = collector.generate_report()
    print(f"Evidence collection test completed. Report: {report_file}")

if __name__ == "__main__":
    main()