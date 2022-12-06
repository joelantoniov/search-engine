== README

Instructions

Rails project:

1- Download rvm: https://rvm.io/rvm/install

gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3

\curl -sSL https://get.rvm.io | bash -s stable --ruby

2- Unpack project

3- Edit Gemfile and comment the last two lines (those modules are no longer necessary) so that it looks like this:

# gem 'ruby-stemmer'
# gem 'mysql2'

4- Execute: bundle install

5- Execute: rails 

6- Application must be running on port 3000. http://localhost:3000

Python project:

1- Install Twisted

2- Execute: python daemont.py

3- Wait until the message appears: Starting service on port: 8888

4- From this moment you can make inquiries in the application.


![alt text](https://github.com/joelantoniov/search-engine/blob/main/ramen-search.jpg)

