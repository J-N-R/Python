# IsCovidNearMe.py
#
# Description:
#    An application that allows a user to input their State and County, and instantly get results.
#
# Notes:
#    The GUI uses John Zelle's graphics.py Tkinter wrapper, found here: https://mcsp.wartburg.edu/zelle/python/graphics.py
#    The inputs are case insensitive and do not have to be exact, but avoid using state abbreviations.
#
#    Example:
#       County: union   State: new jersey  (Good)
#       County: union   State: new         (Good, though the computer will pick which state it thinks fits best)
#       County: union   State: NJ          (BAD. May go through, but accurate results not guarenteed)
#
# Made by: 
#   rivejona@kean.edu
#

import pandas as pd
from graphics import *
from datetime import datetime as dt, timedelta

# Clear the window. Good for changing from one window to another.
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    return


# Go to github and retrieve covid data. If this fails, it will create a critical error.
def read_csv():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv'

    return pd.read_csv(url, error_bad_lines=False)


# Search a given dataframe for state and county
def search(df, state, county):
    
    return df.loc[(df["state"].str.contains(state, case=False)) & (df["county"].str.contains(county, case=False))]


# Test if a click happened inside a given rectangle. This allows us to make buttons
def isInside(mouse, rectangle):
    point1 = rectangle.getP1() # Upper Left
    point2 = rectangle.getP2() # Lower Right

    # return true if mouse was inside, false if not
    return point1.getX() <= mouse.getX() <= point2.getX() and point1.getY() <= mouse.getY() <= point2.getY()


# Open the main search window
def openSearchWindow(win):
    clear(win)

# DRAW ALL WINDOW FEATURES (Text, Buttons, ETC)
  # Create new text labels
    introLabel  = Text(Point(width/2, height/8),       "Is Covid near you?")
    intro2Label = Text(Point(width/2, height/3.75),    "Input your state and county.")
    stateLabel  = Text(Point(width/1.5, height/1.58),   "State")
    countyLabel = Text(Point(width/3.25, height/1.58),  "County")
    checkLabel  = Text(Point(width/2.07, height/1.135),"Check")

  # Create new text Entries
    stateEntry  = Entry(Point(width/1.5, height/1.95),  15)
    countyEntry = Entry(Point(width/3.22, height/1.95), 15) 

  # Create Buttons
    checkButton = Rectangle(Point(width/2.75, height/1.25), Point(width/1.65, height/1.05))
    checkButton.setFill("light grey")

  # Edit Element Sizes, set styles, etc
    introLabel. setSize(25)
    intro2Label.setSize(25)
    stateLabel. setSize(25)
    countyLabel.setSize(25)
    checkLabel .setSize(25)
    stateEntry .setSize(15)
    countyEntry.setSize(15)

    stateEntry .setFill("white")
    countyEntry.setFill("white")
    stateEntry .setStyle("bold")
    countyEntry.setStyle("bold")

  # Draw all creations to the window we created
    checkButton.draw(win)
    introLabel. draw(win)
    intro2Label.draw(win)
    stateLabel. draw(win)
    countyLabel.draw(win)
    checkLabel .draw(win)
    stateEntry. draw(win)
    countyEntry.draw(win)

  # While waiting for input, download the data! This masks the loading time.
    try:
        df = read_csv()

      # If the "Check" button is pressed, try searching with the set State and County.
        while True:
            mouse = win.getMouse()

            if mouse is None:
                continue

            elif isInside(mouse, checkButton):
                checkButton.setFill('grey')
                state  = stateEntry .getText()
                county = countyEntry.getText()

                results = search(df, state, county)
                return openResultsWindow(win, results, 0, state, county)

            else:
                continue


    except:
        return openResultsWindow(win, 0, True)


# Open results window. Will display if there was a success, critical error, or no results.
def openResultsWindow(win, results, error = False, state = None, county = None):
    clear(win)

    if error or results.empty:  # If there was no results or there was an error
        if error:
          # Create Critical Error specific texts and draw them
            errorLabel = Text(Point(width/2, height/4), "There was a critical error.")
            errorLabel.setSize(30)
            errorLabel.draw(win)

            contactDevLabel = Text(Point(width/2, height/1.25), "If this continues,\nplease contact the developer.")
            contactDevLabel.setSize(15)
            contactDevLabel.draw(win)

        elif results.empty:
          # Create Empty Result specific texts and draw them
            noresultsLabel = Text(Point(width/2, height/3.75), "There were no results.")
            noresultsLabel.setSize(30)
            noresultsLabel.draw(win)

            givenStateLabel = Text(Point(width/2, height/16), "For '" + state + "' state, '" + county + "' county,")
            givenStateLabel.setSize(15)
            givenStateLabel.draw(win)

            differentNameLabel = Text(Point(width/2, height/1.25), "Try again\nwith different names.")
            differentNameLabel.setSize(15)
            differentNameLabel.draw(win)

      # Create Generic Error texts / try again button and draw them to the screen
        checkButton = Rectangle(Point(width/4, height/2.1), Point(3*width/4, height/1.6))
        tryAgainLabel = Text(Point(width/2, height/1.82), "Try Again")

        checkButton.setFill("light grey")
        tryAgainLabel.setSize(25)
        tryAgainLabel.setStyle('bold')

        checkButton.draw(win)
        tryAgainLabel.draw(win)

      # If the user clicks on 'try again,' bring them back to the first window.
        while True:
            mouse = win.getMouse()

            if mouse is None:
                continue

            elif isInside(mouse, checkButton):
                checkButton.setFill("grey")

                return openSearchWindow(win)

            else:
                continue
        
        return

    else: # Result found! Print out successful result menu

      # Capitalize / Display state and county names properly by grabbing the real name from the database.
        state = results.iloc[0]['state']
        county = results.iloc[0]['county']

      # Create Text Labels
        string = "For your state of " + state + ","
        stateLabel = Text(Point(width/2, height/10), string)

        preResultsLabel = Text(Point(width/2, height/4.25), "There were...")

        string = str(results.iloc[0]['cases']) + "       " + str(int(results.iloc[0]['deaths']))
        resultsLabel = Text(Point(width/2.05, height/2.05), string)

        casesLabel = Text(Point(width/3.5, height/1.55), "Cases")
        deathsLabel = Text(Point(width-width/3.5, height/1.55), "Deaths")

        string = "In " + county + " county."
        countyLabel = Text(Point(width/2, height/1.2), string)

        string = "(As of: " + results.iloc[0]['date'] + ")"
        dateLabel = Text(Point(width/2, height/1.05), string)

        tryAgainLabel = Text(Point(width/8.125, height/1.14), "Try\nAgain")

      # Create Button for trying again
        checkButton = Rectangle(Point(width/20, height/1.25), Point(width/5, height/1.05))

      # Set Label Sizes and Styles
        resultsLabel.setStyle("bold")
        dateLabel.setStyle("bold")

        stateLabel.setSize(25)
        preResultsLabel.setSize(25)
        resultsLabel.setSize(35)
        casesLabel.setSize(25)
        deathsLabel.setSize(25)
        countyLabel.setSize(25)
        tryAgainLabel.setSize(15)
        dateLabel.setSize(10)

        checkButton.setFill('light grey')

      # Draw all objects to the screen
        stateLabel.draw(win)
        preResultsLabel.draw(win)
        resultsLabel.draw(win)
        casesLabel.draw(win)
        deathsLabel.draw(win)
        countyLabel.draw(win)
        dateLabel.draw(win)
        checkButton.draw(win)
        tryAgainLabel.draw(win)
        

        while True:
            mouse = win.getMouse()

            if mouse is None:
                continue

            elif isInside(mouse, checkButton):
                checkButton.setFill('grey')

                return openSearchWindow(win)

            else:
                continue


# Window Size
width  = 500      # originally 600 by 400
height = 300

# Create new Window
win = GraphWin("Is Covid Near Me?", width, height)
openSearchWindow(win)