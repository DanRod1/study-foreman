from setuptools import setup

# pensez à ajouter json et re dans le requires quand on arrêtera les conneries de proxy
setup(name="pkgFormanApi",
      version="0.0.1-2",
      description="Creation module API foreman pour AH",
      author="anonymous not proud of his code",
      author_email="daniel.da.rodriguez.external@airbus.com",
      packages=["pkgFormanApi"],
      install_requires=["requests_oauthlib","jq"],
      license="GNU"
)
