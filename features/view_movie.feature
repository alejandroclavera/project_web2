Feature: View Movie
  In order to know about Movie
  As a user,
  I want to view the movie details.

  Background: There is one movie with 2 movie
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists movie registered by "user1"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Terror          | 2000 | James Gunn |
    And Exists movie registered by "user2"
      | movie_name    | movie_category | year | director        |
      | Shutter Island| Crime          | 2012 | Martin Scorsese |


  Scenario: View details for added movie
    Given I login as user "user1" with password "password"
    When I view the details for movie "The Tavern"
    Then I'm viewing movie details including
      | movie_category | year | director   |
      | Terror         | 2000 | James Gunn |

