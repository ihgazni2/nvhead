#pip3 uninstall main
pip3 uninstall nvhead
git rm -r dist
git rm -r build
#git rm -r nvhead.egg-info
git rm -r nvhead.egg-info
rm -r dist
rm -r build
#rm -r elist.egg-info
rm -r nvhead.egg-info
git add .
git commit -m "remove old build"
