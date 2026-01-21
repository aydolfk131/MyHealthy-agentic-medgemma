"""
quality_check_agent.py

This agent simulates a quality check of doctor notes and prescriptions
before sending to MedGemma and the patient.
"""

class QualityCheckAgent:
    def __init__(self):
        # Initialize internal state
        self.flags = []

    def review_prescription(self, prescription_text: str):
        """
        Simulate checking the prescription for errors
        """
        self.flags = []

        # Example
        if not prescription_text:
            self.flags.append("Prescription is empty")
        if "mg" not in prescription_text.lower():
            self.flags.append("Dosage unit missing (mg)")

        return self.flags

    def review_doctor_notes(self, notes_text: str):
        """
        Simulate reviewing doctor notes for completenes
        """
        issues = []
        if not notes_text:
            issues.append("Doctor notes are empty")
        if len(notes_text) < 10:
            issues.append("Doctor notes seem too short")
        return issues

# Example usage when running this file
if __name__ == "__main__":
    agent = QualityCheckAgent()
    prescription_flags = agent.review_prescription("Paracetamol 500, 2x daily")
    notes_issues = agent.review_doctor_notes("Mild fever.")
    
    print("Prescription Flags:", prescription_flags)
    print("Notes Issues:", notes_issues)
