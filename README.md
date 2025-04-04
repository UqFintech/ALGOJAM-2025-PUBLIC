# ALGOJAM-2025 PUBLIC

![AlgoJam Banner](competition_documents/algojam_banner.png)

Welcome to the public repository for ALGOJAM-2025! This repository contains all the public documentation and resources related to the competition.

**Data Release:**  
Competition data will be released on **4th of April, 6PM AEST**.

Join us for the event launch in-person at the UQ GHD Auditorium in the Advanced Engineering Building. The Monday presentation evening will take place in the Prentice Building at 7pm.

See: https://uqfintech.org/events

Otherwise, watch the livestreams on our YouTube channel:
https://www.youtube.com/channel/UClC4e9OPixBLdLwLe0l8C4A

---

## Competition Documents

- [Algo-Jam_General.pdf](competition_documents/Algo-Jam_General.pdf)  
  General guidelines and information about the competition.
- [Algo-Jam_Submission Info.pdf](competition_documents/Algo-Jam_SubmissionInfo.pdf)  
  Detailed submission instructions and requirements.
- [Algo-Jam_Specification.pdf](competition_documents/Algo-Jam_Specification_2025.pdf)  
  Data context and some suggested trading strategies.
---

## Repository Structure

- **README.md**  
  This file with an overview of the repository.
- **/competition_documents**  
  Contains competition public documentation and resources.
- **/trader_interface**  
  Contains relevant competitor code: simulation.py runs your implementation of the algorithm.py file.
- **/trader_interface/data**  
  Contains all data for the first simulated year of trading.

---


## Getting Started

1. **Review the Competition Documents:**  
   Start with the general guidelines and submission info to understand the competition requirements.

2. **Stay Updated:**  
   Mark your calendar for the data release on **4th of April, 6PM AEST**.

3. **Explore Additional Resources:**  
   Check the [Competition Documents](competition_documents/) folder for further documentation and details.

4. **Download and Extract Trader Interface:**  
   - Download the `trader_interface` folder from GitHub as a ZIP file.  
   - Extract the ZIP file to your preferred directory.

5. **Environment Setup:**  
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

6. **Install Required Libraries:**  
   The simulation requires the following libraries:  
   - `pandas`
   - `numpy`
   - `matplotlib`  
   Install them using pip:  
   ```bash
   pip install pandas numpy matplotlib
   ```  
   If you have another approved library, feel free to install it as well.

7. **Modify for Your Submission:**  
   Customize the files within the `trader_interface` folder as needed to integrate your trading algorithm.

8. **Run the Simulation:**  
   Once your modifications are complete, run the simulation script to test your algorithm:  
   ```bash
   python simulation.py
   ```

9. **Compatibility:**  
   Ensure your solution is compatible with Python 3.
---

## Updates

This repository and README will be updated regularly with the latest information about ALGOJAM-2025. For any questions or further details, please refer to the contact information provided within the competition documents.

Good luck, and we look forward to your participation!
