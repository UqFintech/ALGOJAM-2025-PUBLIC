# ALGOJAM-2025 PUBLIC

![AlgoJam Banner](competition_documents/algojam_banner.png)

Welcome to the public repository for ALGOJAM-2025! This repository contains all the public documentation and resources related to the competition.

---

## 📅 Data Release
Competition data will be released on **4th of April, 6PM AEST**.

Join us for the event launch in-person at the UQ GHD Auditorium in the Advanced Engineering Building. The Monday presentation evening will take place in the Prentice Building at 7pm.

📺 **Livestream:**  
- [Event Website](https://uqfintech.org/algojam)  
- [YouTube Channel](https://www.youtube.com/channel/UClC4e9OPixBLdLwLe0l8C4A)

---

## 📄 Competition Documents

| Document Name                        | Description                                                  |
|--------------------------------------|--------------------------------------------------------------|
| [Algo-Jam_General.pdf](competition_documents/Algo-Jam_General.pdf) | General guidelines and information about the competition.    |
| [Algo-Jam_Submission Info.pdf](competition_documents/Algo-Jam_SubmissionInfo.pdf) | Detailed submission instructions and requirements.           |
| [Algo-Jam_Specification.pdf](competition_documents/Algo-Jam_Specification_2025.pdf) | Data context and some suggested trading strategies.          |

---

## 📁 Repository Structure

```
README.md
/competition_documents          # Contains public documentation
/trader_interface               # Your code and simulation environment
/trader_interface/data          # Market data for one simulated year
```

---


## 🚀 Getting Started

1. **Review the Competition Documents:**  
   Start with [Algo-Jam_General.pdf](competition_documents/Algo-Jam_General.pdf) and [Algo-Jam_Submission Info.pdf](competition_documents/Algo-Jam_SubmissionInfo.pdf) to understand competition requirements.

2. **Stay Updated:**  
   Mark your calendar for the data release on **4th of April, 6PM AEST**.

3. **Explore Additional Resources:**  
   Check the [Competition Documents](competition_documents/) folder for further documentation and details.

4. **Download and Extract Trader Interface:**  
   - Download the `trader_interface` folder from GitHub as a ZIP file.  
   - Extract it to your preferred directory.

---

## 🛠️ Environment Setup: 
   While setting up a virtual environment is highly encouraged to manage dependencies effectively, it is not strictly necessary.  
   **Using Python's venv:**  
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use: env\Scripts\activate
   ```  
   **Using Conda:**  
   ```bash
   conda create --name trader_env python=3
   conda activate trader_env
   ```

---

## 📦 Install Required Libraries:
   Run the following to install necessary libraries:
   ```bash
   pip install pandas numpy matplotlib
   ```  
   You may also install any additional approved libraries for your strategy.

---

## 🧠 Modify for Your Submission: 
   Customise the files within the `trader_interface` folder implement your trading algorithm.

---

## ▶️ Run the Simulation:
   Once your modifications are complete, run the simulation script to test your algorithm:  
   ```bash
   python simulation.py
   ```
  Ensure your solution runs with Python 3.

---

## 🔄 Updates and Support

This repository and README will be updated regularly with the latest information

For questions, refer to the contact information in the competition documents.

**Join our Discord** for announcements, team coordination, and Q&A:  
[https://discord.gg/ugBuaXuWuf](https://discord.gg/ugBuaXuWuf)

---

## 🎉 Good luck!
We're excited to see what you build happy algojamming!
