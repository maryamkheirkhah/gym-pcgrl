from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gym_pcgrl',
      version='0.1.0',
      install_requires=['gym', 'numpy', 'pillow'],
      author="Ahmed Khalifa",
      author_email="ahmed@akhalifa.com",
      description="A package for \"Procedural Content Generation via Reinforcement Learning\" OpenAI Gym interface.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ]
)