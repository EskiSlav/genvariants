from sys import argv

template = """\\documentclass[14pt]{extarticle}

\\usepackage{scrextend}
\\usepackage{fancyhdr}
\\usepackage{cmap}
\\usepackage[T2A]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[english,russian,ukrainian]{babel}
\\usepackage{indentfirst}
\\usepackage{graphicx}
\\usepackage{hyperref}
\\usepackage{titlesec}
\\usepackage{fancyhdr}
\\usepackage{geometry}
\\usepackage{titlesec}
\\usepackage{scrextend}
\\usepackage{setspace}
\\onehalfspacing

\\usepackage{enumitem}
\\setlist{noitemsep}

\\usepackage{float}

% For XeLaTex
% \\usepackage{fontspec}
%\\usepackage{polyglossia}
%\\setmainfont{Times New Roman}
%\\newfontfamily\\cyrillicfont{Times New Roman}
%\\setmainlanguage{ukrainian}

\\graphicspath{ {images/} }
\\hypersetup{
	colorlinks,
	citecolor=black,
	linkcolor=black,
	filecolor=black,
	urlcolor=black
}

\\geometry{
	a4paper,
	total={165mm,247mm},
	left=30mm,
	top=20mm,
}

\\usepackage[font=small]{caption} % caption size

\\usepackage{array} % padding in table
\\setlength\\extrarowheight{3pt} % or whatever amount is appropriate

% \\pagestyle{fancy}
% \\fancyhf{}
% \\renewcommand{\\headrulewidth}{0.5pt}
%\\renewcommand{\\footrulewidth}{0.1pt}
% \\rhead{\\LaTeX}
% \\lhead{Вячеслав Козачок | Ілля Кузнєцов}

\\cfoot{\\thepage}
%\\titleformat{\\section}
%{\\normalfont\\Large\\bfseries}{\\thesection}{1em}{}

%\\titleformat*{\\subsection}{\\large\\bfseries}

\\usepackage{listings}
\\usepackage{xcolor}

\\definecolor{codegreen}{rgb}{0,0.6,0}
\\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\\definecolor{codepurple}{rgb}{0.58,0,0.82}
\\definecolor{backcolour}{rgb}{0.99,0.99,0.99}
\\definecolor{codeblue}{rgb}{0.1,0.1,0.99}

\\lstdefinestyle{mystyle}{
	backgroundcolor=\\color{backcolour},   
	commentstyle=\\color{codegreen},
	keywordstyle=\\color{codeblue},
	numberstyle=\\scriptsize\\color{codegray},
	stringstyle=\\color{codepurple},
	basicstyle=\\ttfamily\\footnotesize,
	breakatwhitespace=false,         
	breaklines=true,                 
	captionpos=b,                    
	keepspaces=true,                 
	numbers=left,                    
	numbersep=5pt,                  
	showspaces=false,                
	showstringspaces=false,
	showtabs=false,                  
	tabsize=4
}

\\lstset{style=mystyle}

\\begin{document}
"""

USAGE = """Usage: {} [number of variants] [questions per variant]""".format(argv[0])

pdflatex = "pdflatex.exe"

question_file = 'questions.txt'
