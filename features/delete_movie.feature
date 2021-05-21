Feature: Delete Movie
  User can delete movies
  I want to delete a movie register I created

  Background: There are registered users and a movie by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists movie registered by "user1"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Terror          | 2000 | James Gunn |
      | Titanic      | Romance         | 2000 | James Gunn |

  Scenario: Delete owned movie registry
    Given I login as user "user1" with password "password"
    When I delete the movie with name "The Tavern"
    Then There are 1 movie

  Scenario: Try to delete movie but not logged in
    Given I'm not logged in
    When I view the details for movie "Titanic"
    Then There is no "delete" link available

  Scenario: Force delete movie but not the owner permission exception
    Given I login as user "user2" with password "password"
    Then There is no "delete" link available
