"""
Test Evidence Collector - Real Implementation Test
This is a REAL test that will be run to validate the evidence collection system
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
from .evidence_collector import EvidenceCollector

class TestEvidenceCollector:
    """Test suite for EvidenceCollector"""
    
    def setup_method(self):
        """Setup test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.collector = EvidenceCollector(self.temp_dir)
        
        # Create test files
        self.test_file = Path(self.temp_dir) / "test_file.txt"
        self.test_file.write_text("Initial content")
        
        # Initialize git repo for testing
        import subprocess
        subprocess.run(['git', 'init'], cwd=self.temp_dir, capture_output=True)
        subprocess.run(['git', 'config', 'user.email', 'test@example.com'], cwd=self.temp_dir, capture_output=True)
        subprocess.run(['git', 'config', 'user.name', 'Test User'], cwd=self.temp_dir, capture_output=True)
        subprocess.run(['git', 'add', '.'], cwd=self.temp_dir, capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=self.temp_dir, capture_output=True)
    
    def teardown_method(self):
        """Cleanup test environment"""
        shutil.rmtree(self.temp_dir)
    
    def test_session_creation(self):
        """Test session creation"""
        session_id = self.collector.start_session(
            context="Test Implementation",
            purpose="Validate evidence collection system"
        )
        
        assert session_id is not None
        assert session_id.startswith("IMPL-")
        
        # Verify session file exists
        session_file = Path(self.temp_dir) / ".agents" / "evidence" / f"{session_id}.json"
        assert session_file.exists()
        
        # Verify session data
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        assert session_data['session_id'] == session_id
        assert session_data['context'] == "Test Implementation"
        assert session_data['purpose'] == "Validate evidence collection system"
        assert session_data['status'] == "active"
        assert len(session_data['evidence']) == 0
    
    def test_before_state_capture(self):
        """Test before state capture"""
        session_id = self.collector.start_session("Test", "Test")
        
        evidence = self.collector.capture_before_state(
            description="Testing before state capture",
            files=["test_file.txt"]
        )
        
        assert evidence['type'] == "before_state"
        assert evidence['description'] == "Testing before state capture"
        assert "test_file.txt" in evidence['file_checksums']
        assert evidence['file_checksums']['test_file.txt'] is not None
    
    def test_implementation_step_capture(self):
        """Test implementation step capture"""
        session_id = self.collector.start_session("Test", "Test")
        
        # Modify test file
        self.test_file.write_text("Modified content")
        
        evidence = self.collector.capture_implementation_step(
            step="Modify test file",
            changes=["test_file.txt"],
            rationale="Testing implementation step capture"
        )
        
        assert evidence['type'] == "implementation_step"
        assert evidence['step'] == "Modify test file"
        assert "test_file.txt" in evidence['changes']
        assert evidence['rationale'] == "Testing implementation step capture"
    
    def test_after_state_capture(self):
        """Test after state capture"""
        session_id = self.collector.start_session("Test", "Test")
        
        evidence = self.collector.capture_after_state(
            description="Testing after state capture",
            success_criteria=["File modified", "Git status clean"]
        )
        
        assert evidence['type'] == "after_state"
        assert evidence['description'] == "Testing after state capture"
        assert "File modified" in evidence['success_criteria']
        assert "Git status clean" in evidence['success_criteria']
    
    def test_error_capture(self):
        """Test error capture"""
        session_id = self.collector.start_session("Test", "Test")
        
        evidence = self.collector.capture_error(
            error="Test error occurred",
            resolution="Fixed by modifying test file"
        )
        
        assert evidence['type'] == "error"
        assert evidence['error'] == "Test error occurred"
        assert evidence['resolution'] == "Fixed by modifying test file"
    
    def test_screenshot_capture(self):
        """Test screenshot capture"""
        session_id = self.collector.start_session("Test", "Test")
        
        screenshot_path = self.collector.capture_screenshot(
            description="Test screenshot",
            file_path="test_file.txt"
        )
        
        assert screenshot_path is not None
        assert Path(screenshot_path).exists()
        
        # Verify screenshot content
        with open(screenshot_path, 'r') as f:
            content = f.read()
        assert "Test screenshot" in content
        assert "test_file.txt" in content
    
    def test_report_generation(self):
        """Test report generation"""
        session_id = self.collector.start_session("Test", "Test")
        
        # Add some evidence
        self.collector.capture_before_state("Before", ["test_file.txt"])
        self.collector.capture_implementation_step("Step", ["test_file.txt"], "Rationale")
        self.collector.capture_after_state("After", ["Success"])
        
        # Generate report
        report_file = self.collector.generate_report()
        
        assert report_file is not None
        assert Path(report_file).exists()
        
        # Verify report content
        with open(report_file, 'r') as f:
            content = f.read()
        
        assert "Evidence Report" in content
        assert "Test" in content
        assert "Before" in content
        assert "Step" in content
        assert "After" in content
        assert "Total Evidence Items: 3" in content
    
    def test_full_workflow(self):
        """Test complete evidence collection workflow"""
        # Start session
        session_id = self.collector.start_session(
            context="Full Workflow Test",
            purpose="Test complete evidence collection workflow"
        )
        
        # Capture before state
        before_evidence = self.collector.capture_before_state(
            description="Initial state before modifications",
            files=["test_file.txt"]
        )
        
        # Make changes
        self.test_file.write_text("Modified content for workflow test")
        
        # Capture implementation step
        impl_evidence = self.collector.capture_implementation_step(
            step="Modify test file content",
            changes=["test_file.txt"],
            rationale="Testing complete workflow with real file changes"
        )
        
        # Capture after state
        after_evidence = self.collector.capture_after_state(
            description="Final state after modifications",
            success_criteria=["File content modified", "Git status updated"]
        )
        
        # Generate report
        report_file = self.collector.generate_report()
        
        # Verify all evidence was captured
        session_file = Path(self.temp_dir) / ".agents" / "evidence" / f"{session_id}.json"
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        assert len(session_data['evidence']) == 3
        assert session_data['evidence'][0]['type'] == "before_state"
        assert session_data['evidence'][1]['type'] == "implementation_step"
        assert session_data['evidence'][2]['type'] == "after_state"
        
        # Verify report was generated
        assert Path(report_file).exists()
        
        print(f"✅ Full workflow test completed successfully!")
        print(f"📊 Evidence report: {report_file}")
        print(f"📁 Session data: {session_file}")

if __name__ == "__main__":
    # Run the test directly
    test = TestEvidenceCollector()
    test.setup_method()
    try:
        test.test_full_workflow()
        print("🎉 All tests passed!")
    finally:
        test.teardown_method()