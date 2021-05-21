Feature: Edit Movie
  In order to keep updated my previous registers about movie
  As a user
  I want to edit a movie register I created

  Background: There are registered users and a movie by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists movie registered by "user1"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Terror          | 2000 | James Gunn |

  Scenario: Edit owned movie registry country
    Given I login as user "user1" with password "password"
    When I edit the movie with name "The Tavern"
      | movie_category |
      | Comedy         |
    Then I'm viewing the details page for movie by "user1"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Comedy          | 2000 | James Gunn |
    And There are 1 movie

  Scenario: Try to edit movie but not logged in
    Given I'm not logged in
    When I view the details for movie "The Tavern"
    Then There is no "edit" link available

  Scenario: Force edit movie but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the movie with name "The Tavern"
      | movie_category |
      | Comedy         |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for movie "The Tavern"
    Then I'm viewing the details page for movie by "user1"
      | movie_name   | movie_category  | year | director   |
      | The Tavern   | Terror          | 2000 | James Gunn |