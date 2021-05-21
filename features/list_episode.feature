Feature: List Episodes
  In order to keep myself up to date about serie registered in my episodes
  As a user
  I want to list the 3 registered episodes

  Background: There are 3 registered episodes by same user
    Given Exists a user "user" with password "password"
    And Exists episode registered by "user"
      | name            | serie_name    | season   | number |
      |Boda de Haley    | Modern Family | 2        | 20     |
      |Embarazo de Haley| Modern Family | 2        | 21     |
      |Divorcio de Haley| Modern Family | 2        | 22     |

  Scenario: List the episode
    When I list episode
    Then I'm viewing a list containing
      | name            |
      |Boda de Haley    |
      |Embarazo de Haley|
      |Divorcio de Haley|
    And The list contains 3 episode