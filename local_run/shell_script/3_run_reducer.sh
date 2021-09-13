export PYTHONPATH=$PYTHONPATH:../python/
echo $PYTHONPATH
python ../python/cli/run/reducer.py  -n reducer --init=../config/settings-reducer.yaml.template
