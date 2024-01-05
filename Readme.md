The code analysis script (test_run.py) utilizes OpenUnderstand, a specialized library, to access a database
and extract details regarding the classes within the code repository.
1-Clone the OpenUnderstand repository:
git clone https://github.com/m-zakeri/OpenUnderstand.git
cd OpenUnderstand
git fetch
git checkout -b dev origin/dev

2-Make things costumize in config.ini, test_openunderstand.py and test_run.py

Outcomes:

The OpenUnderstand analysis script reports the following classes:

1-SS2
2-String
3-System
4-SS1
5-SS1

Classes:5

now its the original understand's turn:

The Understand software is a paid code analysis utility.
The analysis script (api.py) employs the Understand Python API to scrutinize the Java codebase and display details concerning the classes.

1-Install the Understand tool from SciTools website.

2-Run the analysis script in test Directory:

python api.py

The original Understand analysis script reports the following classes:
ss2
ss1
string

Classes:3

Despite their shared goal of codebase analysis, variations exist in the identified classes between the two tools. OpenUnderstand recognizes supplementary classes like '.', '..', and '.String', potentially denoting system-defined elements.
Recognizing and comprehending these distinctions could assist in selecting the most fitting tool for your analysis requirements.