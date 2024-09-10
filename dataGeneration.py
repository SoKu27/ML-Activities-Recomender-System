import numpy as np
import pandas as pd
import random

samples = 10000

def datalistcreation():
    activities = activitiesDict[random.randint(1, 51)]
    activities2 = activitiesDict[random.randint(1, 51)]

    if ("Learn to play a new musical instrument" in activities or "Learn to play a new musical instrument" in activities2):
        learn_to_play_a_new_musical_instrument.append(1)
    else:
        learn_to_play_a_new_musical_instrument.append(0)
    if ("Take a beginner's coding class" in activities or "Take a beginner's coding class" in activities2):
        take_a_beginners_coding_class.append(1)
    else:
        take_a_beginners_coding_class.append(0)
    if ("Start a vegetable garden" in activities or "Start a vegetable garden" in activities2):
        start_a_vegetable_garden.append(1)
    else:
        start_a_vegetable_garden.append(0)
    if ("Learn a new language" in activities or "Learn a new language" in activities2):
        learn_a_new_language.append(1)
    else:
        learn_a_new_language.append(0)
    if ("Volunteer at a local animal shelter" in activities or "Volunteer at a local animal shelter" in activities2):
        volunteer_at_a_local_animal_shelter.append(1)
    else:
        volunteer_at_a_local_animal_shelter.append(0)
    if ("Take a dance class" in activities or "Take a dance class" in activities2):
        take_a_dance_class.append(1)
    else:
        take_a_dance_class.append(0)
    if ("Start a blog or vlog" in activities or "Start a blog or vlog" in activities2):
        start_a_blog_or_vlog.append(1)
    else:
        start_a_blog_or_vlog.append(0)
    if ("Learn to knit or crochet" in activities or "Learn to knit or crochet" in activities2):
        learn_to_knit_or_crochet.append(1)
    else:
        learn_to_knit_or_crochet.append(0)
    if ("Try a new cuisine" in activities or "Try a new cuisine" in activities2):
        try_a_new_cuisine.append(1)
    else:
        try_a_new_cuisine.append(0)
    if ("Take a photography class" in activities or "Take a photography class" in activities2):
        take_a_photography_class.append(1)
    else:
        take_a_photography_class.append(0)
    if ("Go on a solo camping trip" in activities or "Go on a solo camping trip" in activities2):
        go_on_a_solo_camping_trip.append(1)
    else:
        go_on_a_solo_camping_trip.append(0)
    if ("Learn to paint or draw" in activities or "Learn to paint or draw" in activities2):
        learn_to_paint_or_draw.append(1)
    else:
        learn_to_paint_or_draw.append(0)
    if ("Start a book club" in activities or "Start a book club" in activities2):
        start_a_book_club.append(1)
    else:
        start_a_book_club.append(0)
    if ("Take a pottery class" in activities or "Take a pottery class" in activities2):
        take_a_pottery_class.append(1)
    else:
        take_a_pottery_class.append(0)
    if ("Learn to play a board game" in activities or "Learn to play a board game" in activities2):
        learn_to_play_a_board_game.append(1)
    else:
        learn_to_play_a_board_game.append(0)
    if ("Start a home garden" in activities or "Start a home garden" in activities2):
        start_a_home_garden.append(1)
    else:
        start_a_home_garden.append(0)
    if ("Learn to play a card game" in activities or "Learn to play a card game" in activities2):
        learn_to_play_a_card_game.append(1)
    else:
        learn_to_play_a_card_game.append(0)
    if ("Take a calligraphy class" in activities or "Take a calligraphy class" in activities2):
        take_a_calligraphy_class.append(1)
    else:
        take_a_calligraphy_class.append(0)
    if ("Learn to bake bread" in activities or "Learn to bake bread" in activities2):
        learn_to_bake_bread.append(1)
    else:
        learn_to_bake_bread.append(0)
    if ("Take a DIY home improvement class" in activities or "Take a DIY home improvement class" in activities2):
        take_a_diy_home_improvement_class.append(1)
    else:
        take_a_diy_home_improvement_class.append(0)

activitiesDict = {
    1: "Learn to play a new musical instrument, Start a vegetable garden, Volunteer at a local animal shelter, Learn to knit or crochet, Take a photography class, Learn a new language",
    2: "Start a blog or vlog, Learn to play a new musical instrument, Start a vegetable garden, Take a beginner's coding class, Go on a solo camping trip, Take a photography class, Start a book club",
    3: "Learn to knit or crochet, Try a new cuisine, Take a beginner's coding class, Go on a solo camping trip, Take a photography class, Start a book club",
    4: "Go on a solo camping trip, Start a book club, Try a new cuisine, Start a vegetable garden, Take a DIY home improvement class, Take a photography class, Learn to paint or draw,",
    5: "Take a pottery class, Start a home garden Learn a new language, Start a vegetable garden, Learn to play a new musical instrument, Learn to play a board game, Take a dance class",
    6: "Learn to play a card game,Take a calligraphy class, Learn to bake bread, Learn to play a new musical instrument, Learn to play a board game, Take a dance class",
    7: "Learn to play a board game, Take a calligraphy class, Take a dance class, Learn to play a card game, Take a pottery class, Learn to bake bread, Take a photography class",
    8: "Learn to knit or crochet, Go on a solo camping trip, Take a photography class, Start a book club, Start a vegetable garden, Take a dance class",
    9: "Volunteer at a local animal shelter, Learn to knit or crochet, Take a photography class, Learn to paint or draw, Start a book club, Learn to play a board game",
    10: "Learn to play a card game, Learn a new language Start a book club, Go on a solo camping trip, Start a book club, Start a vegetable garden",
    11: "Take a calligraphy class, Take a beginner's coding class, Learn to knit or crochet, Learn to play a new musical instrument, Try a new cuisine, Learn to paint or draw,",
    12: "Learn to play a card game, Learn to play a board game, Take a beginner's coding class, Learn to bake bread, Learn to play a new musical instrument, Take a photography class, Learn to play a card game, Try a new cuisine, Learn to paint or draw, Start a book club",
    13: "Volunteer at a local animal shelter, Take a DIY home improvement class, Try a new cuisine, Learn a new language, Take a dance class, Learn to play a card game",
    14: "Volunteer at a local animal shelter, Learn a new language, Take a dance class, Start a blog or vlog, Take a DIY home improvement class, Learn to play a new musical instrument",
    15: "Learn to knit or crochet, Learn to paint or draw, Take a pottery class, Start a home garden, Go on a solo camping trip",
    16: "Go on a solo camping trip, Learn to paint or draw, Go on a solo camping trip,Take a photography class, Learn to play a board game",
    17: "Take a pottery class, Start a home garden, Go on a solo camping trip, Take a calligraphy class,Learn to bake bread, Start a book club",
    18: "Take a calligraphy classTake a pottery class, Learn to play a board game, Start a home garden, Start a vegetable garden",
    19: "Take a DIY home improvement class, Learn to play a new musical instrument,Take a pottery class, Learn to play a board gam ", 
    20: "Volunteer at a local animal shelter, Take a dance class, Start a blog or vlog, Take a pottery classLearn to play a board game",
    21: "Learn to knit or crochet, Learn to play a board game, Learn to paint or draw, Try a new cuisine, Take a calligraphy class, Start a home garden, Learn to play a new musical instrument",
    22: "Learn to play a board game, Take a pottery class, Learn to paint or draw, Start a home garden, Take a beginner's coding class, Go on a solo camping trip, Take a dance class",
    23: "Take a pottery class, Start a home garden, Learn to play a card game, Try a new cuisine,Start a vegetable garden, Learn a new language, Volunteer at a local animal shelter, Take a dance class",
    24: "Start a home garden  Try a new cuisine, Learn to play a card game, Learn to play a board game, Start a book club, Take a dance class, Start a blog or vlog, Learn a new language",
    25: "Take a DIY home improvement class, Learn to play a card game, Learn to play a new musical instrument, Take a beginner's coding class, Go on a solo camping trip, Start a book club",
    26: "Volunteer at a local animal shelter, Learn to play a card game, Try a new cuisine  Take a calligraphy class, Learn to bake bread",
    27: "Learn to knit or crochet, Try a new cuisine, Take a photography class, Learn a new language, Learn to play a new musical instrument",
    28: "Go on a solo camping trip, Take a calligraphy class, Learn to paint or draw, Volunteer at a local animal shelter, Learn to knit or crochet Learn a new language",
    29: "Take a pottery class, Learn to bake bread, Go on a solo camping trip, Learn to paint or draw, Start a book club, Start a vegetable garden, Learn to knit or crochet",
    30: "Learn to play a card game, Take a calligraphy class, Take a beginner's coding class, Start a book club, Start a vegetable garden, Take a beginner's coding class, Take a pottery class, Learn to play a board game",
    31: "Take a DIY home improvement class, Take a calligraphy class, Learn to bake bread, Learn a new language, Take a DIY home improvement class, Learn to play a new musical instrument",
    32: "Volunteer at a local animal shelter, Take a dance class,Learn to play a board game, Learn to bake bread",
    33: "Learn to knit or crochet, Try a new cuisine, Take a photography class, Take a DIY home improvement class, Go on a solo camping trip,Start a book club",
    34: "Go on a solo camping trip,Start a book club, Learn to knit or crochet, Learn to play a card game, Take a calligraphy class, Start a home garden",
    35: "Volunteer at a local animal shelter, Take a photography class, Learn a new language, Start a blog or vlog",
    36: "Learn to play a card game, Take a calligraphy class, Learn to bake bread, Start a vegetable garden, Take a DIY home improvement class, Take a beginner's coding class, Go on a solo camping trip",
    37: "Take a DIY home improvement class, Learn to play a new musical instrument, Start a home garden, Take a beginner's coding class, Go on a solo camping trip, Take a photography class, Learn a new language",
    38: "Volunteer at a local animal shelter, Take a dance class, Learn to bake bread, Start a home garden, Start a book club, Take a beginner's coding class",
    39: "Take a photography class, Start a book club, Start a vegetable garden, Take a pottery class, Start a blog or vlog",
    40: "Go on a solo camping trip, Learn to paint or draw, Start a book club, Learn to play a board game, Take a calligraphy class, Learn to bake bread, Take a pottery class",
    41: "Go on a solo camping trip, Take a DIY home improvement class, Take a pottery class, Take a beginner's coding class, Learn to play a new musical instrument",
    42: "Learn to play a board game, Learn to bake bread, Take a pottery class, Go on a solo camping trip, Learn to paint or draw, Start a book club, Start a home garden",
    43: "Take a DIY home improvement class, Learn to play a new musical instrument, Take a beginner's coding class, Volunteer at a local animal shelter, Take a photography class, Learn a new language",
    44: "Take a dance class, Start a blog or vlog, Go on a solo camping trip, Start a book club, Learn to knit or crochet",
    45: "Learn to knit or crochet, Start a book club, Try a new cuisine, Start a book club,  Volunteer at a local animal shelter, Start a blog or vlog",
    46: "Try a new cuisine, Start a vegetable garden, Learn to paint or draw, Start a book club, Learn to knit or crochet, Start a blog or vlog",
    47: "Go on a solo camping trip, Start a home garden, Start a vegetable garden,Take a pottery class, Try a new cuisine, Take a dance class, Start a blog or vlog, Learn a new language",
    48: "Learn to play a card game, Take a calligraphy class, Learn to bake bread, Learn a new language, Try a new cuisine, Volunteer at a local animal shelter",
    49: "Take a DIY home improvement class, Take a beginner's coding class, Go on a solo camping trip, Learn to play a board game, Start a home garden, Start a vegetable garden",
    50: "Try a new cuisine, Learn to play a new musical instrument Take a photography class, Take a dance class, Go on a solo camping trip, Learn to play a board game, Start a home garden, Learn to paint or draw, Start a vegetable garden",
    51: "Learn to knit or crochet, Learn to play a new musical instrument, Take a photography class, Take a beginner's coding class, Take a pottery class, Learn to paint or draw, Take a beginner's coding class"
}

activities = [
"Learn to play a new musical instrument",
"Take a beginner's coding class",
"Start a vegetable garden",
"Learn a new language",
"Volunteer at a local animal shelter",
"Take a dance class",
"Start a blog or vlog",
"Learn to knit or crochet",
"Try a new cuisine",
"Take a photography class",
"Go on a solo camping trip",
"Learn to paint or draw",
"Start a book club",
"Take a pottery class",
"Learn to play a board game",
"Start a home garden",
"Learn to play a card game",
"Take a calligraphy class",
"Learn to bake bread",
"Take a DIY home improvement class"
]

keys = list(activitiesDict.keys())

data = {
    'Age': np.random.randint(1, 101, size=samples),
    'Gender': np.round(np.random.randint(1, 3, size=samples)),
    'nightorday': np.round(np.random.randint(1, 3, size=samples))
}
for i in activities:
    data[i] = []

activitiesList = []
learn_to_play_a_new_musical_instrument = []
take_a_beginners_coding_class = []
start_a_vegetable_garden = []
learn_a_new_language = []
volunteer_at_a_local_animal_shelter = []
take_a_dance_class = []
start_a_blog_or_vlog = []
learn_to_knit_or_crochet = []
try_a_new_cuisine = []
take_a_photography_class = []
go_on_a_solo_camping_trip = []
learn_to_paint_or_draw = []
start_a_book_club = []
take_a_pottery_class = []
learn_to_play_a_board_game = []
start_a_home_garden = []
learn_to_play_a_card_game = []
take_a_calligraphy_class = []
learn_to_bake_bread = []
take_a_diy_home_improvement_class = []


for i in range(samples):
    datalistcreation()


data['Learn to play a new musical instrument'] = learn_to_play_a_new_musical_instrument
data['Take a beginner\'s coding class'] = take_a_beginners_coding_class
data['Start a vegetable garden'] = start_a_vegetable_garden
data['Learn a new language'] = learn_a_new_language
data['Volunteer at a local animal shelter'] = volunteer_at_a_local_animal_shelter
data['Take a dance class'] = take_a_dance_class
data['Start a blog or vlog'] = start_a_blog_or_vlog
data['Learn to knit or crochet'] = learn_to_knit_or_crochet
data['Try a new cuisine'] = try_a_new_cuisine
data['Take a photography class'] = take_a_photography_class
data['Go on a solo camping trip'] = go_on_a_solo_camping_trip
data['Learn to paint or draw'] = learn_to_paint_or_draw
data['Start a book club'] = start_a_book_club
data['Take a pottery class'] = take_a_pottery_class
data['Learn to play a board game'] = learn_to_play_a_board_game
data['Start a home garden'] = start_a_home_garden
data['Learn to play a card game'] = learn_to_play_a_card_game
data['Take a calligraphy class'] = take_a_calligraphy_class
data['Learn to bake bread'] = learn_to_bake_bread
data['Take a DIY home improvement class'] = take_a_diy_home_improvement_class

activitiesDataFrame = pd.DataFrame(data)
print(activitiesDataFrame)

activitiesDataFrame.to_csv('activitiesData.csv', index=False)


