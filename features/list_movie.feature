Feature: List Movies
  In order to keep myself up to date about movie registered in my movies
  As a user
  I want to list the 3 registered movies

  Background: There are 3 registered movies by same user
    Given Exists a user "user" with password "password"
    And Exists movie registered by "user"
      | movie_name          | movie_category  | year | director        |
      | The Tavern          | Terror          | 2000 | James Gunn      |
      | Shutter Island      | Crime           | 2012 | Martin Scorsese |
      | Cannibal Holocaust  | Terror          | 1980 | Ruggero Deodato |

  Scenario: List the movies
    When I list movie
    Then I'm viewing a list containing
      | movie_name          |
      | The Tavern          |
      | Shutter Island      |
      | Cannibal Holocaust  |
    And The list contains 3 movies
