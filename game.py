#!/bin/python

from player import Player
import logging
from random import shuffle
global logger
logger = logging
logger.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='molkky.log', level=logging.DEBUG)

class Game(object):
  def __init__(self, players):
    logger.debug("initialisation of Game")
    if isinstance(players, list):
      self.players = players
    else:
      raise("wrong instanciation")
    self.game = dict() 
    self.randomise_player()
    self.game_engine()  

  def randomise_player(self):
    logger.info("radomisation of player")
    logger.debug("list player before: {}".format(self.players))
    shuffle(self.players)
    logger.debug("list player after: {}".format(self.players))
    self.new_game()

  def new_game(self):
    logger.info("instanciation of new dictionnary game")
    for person in self.players:
      self.game[person] = {'score':0, 'try':0}


  def calculate_pins(self, pin):
    logger.debug("define what was scored")
    if len(pin) is 1:
      return pin[0]
    else:
      return len(pin)

  def same_score(self, player):
    logger.info("check if same score as another player")
    self.game[player]
    print(self.game)
    test_score = self.game.copy()
    test_score.pop(player)
    print(self.game)
    for p in test_score:
      print(self.game[p])
      if self.game[player]['score'] is self.game[p]['score']:
        if int(self.game[p]['score']) >= 25:
          self.game[p]['score'] = 25
        else:
          self.game[p]['score'] = 0
        print("{} has same score as {}, {} fall back to {}".format(player.name, p.name, p.name, self.game[p]['score']))

  def game_engine(self):
    logger.debug("start of engine")
    while 1:
      for player in self.players:
        pin=input("{} turn:\n which pin fell?\n".format(player.name)).split()
        if all(i > 12 and i <0 for i in pin) and len(pin) > 12:
          pin=input("wrong insertion...\n {} turn:\n which pin fell?\n".format(player.name)).split()       
        
        logger.debug("pin {} fell".format(pin))
        if not pin  and self.game[player]['try'] is 3:
          print("third try without scoring, {} fall back to 0".format(player.name))
          self.game[player]['try'] = 0
          self.game[player]['score'] = 0
        elif not pin:
          self.game[player]['try'] += 1
          logger.debug("the player {} made {} consecutive time 0".format(player.name, self.game[player]['try']))
          continue
      
        logger.debug("calculate new score of player {}".format(player.name)) 
        self.game[player]['score'] = self.game[player]['score'] + int(self.calculate_pins(pin))
        
        logger.debug("check if 50 is reach")
        if int(self.game[player]['score']) is 50:
          self.end_of_game(player)
       
        elif int(self.game[player]['score']) > 50:
          logger.debug("50 overreach fall back to zero")
          self.game[player]['score'] = 25
 
        self.same_score(player)
        logger.info("next player")
        
 
  def end_of_game(self, player):
    print("Player {} won!".format(player.name))
    exit(0)
