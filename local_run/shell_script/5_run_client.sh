export PYTHONPATH=$PYTHONPATH:../python/
echo $PYTHONPATH
python ../python/cli/run/client.py  -n client --init=../config/settings-client.yaml.template
