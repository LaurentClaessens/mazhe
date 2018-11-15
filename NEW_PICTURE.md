# How to create a new picture with Yanntricks ?

This is a small howto for myself; I still have to make it much simpler for the potential contributors.

- Use the script `new_picture.py` for creating a skeleton.
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


Sage

Launch Sage in the directory `src_phystricks`

## Get Sage

- Download
- Unzip
- Copy to `~/.Sage` so that the directory `~/.Sage` contains the bash executable `sage`.

