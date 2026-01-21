"""
This agent handles sending doctor-approved notes and prescriptions
to patients and generating nurse-friendly printable sheets.
"""

import qrcode
from PIL import Image
import os
from datetime import datetime, timedelta
import hashlib


class CommunicationAgent:
    def __init__(self, output_dir="outputs"):
        """
        Initializes the agent with an output directory
        for QR codes or printable files.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    def _generate_checksum(text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()[:6].upper()

    def generate_patient_token(self, content: str, filename: str, validity_days: int = 3):
        issued_at = datetime.now()
        expires_at = issued_at + timedelta(days=validity_days)
        token_text = f"""
    PATIENT TOKEN
    Issued: {issued_at.strftime('%Y-%m-%d %H:%M')}
    Expires: {expires_at.strftime('%Y-%m-%d %H:%M')}
    CONTENT:{content.strip()}
    """.strip()
        checksum = _generate_checksum(token_text)
        final_text = f"{token_text}\n\nChecksum: {checksum}"

    # Create image
    img = Image.new("RGB", (500, 500), "white")
    draw = ImageDraw.Draw(img)

    draw.rectangle([20, 20, 480, 480], outline="black", width=3)
    draw.multiline_text((30, 40), final_text, fill="black", spacing=6)

    path = f"{self.output_dir}/{filename}.png"
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
