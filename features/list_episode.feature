Feature: List Episodes
  In order to keep myself up to date about serie registered in my episodes
  As a user
  I want to list the 3 registered episodes

  Background: There are 3 registered episodes by same user
    Given Exists a user "user" with password "password"
    And Exists serie registered by "user"
      | serie_name      | category | year   |
      | Modern Family  | Comedy    | 2000   |
      | Walking Dead   | Terror    | 2008   |


  Scenario: List the episode
    Given I login as user "user" with password "password"
    When I register episode at serie "Modern Family"
       | name              | season   | number |
       | Boda de Haley     | 2        | 20    |
       | Embarazo de Haley | 2        | 20    |
       | Divorcio de Haley | 2        | 20    |
    Then I list episode "Modern Family"
    And Viewing a list episodes that containing
      | name            |
      |Boda de Haley    |
      |Embarazo de Haley|
      |Divorcio de Haley|
    And The list contains 3 episodes