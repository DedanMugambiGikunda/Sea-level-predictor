import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["year"]
    y = df["CSIRO Adjustment Sea level"]

    fig, ax = plt.subplots(figsize = (12,12))
    ax = plt.scatter(x,y)

    # Create first line of best fit
    reg = linregress(x,y)
    print(reg)
    x_forcast = pd.series(([1 for 1 in range(1850,2051)]))
    y_forcast = reg.slope * x_forcast + reg_intercept
    plt.plot(x_forcast, y_forcast, 'r-')

    df_forc = df.loc[df["year"] >= 2000]
    new_x = df_forc["year"]
    new_y = df_forc["CSIRO Adjusted Sea Level"]


    # Create second line of best fit
    new_reg = linregress(new_x, new_y)
    new_x forecast = pd.series(([1 for 1 in range(2000, 2051)]))
    new_y forecast = new.reg.slope*new_x_forecast + new_reg.intercept
    plt.plot(new_x_forecast, new_y_forecast, 'orange')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea level(inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot