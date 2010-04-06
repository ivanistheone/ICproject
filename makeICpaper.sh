
PAPERNAME="InterferenceOuterBound"
SERVER="http://levski.cnd.mcgill.ca:8001"

TOPMATTER="triQECC-topmatter"
BOTTOMMATTER="triQECC-bottommatter"
BIBFILE="InterferenceChannelBib"

echo "Now building the paper "$PAPERNAME


#get paper
wget $SERVER/ep/pad/export/$PAPERNAME/latest?format=txt -O $PAPERNAME.tex_part


#get top matter & bottom matter 
wget $SERVER/ep/pad/export/$TOPMATTER/latest?format=txt -O topmatter.tex_part
wget $SERVER/ep/pad/export/$BOTTOMMATTER/latest?format=txt -O bottommatter.tex_part

# concatenate
cat topmatter.tex_part $PAPERNAME.tex_part bottommatter.tex_part > $PAPERNAME.tex


#getting extra files
#wget $SERVER/ep/pad/export/Qcircuit-tex/latest?format=txt -O Qcircuit.tex
wget $SERVER/ep/pad/export/header-tex/latest?format=txt -O header.tex


# get bibtex file
wget $SERVER/ep/pad/export/$BIBFILE/latest?format=txt -O interferenceChannel.bib


# build
pdflatex $PAPERNAME.tex
pdflatex $PAPERNAME.tex
bibtex $PAPERNAME
pdflatex $PAPERNAME.tex


#cleanup

#rm header.tex
rm $PAPERNAME.aux bottommatter.tex_part $PAPERNAME.log $PAPERNAME.tex_part topmatter.tex_part InterferenceOuterBound.blg
