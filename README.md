# Antidote

This is our HackGT 2016 project.

You can read a little more about the motivation for the project and the implementation on our [Devpost](http://devpost.com/software/overdose).

## Branches

The [original-hackgt branch](https://github.com/Bobzeka/BMSHackGT2016/tree/Original-HackGT) contains
entirely unedited code from the 9am close of the hackathon.

The [new branch](https://github.com/Bobzeka/BMSHackGT2016/tree/new) will soon contain a few minor changes
like printing out tweets so that you can see a little more what the code does behind the scenes.

## The Problem with the Project

The problem that we found out during the hackathon is that Twitter does not really like to give us tweet
location data. The intentially strip some of the locations from tweets when you use the search portion of
their REST API requests. The result is only about one tweet every thousand would give us location data and
due to the limitations of the free API key, this turned out to be entirely impossible to use. The project
here contains a front end that includes only sample location data from Google Heatmap API's tutorial due
to the tweet location issue.


Languages: Python, HTML/CSS, JavaScript
APIs: Twitter, Google Heatmap
Libraries: SKLearn
