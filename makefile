
DEL_FILE      = rm -f

clean:
	-$(DEL_FILE) *.md5
	-$(DEL_FILE) *.pstricks
	-$(DEL_FILE) *.comment
	-$(DEL_FILE) *.pdf
	-$(DEL_FILE) *.pyc
	-$(DEL_FILE) phystricks*.py
	-$(DEL_FILE) *.dpth
	-$(DEL_FILE) *.aux
	-$(DEL_FILE) *.out
	-$(DEL_FILE) tikzFIGLabelFig*
	videlatex.sh

everything:
	make pictures everything-no-external
	make pictures everything-no-external
	make everything-external
frido:
	make pictures frido-no-external
	make pictures frido-no-external
	make frido-external
frido-external:
	pytex lst_frido.py --lotex 
frido-no-external:
	pytex lst_everything.py --lotex  --no-external
everything-external:
	pytex lst_everything.py --lotex 
everything-no-external:
	pytex lst_frido.py --lotex  --no-external
pictures:
	./figures_mazhe.py --all
all:frido everything
rebuild:clean all
