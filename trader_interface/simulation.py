# Library Imports
import os
import pandas as pd
from algorithm import Algorithm
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
from matplotlib.gridspec import GridSpec
import math

##############################
# Define constants
##############################
# PRODUCTS AND THEIR INDIVIDUAL BUDGETS IN $AUD
positionLimits = {
    "Fintech Token": 35,
    "Purple Elixir": 10000,
    "Quantum Universal Algorithmic Currency Koin": 40000,
    "Dawg Food": 400,
    "UQ Dollar": 650,
    "Fried Chicken": 30000,
    "Secret Spices": 200,
    "Goober Eats": 75000, 
    "Raw Chicken": 2500,
    "Rare Watch": 250,    
}
# TOTAL DAILY BUDGET IN $AUD
totalDailyBudget = 600000
##############################

# Trading Engine Class, Controlling Trades Tracking
class TradingEngine:
    def __init__(self, dataFolder='./data/'):
        # Init variables
        self.dataFolder = dataFolder
        # Store active positions
        self.positions = {}
        # Position Limits
        self.positionLimits = positionLimits
        # Daily return history of each instrument
        self.returnsHistory = {}
        # Instrument cumulative returns history
        self.cumulativeReturnsHistory = {}
        # Store position as % of limit for graphing
        self.pcPositionHistorys = {}
        # Daily return history of combined instruments
        self.totalReturnHistory = []
        # Cumulative historical value of combined instruments
        self.totalValueHistory = []
        # Total days in simulation
        self.totalDays = 0
        # Track total PNL across all instruments
        self.totalPNL = 0
        # Track pc of total budget used daily
        self.pcTotalBudget = []
        # Setup functions
        self.load_data()
        self.initialize_positions()
        

    # For loading in relevant data from .CSV Files
    def load_data(self):
        self.data = {}
        for file in os.listdir(self.dataFolder):
            if file.endswith('_price_history.csv'):
                instrumentName = file.split('_')[0]
                if instrumentName in positionLimits.keys():
                    filePath = os.path.join(self.dataFolder, file)
                    self.data[instrumentName] = pd.read_csv(filePath)
                else:
                    print(f"No position limit set for {instrumentName}. This dataset will not be loaded.")
        # Ensure that all data have same length of days
        numDays = len(self.data[list(self.data.keys())[0]])
        print(f"Expected number of days: {numDays}")
        for instrument, data in self.data.items():
            if len(data) != numDays:
                print(f"Mismatch found for {instrument}: has {len(data)} days instead of {numDays}")
        print("Continuing with dataset verification...")
        for data in self.data.values():
            # if a dataset has a different number of days, exit
            if len(data) != numDays:
                print("\nError, not all datasets are the same length.\bExiting...")
                exit(1)
        # Otherwise, all data should have the same number of days.
        self.totalDays = numDays
        print("Datasets loaded successfully.")

    # Set initial positions to 0 for each
    def initialize_positions(self):
        for instrument in positionLimits: 
            self.positions[instrument] = 0
            self.returnsHistory[instrument] = []
            self.cumulativeReturnsHistory[instrument] = []
            self.pcPositionHistorys[instrument] = []

    # Helper function to check that a given order is within the daily budget.
    # Also records the total utilisation of the daily budget.
    def notWithinBudget(self, desiredPositions, priceHistory):
        # calc total value of positions
        totVal = 0
        for instrument, history in priceHistory.items():
            pos = desiredPositions[instrument]
            price = history[-1]
            value = abs(pos*price)
            totVal += value
        # if the budget is exceeded
        if totVal > totalDailyBudget:
            print("#########")
            print(f"Over budget by ${totVal-totalDailyBudget}.")
            # display values of each instrument position.
            for instrument, prcHistory in priceHistory.items():
                pos = desiredPositions[instrument]
                price = prcHistory[-1]
                value = abs(pos*price)
                totVal += value
                print(f"{instrument} position value: ${value}.")
            print("#########")
            # record zero as daily position used of budget, as position will be reset to zero
            self.pcTotalBudget.append(0)
            # return true, as desired position not within budget.
            return True
        # within daily budget, so record % usage
        pcBudgetUsage = round(totVal*100/totalDailyBudget,2)
        self.pcTotalBudget.append(pcBudgetUsage)
        # return false, as within the daily budget
        return False

    # Process submitted algorithm
    def run_algorithms(self, algorithmsInstance):
        # Loop through each day of data (leaving the last)
        for day in range(self.totalDays -1 ):
            # Get current data history at this point in time
            historicalData = {}
            for instrument, priceData in self.data.items():
                # Fetch all relevant data
                priceHistory = priceData['Price'][:day+1].tolist()
                # Add them to the historicalData store
                historicalData[instrument] = priceHistory     
            # Update the algorithms instance with the new information
            algorithmsInstance.day = day
            algorithmsInstance.data = historicalData
            algorithmsInstance.positions = self.positions
            algorithmsInstance.positionLimits = self.positionLimits
            # Now get the desired positions from the competitors algorithm
            desiredPositions = algorithmsInstance.get_positions()
            
            # Check if the desired positions are within total budget
            if self.notWithinBudget(desiredPositions, historicalData):
                # Set all desired positions to zero
                for instrument in desiredPositions.keys():
                    desiredPositions[instrument] = 0
                print(f"REQUESTED POSIITONS EXCEED DAILY BUDGET OF: ${totalDailyBudget}.")
                print(f"SET ALL DESIRED POSITIONS FOR DAY {day} TO ZERO.")
                
            # Store total return for the day
            dailyReturn = 0
            # Process profit/loss for each instrument:
            for instrument, priceData in self.data.items():
                # Perform desired position quality checks (int and within limits)
                if (type(desiredPositions[instrument]) != type(1) or # not an int
                        abs(desiredPositions[instrument]) > self.positionLimits[instrument] # not within limits
                        ):
                    # Incorrect value provided. Skip
                    print(f"Position given for {instrument} on day {day} invalid.")
                    print(f"Position given was {desiredPositions[instrument]}.")
                    print(f"The limit for this instrument today is: {self.positionLimits[instrument]}")
                    print(f"Setting desired position to zero units.")
                    # Set zero
                    desiredPositions[instrument] = 0
                # Calculate PNL if not day 0
                if day != 0:
                    existingPosition = self.positions[instrument]
                    currPrice = priceData["Price"][day]
                    lastPrice = priceData["Price"][day-1]
                    instrumentPNL = existingPosition * (currPrice - lastPrice)
                    instrumentPNL = quantize_decimal(instrumentPNL, 2)
                    self.returnsHistory[instrument].append(instrumentPNL)
                    self.cumulativeReturnsHistory[instrument].append(
                        instrumentPNL + self.cumulativeReturnsHistory[instrument][-1]
                    )
                    # add it to the daily return
                    dailyReturn += instrumentPNL
                else:
                    # No trades executed first day
                    self.returnsHistory[instrument].append(0)
                    self.cumulativeReturnsHistory[instrument].append(0)
            # Store positions in historical tracker for graphing
            for instrument, desiredPosition in desiredPositions.items():
                self.pcPositionHistorys[instrument].append(round(desiredPosition*100/self.positionLimits[instrument]))
            # Add the daily return to the tracker
            self.totalReturnHistory.append(dailyReturn)
            # Update total PNL
            self.totalPNL += dailyReturn
            # Display PNL
            print(f"Total PNL @ Day {day}: {self.totalPNL}")
            # Update total Value
            self.totalValueHistory.append(self.totalPNL)
            # Update simluator information
            self.positions = desiredPositions
            

    def plot_returns(self):
        # Set figure size
        fig = plt.figure(figsize=(16, 9))
        gs = GridSpec(16, 16, figure=fig)
        # Adjust spacing between subplots
        fig.subplots_adjust(wspace=10, hspace=10)
        ax1 = fig.add_subplot(gs[:8, 8:])
        ax2 = fig.add_subplot(gs[8:12, 8:])
        ax3 = fig.add_subplot(gs[:8, :8])
        ax4 = fig.add_subplot(gs[12:, 8:])
        ax5 = fig.add_subplot(gs[8:, :8])
        # Print metrics
        print('#' * 50)
        print(f"Total PNL ($): {self.totalPNL}")
        print('#' * 50)
        for instrument, returns in self.cumulativeReturnsHistory.items():
            instrumentReturn = returns[-1]
            print(f"{instrument} Returns ($): {instrumentReturn}")
        print('#' * 50)
        # Store the lines for toggling visibility
        lines = []
        # Plot individual instrument returns
        for instrument, returns in self.cumulativeReturnsHistory.items():
            line, = ax1.plot(returns, label=instrument)
            lines.append(line)
            # Plot the point at the final value
            #ax1.scatter(len(returns) - 1, returns[-1], color='red', zorder=5)
            #ax1.annotate(f'{returns[-1]:.2f}', (len(returns) - 1, returns[-1]), textcoords="offset points", xytext=(0, 10), ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        legend1 = ax1.legend()
        ax1.set_title('Individual Instrument Cumulative P&L ($AUD)')
        # Plot historical instrument positions
        for instrument, returns in self.pcPositionHistorys.items():
            line, = ax4.plot(returns, label=instrument, linewidth=1, alpha=1)
            lines.append(line)
        ax4.set_title(r'Historical Instrument Position (% of limit)')
        # Plot total return history
        line, = ax3.plot(self.totalValueHistory, label='Total Return', color='black')
        lines.append(line)
        # Plot a point at the final value of total return
        ax3.scatter(len(self.totalValueHistory) - 1, self.totalValueHistory[-1], color='red', zorder=5)
        ax3.annotate(f'{self.totalValueHistory[-1]:.2f}', (len(self.totalValueHistory) - 1, self.totalValueHistory[-1]), textcoords="offset points", xytext=(0, 10), ha='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        legend3 = ax3.legend()
        ax3.set_title('Cumulative Profit & Loss ($AUD)')
        # Plot individual instrument historical P&L
        for instrument, returns in self.returnsHistory.items():
            line, = ax2.plot(returns, label=instrument)
            lines.append(line)
        ax2.set_title(r'Daily Individual P&L ($AUD)')
        # Plot daily budget usage graph
        line, = ax5.plot(self.pcTotalBudget, label='Budget Utilisation', color='black')
        ax5.set_title('Percentage of Total Daily Limit Utilised (%)')
        ax5.set_ylim(0, 100)
        # Handle picking legend options
        def on_pick(event):
            legend_item = event.artist
            is_visible = not legend_item.get_visible()
            legend_item.set_visible(is_visible)
            
            for orig_line in lines:
                if legend_item.get_label() == orig_line.get_label():
                    orig_line.set_visible(is_visible)
            
            fig.canvas.draw()
        # Enable picking on legend items
        for legend in [legend1, legend3]:
            for legend_item in legend.get_lines():
                legend_item.set_picker(True)
        # Connect the pick event
        fig.canvas.mpl_connect('pick_event', on_pick)
        # Save the figure
        output_dir = './simulation_results'
        os.makedirs(output_dir, exist_ok=True)
        fig.savefig(os.path.join(output_dir, 'returns_plot.png'), dpi=300)
        plt.show()
        plt.close(fig)

        

# Function to round a float
def quantize_decimal(value, decimal_places=2):
    decimal_value = Decimal(value)
    if decimal_value % 1 == 0:  # Check if the number is an integer
        return decimal_value.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    else:  # For non-integers, round to the specified decimal places
        rounding_format = '1.' + '0' * decimal_places
        return decimal_value.quantize(Decimal(rounding_format), rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    engine = TradingEngine()
    algorithmInstance = Algorithm(engine.positions)
    engine.run_algorithms(algorithmInstance)
    engine.plot_returns()

