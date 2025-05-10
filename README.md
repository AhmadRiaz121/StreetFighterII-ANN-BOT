# AI Game-Playing Bot using Supervised Learning

## Introduction

This project aims to develop an AI bot capable of playing a video game using an emulator. The bot is trained through supervised learning to detect the current game state (e.g., player positions, screen visuals) and decide the next appropriate action. The focus is on building and training a Multilayer Perceptron (MLP) model to perform this task using game data.

The game used for training is **Street Fighter II Turbo (U)**, played via the **BizHawk** emulator.

---

## Tools and Technologies Used

| Tool/Technology      | Purpose                                                      |
|----------------------|--------------------------------------------------------------|
| Python               | Programming language for implementation                      |
| BizHawk Emulator     | Game platform for training and testing                       |
| Artificial Neural Network | Machine learning model used to learn patterns             |
| Multilayer Perceptron (MLP) | Specific ANN model used for supervised learning         |
| TensorFlow Keras     | Framework for building and training the MLP model            |

---

## Project Objectives

- Build an AI bot that can learn and play a video game
- Collect and preprocess game data for training
- Train a predictive model to determine the next game move
- Test the bot in a simulated environment
- Explore AI applications in supervised learning scenarios

---

## Working Methodology

### 1. Game Setup
- Game: **Street Fighter II Turbo (U)** using BizHawk emulator
- Connected the emulator with a Python script through its API

### 2. Data Collection
- Played the game manually
- Captured frame-by-frame data (player positions, health, moves, button presses)
- Stored data in `GameData.csv`

### 3. Data Preprocessing
- Removed unnecessary columns
- Engineered features like `x_diff` and `y_diff` to represent distance between players
- Normalized data using `StandardScaler`
- Performed an 80/20 train-test split

### 4. Model Training
- Model: **Multilayer Perceptron (MLP)**
- Architecture:
  - Input Layer: Normalized feature vectors
  - Hidden Layers: Two dense layers with 64 ReLU-activated neurons
  - Output Layer: 10 sigmoid-activated neurons (one per Player 2 button)
- Loss Function: Mean Squared Error (MSE)
- Optimizer: Adam
- Training: 1000 epochs, batch size of 32
- Saved model as `BotModel.h5` and scaler for later use

---

## Challenges Faced

- **Data Diversity**: Initial dataset was repetitive and caused overfitting
- **Prediction Accuracy**: Bot behavior was erratic and unrealistic during gameplay

### Solutions
- Recollected a more diverse dataset by including varied game states (attacking, jumping, blocking, retreating)
- Enhanced feature engineering
- Removed noisy data to improve generalization

---

## Results and Observations

- Post-retraining, the bot displayed more intelligent behaviors:
  - Jumped, attacked, and retreated based on opponent positioning
  - Executed complex multi-button moves
  - Mimicked human-like gameplay
- Inclusion of `x_diff`, `y_diff`, and other engineered features improved model performance
- Achieved high prediction accuracy on test data and live gameplay

---

## Conclusion

This project successfully demonstrates how supervised learning can be applied to simulate game-playing AI. Despite the absence of a reward-based reinforcement mechanism, the trained bot performed rationally by reacting to game states. The experience highlighted the importance of good data collection, feature engineering, and model tuning in building AI that can mimic human behavior in dynamic environments.