# strategyGame
Software Engineering

**Structure Basics**
 The game is divided in two main files. Model, View, Controller. Methods from this classes are called in the class Game, adn Game is called in a loop inside of main. THe Game file can be elliminated in future version. It is only present in case something special wants to be done.
 
 **Model**
 
 - **run**
  Controlls the loop of the game.
  It is only changed when either quit is pressed in the menu stage or when the x at corned of the window is pressed.
 - **sprites**
  Array that contains the sprites to be desplayed by the View class.
  It's content is modified depending on the current stage of the game. So far there are only two stages defined and one array of sprites for each stage.
 
 **View**
 Class incharged of the rendering process. It uses the **sprites** array defined in model and calls the method **draw()** to perform this action.
 
 **Controller**
 Reads events from the pygame queue and calls functions from the **model** class to process them.
 
