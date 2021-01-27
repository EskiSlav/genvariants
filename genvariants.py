# -*- coding: utf-8 -*-
from subprocess import Popen
from platform import platform
from os import remove, system, makedirs
from config import * 
from random import choice
from threading import Thread

OS = platform()[0]

def get_questions() -> list:
    with open(question_file, 'r') as f:
        questions = f.readlines()

    return questions

def delete_var_files():
    i = 1
    while True:
        try:
            remove(f"var{i}.out")
            remove(f"var{i}.aux")
            remove(f"var{i}.log")
            i += 1
        except OSError:
            break
    while True:
        try:
            remove(f"out\\var{i}.out")
            remove(f"out\\var{i}.aux")
            remove(f"out\\var{i}.log")
            i += 1
        except OSError:
            break

def gen_tex_files(variants: int, questions_per_variant: int):
    questions = get_questions()

    for i in range(1, variants):
        chosen_questions = set()
        while not len(chosen_questions) == questions_per_variant:
            chosen_questions.add(choice(questions))

        chosen_questions = sorted(list(chosen_questions))
        variant_file = open(f"var{i}.tex", 'w')
        s = ''

        for cq in chosen_questions:
            s += cq

        variant_file.write(template + s + "\\end{document}")
        variant_file.close()



def gen_pdf_files(number_of_variants):
    try:
        makedirs('out')
    except FileExistsError:
        pass

    for i in range(1, number_of_variants):
        Popen(['pdflatex.exe', '-output-directory=out', f'var{i}.tex'])

if __name__ == '__main__':
    
    if not len(argv) == 3:
        print(USAGE)
        exit()

    number_of_variants = int(argv[1])
    questions_per_variant = int(argv[2])

    gen_tex_files(number_of_variants, questions_per_variant)
    gen_pdf_files(number_of_variants)
    delete_var_files()
