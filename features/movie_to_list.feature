Feature: Add movie to my movie list
  In order to register a movie to my list,
  As a user
  I want to register a movie together with its movieName, movieCategory, year and director into my movies list


Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists movie registered by "user"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Terror          | 2000 | James Gunn |


Scenario: Add a movie to my list
    Given I login as user "user" with password "password"
    When I add a movie to my list with the name "The Tavern"
      | movie_name   | movie_category | year | director   |
      | The Tavern  | Terror          | 2000 | James Gunn |
    Then I am viewing the details page for my movies by "user"
      | movie_name   | movie_category | year | director   |
      | The Tavern  | Terror          | 2000 | James Gunn |
    And There are 1 movie




