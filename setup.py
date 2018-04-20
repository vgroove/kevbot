from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='kevbot',
      version='0.0.1',
      description='Friendly chatbot and assistant',
      long_description="Kevbot is a chatbot currently made for joinng Discord servers. He can be configured to talk on command or randomly and can be trained on past conversations or any text file. Kevbot's architecture makes it easy to add new commands or even adapters to other chat platforms",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Communications :: Chat',
      ],
      keywords='kevbot chatbot discord markov nlp'
      url='http://github.com/vgroove/kevbot',
      author='vgroove',
      license='MIT',
      packages=['kevbot'],
      install_requires=[
          'discord.py>=0.16.7',
          'concurrent',
          'random',
          'requests',
          'json',
          'asyncio',
          'pymongo>=3.4.0'
      ],
      include_package_data=True,
      zip_safe=False)
