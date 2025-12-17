from setuptools import find_packages, setup

setup(
    name="mcqgenerator1",
    version="0.1.0",
    author="Ansh Arora",
    author_email="aaransh27@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
