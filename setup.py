from distutils.core import setup

setup(
  name = 'straattaal_bijbel',         # How you named your package folder (MyLib)
  packages = ['straattaal_bijbel'],   # Chose the same as "name"
  version = '349058290485923485902349023849082390582905802938409238409823403495893485938904859304859083940850938495384958398267438957638945763459867349856789345768973459867893457689347689734598673495867394586739480506793845769384573490582904859234859023490238490823905829058029384092384098234034958934859389048593048590839408509384953849583982674389576389457634598673498567893457689734598678934576893476897345986734958673945867394805067938457693845798234.0',      # Start with a small number and increase it with every change you make
  license='Apache 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'God',                   # Type in your name
  author_email = 'god@prutsor.nl',      # Type in your E-Mail
  url = 'https://github.com/Prutsor/bijbel-straattaal',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Prutsor/bijbel-straattaal/archive/refs/tags/bijbel4life.tar.gz',    # I explain this later on
  keywords = ['bijbel', 'god', 'patta'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)