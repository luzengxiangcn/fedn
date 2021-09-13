export PYTHONPATH=$PYTHONPATH:../python/
echo $PYTHONPATH
python ../python/cli/run/combiner.py  -n combiner --init=../config/settings-combiner.yaml.template
