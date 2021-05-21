Feature: Register Movie
  In order to upload a movie,
  As a user
  I want to register a movie together with its movieName, movieCategory, year and director

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register movie
    Given I login as user "user" with password "password"
    When I register movie
      | movie_name   | movie_category | year | director   |
      | The Tavern  | Terror          | 2000 | James Gunn |
    Then I'm viewing the details page for movie by "user"
      | movie_name   | movie_category | year | director   |
      | The Tavern  | Terror          | 2000 | James Gunn |
    And There are 1 movie
  
    Scenario: Try to register a movie but not logged in
    Given I'm not logged in
    When I register movie
      | movie_name   | movie_category | year | director   |
      | The Tavern  | Terror          | 2000 | James Gunn |
    Then I'm redirected to the login form
    And There are 0 movie