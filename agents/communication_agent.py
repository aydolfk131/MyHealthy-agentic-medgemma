"""
This agent handles sending doctor-approved notes and prescriptions
to patients and generating nurse-friendly printable sheets.
"""

import qrcode
from PIL import Image
import os

class CommunicationAgent:
    def __init__(self, output_dir="outputs"):
        """
        Initializes the agent with an output directory
        for QR codes or printable files.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_patient_qr(self, message: str, filename: str):
        """
        Generates a QR code for the patient containing
        doctor notes and prescription instructions.
        """
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(message)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        path = os.path.join(self.output_dir, f"{filename}.png")
        img.save(path)
        return path

    def generate_nurse_sheet(self, notes_text: str, prescription_text: str, filename: str):
        
        #Creates a simple text file that nurses can print with all relevant patient info.
        path = os.path.join(self.output_dir, f"{filename}.txt")
        with open(path, "w") as f:
            f.write("=== Nurse Patient Sheet ===\n\n")
            f.write("Doctor Notes:\n")
            f.write(notes_text + "\n\n")
            f.write("Prescription:\n")
            f.write(prescription_text + "\n")
        return path

# Example usage when running this file directly
if __name__ == "__main__":
    comm_agent = CommunicationAgent()
    
    qr_path = comm_agent.generate_patient_qr(
        "Take Paracetamol 500mg twice daily after meals",
        "patient_qr_001"
    )
    print("QR code saved at:", qr_path)
    
    nurse_sheet_path = comm_agent.generate_nurse_sheet(
        "Patient has mild fever, monitor temperature every 4h",
        "Paracetamol 500mg, 2x daily",
        "nurse_sheet_001"
    )
    print("Nurse sheet saved at:", nurse_sheet_path)
