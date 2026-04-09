MINI PROJECT SUBMISSION DETAILS

Student Name: ALOK KUMAR
Enrollment Number: 92400527276
Project Title: Free Fire 2D Arena
Project Category: Python Mini Project
Project Type: 2D Action Game with SQLite Database

INTRODUCTION
Free Fire 2D Arena is a Python based mini project developed using the Pygame library. This project is inspired by battle royale style gameplay where the player enters an arena, fights enemy bots, collects loot, survives the shrinking safe zone and tries to achieve the highest possible score. The project also includes a SQLite database to store important records and game progress related information.

OBJECTIVE OF THE PROJECT
The main objective of this project is to design and develop an interactive 2D game using Python. The project demonstrates the practical use of programming concepts such as game loops, collision detection, event handling, object management, artificial enemy behavior, file handling and database integration. It is prepared as a mini project submission for academic evaluation.

PROJECT DESCRIPTION
In this game, the player controls a character inside a combat arena. The player can move in different directions, aim using the mouse and fire different types of weapons. Enemy bots attack the player and move dynamically in the arena. Loot items like ammo, medkits and armor are scattered or dropped during gameplay. A shrinking zone creates pressure on the player to keep moving and survive inside the safe area. At the end of each match, game statistics are recorded inside the database.

MAIN FEATURES OF THE PROJECT
- Real time player movement using keyboard controls
- Mouse based aiming and firing mechanism
- Multiple guns with different speed, damage, spread, magazine and reload timing
- Enemy AI for chasing, strafing and attacking the player
- Safe zone system that shrinks over time
- Loot collection system for ammo, medkits and armor
- Health and armor system
- Mini map for area awareness
- HUD for live display of score, level, ammo, time and stats
- Kill feed and end match summary
- Persistent SQLite database support
- Match history and career statistics storage

TOOLS AND TECHNOLOGIES USED
- Python
- Pygame
- SQLite
- Microsoft Word document for project report
- PDF document for final submission

DATABASE INFORMATION
Database File Name: game_data.db

The SQLite database is used to save the following data:
- High score
- Number of matches played
- Number of wins
- Total kills
- Total damage dealt
- Total damage taken
- Best level reached
- Best survival time
- Match history records

The database helps make the project more realistic because the player data remains available even after closing and reopening the game.

PROJECT FILE STRUCTURE
1. documents
   - Python_Game.docx
   - Python_Game.pdf

2. code
   - main.py
   - database.py
   - highscore.txt
   - images folder
   - sounds folder

3. database
   - game_data.db

4. README.txt

DETAILS OF IMPORTANT FILES
- main.py
  This is the main game file. It contains the game window setup, player controls, enemy AI, map drawing, HUD rendering, bullet logic, loot system, safe zone logic and match handling.

- database.py
  This file contains the code required for database connection, table creation, data loading and match record storage. It manages all SQLite operations of the project.

- game_data.db
  This is the SQLite database file in which the project stores persistent game records.

- Python_Game.docx
  This is the project document/report prepared in Word format.

- Python_Game.pdf
  This is the PDF version of the project report prepared for submission.

HOW TO RUN THE PROJECT
1. Install Python 3 on the system.
2. Open terminal or command prompt in the project code folder.
3. Install pygame if it is not already installed by using:
   pip install pygame
4. Run the following command:
   python main.py

GAME CONTROLS
- Move Up: W or Up Arrow
- Move Down: S or Down Arrow
- Move Left: A or Left Arrow
- Move Right: D or Right Arrow
- Shoot: Left Mouse Button
- Reload Gun: R
- Use Medkit: H
- Pause Game: P
- Select Guns: Keys 1 to 5

GAMEPLAY FLOW
1. Start the game from the main menu.
2. Enter the arena and move around to survive.
3. Collect loot items to increase survival chances.
4. Fight enemy bots using different guns.
5. Stay inside the shrinking zone.
6. Eliminate enemies and increase score.
7. At the end of the match, the game saves the result in the database.

EDUCATIONAL VALUE OF THE PROJECT
This project is useful for understanding:
- Python programming fundamentals
- Game development basics
- Sprite handling and rendering
- Keyboard and mouse event management
- Collision detection
- Data persistence using SQLite
- Modular programming structure
- Project packaging and documentation

CONCLUSION
Free Fire 2D Arena is a complete Python mini project that combines game development with database integration. It is interactive, visually improved and practically useful for demonstrating programming, logic building and data management concepts. The project contains source code, supporting assets, database file and documentation required for mini project submission.

SUBMISSION NOTE
This package includes the source code, database, document files and README as required for final mini project submission.
