## TITLE: Healthy Gym!

## Short Description:
  An app for gym administrators that can assist with managing members, trainers, and programs.

## Basic CRUD
  CREATE --  Can make new members, trainers, locations, programs, and schedules.
  READ -- Can show members, trainers, locations, programs, and schedules.
  UPDATE -- Can edit a member's membership type, a trainer's name, and a location's city.  
  DELETE -- Can remove members, trainers, locations, and programs.

## Getting Started:
  To get started with this repo, in the terminal run the following commands:
     
    $ pipenv install 
    $ pipenv shell 
    $ python lib/cli.py


  Once program is running, can fill with test data by navigating to the dev menu and selecting the option "Put in Test Data":
    $6
    $2
  
  If you want to clear data that was inputted from a few runs and restart to test data, select the option to "Reset with Test Data" 
    $6
    $3
  
  If you want to just clear all data and start with no data, navigate to the dev menu and select "Clear All Data"
    $6
    $4

once those are done, you will put 

  $ python3 lib/cli.py 

to start the program!


## Collaborators:
    Jefferey
    Hadil
    Katie

## ERD
[Imgur](https://i.imgur.com/tn83vF5.png)

## drawio
[Imgur](https://i.imgur.com/pjEmMsh.png)

## Trello Board:
https://trello.com/b/KyUFcJNo/phase-3

## Futre Plans
- Implement full CRUD in Schedule class
- Expand the Location class to contain more than the city property and further utiliza those 
- Expand the Schedule class to do more than basic CRUD
  - Such as, being able to look up all of the instances of Schedule a member is attached to
- Create a GUI that will contain calendar and pop up when selecting the date when adding a new instance of Schedule
- Have unique designs for each sub menu
- Further explore adding functions to helpers.pyI