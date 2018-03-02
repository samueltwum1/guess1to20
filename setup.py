from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A number creator',
  author = 'Sam',
  author_email = 'sam@gmail.com',
  url = 'git@github.com:samueltwum1/guess1to20.git', # use the URL to the github repo
  download_url = 'https://github.com/samueltwum1/guess1to20.git', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
