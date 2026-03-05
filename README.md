[![Build Status](https://app.travis-ci.com/ajslezak/team1-mon-spring26.svg?token=dcYXppMHqANaxxTZhnsR&branch=develop)](https://app.travis-ci.com/ajslezak/team1-mon-spring26) [![Coverage Status](https://coveralls.io/repos/github/ajslezak/team1-mon-spring26/badge.svg?branch=main)](https://coveralls.io/github/ajslezak/team1-mon-spring26?branch=main)

# Django Poll Application

- [Elastic Beanstalk url](http://polls.eba-chiviqwv.us-east-2.elasticbeanstalk.com/polls/)

## Notes
- This is the demo application from steps 1-4 [Writing your first Django app](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
- I used (_extends "admin/base_site.html"_) the Admin site css to make the Poll application look better
- Coveralls is reporting coverage correctly, but it's reporting under the "team1-mon-spring26" repo.
  I had to use this token because the token for this repo would not populate the branch and pull fields,
  meaning the Coverage badge was always "Unknown" 
