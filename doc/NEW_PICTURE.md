# How to create a new picture with Yanntricks ?

This is a small howto for myself; I still have to make it much simpler for the potential contributors.

- Use the script `new_picture.py` (furnished with `Yanntricks`) for creating a skeleton.
- Copy the new files to a tmp directory
- Compile once, for creating the new files.

Copie

- Le fichier `Fig_JOQVoolPTsYPZK.pstricks` va dans `auto/pictures_tex`.
- Les fichiers md5 et pdf vont dans `auto/pictures_tikz`   
- The file `phystricksJOQVoolPTsYPZK.py` goes to `src_phystricks`.

Git

git add the files
phystricksJOQVoolPTsYPZK.py 
Fig_JOQVoolPTsYPZK.pstricks 
tikzFIGLabelFigJOQVoolPTsYPZKPICTJOQVoolPTsYPZK.pdf 
tikzFIGLabelFigJOQVoolPTsYPZKPICTJOQVoolPTsYPZK.md5

Prepare tests

In the file `src_phystricks/figures_mazhe.py`, add the line
```
from phystricksJOQVoolPTsYPZK import JOQVoolPTsYPZK
```
and the line
```
append_picture(JOQVoolPTsYPZK,1)
```


## modifier une image

Changer et compiler
```
    set name SBTooEasQsT

    rm ./build/build_giulietta/src_yanntricks/yanntricks$name.py
    rm ./build/build_giulietta/src_yanntricks/Fig_$name.pstricks.recall
    rm ./build/build_giulietta/auto/pictures_tikz/tikz$name.pdf
    rm ./build/build_giulietta/auto/pictures_tikz/tikz$name.md5
    rm ./build/build_giulietta/auto/pictures_tex/Fig_$name.pstricks
    rm ./Fig_$name.pstricks
    rm ./Fig_$name.comment
    rm ./src_yanntricks/Fig_$name.pstricks.recall
    rm ./auto/pictures_tikz/tikz$name.pdf
    rm ./auto/pictures_tikz/tikz$name.md5
    rm ./auto/pictures_tex/Fig_$name.pstricks
    rm ./$name.yanntricks.aux

    nvim src_yanntricks/yanntricks$name.py
    cd src_yanntricks
    ./yanntricks$name.py
    mv ../Fig_$name.pstricks ../auto/pictures_tex/

    ./lst_actu.py
```
