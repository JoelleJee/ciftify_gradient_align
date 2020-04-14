# Steps in computing and analyzing the gradients

## load gnu-parallel and load the python virtual environment
```sh
module load gnu-parallel qbatch/2.1.5
source ~/.virtualenvs/gradients/bin/activate
```
## run all scripts that start with the form of *.1_
Start with the scripts in the 01_build_gradients folder to first build the gradients and visualize them.\
Then run the scripts in the 02_analyses folder to run within- and between-subject analyses and produce plots. \

## submitting qbatch commands
When submitting qbatch commands, the text file with all subcommands are produced with the commands_for_qbatch.ipynb file.\
Run the corresponding code block in commands_for_qbatch.ipynb to produce appropriate codes.\

