### Project Name
**MyHealth – Agentic Offline Clinical Workflow**

---

### Your Team
**Team Members:**
- Adie Kajes – Project Lead & AI Integration  
- [Member 2] 

Roles:
- Adie: Designed the overall agentic workflow, implemented MedGemma agents.  
- Backend: Developed offline QR transfer, data locking, and local storage.  
- UX: Created patient and nurse outputs, and demo-ready visualizations.  

---

### Problem Statement
In many low-resource healthcare environments, including rural clinics in Zimbabwe, patients often receive prescriptions and medical instructions they do not fully understand, leading to poor medication adherence and increased clinical workload.  

Cloud-based AI tools are not feasible due to limited internet connectivity and privacy concerns. Doctors and nurses need offline, privacy-preserving tools that assist them in improving patient comprehension and adherence without replacing human decision-making.  

**Impact Potential:**  
- Reduces prescription errors and miscommunication  
- Improves medication adherence via adaptive reminders  
- Decreases workload for nurses and doctors  
- Increases patient engagement and education  

---

### Overall Solution
**HealthMate** is an offline-first, human-in-the-loop system that deploys MedGemma as **three constrained agents**:

1. **Prescription Quality-Check Agent:** Flags incomplete or ambiguous prescriptions for doctor review.  
2. **Clinical Communication Agent:** Converts doctor-approved notes into patient-friendly explanations and structured nurse monitoring sheets.  
3. **Patient Adherence Agent:** Tracks missed doses and adapts reminder messages to improve compliance.  

Doctors retain full control: MedGemma never diagnoses or prescribes. Data is transferred securely via **offline QR codes** and stored locally with read-only locks to ensure privacy.  

This system demonstrates effective use of **HAI-DEF models** in a real-world workflow, improving patient outcomes while respecting medical authority.

---

### Technical Details
- **Agents:** Python scripts using MedGemma for text analysis and generation.  
- **Offline Transfer:** QR codes encode signed, read-only patient data for offline scanning.  
- **Data Privacy:** All outputs are local; patient app is locked via PIN/biometric authentication.  
- **Workflow:** Doctor → Quality-Check Agent → Doctor Approval → Communication Agent → QR Transfer → Patient → Adherence Agent → Nurse Sheet  
- **Reproducibility:** Synthetic patient data used in notebooks for safe, reproducible demonstration.  
- **Deployment:** Fully functional on Kaggle Notebook for judges; modular Python scripts stored in GitHub repo for clarity and maintainability.  

**Repository structure:**
