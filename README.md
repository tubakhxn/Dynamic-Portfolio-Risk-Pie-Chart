
# Dynamic Portfolio Risk Contribution Pie Chart

## dev/creator = tubakhxn

## What is this project about?
This project is a beginner-friendly Python app that visualizes how each asset in a portfolio contributes to overall risk (volatility) in real time. It simulates synthetic returns for several assets, calculates their risk contributions, and displays them in an animated, interactive pie chart. Users can adjust asset weights with sliders and instantly see the impact on portfolio risk.

**Relevant Wikipedia links:**
- [Portfolio (finance)](https://en.wikipedia.org/wiki/Portfolio_(finance))
- [Risk (finance)](https://en.wikipedia.org/wiki/Risk)
- [Volatility (finance)](https://en.wikipedia.org/wiki/Volatility_(finance))
- [Pie chart](https://en.wikipedia.org/wiki/Pie_chart)

## How to fork this project
1. On GitHub, click the **Fork** button at the top right of the repository page.
2. Clone your fork to your local machine:
   ```sh
   git clone https://github.com/your-username/Dynamic-Portfolio-Contribution-Pie-Chart.git
   ```
3. Install dependencies and run as described below.


## Features
- Simulates 3–5 assets with synthetic returns
- Calculates each asset's contribution to total portfolio volatility
- Animated pie chart visualizes risk contributions
- Interactive sliders to adjust asset weights
- Real-time, smooth chart updates
- Beginner-friendly, modular code with comments
- Auto-installs dependencies (numpy, matplotlib)


## Test Cases
- Run with default settings (4 assets, equal weights)
- Adjust sliders to set one asset to 100% weight (should show 100% risk from that asset)
- Set all weights to zero (should auto-normalize to equal weights)
- Try with different random seeds in `data_generator.py`


## Key Insight
Risk contribution is not always proportional to portfolio weight—assets with higher volatility or correlation can dominate risk even at low weights.


## How to Run
1. Install Python 3.7+
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   python src/main.py
   ```


## Output
- Animated pie chart showing each asset's risk contribution
- Sliders to interactively adjust portfolio weights


## Tech Stack
- Python
- numpy
- matplotlib


## Applications
- Portfolio management education
- Risk analysis demos
- Interactive finance teaching tools


## Future Improvements
- Add real financial data import
- Support for more assets and custom names
- Export results as images or CSV
- Add other risk measures (e.g., Value at Risk)
