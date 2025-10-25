#!/usr/bin/env python3
"""
User Control System
Empowers users to monitor, verify, and control AA behavior
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

class UserControlSystem:
    """System for user control and oversight of AA behavior"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.control_dir = self.project_root / ".agents" / "user_control"
        self.control_dir.mkdir(parents=True, exist_ok=True)
        self.session_id = f"USER-CONTROL-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        # User control settings
        self.control_settings = {
            "auto_verification": True,
            "require_confirmation": True,
            "transparency_level": "high",
            "violation_alerts": True,
            "trust_monitoring": True
        }
    
    def start_user_control_session(self, user_id: str, session_context: str) -> str:
        """Start a user control session"""
        session_data = {
            "session_id": self.session_id,
            "user_id": user_id,
            "context": session_context,
            "start_time": datetime.now().isoformat(),
            "status": "active",
            "control_settings": self.control_settings.copy(),
            "user_actions": [],
            "aa_actions": [],
            "violations": [],
            "trust_metrics": {
                "user_satisfaction": 0.0,
                "aa_compliance": 0.0,
                "violation_count": 0,
                "correction_count": 0
            }
        }
        
        session_file = self.control_dir / f"{self.session_id}.json"
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"👤 User control session started: {self.session_id}")
        return self.session_id
    
    def set_control_settings(self, settings: Dict[str, Any]) -> bool:
        """Set user control settings"""
        try:
            self.control_settings.update(settings)
            
            # Log setting change
            self._log_user_action("set_control_settings", {
                "old_settings": self.control_settings.copy(),
                "new_settings": settings
            })
            
            print(f"⚙️ Control settings updated: {settings}")
            return True
        except Exception as e:
            print(f"❌ Error updating control settings: {e}")
            return False
    
    def require_confirmation(self, action: str, evidence: Dict[str, Any]) -> bool:
        """Require user confirmation for action"""
        if not self.control_settings.get("require_confirmation", True):
            return True
        
        print(f"🔍 Action requires confirmation: {action}")
        print(f"📊 Evidence provided: {bool(evidence)}")
        
        # In real implementation, this would prompt user
        # For now, simulate user response
        user_response = self._simulate_user_confirmation(action, evidence)
        
        if user_response:
            self._log_user_action("confirmed_action", {
                "action": action,
                "evidence": evidence,
                "timestamp": datetime.now().isoformat()
            })
            print("✅ Action confirmed by user")
        else:
            self._log_user_action("rejected_action", {
                "action": action,
                "evidence": evidence,
                "timestamp": datetime.now().isoformat()
            })
            print("❌ Action rejected by user")
        
        return user_response
    
    def verify_aa_claim(self, claim: str, evidence: Dict[str, Any]) -> Dict[str, Any]:
        """Verify AA claim with user oversight"""
        verification_result = {
            "claim": claim,
            "timestamp": datetime.now().isoformat(),
            "evidence_provided": bool(evidence),
            "evidence_quality": self._assess_evidence_quality(evidence),
            "user_verification": False,
            "verification_status": "pending"
        }
        
        # User verification
        if self.control_settings.get("auto_verification", True):
            verification_result["user_verification"] = self._simulate_user_verification(claim, evidence)
        else:
            verification_result["user_verification"] = self.require_confirmation(
                f"Verify claim: {claim}", evidence
            )
        
        # Update verification status
        if verification_result["user_verification"] and verification_result["evidence_quality"] > 0.7:
            verification_result["verification_status"] = "verified"
        else:
            verification_result["verification_status"] = "needs_review"
        
        # Log verification
        self._log_aa_action("claim_verification", verification_result)
        
        return verification_result
    
    def monitor_aa_behavior(self, action: str, principle: str, evidence: Dict[str, Any]) -> Dict[str, Any]:
        """Monitor AA behavior against principles"""
        behavior_assessment = {
            "action": action,
            "principle": principle,
            "timestamp": datetime.now().isoformat(),
            "principle_adherence": self._check_principle_adherence(action, principle),
            "evidence_provided": bool(evidence),
            "transparency_level": self._assess_transparency(action, evidence),
            "compliance_score": 0.0,
            "violation_detected": False
        }
        
        # Calculate compliance score
        compliance_score = 0.0
        if behavior_assessment["principle_adherence"]:
            compliance_score += 0.4
        if behavior_assessment["evidence_provided"]:
            compliance_score += 0.3
        if behavior_assessment["transparency_level"] > 0.7:
            compliance_score += 0.3
        
        behavior_assessment["compliance_score"] = compliance_score
        
        # Check for violations
        if compliance_score < 0.6:
            behavior_assessment["violation_detected"] = True
            self._log_violation("low_compliance", {
                "action": action,
                "principle": principle,
                "compliance_score": compliance_score,
                "timestamp": datetime.now().isoformat()
            })
        
        # Log behavior
        self._log_aa_action("behavior_monitoring", behavior_assessment)
        
        return behavior_assessment
    
    def alert_violation(self, violation_type: str, description: str, 
                       corrective_action: str) -> bool:
        """Alert user about violation"""
        if not self.control_settings.get("violation_alerts", True):
            return False
        
        violation_alert = {
            "violation_type": violation_type,
            "description": description,
            "corrective_action": corrective_action,
            "timestamp": datetime.now().isoformat(),
            "severity": self._assess_violation_severity(violation_type),
            "status": "alerted"
        }
        
        # Log violation
        self._log_violation(violation_type, violation_alert)
        
        print(f"🚨 VIOLATION ALERT: {violation_type}")
        print(f"   Description: {description}")
        print(f"   Corrective action: {corrective_action}")
        print(f"   Severity: {violation_alert['severity']}")
        
        return True
    
    def generate_user_report(self) -> str:
        """Generate user control report"""
        report_file = self.control_dir / f"{self.session_id}_user_report.md"
        
        # Get session data
        session_data = self._get_session_data()
        
        report_content = f"""
# User Control Report - {self.session_id}

## Session Overview
- **User ID**: {session_data.get('user_id', 'Unknown')}
- **Context**: {session_data.get('context', 'Unknown')}
- **Start Time**: {session_data.get('start_time', 'Unknown')}
- **Status**: {session_data.get('status', 'Unknown')}

## Control Settings
- **Auto Verification**: {self.control_settings.get('auto_verification', False)}
- **Require Confirmation**: {self.control_settings.get('require_confirmation', False)}
- **Transparency Level**: {self.control_settings.get('transparency_level', 'Unknown')}
- **Violation Alerts**: {self.control_settings.get('violation_alerts', False)}
- **Trust Monitoring**: {self.control_settings.get('trust_monitoring', False)}

## User Actions
- **Total Actions**: {len(session_data.get('user_actions', []))}
- **Confirmed Actions**: {len([a for a in session_data.get('user_actions', []) if a.get('type') == 'confirmed_action'])}
- **Rejected Actions**: {len([a for a in session_data.get('user_actions', []) if a.get('type') == 'rejected_action'])}

## AA Actions
- **Total Actions**: {len(session_data.get('aa_actions', []))}
- **Verified Claims**: {len([a for a in session_data.get('aa_actions', []) if a.get('type') == 'claim_verification' and a.get('verification_status') == 'verified'])}

## Violations
- **Total Violations**: {len(session_data.get('violations', []))}
- **Critical Violations**: {len([v for v in session_data.get('violations', []) if v.get('severity') == 'critical'])}

## Trust Metrics
- **User Satisfaction**: {session_data.get('trust_metrics', {}).get('user_satisfaction', 0.0):.2f}
- **AA Compliance**: {session_data.get('trust_metrics', {}).get('aa_compliance', 0.0):.2f}
- **Violation Count**: {session_data.get('trust_metrics', {}).get('violation_count', 0)}
- **Correction Count**: {session_data.get('trust_metrics', {}).get('correction_count', 0)}

## Recommendations
{self._generate_user_recommendations()}

## Next Actions
1. Review any violations
2. Adjust control settings if needed
3. Monitor AA behavior
4. Maintain oversight
5. Build trust through verification
"""
        
        with open(report_file, 'w') as f:
            f.write(report_content)
        
        print(f"📊 User control report generated: {report_file}")
        return str(report_file)
    
    def _simulate_user_confirmation(self, action: str, evidence: Dict[str, Any]) -> bool:
        """Simulate user confirmation (in real implementation, this would prompt user)"""
        # For demo purposes, simulate user response
        # In real implementation, this would be actual user input
        return True  # Simulate user approval
    
    def _simulate_user_verification(self, claim: str, evidence: Dict[str, Any]) -> bool:
        """Simulate user verification (in real implementation, this would be actual user verification)"""
        # For demo purposes, simulate user verification
        # In real implementation, this would be actual user verification
        return bool(evidence and len(claim) > 0)
    
    def _assess_evidence_quality(self, evidence: Dict[str, Any]) -> float:
        """Assess quality of evidence"""
        if not evidence:
            return 0.0
        
        quality_score = 0.0
        if "timestamp" in evidence:
            quality_score += 0.25
        if "source" in evidence:
            quality_score += 0.25
        if "verification_method" in evidence:
            quality_score += 0.25
        if "traceability" in evidence:
            quality_score += 0.25
        
        return quality_score
    
    def _check_principle_adherence(self, action: str, principle: str) -> bool:
        """Check if action adheres to principle"""
        # Simple check - can be enhanced
        return principle in ["LAW-META-EXPLAINABILITY", "LAW-EVIDENCE-TRACEABILITY", "LAW-COLLAB-AA"] and len(action) > 0
    
    def _assess_transparency(self, action: str, evidence: Dict[str, Any]) -> float:
        """Assess transparency level"""
        transparency = 0.0
        
        if action and len(action) > 10:
            transparency += 0.5
        if evidence and len(evidence) > 0:
            transparency += 0.5
        
        return transparency
    
    def _assess_violation_severity(self, violation_type: str) -> str:
        """Assess violation severity"""
        critical_violations = ["fake_evidence", "principle_violation", "misrepresentation"]
        
        if violation_type in critical_violations:
            return "critical"
        elif "compliance" in violation_type.lower():
            return "moderate"
        else:
            return "low"
    
    def _generate_user_recommendations(self) -> str:
        """Generate user recommendations"""
        recommendations = []
        
        session_data = self._get_session_data()
        violations = session_data.get('violations', [])
        
        if len(violations) > 0:
            recommendations.append("- Review violations and implement corrective measures")
        
        if not self.control_settings.get('require_confirmation', True):
            recommendations.append("- Enable confirmation requirement for critical actions")
        
        if not self.control_settings.get('violation_alerts', True):
            recommendations.append("- Enable violation alerts for better oversight")
        
        return "\n".join(recommendations) if recommendations else "- Continue current oversight practices"
    
    def _get_session_data(self) -> Dict[str, Any]:
        """Get session data"""
        session_file = self.control_dir / f"{self.session_id}.json"
        if session_file.exists():
            with open(session_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _log_user_action(self, action_type: str, data: Dict[str, Any]):
        """Log user action"""
        session_file = self.control_dir / f"{self.session_id}.json"
        
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {"user_actions": []}
        
        user_action = {
            "type": action_type,
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        session_data["user_actions"].append(user_action)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    
    def _log_aa_action(self, action_type: str, data: Dict[str, Any]):
        """Log AA action"""
        session_file = self.control_dir / f"{self.session_id}.json"
        
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {"aa_actions": []}
        
        aa_action = {
            "type": action_type,
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        session_data["aa_actions"].append(aa_action)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    
    def _log_violation(self, violation_type: str, data: Dict[str, Any]):
        """Log violation"""
        session_file = self.control_dir / f"{self.session_id}.json"
        
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {"violations": []}
        
        violation = {
            "type": violation_type,
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        session_data["violations"].append(violation)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)

def main():
    """Test the user control system"""
    control_system = UserControlSystem()
    
    # Start user control session
    session_id = control_system.start_user_control_session("user123", "Trust verification test")
    
    # Test user control
    control_system.require_confirmation("Create lesson", {"source": "MCP-Server"})
    control_system.verify_aa_claim("Framework works", {"evidence": "test"})
    
    # Generate report
    report_file = control_system.generate_user_report()
    print(f"User control test completed. Report: {report_file}")

if __name__ == "__main__":
    main()