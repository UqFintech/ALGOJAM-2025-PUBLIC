import numpy as np

# Custom trading Algorithm
class Algorithm():

    ########################################################
    # NO EDITS REQUIRED TO THESE FUNCTIONS
    ########################################################
    # FUNCTION TO SETUP ALGORITHM CLASS
    def __init__(self, positions):
        # Initialise data stores:
        # Historical data of all instruments
        self.data = {}
        # Initialise position limits
        self.positionLimits = {}
        # Initialise the current day as 0
        self.day = 0
        # Initialise the current positions
        self.positions = positions
    # Helper function to fetch the current price of an instrument
    def get_current_price(self, instrument):
        # return most recent price
        return self.data[instrument][-1]
    ########################################################

    # RETURN DESIRED POSITIONS IN DICT FORM
    def get_positions(self):
        # Get current position
        currentPositions = self.positions
        # Get position limits
        positionLimits = self.positionLimits
        
        # Declare a store for desired positions
        desiredPositions = {}
        # Loop through all the instruments you can take positions on.
        for instrument, positionLimit in positionLimits.items():
            # For each instrument initilise desired position to zero
            desiredPositions[instrument] = 0

        # IMPLEMENT CODE HERE TO DECIDE WHAT POSITIONS YOU WANT 
        #######################################################################
        # Buy dawg food, chicken and spices, at their maximum amount
        trade_ins = ["Dawg Food", "Raw Chicken", "Secret Spices"]
        if self.day > 2:
            for ins in trade_ins:
                # if price has gone down buy
                if self.data[ins][-2] > self.data[ins][-1]:
                    desiredPositions[ins] = positionLimits[ins]
                    desiredPositions[ins] = 0
                else:
                    desiredPositions[ins] = -positionLimits[ins]

        print("day", self.day)

        #######################################################################
        # Return the desired positions
        return desiredPositions
