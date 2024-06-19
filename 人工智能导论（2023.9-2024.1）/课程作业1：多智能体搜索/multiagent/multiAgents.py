# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        # choose legal move
        legalMoves = gameState.getLegalActions()
        # choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        # get the best score
        bestScore = max(scores)
        # get the index of the best score
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        # choose randomly among the best
        chosenIndex = random.choice(bestIndices)

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Initialize a base score using the game score
        score = successorGameState.getScore()

        # Calculate the distance to the closest food pellet
        min_food_distance = float('inf')
        for food in newFood.asList():
            distance = util.manhattanDistance(newPos, food)
            if distance < min_food_distance:
                min_food_distance = distance

        # Consider the proximity of ghosts and their scared times
        ghost_score = 0
        for i, ghost_state in enumerate(newGhostStates):
            ghost_pos = ghost_state.getPosition()
            ghost_distance = util.manhattanDistance(newPos, ghost_pos)
            if newScaredTimes[i] > 0:
                #If Pacman can eat the ghost, increase the score
                ghost_score += 100.0 / (ghost_distance + 1)
            else:
                # If a ghost is too close, decrease the score significantly
                if ghost_distance < 2:
                    ghost_score -= 1000.0
                else:
                    # Otherwise, slightly penalize for being near a ghost
                    ghost_score -= 10.0 / (ghost_distance + 1)

        # Combine the base score, food distance, and ghost score
        total_score =  score + 10.0 / (min_food_distance + 1) + ghost_score

        return total_score

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState: GameState):
        maxVal = -float('inf')
        bestAction = None
        for action in gameState.getLegalActions(0):
            value = self.getMin(gameState.generateSuccessor(0, action), 0, 1)
            if value > maxVal:
                maxVal = value
                bestAction = action
        return bestAction

    def getMax(self, gameState, depth, agentIndex):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        maxVal = -float('inf')
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents() - 1:
                value = self.getMin(gameState.generateSuccessor(agentIndex, action), depth + 1, 0)
            else:
                value = self.getMin(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
            maxVal = max(maxVal, value)
        return maxVal

    def getMin(self, gameState, depth, agentIndex):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        minVal = float('inf')
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents() - 1:
                value = self.getMax(gameState.generateSuccessor(agentIndex, action), depth + 1, 0)
            else:
                value = self.getMin(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
            minVal = min(minVal, value)
        return minVal


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        maxVal, bestAction = self.getMax(gameState)
        return bestAction

    def getMax(self, gameState, depth=0, agentIndex=0, alpha=-float('inf'), beta=float('inf')):
        # 达到搜索深度
        if depth == self.depth:
            return self.evaluationFunction(gameState), None
        # 不合法
        if len(gameState.getLegalActions(agentIndex)) == 0:
            return self.evaluationFunction(gameState), None
        # 获得吃豆人的所有合法操作，并进行遍历
        maxVal = -float('inf')
        bestAction = None
        for action in gameState.getLegalActions(agentIndex):
            # 计算幽灵
            value, _ = self.getMin(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1, alpha, beta)
            if value > maxVal:
                maxVal = value
                bestAction = action
            if maxVal > beta:
                return maxVal, bestAction
            alpha = max(alpha, maxVal)
        return maxVal, bestAction

    def getMin(self, gameState, depth=0, agentIndex=1, alpha=-float('inf'), beta=float('inf')):
        if depth == self.depth:
            return self.evaluationFunction(gameState), None
        if len(gameState.getLegalActions(agentIndex)) == 0:
            return self.evaluationFunction(gameState), None
        minVal = float('inf')
        bestAction = None
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents() - 1:
                value = self.getMax(gameState.generateSuccessor(agentIndex, action), depth + 1, 0, alpha, beta)[0]
            else:
                value = \
                    self.getMin(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1, alpha, beta)[0]
            if value < minVal:
                minVal = value
                bestAction = action
            # 剪枝操作
            if value < alpha:
                return value, action
            beta = value if value < beta else beta
        return minVal, bestAction

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        maxVal, bestAction = self.getMax(gameState)
        return bestAction

    def getMax(self, gameState, depth=0, agentIndex=0):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        maxVal = -float('inf')
        bestAction = None
        for action in gameState.getLegalActions(agentIndex):
            value, _ = self.getExpectation(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)
            if value > maxVal:
                maxVal = value
                bestAction = action
        return maxVal, bestAction

    def getExpectation(self, gameState, depth=0, agentIndex=1):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        legalActions = gameState.getLegalActions(agentIndex)
        numActions = len(legalActions)
        expectation = 0.0

        for action in legalActions:
            if agentIndex == gameState.getNumAgents() - 1:
                value, _ = self.getMax(gameState.generateSuccessor(agentIndex, action), depth + 1, 0)
            else:
                value, _ = self.getExpectation(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1)

            expectation += value / numActions

        return expectation, None


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).
    """
    # Extract relevant information from the game state
    pacmanPosition = currentGameState.getPacmanPosition()
    foodGrid = currentGameState.getFood()
    ghostStates = currentGameState.getGhostStates()
    capsules = currentGameState.getCapsules()

    # Calculate the distance to the nearest food
    foodDistances = [manhattanDistance(pacmanPosition, food) for food in foodGrid.asList()]
    minFoodDistance = min(foodDistances) if foodDistances else 0

    # Calculate the distance to the nearest ghost
    ghostDistances = [manhattanDistance(pacmanPosition, ghost.getPosition()) for ghost in ghostStates]
    minGhostDistance = min(ghostDistances) if ghostDistances else 0

    # Calculate the distance to the nearest capsule (power pellet)
    capsuleDistances = [manhattanDistance(pacmanPosition, capsule) for capsule in capsules]
    minCapsuleDistance = min(capsuleDistances) if capsuleDistances else 0

    # Calculate the remaining number of food dots
    numFoodLeft = len(foodGrid.asList())

    # Calculate the score of the current game state
    score = currentGameState.getScore()

    # Define weights for different factors
    foodWeight = 1
    ghostWeight = 10
    capsuleWeight = 5

    # Calculate the overall evaluation function
    evaluation = score - foodWeight * minFoodDistance - ghostWeight * minGhostDistance - capsuleWeight * minCapsuleDistance - numFoodLeft

    return evaluation

# Abbreviation
better = betterEvaluationFunction