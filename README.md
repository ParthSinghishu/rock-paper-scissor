# Rock–Paper–Scissors Game

This project is a simple rule-based implementation of the classic *Rock–Paper–Scissors* game using Python.  
It is designed as a beginner-level project for the “Introduction to AIML” course where the focus is on  
understanding basic decision-making, control flow, modular code, and user interaction.

Although this project does not use machine learning, it demonstrates how a computer can take decisions  
based on programmed rules — which is one of the core ideas behind Artificial Intelligence.

---

## 🔹 Features
- User vs CPU match  
- Best-of-N rounds (user chooses N)  
- Clean input validation  
- Scoreboard after every round  
- Random CPU move selection  
- Option to save match summary in a text file  
- Modular code (separate files for logic, game flow, report)

---

## 🔹 How It Works
1. The user selects the number of rounds (only odd numbers like 3, 5, 7).  
2. In every round:
   - User enters rock/paper/scissors  
   - CPU makes a random choice  
   - Program compares choices and updates the score  
3. First to reach the required wins is declared the match winner.  
4. The user can choose to save a match summary as a `.txt` file in the `reports/` folder.

---

## 🔹 Project File Structure
rock-paper-scissors/
│   
├── main.py → Controls game flow   
├── game_module.py → Handles choices, winner logic, CPU moves   
├── report_module.py → Saves match results in reports/   
├── README.md → Project documentation   
├── statement.md → Problem statement + scope   
│   
├── diagrams/ → Text-based design diagrams   
│ ├── use_case.txt         
│ ├── sequence.txt   
│ ├── class_diagram.txt   
│   
└── reports/   
└── sample_match.txt   


## 🔹 How to Run
1. Install Python (3.8+ recommended).  
2. Open the folder in terminal or Git Bash.  
3. Run: `py main.py`

## 🔹 Screenshot

<img width="1896" height="839" alt="Screenshot 2025-11-24 214817" src="https://github.com/user-attachments/assets/33efb9c1-8735-4acd-b281-8ae80fda20ac" />
<img width="1893" height="171" alt="Screenshot 2025-11-24 214856" src="https://github.com/user-attachments/assets/7ac8e06e-5f44-449a-bfd9-5d9019788a76" />


 
